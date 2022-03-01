import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
from PySide6.QtGui import QCloseEvent

from main_form import Ui_draw_helper
from range_set_form import Ui_range_set

class range_set(QDialog, Ui_range_set):
    def __init__(self):
        super(range_set, self).__init__()
        self.setupUi(self)
        self.flag = False
        self.range = 5        
        self.btn_ok.clicked.connect(self.btn_ok_click)
        self.lineEdit.textChanged.connect(self.change_text)
        self.exec()

    def change_text(self, text):
        self.lineEdit.setText(text)
        self.range = int(text)

    def btn_ok_click(self):
        self.flag = True
        self.close()

    def setting(self):
        return self.flag, self.range

class Mainwindow(QMainWindow, Ui_draw_helper):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.range = 5
        self.action_rangesetting.triggered.connect(self.rangesetting_click)
        self.action_exit.triggered.connect(self.exit_click)
        self.label_2.setText("현재 설정 값 : ", self.range)
    
    def rangesetting_click(self):
        print("거리설정 클릭 !")
        flag, self.range = range_set.setting(range_set())
        print(flag, range)
        pass

    def exit_click(self):
        print("나가기 클릭")
        self.close()
        pass

    def closeEvent(self, event: QCloseEvent) -> None:
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()