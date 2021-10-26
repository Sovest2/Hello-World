import time

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QSpinBox, QListWidget

from styles import *
import settings

class SettingsWindow(QWidget):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setup()
        self.click_time = time.time()
        self.click_counter = 0

    def setup(self):
        self.setGeometry(settings.main_window.geometry())
        self.setFixedSize(300, 500)
        self.setWindowTitle("Настройки")
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")

        self.budget_label = QLabel("Бюджет:", self)
        self.budget_label.setGeometry(0, 20, 111, 21)
        self.budget_label.setStyleSheet(TextStyles.subtitle())

        self.days_label  = QLabel("Дней выжить: ", self)
        self.days_label.setGeometry(0, 60, 111, 21)
        self.days_label.setStyleSheet(TextStyles.subtitle())
        self.days_label.mousePressEvent = self.easter_egg

        self.budget_edit = QLineEdit(f"{settings.budget}", self)
        self.budget_edit.setGeometry(120, 20, 181, 21)
        self.budget_edit.setStyleSheet(f"color:{BASE_TEXT_COLOR};")


        self.days_spin = QSpinBox(self, value=settings.days)
        self.days_spin.setGeometry(120, 60, 42, 22)
        self.days_spin.setRange(1, 31)
        self.days_spin.setStyleSheet(f"color:{BASE_TEXT_COLOR};")

        self.wastes_label = QLabel("История трат:", self)
        self.wastes_label. setGeometry(0, 120, 300, 30)
        self.wastes_label.setStyleSheet(TextStyles.title())

        self.wastes_list = QListWidget(self)
        self.wastes_list.setGeometry(0, 150, 300, 250)
        self.wastes_list.setStyleSheet(DesignStyles.list_widget())
        self.wastes_list.addItems(settings.wastes)

        self.exit_button = QPushButton("Назад",self)
        self.exit_button.setGeometry(0, 420, 300, 30)
        self.exit_button.setStyleSheet(ButtonStyles.delete())
        self.exit_button.clicked.connect(self.exit_click)

        self.confirm_button = QPushButton("Применить",self)
        self.confirm_button.setGeometry(0, 450, 300, 60)
        self.confirm_button.setStyleSheet(ButtonStyles.confirm())
        self.confirm_button.clicked.connect(self.confirm_click)

        self.show()

    def easter_egg(self):
        now = time.time()
        if (now - self.click_time < 2): 
            self.click_counter += 1
            self.click_time = now
            if self.click_counter >= 10:
                self.wastes_list.addItem("Где деньги, Лебовски?")
                self.click_counter = 0
        else:
            self.click_counter = 0
            self.click_time = now

    def exit_click(self):
        self.close()
        
        settings.main_window.setGeometry(self.geometry())
        settings.main_window.show()

    def confirm_click(self):

        try:
            # изменение значений
            settings.days = self.days_spin.value()
            settings.budget = float(self.budget_edit.text())

        except ValueError:
            print("Возникла ошибка")
        else:
            # Обновление данных в приложении
            settings.money = round(settings.budget/settings.days, 2)
            
            settings.main_window.money_label.setText(f"{settings.money}")