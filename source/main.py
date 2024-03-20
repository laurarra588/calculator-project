import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    cw = QWidget()
    v_layout = QVBoxLayout()
    cw.setLayout(v_layout)

    window.setCentralWidget(cw)
    window.show()


    app.exec()