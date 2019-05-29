# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'action_replay.ui',
# licensing of 'action_replay.ui' applies.
#
# Created: Wed May 22 15:43:47 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionReplay(object):
    def setupUi(self, ActionReplay):
        ActionReplay.setObjectName("ActionReplay")
        ActionReplay.resize(469, 407)
        ActionReplay.setMouseTracking(False)
        ActionReplay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ActionReplay)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 163, 170))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_recording = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.start_recording.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.start_recording.setAutoDefault(True)
        self.start_recording.setDefault(True)
        self.start_recording.setFlat(False)
        self.start_recording.setObjectName("start_recording")
        self.verticalLayout_2.addWidget(self.start_recording)
        self.stop_recording = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stop_recording.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.stop_recording.setObjectName("stop_recording")
        self.verticalLayout_2.addWidget(self.stop_recording)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.draw_action = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.draw_action.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.draw_action.setObjectName("draw_action")
        self.verticalLayout_3.addWidget(self.draw_action)
        self.replay_action = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.replay_action.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.replay_action.setObjectName("replay_action")
        self.verticalLayout_3.addWidget(self.replay_action)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.load_action = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.load_action.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.load_action.setObjectName("load_action")
        self.horizontalLayout_2.addWidget(self.load_action)
        self.save_action = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.save_action.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.save_action.setObjectName("save_action")
        self.horizontalLayout_2.addWidget(self.save_action)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quick_load_action = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.quick_load_action.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.quick_load_action.setObjectName("quick_load_action")
        self.horizontalLayout.addWidget(self.quick_load_action)
        self.quick_save_action = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.quick_save_action.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.quick_save_action.setObjectName("quick_save_action")
        self.horizontalLayout.addWidget(self.quick_save_action)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.list_saved_actions = QtWidgets.QListWidget(ActionReplay)
        self.list_saved_actions.setGeometry(QtCore.QRect(170, 0, 291, 401))
        self.list_saved_actions.setStyleSheet("border-radius: 0px;\n"
"border: 1px solid rgb(186, 189, 182);")
        self.list_saved_actions.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.list_saved_actions.setTextElideMode(QtCore.Qt.ElideRight)
        self.list_saved_actions.setWordWrap(True)
        self.list_saved_actions.setObjectName("list_saved_actions")
        self.widget = QtWidgets.QWidget(ActionReplay)
        self.widget.setGeometry(QtCore.QRect(0, 180, 161, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.record_move = QtWidgets.QCheckBox(self.widget)
        self.record_move.setStyleSheet("")
        self.record_move.setChecked(True)
        self.record_move.setObjectName("record_move")
        self.verticalLayout.addWidget(self.record_move)
        self.record_click = QtWidgets.QCheckBox(self.widget)
        self.record_click.setChecked(True)
        self.record_click.setObjectName("record_click")
        self.verticalLayout.addWidget(self.record_click)
        self.record_scroll = QtWidgets.QCheckBox(self.widget)
        self.record_scroll.setChecked(True)
        self.record_scroll.setObjectName("record_scroll")
        self.verticalLayout.addWidget(self.record_scroll)
        self.record_keydown = QtWidgets.QCheckBox(self.widget)
        self.record_keydown.setChecked(True)
        self.record_keydown.setObjectName("record_keydown")
        self.verticalLayout.addWidget(self.record_keydown)
        self.record_keyup = QtWidgets.QCheckBox(self.widget)
        self.record_keyup.setChecked(True)
        self.record_keyup.setObjectName("record_keyup")
        self.verticalLayout.addWidget(self.record_keyup)

        self.retranslateUi(ActionReplay)
        QtCore.QMetaObject.connectSlotsByName(ActionReplay)

    def retranslateUi(self, ActionReplay):
        ActionReplay.setWindowTitle(QtWidgets.QApplication.translate("ActionReplay", "ActionReplay", None, -1))
        self.start_recording.setText(QtWidgets.QApplication.translate("ActionReplay", "Record Action", None, -1))
        self.stop_recording.setText(QtWidgets.QApplication.translate("ActionReplay", "Stop Recording", None, -1))
        self.draw_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Draw Action", None, -1))
        self.replay_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Replay Action", None, -1))
        self.load_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Load Action", None, -1))
        self.save_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Save Action", None, -1))
        self.quick_load_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Quick Load", None, -1))
        self.quick_save_action.setText(QtWidgets.QApplication.translate("ActionReplay", "Quick Save", None, -1))
        self.list_saved_actions.setSortingEnabled(True)
        self.record_move.setText(QtWidgets.QApplication.translate("ActionReplay", "Mouse Movement", None, -1))
        self.record_click.setText(QtWidgets.QApplication.translate("ActionReplay", "Mouse Clicks", None, -1))
        self.record_scroll.setText(QtWidgets.QApplication.translate("ActionReplay", "Mouse Scroll", None, -1))
        self.record_keydown.setText(QtWidgets.QApplication.translate("ActionReplay", "Key Down", None, -1))
        self.record_keyup.setText(QtWidgets.QApplication.translate("ActionReplay", "Key Up", None, -1))

