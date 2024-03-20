
from PySide6.QtWidgets import (QMainWindow, 
                               QWidget, QVBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None ) -> None:
        super().__init__(parent)

        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculator')
    

    def adjustFixedSize(self) -> None:
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetTovLayout(self,widget: QWidget):
        self.vLayout.addWidget(widget)

