#!/usr/bin/env python3
import time
import logging
import json
import sys
from timeit import default_timer as timer
from pynput import mouse, keyboard
from PySide2 import QtCore, QtWidgets, QtGui


class ActionReplay(object):
    """Take control over KB/M and replay a list of actions"""

    def __init__(self):
        self.mouse_controller = mouse.Controller()
        self.keyboard_controller = keyboard.Controller()
        self.replay = True

    def start(self, actions):
        """Start replacing the list of actions passed as method argument"""
        logger.info('Replay started')
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


class ActionRecorder(object):
    """Record kb/m actions to an action log to be replayed"""

    def __init__(self):
        self.action_log = []
        self.last_action = 0
        self.recording = False
        self.filename = './action.replay'
        logger.info('Action Recorder initialized')

    def save_actions(self, filename='./action.replay'):
        """Save recorded actions to file for reuse"""
        json_log = json.dumps(self.action_log)
        with open(filename, 'w') as f:
            f.write(json_log)

    def load_actions(self, filename='./action.replay'):
        """Load recorded actions from file for reuse"""
        with open(filename, 'r') as f:
            self.action_log = json.load(f)

    def add_action(self, x=0, y=0, button=None, pressed=False, scroll_x=0, scroll_y=0, key=None):
        """Save actions to list in memory to be played or saved"""
        if not self.recording:
            return
        if key == keyboard.Key.esc:
            logger.info('Stop recording hotkey detected - Stopping recording')
            self.recording = False
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
        # logger.debug(action)
        logger.debug("Adding action")
        self.action_log.append(action)

    def log_move(self, x, y):
        """Call add_action for mouse move event"""
        self.add_action(x, y)

    def log_click(self, x, y, button, pressed):
        """Call add_action for mouse click event"""
        self.add_action(x, y, button=button, pressed=pressed)

    def log_scroll(self, x, y, dx, dy):
        """Call add_action for mouse scroll event"""
        self.add_action(x=x, y=y, scroll_x=dx, scroll_y=dy)

    def log_key_down(self, key):
        """Call add_action for key down event"""
        self.add_action(key=key, pressed=True)

    def log_key_up(self, key):
        """Call add_action for key up event"""
        self.add_action(key=key, pressed=False)

    def start(self):
        """Start kb/m listeners and set recording variable to True, wipe actions"""
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
        self.action_log = []
        self.recording = True
        self.last_action = timer()
        logger.info('Recording started')

    def stop(self):
        """Set recording variable to False"""
        self.recording = False
        logger.info('Recording stopped')


class ActionWidget(object):
    """Present GUI for controlling Action Record/Replay"""

    def setupUi(self, Widget):
        Widget.setObjectName("Action Replay")
        Widget.resize(400, 300)
        Widget.setMouseTracking(False)
        self.action_recorder = ActionRecorder()
        self.action_replayer = ActionReplay()
        self.gridLayoutWidget = QtWidgets.QWidget(Widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stop_recording = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stop_recording.setObjectName("stop_recording")
        self.gridLayout.addWidget(self.stop_recording, 3, 0, 1, 1)
        self.console_output = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.console_output.setObjectName("console_output")
        self.gridLayout.addWidget(self.console_output, 0, 0, 1, 1)
        self.start_recording = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start_recording.setObjectName("start_recording")
        self.gridLayout.addWidget(self.start_recording, 2, 0, 1, 1)
        self.replay_action = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.replay_action.setObjectName("replay_action")
        self.gridLayout.addWidget(self.replay_action, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.start_recording.clicked.connect(
            self.start_recorder)
        self.stop_recording.clicked.connect(self.stop_recorder)
        self.replay_action.clicked.connect(self.start_replay)
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtWidgets.QApplication.translate(
            "Widget", "Widget", None, -1))
        self.stop_recording.setText(QtWidgets.QApplication.translate(
            "ActionReplay", "Stop Recording", None, -1))
        self.start_recording.setText(QtWidgets.QApplication.translate(
            "ActionReplay", "Record Action", None, -1))
        self.replay_action.setText(QtWidgets.QApplication.translate(
            "ActionReplay", "Replay Action", None, -1))

    def start_recorder(self):
        """Start the ActionRecorder instance"""
        logger.info('GUI initiated recorder start')
        self.action_recorder.start()

    def stop_recorder(self):
        """Stop the ActionRecorder instance"""
        logger.info('GUI initiated recorder stop')
        self.action_recorder.stop()

    def start_replay(self):
        """Start the ActionReplay instance"""
        logger.info('GUI initiated replay start')
        self.action_recorder.stop()
        self.action_replayer.start(self.action_recorder.action_log)


def record_replay():
    Recorder = ActionRecorder()
    try:
        Recorder.start()
        while Recorder.recording:
            time.sleep(1)
        Replayer = ActionReplay()
        Replayer.start(Recorder.action_log)
    except KeyboardInterrupt:
        logger.warning("Keyboard interrupt - application exiting")


def main():
    app = QtWidgets.QApplication([])
    widget_object = QtWidgets.QWidget()
    action_widget = ActionWidget()
    action_widget.setupUi(widget_object)
    logger.info("Starting widget")
    widget_object.show()
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
