import os
from datetime import date

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import  QWidget, QPushButton, QLabel

from styles import *
import settings
from settings_window import SettingsWindow

btn_w = 76
btn_h = 57

waste = ""

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setFixedSize(300, 500)
        self.setWindowTitle("Выживем?")
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")

        titile_font = QFont('Verdana', 20, QFont.Weight.Bold)
        subtitle_font = QFont('Roboto', 11, QFont.Weight.Normal)

        # Сколько можно потратить
        self.money_label = QLabel(f"{settings.money}", self)
        self.money_label.setGeometry(0, 35, 300, 50)
        self.money_label.setStyleSheet(TextStyles.title())
        self.money_label.setFont(titile_font)

        # На сегодня
        self.top_label = QLabel("На сегодня", self)
        self.top_label.setGeometry(0, 80, 300, 15)
        self.top_label.setStyleSheet(TextStyles.subtitle())
        self.top_label.setFont(subtitle_font)

        # Потрачено
        self.waste_label = QLabel(f"Потрачено:\n{waste}", self)
        self.waste_label.setGeometry(0, 130, 300, 140)
        self.waste_label.setStyleSheet(TextStyles.wasted())
        self.waste_label.setFont(titile_font)

        # Кнопки
        self.zeroButton = QPushButton("0", self)
        self.zeroButton.setGeometry(0, 440, btn_w * 2, btn_h)
        self.zeroButton.setStyleSheet(ButtonStyles.base())
        self.zeroButton.clicked.connect(lambda: self.button_click("0"))

        self.dotButton = QPushButton(".", self)
        self.dotButton.setGeometry(152, 440, btn_w, btn_h)
        self.dotButton.setStyleSheet(ButtonStyles.base())
        self.dotButton.clicked.connect(lambda: self.button_click("."))

        self.enterButton = QPushButton("↵", self)
        self.enterButton.setGeometry(227, 326, 76, btn_h * 3)
        self.enterButton.setStyleSheet(ButtonStyles.enter())
        self.enterButton.clicked.connect(lambda: self.button_click("↵"))

        self.deleteButton = QPushButton("\u2190", self)
        self.deleteButton.setGeometry(227, 269, btn_w, btn_h)
        self.deleteButton.setStyleSheet(ButtonStyles.delete())
        self.deleteButton.clicked.connect(lambda: self.button_click("\u2190"))

        self.oneButton = QPushButton("1", self)
        self.oneButton.setGeometry(0, 383, btn_w, btn_h)
        self.oneButton.setStyleSheet(ButtonStyles.base())
        self.oneButton.clicked.connect(lambda: self.button_click("1"))

        self.twoButton = QPushButton("2", self)
        self.twoButton.setGeometry(76, 383, btn_w, btn_h)
        self.twoButton.setStyleSheet(ButtonStyles.base())
        self.twoButton.clicked.connect(lambda: self.button_click("2"))

        self.threeButton = QPushButton("3", self)
        self.threeButton.setGeometry(152, 383, btn_w, btn_h)
        self.threeButton.setStyleSheet(ButtonStyles.base())
        self.threeButton.clicked.connect(lambda: self.button_click("3"))

        self.fourButton = QPushButton("4", self)
        self.fourButton.setGeometry(0, 326, btn_w, btn_h)
        self.fourButton.setStyleSheet(ButtonStyles.base())
        self.fourButton.clicked.connect(lambda: self.button_click("4"))

        self.fiveButton = QPushButton("5", self)
        self.fiveButton.setGeometry(76, 326, btn_w, btn_h)
        self.fiveButton.setStyleSheet(ButtonStyles.base())
        self.fiveButton.clicked.connect(lambda: self.button_click("5"))

        self.sixButton = QPushButton("6", self)
        self.sixButton.setGeometry(152, 326, btn_w, btn_h)
        self.sixButton.setStyleSheet(ButtonStyles.base())
        self.sixButton.clicked.connect(lambda: self.button_click("6"))

        self.sevenButton = QPushButton("7", self)
        self.sevenButton.setGeometry(0, 269, btn_w, btn_h)
        self.sevenButton.setStyleSheet(ButtonStyles.base())
        self.sevenButton.clicked.connect(lambda: self.button_click("7"))

        self.eightButton = QPushButton("8", self)
        self.eightButton.setGeometry(76, 269, btn_w, btn_h)
        self.eightButton.setStyleSheet(ButtonStyles.base())
        self.eightButton.clicked.connect(lambda: self.button_click("8"))

        self.nineButton = QPushButton("9", self)
        self.nineButton.setGeometry(152, 269, btn_w, btn_h)
        self.nineButton.setStyleSheet(ButtonStyles.base())
        self.nineButton.clicked.connect(lambda: self.button_click("9"))

        self.settingsButton = QPushButton("", self)
        self.settingsButton.setGeometry(270, 0, 30, 30)
        self.settingsButton.setStyleSheet(ButtonStyles.settings())
        self.settingsButton.setIcon(QIcon(os.path.dirname(__file__) + "/settings.png"))
        self.settingsButton.clicked.connect(self.settings_click)

    def keyPressEvent(self, event):
        if 48 <= event.key() <= 57:
            # Нажата цифра
            self.button_click(chr(event.key()))

        elif event.key() == 46:
            # Нажата точка
            self.button_click(".")

        elif event.key() == 16777219:
            # Нажат backspace
            self.button_click("\u2190")

        elif event.key() == 16777220:
            # Нажат enter
            self.button_click("↵")


    def button_click(self, char):
        global waste

        if char == "\u2190":
            waste = waste[:-1]
        elif char == "↵":
            try:
                waste = float(waste)
            except ValueError:
                print("Число введено неверно")
            else:
                if waste > 0:
                    settings.money -= waste
                    settings.wastes.append(f"{date.today()} - {waste}")
                    self.money_label.setText(f"{round(settings.money,2)}")
            finally:
                waste = ""
        else:
            waste+= char

        self.waste_label.setText(f"Потрачено:\n{waste}")

    def settings_click(self):
        self.settings = SettingsWindow()
        self.close()

