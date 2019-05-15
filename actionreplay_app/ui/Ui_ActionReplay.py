# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'action_replay.ui',
# licensing of 'action_replay.ui' applies.
#
# Created: Wed May 15 13:03:55 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionReplay(object):
    def setupUi(self, ActionReplay):
        ActionReplay.setObjectName("ActionReplay")
        ActionReplay.resize(400, 300)
        ActionReplay.setMouseTracking(False)
        self.gridLayoutWidget = QtWidgets.QWidget(ActionReplay)
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)

        self.retranslateUi(ActionReplay)
        QtCore.QMetaObject.connectSlotsByName(ActionReplay)

    def retranslateUi(self, ActionReplay):
        ActionReplay.setWindowTitle(QtWidgets.QApplication.translate("ActionReplay", "ActionReplay", None, -1))
        self.stop_recording.setText(QtWidgets.QApplication.translate("ActionReplay", "Stop Recording", None, -1))
        self.start_recording.setText(QtWidgets.QApplication.translate("ActionReplay", "Record Action", None, -1))
        self.replay_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Replay Action", None, -1))

