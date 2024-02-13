from PyQt6.QtWidgets import (
    QMainWindow, QWidget,
    QLineEdit, QListView, QPushButton,
    QVBoxLayout, QMessageBox,
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QGuiApplication
from PyQt6.QtCore import QDateTime
from client.utils import send_data_request, get_data_request


class SuccessPopup(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        
        self.setWindowTitle("Успешно")
        self.setText("Данные отправлены на сервер")
        

class ErrorPopup(QMessageBox):
    def __init__(self, e):
        QMessageBox.__init__(self)
        self.e = e
        
        self.setWindowTitle("Ошибка")
        self.setText(self.e)
        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Главное окно")
        
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_size = self.geometry()
        x = (screen_geometry.width() - window_size.width()) // 2
        y = (screen_geometry.height() - window_size.height()) // 2
        self.setGeometry(x, y, window_size.width(), window_size.height())
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        layout = QVBoxLayout()
        self.centralWidget.setLayout(layout)
        
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)
        
        self.list_view = QListView()
        layout.addWidget(self.list_view)
        
        self.send_post_button = QPushButton("Отправить данные")
        self.send_post_button.clicked.connect(self.send_data)
        layout.addWidget(self.send_post_button)

        self.send_get_button = QPushButton("Получить данные")
        self.send_get_button.clicked.connect(self.get_data)
        layout.addWidget(self.send_get_button)
        
        self.model = QStandardItemModel()
        self.list_view.setModel(self.model)
        
        self.push_num = 0
    
    def _success(self):
        popup = SuccessPopup()
        popup.exec()
    
    def _handle_error(self, error):
        popup = ErrorPopup(str(error))
        popup.exec()
                
    def send_data(self):
        self.push_num += 1
        
        try:
            send_data_request(
                    self.line_edit.text(),
                    self.push_num,
                    QDateTime.currentDateTime().toString('yyyyMd HH:mm:ss')
                    )
            self._success()
        except Exception as e:
            self._handle_error(e)
        
    def get_data(self):
        try:
            data = get_data_request()
            self.update_list_view(data)
        except Exception as e:
            self._handle_error(e)
        
    def update_list_view(self, data):
        self.model.clear()
        for item in data:
            try:
                row = QStandardItem(f"Текст: {item['content']}, Дата и время: {item['created_datetime']}, Номер нажатия: {item['push_num']}")
                self.model.appendRow(row)
            except Exception as e:
                self._handle_error(e)