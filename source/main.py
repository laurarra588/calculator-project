
import ctypes
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from buttons import Button, ButtonsGrid

if __name__ == '__main__':

    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication()

    setupTheme()
    
    window = MainWindow()

    # Define the icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info('Sua conta')
    window.addWidgetTovLayout(info)

    # Display
    display = Display()
    window.addWidgetTovLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    # Button
    buttonsGrid.addWidget(Button('0'), 0 , 0)
    buttonsGrid.addWidget(Button('1'), 0 , 1)
    buttonsGrid.addWidget(Button('2'), 0 , 2)
    

    window.adjustFixedSize()
    window.show()
    app.exec()
    
    