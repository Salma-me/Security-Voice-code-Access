# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task5UImanar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 977)
        MainWindow.setStyleSheet("QMainWindow, QDialog{\n"
"    /*background-color: rgb(231, 237, 255);*/\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"/*-------------------------------------------------------------------*/\n"
"QMenuBar,QMenuBar::item {\n"
"    color: white;\n"
"  /*    background-color: rgb(100, 0, 150); /* main background color \n"
"    background-color: rgb(186, 180, 200);*/\n"
"    background-color: rgb(170, 165, 194);\n"
"}\n"
"\n"
"QMenu,QMenu::item {\n"
"    color: black;\n"
"    background-color: white;\n"
"    margin: 1px;\n"
"    padding: 1px;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QMenuBar::item:selected,QMenuBar::item:pressed,\n"
"QMenu::item:selected,QMenu::item:pressed {\n"
"    color: white;\n"
"    background-color: rgb(90, 0, 155);\n"
"}\n"
"\n"
"/*-------------------------------------------------------------------*/\n"
"QListWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(127, 64, 191);\n"
"    padding-top: 12px;\n"
"    padding-bottom: 12px;\n"
"/*    padding-right: 5px;\n"
"    padding-left: 5px;*/\n"
"}\n"
"\n"
"QListWidget::item{\n"
"    padding: 2px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    border-bottom: 2px solid rgb(127, 64, 191);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"/*    background: rgb(211, 196, 255);*/\n"
"    background-color: rgba(114, 0, 214,255);\n"
"    border-radius: 6px;    \n"
"    color: white;\n"
"}\n"
"\n"
"QListWidget::item:disabled,\n"
"QListWidget::item:disabled:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"/*-------------------------------------------------------------------*/\n"
"QPushButton{\n"
"    margin-top: 5px;\n"
"    border: 1px solid white;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton::hover{\n"
"    /*background-color: rgb(114, 0, 214);*/\n"
"    border: 1.5px solid;\n"
"    border-color: rgb(140, 0, 210);\n"
"}\n"
"QPushButton::pressed{\n"
"    /*background-color: rgb(114, 0, 214);*/\n"
"    border: 4px solid;\n"
"    border-color: rgb(70, 0, 105);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(50, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setEnabled(False)
        self.toolButton_2.setAutoFillBackground(False)
        self.toolButton_2.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.toolButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icons/main.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_7.addWidget(self.toolButton_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("PT Simple Bold Ruled")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(70, 0, 105);\n"
"border: 1px solid rgb(70, 0, 105);\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_13.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(70, 0, 105);\n"
"border: 1px solid rgb(70, 0, 105);\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_13.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_5_ac_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_5_ac_2.setMinimumSize(QtCore.QSize(100, 120))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5_ac_2.setFont(font)
        self.label_5_ac_2.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(127, 64, 191);\n"
"color: rgb(70, 0, 105);")
        self.label_5_ac_2.setText("")
        self.label_5_ac_2.setScaledContents(False)
        self.label_5_ac_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5_ac_2.setObjectName("label_5_ac_2")
        self.gridLayout_13.addWidget(self.label_5_ac_2, 3, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.pushButton_record = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_record.setMinimumSize(QtCore.QSize(120, 116))
        self.pushButton_record.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_record.setFont(font)
        self.pushButton_record.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_record.setStyleSheet("/*margin-top: 5px;\n"
"border: 1px solid white;\n"
"border-radius: 40px;*/")
        self.pushButton_record.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_record.setIcon(icon1)
        self.pushButton_record.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_record.setFlat(False)
        self.pushButton_record.setObjectName("pushButton_record")
        self.gridLayout_2.addWidget(self.pushButton_record, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setMinimumSize(QtCore.QSize(400, 515))
        self.label_status.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(127, 64, 191);")
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.gridLayout_13.addWidget(self.label_status, 1, 0, 1, 1)
        self.gridLayout_13.setRowStretch(1, 3)
        self.gridLayout_13.setRowStretch(3, 1)
        self.gridLayout_3.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(70, 0, 105);\n"
"border: 1px solid rgb(70, 0, 105);\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.graphicsView_similarity = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_similarity.setMinimumSize(QtCore.QSize(600, 300))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(9)
        self.graphicsView_similarity.setFont(font)
        self.graphicsView_similarity.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(127, 64, 191);")
        self.graphicsView_similarity.setObjectName("graphicsView_similarity")
        self.gridLayout_5.addWidget(self.graphicsView_similarity, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(70, 0, 105);\n"
"border: 1px solid rgb(70, 0, 105);\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.widget_spectrogram = QtWidgets.QWidget(self.centralwidget)
        self.widget_spectrogram.setMinimumSize(QtCore.QSize(600, 300))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(9)
        self.widget_spectrogram.setFont(font)
        self.widget_spectrogram.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(127, 64, 191);")
        self.widget_spectrogram.setObjectName("widget_spectrogram")
        self.gridLayout.addWidget(self.widget_spectrogram, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.listWidget_persons = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_persons.setEnabled(True)
        self.listWidget_persons.setMinimumSize(QtCore.QSize(0, 70))
        self.listWidget_persons.setMaximumSize(QtCore.QSize(16777215, 86))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_persons.setFont(font)
        self.listWidget_persons.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget_persons.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(127, 64, 191);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"")
        self.listWidget_persons.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_persons.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_persons.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget_persons.setAutoScrollMargin(16)
        self.listWidget_persons.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget_persons.setProperty("showDropIndicator", False)
        self.listWidget_persons.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget_persons.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listWidget_persons.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_persons.setMovement(QtWidgets.QListView.Static)
        self.listWidget_persons.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget_persons.setProperty("isWrapping", True)
        self.listWidget_persons.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_persons.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget_persons.setModelColumn(0)
        self.listWidget_persons.setUniformItemSizes(False)
        self.listWidget_persons.setWordWrap(False)
        self.listWidget_persons.setSelectionRectVisible(False)
        self.listWidget_persons.setItemAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.setObjectName("listWidget_persons")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_persons.addItem(item)
        self.gridLayout_4.addWidget(self.listWidget_persons, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("padding-left: 10px;\n"
"color: rgb(70, 0, 105);")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 26))
        self.menubar.setObjectName("menubar")
        self.menuSecurity_Mood = QtWidgets.QMenu(self.menubar)
        self.menuSecurity_Mood.setObjectName("menuSecurity_Mood")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionvoice_code = QtWidgets.QAction(MainWindow)
        self.actionvoice_code.setObjectName("actionvoice_code")
        self.actionVoice_fingerprint = QtWidgets.QAction(MainWindow)
        self.actionVoice_fingerprint.setObjectName("actionVoice_fingerprint")
        self.menuSecurity_Mood.addAction(self.actionvoice_code)
        self.menuSecurity_Mood.addAction(self.actionVoice_fingerprint)
        self.menubar.addAction(self.menuSecurity_Mood.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Voice Security System"))
        self.label_6.setText(_translate("MainWindow", "Access Status"))
        self.label_5.setText(_translate("MainWindow", "Results"))
        self.label_4.setText(_translate("MainWindow", "Similarity Analysis"))
        self.label_2.setText(_translate("MainWindow", "Your Spectrogram"))
        self.listWidget_persons.setSortingEnabled(False)
        __sortingEnabled = self.listWidget_persons.isSortingEnabled()
        self.listWidget_persons.setSortingEnabled(False)
        item = self.listWidget_persons.item(0)
        item.setText(_translate("MainWindow", "Sarah"))
        item = self.listWidget_persons.item(1)
        item.setText(_translate("MainWindow", "Manar"))
        item = self.listWidget_persons.item(2)
        item.setText(_translate("MainWindow", "Salma"))
        item = self.listWidget_persons.item(3)
        item.setText(_translate("MainWindow", "Yasmeen"))
        item = self.listWidget_persons.item(4)
        item.setText(_translate("MainWindow", "name 5"))
        item = self.listWidget_persons.item(5)
        item.setText(_translate("MainWindow", "name 6"))
        item = self.listWidget_persons.item(6)
        item.setText(_translate("MainWindow", "name 7"))
        item = self.listWidget_persons.item(7)
        item.setText(_translate("MainWindow", "name 8"))
        self.listWidget_persons.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Select the allowed persons:"))
        self.menuSecurity_Mood.setTitle(_translate("MainWindow", "Security Mood"))
        self.actionvoice_code.setText(_translate("MainWindow", "Voice fingerprint"))
        self.actionVoice_fingerprint.setText(_translate("MainWindow", "Voice code"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
