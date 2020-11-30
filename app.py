from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from appUI import Ui_MainWindow
import sys
import time
from appModel import Model

# ini program utamanya
class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.model = Model()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.resetMinesweeperButton()

    def debugPrint(self, msg):
        self.debugTextBrowser.append(msg)

    # slot
    def startAIButtonSlot(self):
        self.debugPrint("AI started!")
        self.model.startAI()
        self.model.updater.progress.connect(self.updateUI)
        self.model.updater.start()
        self.unmarkAllMinesweeperButton()

    # slot
    def resetButtonSlot(self):
        self.debugPrint("Resetting minesweeper")
        self.model.program.is_finished = 2
        self.resetMinesweeperButton()
        self.model.bombs = 0
        self.model.size = 4
        self.model.bombLoc = []
        self.bombsLineEdit.setText(str(self.model.bombs))
        self.jumlah_bomLabel.setText(str(self.model.bombs))

    # slot
    def kotakButtonSlot(self, col, row):
        self.debugPrint(f"Kotak {col}:{row} clicked")
        res = self.toggleMarkMinesweeperButton(col, row)
        if res:
            self.model.bombLoc.append((col, row))
            self.model.bombs += 1
        else:
            self.model.bombLoc.remove((col, row))
            self.model.bombs -= 1
        self.bombsLineEdit.setText(str(self.model.bombs))
        self.jumlah_bomLabel.setText(str(self.model.bombs))

    # slot
    def sizeTextChanged(self, size):
        i_size = 4
        try:
            i_size = int(size)
            if i_size < 4:
                i_size = 4
            if i_size > 10:
                i_size = 10
        except:
            i_size = 4
        self.debugPrint(f"size changed to {i_size}")
        delta = i_size - self.model.size
        self.removeAllMinesweeperButton()
        for i in range(i_size):
            for j in range(i_size):
                self.addMinesweeperButton(i, j)
                    
        self.model.size = int(i_size)

    # slot
    def updateUI(self, papan):
        for col, row, nilai_sel, status in papan:
            if status == "closed":
                self.markMinesweeperButton(col, row)
                self.model.bombs -= 1
                self.jumlah_bomLabel.setText(str(self.model.bombs))
            elif nilai_sel == "X":
                continue
            else: #pasti kebuka dan ada nilainya
                self.openMinesweeperButton(col, row, nilai_sel)

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()