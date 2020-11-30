# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        self.msButtons = {}
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.msFrame = QtWidgets.QFrame(self.centralwidget)
        self.msFrame.setMinimumSize(QtCore.QSize(200, 480))
        self.msFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msFrame.setObjectName("msFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.msFrame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 177, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(93, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.petakGridLayout = QtWidgets.QGridLayout()
        self.petakGridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.petakGridLayout.setSpacing(0)
        self.petakGridLayout.setObjectName("petakGridLayout")
        self.gridLayout.addLayout(self.petakGridLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 177, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.msFrame)
        self.sidebarFrame = QtWidgets.QFrame(self.centralwidget)
        self.sidebarFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sidebarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebarFrame.setObjectName("sidebarFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sidebarFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLabel = QtWidgets.QLabel(self.sidebarFrame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.initialInputFrame = QtWidgets.QFrame(self.sidebarFrame)
        self.initialInputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.initialInputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.initialInputFrame.setObjectName("initialInputFrame")
        self.formLayout = QtWidgets.QFormLayout(self.initialInputFrame)
        self.formLayout.setObjectName("formLayout")
        self.sizeLabel = QtWidgets.QLabel(self.initialInputFrame)
        self.sizeLabel.setObjectName("sizeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sizeLabel)
        self.sizeLineEdit = QtWidgets.QLineEdit(self.initialInputFrame)
        self.sizeLineEdit.setObjectName("sizeLineEdit")
        self.sizeLineEdit.setText("4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sizeLineEdit)
        self.bombsLineEdit = QtWidgets.QLineEdit(self.initialInputFrame)
        self.bombsLineEdit.setObjectName("bombsLineEdit")
        self.bombsLineEdit.setReadOnly(True)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bombsLineEdit)
        self.bombsLabel = QtWidgets.QLabel(self.initialInputFrame)
        self.bombsLabel.setObjectName("bombsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bombsLabel)
        self.verticalLayout_2.addWidget(self.initialInputFrame)
        self.startAIButton = QtWidgets.QPushButton(self.sidebarFrame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.startAIButton.setFont(font)
        self.startAIButton.setObjectName("startAIButton")
        self.verticalLayout_2.addWidget(self.startAIButton)
        self.bombsLeftFrame = QtWidgets.QFrame(self.sidebarFrame)
        self.bombsLeftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bombsLeftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bombsLeftFrame.setObjectName("bombsLeftFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bombsLeftFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bombsLeftLabel = QtWidgets.QLabel(self.bombsLeftFrame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.bombsLeftLabel.setFont(font)
        self.bombsLeftLabel.setObjectName("bombsLeftLabel")
        self.horizontalLayout_2.addWidget(self.bombsLeftLabel)
        self.jumlah_bomLabel = QtWidgets.QLabel(self.bombsLeftFrame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.jumlah_bomLabel.setFont(font)
        self.jumlah_bomLabel.setObjectName("jumlah_bomLabel")
        self.horizontalLayout_2.addWidget(self.jumlah_bomLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.bombsLeftFrame)
        self.debugFrame = QtWidgets.QFrame(self.sidebarFrame)
        self.debugFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.debugFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.debugFrame.setObjectName("debugFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.debugFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.debugLabel = QtWidgets.QLabel(self.debugFrame)
        self.debugLabel.setObjectName("debugLabel")
        self.verticalLayout.addWidget(self.debugLabel)
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.debugFrame)
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.verticalLayout.addWidget(self.debugTextBrowser)
        self.resetButton = QtWidgets.QPushButton(self.debugFrame)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout.addWidget(self.resetButton)
        self.verticalLayout_2.addWidget(self.debugFrame)
        self.horizontalLayout.addWidget(self.sidebarFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.startAIButton.clicked.connect(self.startAIButtonSlot)
        self.sizeLineEdit.returnPressed.connect(lambda: self.sizeTextChanged(self.sizeLineEdit.text()))
        self.resetButton.clicked.connect(self.resetButtonSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Minesweeper AI"))
        self.sizeLabel.setText(_translate("MainWindow", "Size"))
        self.sizeLineEdit.setPlaceholderText(_translate("MainWindow", "Enter Minesweeper size here..."))
        self.bombsLineEdit.setPlaceholderText(_translate("MainWindow", "Click a square enter bomb location"))
        self.bombsLabel.setText(_translate("MainWindow", "Bombs"))
        self.startAIButton.setText(_translate("MainWindow", "Start AI!"))
        self.bombsLeftLabel.setText(_translate("MainWindow", "Bombs left:"))
        self.jumlah_bomLabel.setText(_translate("MainWindow", "0"))
        self.debugLabel.setText(_translate("MainWindow", "AI Output"))
        self.resetButton.setText(_translate("MainWindow", "Reset Minesweeper"))

    def addMinesweeperButton(self, col, row):
        # id is string in format "col;row" eg. "0;0"
        id = f"{col};{row}"
        petakButton = QtWidgets.QPushButton(self.msFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(petakButton.sizePolicy().hasHeightForWidth())
        petakButton.setSizePolicy(sizePolicy)
        petakButton.setMinimumSize(QtCore.QSize(40, 40))
        petakButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(13)
        petakButton.setFont(font)
        petakButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        petakButton.setObjectName(f"petakButton:{id}")
        petakButton.setText("")
        petakButton.clicked.connect(lambda : self.kotakButtonSlot(col, row))
        self.petakGridLayout.addWidget(petakButton, col, row, 1, 1)
        self.msButtons[id] = petakButton

    def removeMinesweeperButton(self, col, row):
        id = f"{col};{row}"
        petakButton = self.msButtons[id]
        self.petakGridLayout.removeWidget(petakButton)
        petakButton.deleteLater()
        self.msButtons[id] = None

    def removeAllMinesweeperButton(self):
        for id, petakButton in self.msButtons.items():
            if not petakButton:
                continue
            col, row = id.split(";")
            col = int(col)
            row = int(row)
            self.removeMinesweeperButton(col, row)

    def resetMinesweeperButton(self):
        self.removeAllMinesweeperButton()
        for i in range(4):
            for j in range(4):
                self.addMinesweeperButton(i,j)

    def openMinesweeperButton(self, col, row, nilai):
        id = f"{col};{row}"
        petakButton = self.msButtons[id]
        petakButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        petakButton.setStyleSheet("background-color : white")
        petakButton.setText(str(nilai))
        petakButton.setEnabled(False)

    def markMinesweeperButton(self, col, row):
        id = f"{col};{row}"
        petakButton = self.msButtons[id]
        petakButton.setText("💣")

    def unmarkMinesweeperButton(self, col, row):
        id = f"{col};{row}"
        petakButton = self.msButtons[id]
        petakButton.setText("")

    def toggleMarkMinesweeperButton(self, col, row):
        id = f"{col};{row}"
        petakButton = self.msButtons[id]
        if petakButton.text() == "":
            self.markMinesweeperButton(col, row)
            return True
        else:
            self.unmarkMinesweeperButton(col, row)
            return False

    def unmarkAllMinesweeperButton(self):
        for id, petakButton in self.msButtons.items():
            if not petakButton:
                continue
            if petakButton.text() == "":
                continue
            col, row = id.split(";")
            col = int(col)
            row = int(row)
            self.unmarkMinesweeperButton(col, row)

    @pyqtSlot()
    def startAIButtonSlot(self):
        pass

    @pyqtSlot()
    def resetButtonSlot(self):
        pass

    @pyqtSlot()
    def kotakButtonSlot(self, col, row):
        pass

    @pyqtSlot()
    def sizeTextChanged(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
