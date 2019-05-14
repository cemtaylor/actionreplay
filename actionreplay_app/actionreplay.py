#!/usr/bin/env python3
import time
import logging
from timeit import default_timer as timer
from pynput import mouse, keyboard


def ActionReplay(actions):
    time.sleep(1)
    logger.info('Replay started')
    for action in actions:
        time.sleep(action['time'])
        if action['key']:
            if action['pressed']:
                keyboard_controller.press(action['key'])
                logger.debug("Key %s Pressed", action['key'])
            else:
                keyboard_controller.release(action['key'])
                logger.debug("Key %s Released", action['key'])
        else:
            if mouse_controller.position != action['pos']:
                mouse_controller.position = action['pos']
                logger.debug("Mouse moved to %s", action['pos'])
            if action['scrollX'] or action['scrollY']:
                mouse_controller.scroll(action['scrollX'], action['scrollY'])
                logger.debug(
                    f"Scrolled {action['scrollX'],action['scrollY']}")
            if action['button']:
                if action['pressed']:
                    mouse_controller.press(action['button'])
                    logger.debug("Mouse button %s Pressed", action['button'])
                else:
                    mouse_controller.release(action['button'])
                    logger.debug(
                        "Mouse button %s Released", action['button'])


class ActionRecorder(object):
    def __init__(self):
        self.action_log = []
        self.last_action = timer()
        self.recording = False
        logger.info('Action Recorder initialized')

    def add_action(self, x=0, y=0, button=None, pressed=False, scrollX=0, scrollY=0, key=None):
        if self.recording == False:
            return
        if key == keyboard.Key.esc:
            logger.info('Escape key detected - Ending recording')
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
            'scrollX': scrollX,
            'scrollY': scrollY,
            'time': action_time
        }
        self.action_log.append(action)

    def log_move(self, x, y):
        self.add_action(x, y)

    def log_click(self, x, y, button, pressed):
        self.add_action(x, y, button=button, pressed=pressed)

    def log_scroll(self, x, y, dx, dy):
        self.add_action(x=x, y=y, scrollX=dx, scrollY=dy)

    def log_key_down(self, key):
        self.add_action(key=key, pressed=True)

    def log_key_up(self, key):
        self.add_action(key=key, pressed=False)

    def start(self):
        self.recording = True
        logger.info('Recording started')

    def stop(self):
        self.recording = False
        logger.info('Recording stopped')


def main():
    try:
        while Recorder.recording:
            time.sleep(1)
        ActionReplay(Recorder.action_log)
    except KeyboardInterrupt:
        logger.warning("Keyboard interrupt - application exiting")


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
    ###
    logger.info('Application started')
    # Create recorder instance
    Recorder = ActionRecorder()
    # Start listeners & create controllers for kb/m
    mouse_listener = mouse.Listener(
        on_move=Recorder.log_move,
        on_click=Recorder.log_click,
        on_scroll=Recorder.log_scroll
    )
    mouse_listener.start()
    logger.info('Mouse listener started')
    mouse_controller = mouse.Controller()

    keyboard_listener = keyboard.Listener(
        on_press=Recorder.log_key_down,
        on_release=Recorder.log_key_up
    )
    keyboard_listener.start()
    logger.info('Keyboard listener started')
    keyboard_controller = keyboard.Controller()
    # Start the recorder
    Recorder.start()
    main()
    logger.info('Application closed')
