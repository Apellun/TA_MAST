import sys
from PyQt6.QtWidgets import QApplication
from client.interface import MainWindow, ErrorPopup

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
        
    except Exception as e:
        window.close()
        popup = ErrorPopup(f"Ошибка во время исполнения программы.\n{e}")
        popup.exec()