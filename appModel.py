from PyQt5.QtCore import QThread, pyqtSignal
import threading
import time
from program import MainProgram

# Model: pengkoneksi UI dengan program aslinya
class Model:
    def __init__(self):
        self.size = 4
        self.bombs = 0
        self.bombLoc = []
        self.program = None
        self.updater = None
        self.programThread = None

    def startAI(self):
        self.program = MainProgram()
        self.program.ukuran = self.size
        self.program.jumlah_bom = self.bombs
        self.program.bombLoc = self.bombLoc
        self.programThread = threading.Thread(
            target=self.program.main
        )
        self.programThread.start()
        self.updater = checkFromProgram(self)

class checkFromProgram(QThread):
    progress = pyqtSignal(list)

    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self):
        print("run")
        while self.model.program.is_finished == 0:
            time.sleep(0.1)
        print("setup finished")
        while not self.model.program.is_finished == 2:
            time.sleep(0.1)
            self.progress.emit(self.model.program.updatePapanBasedOnFacts())