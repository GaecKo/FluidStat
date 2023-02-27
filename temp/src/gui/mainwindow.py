from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from .ui.mainwindow_ui import Ui_MainWindow
from ..backend.systeminfo import SystemInfo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/icon.png"))
        self.system_info = SystemInfo()
        self.system_info.cpu_usage_signal.connect(self.ui.cpu_usage.setValue)
        self.system_info.memory_usage_signal.connect(self.ui.memory_usage.setValue)
        self.system_info.gpu_usage_signal.connect(self.ui.gpu_usage.setValue)
        self.system_info.battery_info_signal.connect(self.ui.battery_info.setValue)
        self.thread = QThread()
        self.system_info.moveToThread(self.thread)
        self.thread.started.connect(self.system_info.run)
        self.thread.start()
