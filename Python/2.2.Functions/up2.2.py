from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

btn_w = 76
btn_h = 57

BACKGROUND_COLOR = "rgb(0, 0, 0)"
DESCRIPTION_TEXT_COLOR = "rgb(172, 172, 172)"
BASE_TEXT_COLOR = "rgb(255, 255, 255)"
ACCENT_COLOR = "rgb(255, 170, 0)"

money = 769
waste = ""
wastes = []

class ButtonStyles:
    def delete():
        return """
        QPushButton {
            background-color: rgb(200, 200, 200);
            font-size: 25px;
            padding-bottom: 5px;
            border: 1px solid rgb(150, 150, 150);
        }
        QPushButton:hover:pressed {
            background-color: rgb(172, 172, 172);
        }
        """

    def base():
        return """
        QPushButton {
            background-color: rgb(255, 255, 255);
            border: 1px solid rgb(150, 150, 150);
            font-family: 'Roboto', sans-serif;
            font-size: 15px;
        }
        QPushButton:hover:pressed {
            background-color: rgb(172, 172, 172);
        }
        """

    def enter():
        return """
        QPushButton {
            background-color: rgb(255, 170, 0);
            border: 1px solid rgb(150, 150, 150);
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            font-size: 40px;
            padding-top: 80px;
        }
        QPushButton:hover:pressed {
            background-color: rgb(230, 150, 0);
        }
        """

class TextStyles:

    def title():
        return """
        color: rgb(255, 255, 255);
        padding-left: 10px;
        border-top: 1px solid rgba(60,60,60, .8);
        """

    def subtitle():
        return """
        color: rgb(172, 172, 172);
        padding-left: 17px;
        """

    def wasted():
        return """
        color: rgb(255, 255, 255);
        padding-left: 10px;
        border-top: 1px solid rgba(60,60,60, .8);
        """

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setFixedSize(300, 500)
        self.setWindowTitle("???????????????")
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")

        titile_font = QFont('Verdana', 20, QFont.Weight.Bold)
        subtitle_font = QFont('Roboto', 11, QFont.Weight.Normal)

        # ?????????????? ?????????? ??????????????????
        self.money_label = QLabel(f"{money}", self)
        self.money_label.setGeometry(0, 25, 300, 80)
        self.money_label.setStyleSheet(TextStyles.title())
        self.money_label.setFont(titile_font)

        # ???? ??????????????
        self.top_label = QLabel("???? ??????????????", self)
        self.top_label.setGeometry(0, 80, 300, 15)
        self.top_label.setStyleSheet(TextStyles.subtitle())
        self.top_label.setFont(subtitle_font)

        # ??????????????????
        self.waste_label = QLabel(f"??????????????????: \n{waste}", self)
        self.waste_label.setGeometry(0, 130, 300, 140)
        self.waste_label.setStyleSheet(TextStyles.wasted())
        self.waste_label.setFont(titile_font)

        # ????????????
        self.zeroButton = QPushButton("0", self)
        self.zeroButton.setGeometry(0, 440, btn_w * 2, btn_h)
        self.zeroButton.setStyleSheet(ButtonStyles.base())
        self.zeroButton.clicked.connect(lambda: self.button_click("0"))

        self.dotButton = QPushButton(".", self)
        self.dotButton.setGeometry(152, 440, btn_w, btn_h)
        self.dotButton.setStyleSheet(ButtonStyles.base())
        self.dotButton.clicked.connect(lambda: self.button_click("."))

        self.enterButton = QPushButton("???", self)
        self.enterButton.setGeometry(227, 326, 76, btn_h * 3)
        self.enterButton.setStyleSheet(ButtonStyles.enter())
        self.enterButton.clicked.connect(lambda: self.button_click("???"))

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

    def button_click(self, char):
        global waste
        global money

        if char == "\u2190":
            waste = waste[:-1]
        elif char == "???":
            money -= float(waste)
            waste = ""
            self.money_label.setText(f"{money}")
        else:
            waste += char

        self.waste_label.setText(f"??????????????????:\n{waste}")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
