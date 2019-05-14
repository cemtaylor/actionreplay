#!/usr/bin/env python3
import time
from timeit import default_timer as timer
from pynput import mouse, keyboard


def log_move(x, y):
    action_log.append(x, y)


def log_click(x, y, button, pressed):
    action_log.append(x, y, button=button, pressed=pressed)


def log_scroll(x, y, dx, dy):
    action_log.append(x=x, y=y, scrollX=dx, scrollY=dy)


def log_key_down(key):
    action_log.append(key=key, pressed=True)


def log_key_up(key):
    action_log.append(key=key, pressed=False)


def replay(actions):
    for action in actions:
        time.sleep(action['time'])
        if action['key']:
            if action['pressed']:
                keyboard_controller.press(action['key'])
                print(f"Key: {action['key']} Pressed")
            else:
                keyboard_controller.release(action['key'])
                print(f"Key: {action['key']} Released")
        else:
            mouse_controller.position = action['pos']
            print(f"Mouse moved to: {action['pos']}")
            if action['button']:
                print(f"Mouse button: {action['button']}")
                if action['pressed']:
                    mouse_controller.press(action['button'])
                    print(f"Mouse button: {action['button']} Pressed")
                else:
                    mouse_controller.release(action['button'])
                    print(f"Mouse button: {action['button']} Released")


class ActionLog(object):
    def __init__(self):
        self.action_log = []
        self.last_action = timer()
        self.recording = True

    def append(self, x=0, y=0, button=None, pressed=False, scrollX=0, scrollY=0, key=None):
        if self.recording == False:
            return
        if key == keyboard.Key.esc:
            print("User entered escape - ending recording")
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


def main():
    try:
        while action_log.recording:
            pass
        print("REPLAYING ACTIONS")
        replay(action_log.action_log)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    action_log = ActionLog()
    mouse_listener = mouse.Listener(
        on_move=log_move,
        on_click=log_click,
        on_scroll=log_scroll
    )
    mouse_listener.start()
    mouse_controller = mouse.Controller()

    keyboard_listener = keyboard.Listener(
        on_press=log_key_down,
        on_release=log_key_up
    )
    keyboard_listener.start()
    keyboard_controller = keyboard.Controller()
    print("Recording Active")
    main()
    print("Ended")
