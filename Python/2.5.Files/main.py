import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow
import settings

settings.load_data()
app = QApplication(sys.argv)
app.destroyed.connect(settings.save_data)

settings.main_window = MainWindow()
settings.main_window.show()

app.exec()