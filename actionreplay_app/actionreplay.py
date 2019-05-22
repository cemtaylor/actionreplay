#!/usr/bin/env python3
import time
import logging
import json
import sys
import copy
from timeit import default_timer as timer
from pynput import mouse, keyboard
# GUI imports
import os
from PySide2 import QtCore, QtWidgets, QtGui
from ui import Ui_ActionReplay
# Vision imports
import cv2
import numpy as np


class ActionReplay(object):
    """Take control over KB/M and replay a list of actions"""

    def __init__(self):
        self.mouse_controller = mouse.Controller()
        self.keyboard_controller = keyboard.Controller()
        self.replay = True

    def draw(self, actions: list):
        """Draw the path the mouse would take with the current action set"""
        img = np.zeros((1080, 1920, 3), np.uint8)
        line_color = (255, 255, 255)
        for i in range(len(actions)):
            if i == 0:
                continue
            last_action = actions[i-1]
            action = actions[i]
            if action['button']:
                if action['pressed']:
                    line_color = (128, 70, 0)
                    cv2.circle(img, pos,
                               15, line_color, 2)
                else:
                    line_color = (30, 180, 0)
                    cv2.circle(img, pos,
                               13, line_color, 2)
            if action['pos'] and last_action['pos']:
                last_pos = (last_action['pos'][0], last_action['pos'][1])
                pos = (action['pos'][0], action['pos'][1])
                cv2.line(img, last_pos, pos, line_color, 2)
                line_color = (255, 255, 255)
        cv2.imwrite('action.png', img)
        logger.info("Finished drawing")

    def start(self, actions: list):
        """Start replacing the list of actions passed as method argument"""
        logger.info('Replay started')
        self.draw(actions)
        for action in actions:
            if not self.replay:
                break
            time.sleep(action['time'])
            if action['key']:
                if action['pressed']:
                    self.keyboard_controller.press(action['key'])
                    logger.debug("Key %s Pressed", action['key'])
                else:
                    self.keyboard_controller.release(action['key'])
                    logger.debug("Key %s Released", action['key'])
            else:
                if self.mouse_controller.position != action['pos']:
                    self.mouse_controller.position = action['pos']
                    logger.debug("Mouse moved to %s", action['pos'])
                if action['scroll_x'] or action['scroll_y']:
                    self.mouse_controller.scroll(
                        action['scroll_x'], action['scroll_y'])
                    logger.debug(
                        "Scrolled %s", (action['scroll_x'], action['scroll_y']))
                if action['button']:
                    if action['pressed']:
                        self.mouse_controller.press(action['button'])
                        logger.debug("Mouse button %s Pressed",
                                     action['button'])
                    else:
                        self.mouse_controller.release(action['button'])
                        logger.debug(
                            "Mouse button %s Released", action['button'])
        logger.info('Replay finished')


class ActionRecorder(object):
    """Record kb/m actions to an action log to be replayed"""

    def __init__(self):
        self.action_log = []
        self.last_action = 0
        self.recording = False
        self.click = True
        self.move = True
        self.keydown = True
        self.keyup = True
        self.scroll = True
        self.filename = './action.replay'
        logger.info('Action Recorder initialized')

    def save(self, actions, filename='./action.replay'):
        """Save recorded actions to file for reuse"""
        if not actions:
            actions = self.action_log
        # Convert from pynput objects to int/str we can convert back when loaded
        # Creates a copy of the passed actions to ensure we dont alter original
        saved_actions = copy.deepcopy(actions)
        for action in saved_actions:
            if action['key']:
                try:
                    action['key'] = action['key'].value.vk
                except AttributeError:
                    action['key'] = action['key'].vk
            elif action['button']:
                action['button'] = action['button'].name
        json_log = json.dumps(saved_actions)
        with open(filename, 'w') as f:
            f.write(json_log)

    def load(self, filename='./action.replay'):
        """Load recorded actions from file for reuse"""
        with open(filename, 'r') as f:
            actions = json.load(f)
        for action in actions:
            if action['key']:
                action['key'] = keyboard.KeyCode(action['key'])
            elif action['button']:
                action['button'] = getattr(mouse.Button, action['button'])
        self.action_log = actions

    def add(self, x=0, y=0, button=None, pressed=False, scroll_x=0, scroll_y=0, key=None):
        """Save actions to list in memory to be played or saved"""
        if not self.recording:
            return
        if key == keyboard.Key.esc:
            logger.info('Stop recording hotkey detected - Stopping recording')
            self.stop()
            return
        current_time = timer()
        action_time = current_time - self.last_action
        self.last_action = current_time
        action = {
            'pos': (x, y),
            'button': button,
            'key': key,
            'pressed': pressed,
            'scroll_x': scroll_x,
            'scroll_y': scroll_y,
            'time': action_time
        }
        self.action_log.append(action)

    def start(self, click=True, move=True, scroll=True, keydown=True, keyup=True):
        """Start kb/m listeners and set recording variable to True, wipe actions"""
        # Ensure action log is empty
        self.action_log = []

        # Configure actions being recorded
        if not click:
            self.click = click
        if not move:
            self.move = move
        if not scroll:
            self.scroll = scroll
        if not keydown:
            self.keydown = keydown
        if not keyup:
            self.keyup = keyup

        # Start listeners
        mouse_listener = mouse.Listener(
            on_move=self.log_move,
            on_click=self.log_click,
            on_scroll=self.log_scroll
        )
        mouse_listener.start()
        logger.info('Mouse listener started')
        keyboard_listener = keyboard.Listener(
            on_press=self.log_key_down,
            on_release=self.log_key_up
        )
        keyboard_listener.start()
        logger.info('Keyboard listener started')

        # Enable recording and start timer
        self.recording = True
        self.last_action = timer()
        logger.info('Recording started')

    def stop(self):
        """Set recording variable to False"""
        self.recording = False
        logger.info('Recording stopped')
        return

    def log_move(self, x: int, y: int):
        """Call add for mouse move event"""
        if self.move:
            self.add(x, y)

    def log_click(self, x: int, y: int, button, pressed: bool):
        """Call add for mouse click event"""
        if self.click:
            self.add(x, y, button=button, pressed=pressed)

    def log_scroll(self, x: int, y: int, dx: int, dy: int):
        """Call add for mouse scroll event"""
        if self.scroll:
            self.add(x=x, y=y, scroll_x=dx, scroll_y=dy)

    def log_key_down(self, key):
        """Call add for key down event"""
        if self.keydown:
            self.add(key=key, pressed=True)

    def log_key_up(self, key):
        """Call add for key up event"""
        if self.keyup:
            self.add(key=key, pressed=False)


class ActionThread(QtCore.QThread):
    def __init__(self, parent, run_func, arguments=None, **kwargs):
        super(ActionThread, self).__init__(parent)
        self._passed_method = run_func
        self._passed_arguments = arguments
        self._kwargs = kwargs

    def run(self):
        # This try/except is required to debug threds with vscode - it should be removed in release
        try:
            import ptvsd
            ptvsd.debug_this_thread()
        except:
            pass
        if self._passed_arguments and not self._kwargs:
            self._passed_method(self._passed_arguments)
        elif not self._passed_arguments and self._kwargs:
            self._passed_method(**self._kwargs)
        elif self._passed_arguments and self._kwargs:
            self._passed_method(self._passed_arguments, **self._kwargs)
        else:
            self._passed_method()


class ActionWidget(QtWidgets.QWidget):
    """Present GUI for controlling Action Record/Replay"""

    def __init__(self):
        super().__init__()
        logger.info('GUI initiated')
        # Set class variables
        self.recording_options = {
            'move': True,
            'click': True,
            'scroll': True,
            'keydown': True,
            'keyup': True
        }
        # Initiate recorder/replayer
        self.action_recorder = ActionRecorder()
        self.action_replayer = ActionReplay()

        # Create GUI
        self.ui = Ui_ActionReplay.Ui_ActionReplay()
        self.ui.setupUi(self)

        # Main button actions
        self.ui.start_recording.clicked.connect(self.record)
        self.ui.stop_recording.clicked.connect(self.stop)
        self.ui.save_action.clicked.connect(self.save)
        self.ui.load_action.clicked.connect(self.load)
        self.ui.quick_save_action.clicked.connect(self.quick_save)
        self.ui.quick_load_action.clicked.connect(self.quick_load)
        self.ui.replay_action.clicked.connect(self.replay)
        self.ui.draw_action.clicked.connect(self.draw_actions)

        # Recording toggles
        self.ui.record_move.toggled.connect(
            lambda: self.toggle_recording_option('move'))
        self.ui.record_click.toggled.connect(
            lambda: self.toggle_recording_option('click'))
        self.ui.record_scroll.toggled.connect(
            lambda: self.toggle_recording_option('scroll'))
        self.ui.record_keydown.toggled.connect(
            lambda: self.toggle_recording_option('keydown'))
        self.ui.record_keyup.toggled.connect(
            lambda: self.toggle_recording_option('keyup'))

        # Populate list of recent saved actions
        saved_items = self.find_saved_actions(os.getcwd())
        self.show_saved_items(saved_items)

    def show_saved_items(self, saved_items):
        already_listed = []
        for i in range(len(saved_items)):
            if self.ui.list_saved_actions.item(i):
                already_listed.append(
                    self.ui.list_saved_actions.item(i).text())
        for item in saved_items:
            if item not in already_listed:
                self.ui.list_saved_actions.addItem(item)

    def find_saved_actions(self, directory='.'):
        saved_items = []
        with os.scandir(directory) as listed_files:
            for item in listed_files:
                if item.is_file() and ".replay" in item.name:
                    saved_items.append(item.path)
                elif not item.is_file():
                    new_dir = self.find_saved_actions(item.path)
                    if new_dir:
                        saved_items.append(new_dir)
        if len(saved_items) > 0:
            return saved_items

    def toggle_recording_option(self, option):
        """Invert the state of the passed recording option to determine what is recorded"""
        self.recording_options[option] = not self.recording_options[option]
        logger.info("Toggling %s option to %s" %
                    (option, self.recording_options[option]))

    def record(self):
        """Start the ActionRecorder instance"""
        logger.info('GUI initiated recorder start')
        _thread = ActionThread(
            self, self.action_recorder.start, **self.recording_options)
        _thread.start()

    def stop(self):
        """Stop the ActionRecorder instance"""
        logger.info('GUI initiated recorder stop')
        _thread = ActionThread(self, self.action_recorder.stop)
        _thread.start()

    def save(self):
        """Save actions to file"""
        logging.info("GUI initiated save")
        file_name = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Replay", "./", ".replay")
        if file_name:
            save_options = {
                'actions': self.action_recorder.action_log, 'filename': ''.join(file_name)}
            _thread = ActionThread(
                self, self.action_recorder.save, **save_options)
            _thread.start()
            saved_items = self.find_saved_actions(os.getcwd())
            self.show_saved_items(saved_items)

    def load(self):
        """Load actions from file"""
        logging.info("GUI initiated load")
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Replay", "./", "*.replay")
        if file_name:
            load_options = {'filename': file_name[0]}
            _thread = ActionThread(
                self, self.action_recorder.load, **load_options)
            _thread.start()

    def quick_save(self):
        """Quick save actions to default action.replay file"""
        logger.info("GUI initiated action quick save")
        _thread = ActionThread(
            self, self.action_recorder.save, self.action_recorder.action_log)
        _thread.start()

    def draw_actions(self):
        """Draw mouse actions to file"""
        logger.info("GUI initiated action quick save")
        _thread = ActionThread(
            self, self.action_replayer.draw, self.action_recorder.action_log)
        _thread.start()

    def quick_load(self):
        """Quick load actions from default actio.replay file"""
        logger.info('GUI initiated action quick load')
        _thread = ActionThread(self, self.action_recorder.load)
        _thread.start()

    def replay(self):
        """Start the ActionReplay instance"""
        logger.info('GUI initiated replay start')
        self.action_recorder.stop()
        _thread = ActionThread(
            self, self.action_replayer.start, self.action_recorder.action_log)
        _thread.start()
        self.activateWindow()


def main():
    app = QtWidgets.QApplication([])
    action_widget = ActionWidget()
    logger.info("Starting widget")
    action_widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # Configure logging
    logger = logging.getLogger('actionreplay')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt='%(asctime)s,%(levelname)s,%(message)s',
        datefmt='%Y-%m-%d,%H:%M:%S%z'
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logfile_handler = logging.FileHandler(filename="actionreplay.log")
    logfile_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logfile_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(logfile_handler)
    # Start application
    logger.info('#'*30)
    logger.info('Application started')
    main()
    logger.info('Application closed')
