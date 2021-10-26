import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow
import settings

app = QApplication(sys.argv)
settings.main_window = MainWindow()
settings.main_window.show()

app.exec()