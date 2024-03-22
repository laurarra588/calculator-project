
import ctypes
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from buttons import Button, ButtonsGrid
import qdarktheme

if __name__ == '__main__':

    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication()

    dark_stylesheet = qdarktheme.load_stylesheet('dark')
    
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
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid) 
    
    app.setStyleSheet(dark_stylesheet)
    window.adjustFixedSize()
    window.show()
    app.exec()
    
    