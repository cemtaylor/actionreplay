# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'action_replay.ui',
# licensing of 'action_replay.ui' applies.
#
# Created: Fri May 17 11:06:36 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionReplay(object):
    def setupUi(self, ActionReplay):
        ActionReplay.setObjectName("ActionReplay")
        ActionReplay.resize(470, 363)
        ActionReplay.setMouseTracking(False)
        self.save_action = QtWidgets.QPushButton(ActionReplay)
        self.save_action.setGeometry(QtCore.QRect(230, 80, 111, 36))
        self.save_action.setObjectName("save_action")
        self.load_action = QtWidgets.QPushButton(ActionReplay)
        self.load_action.setGeometry(QtCore.QRect(340, 80, 111, 36))
        self.load_action.setObjectName("load_action")
        self.replay_action = QtWidgets.QPushButton(ActionReplay)
        self.replay_action.setGeometry(QtCore.QRect(10, 320, 441, 36))
        self.replay_action.setObjectName("replay_action")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ActionReplay)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 229, 242))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_recording = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.start_recording.setAutoDefault(True)
        self.start_recording.setDefault(True)
        self.start_recording.setFlat(False)
        self.start_recording.setObjectName("start_recording")
        self.verticalLayout_2.addWidget(self.start_recording)
        self.stop_recording = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stop_recording.setObjectName("stop_recording")
        self.verticalLayout_2.addWidget(self.stop_recording)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.record_move = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.record_move.setChecked(True)
        self.record_move.setObjectName("record_move")
        self.verticalLayout.addWidget(self.record_move)
        self.record_click = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.record_click.setChecked(True)
        self.record_click.setObjectName("record_click")
        self.verticalLayout.addWidget(self.record_click)
        self.record_scroll = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.record_scroll.setChecked(True)
        self.record_scroll.setObjectName("record_scroll")
        self.verticalLayout.addWidget(self.record_scroll)
        self.record_keydown = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.record_keydown.setChecked(True)
        self.record_keydown.setObjectName("record_keydown")
        self.verticalLayout.addWidget(self.record_keydown)
        self.record_keyup = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.record_keyup.setChecked(True)
        self.record_keyup.setObjectName("record_keyup")
        self.verticalLayout.addWidget(self.record_keyup)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.quick_save_action = QtWidgets.QPushButton(ActionReplay)
        self.quick_save_action.setGeometry(QtCore.QRect(230, 20, 92, 36))
        self.quick_save_action.setObjectName("quick_save_action")
        self.quick_load_action = QtWidgets.QPushButton(ActionReplay)
        self.quick_load_action.setGeometry(QtCore.QRect(360, 20, 92, 36))
        self.quick_load_action.setObjectName("quick_load_action")

        self.retranslateUi(ActionReplay)
        QtCore.QMetaObject.connectSlotsByName(ActionReplay)

    def retranslateUi(self, ActionReplay):
        ActionReplay.setWindowTitle(QtWidgets.QApplication.translate("ActionReplay", "ActionReplay", None, -1))
        self.save_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Save Action", None, -1))
        self.load_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Load Action", None, -1))
        self.replay_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Replay Action", None, -1))
        self.start_recording.setText(QtWidgets.QApplication.translate("ActionReplay", "Record Action", None, -1))
        self.stop_recording.setText(QtWidgets.QApplication.translate("ActionReplay", "Stop Recording", None, -1))
        self.record_move.setText(QtWidgets.QApplication.translate("ActionReplay", "Mouse Movement", None, -1))
        self.record_click.setText(QtWidgets.QApplication.translate("ActionReplay", "Mouse Clicks", None, -1))
        self.record_scroll.setText(QtWidgets.QApplication.translate("ActionReplay", "Mouse Scroll", None, -1))
        self.record_keydown.setText(QtWidgets.QApplication.translate("ActionReplay", "Key Down", None, -1))
        self.record_keyup.setText(QtWidgets.QApplication.translate("ActionReplay", "Key Up", None, -1))
        self.quick_save_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Quick Save", None, -1))
        self.quick_load_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Quick Load", None, -1))

