BACKGROUND_COLOR = "rgb(0, 0, 0)"
DESCRIPTION_TEXT_COLOR = "rgb(172, 172, 172)"
BASE_TEXT_COLOR = "rgb(255, 255, 255)"
ACCENT_COLOR = "rgb(255, 170, 0)"


class ButtonStyles:
    def confirm():
        return """
        QPushButton {
            background-color: rgb(255, 170, 0);
            border: 1px solid rgb(150, 150, 150);
            font-family: 'Roboto', sans-serif;
            font-size: 30px;
            padding-bottom: 15px;
        }
        QPushButton:hover:pressed {
            background-color: rgb(230, 150, 0);
        }
        """

    def settings():
        return """
        QPushButton {
            background-color: rgba(200, 200, 200, .0);
        }
        QPushButton:hover:pressed {
            background-color: rgba(200, 200, 200, .25);
        }
        """

    def delete():
        return """
        QPushButton {
            background-color: rgb(200, 200, 200);
            border: 1px solid rgb(150, 150, 150);
            font-size: 25px;
            padding-bottom: 5px;
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


class DesignStyles:
    def list_widget():
        return """
        color: rgb(172,172,172);
        padding-left: 10px;
        padding-top: 10px;
        margin-top: 10px;
        border: none;
        border-top: 1px solid rgba(60,60,60, .8);
        """

# print("Я прекрасен!")