from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QWidget, QVBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None ) -> None:
        super().__init__(parent)


