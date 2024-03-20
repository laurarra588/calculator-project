import sys
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()

    # Define the icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    window.adjustFixedSize()
    window.show()
    app.exec()