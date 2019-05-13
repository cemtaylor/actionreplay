#!/usr/bin/env python3
import pyautogui
import time
from pymouse import PyMouse, PyMouseEvent  # pyuserinput
from pykeyboard import PyKeyboard  # pyuserinput


def replay(actions):
    for i in range(len(actions)):
        action = actions[i]
        try:
            if action['click'] and actions[i+1]['click']:
                pyautogui.dragTo(action['pos'])
            else:
                pyautogui.moveTo(action['pos'])
                if action['click']:
                    pyautogui.click(action['pos'], button='left', clicks=1)
        except IndexError:
            pass


class FinishRecording(Exception):
    pass


class Record(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.down = False
        self.action_log = []

    def move(self, x, y):
        action = {'pos': (x, y), 'click': self.down}
        self.action_log.append(action)

    def click(self, x, y, button, press):
        if button == 1:
            if press:
                self.down = True
                action = {'pos': (x, y), 'click': self.down}
                self.action_log.append(action)
            else:
                self.down = False
        else:
            # Exit if any other mouse button used
            # This self.stop() should work but it traps us in the recorder class
            # we raise an exception instead.
            # self.stop()
            raise FinishRecording("Finished recording")


R = Record()
R.daemon = True
try:
    R.run()
    print("this is a daemon")
except FinishRecording:
    print("Run complete")
    input("anything to replay\n")
    time.sleep(2)
    replay(R.action_log)
