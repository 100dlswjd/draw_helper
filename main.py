import sys
import time

import win32api
import win32con
import keyboard_tool

from threading import Thread, Event

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
        self.label_2.setText(f"현재 설정 값 : {self.range}")
        self.exit_event = Event()
        self.exit_event.clear()
        self.worker = Thread(target = self.main_thread_proc)
        self.worker.start()

    def main_thread_proc(self):
        while self.exit_event.is_set() == False:
            Pos = win32api.GetCursorPos()
            temPos = [0,0]
            if win32api.GetAsyncKeyState(win32con.VK_NUMPAD1) & 0x8000:
                keyboard_tool.pressAndHold("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                keyboard_tool.release("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.05)
                for idx in range(self.range):
                    temPos[0] = Pos[0] - idx
                    temPos[1] = Pos[1] + idx
                    win32api.SetCursorPos((temPos[0], temPos[1]))
                    time.sleep(.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                win32api.SetCursorPos(Pos)

            elif win32api.GetAsyncKeyState(win32con.VK_NUMPAD2) & 0x8000:
                keyboard_tool.pressAndHold("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                keyboard_tool.release("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.05)
                for idx in range(self.range):
                    temPos[0] = Pos[0] 
                    temPos[1] = Pos[1] + idx
                    win32api.SetCursorPos((temPos[0], temPos[1]))
                    time.sleep(.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                win32api.SetCursorPos(Pos)

            elif win32api.GetAsyncKeyState(win32con.VK_NUMPAD3) & 0x8000:
                keyboard_tool.pressAndHold("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                keyboard_tool.release("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.05)
                for idx in range(self.range):
                    temPos[0] = Pos[0] + idx
                    temPos[1] = Pos[1] + idx
                    win32api.SetCursorPos((temPos[0], temPos[1]))
                    time.sleep(.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                win32api.SetCursorPos(Pos)

            elif win32api.GetAsyncKeyState(win32con.VK_NUMPAD4) & 0x8000:
                keyboard_tool.pressAndHold("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                keyboard_tool.release("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.05)
                for idx in range(self.range):
                    temPos[0] = Pos[0] - idx
                    temPos[1] = Pos[1]
                    win32api.SetCursorPos((temPos[0], temPos[1]))
                    time.sleep(.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                win32api.SetCursorPos(Pos)

            elif win32api.GetAsyncKeyState(win32con.VK_NUMPAD6) & 0x8000:
                keyboard_tool.pressAndHold("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                keyboard_tool.release("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.05)
                for idx in range(self.range):
                    temPos[0] = Pos[0] + idx
                    temPos[1] = Pos[1]
                    win32api.SetCursorPos((temPos[0], temPos[1]))
                    time.sleep(.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                win32api.SetCursorPos(Pos)

            elif win32api.GetAsyncKeyState(win32con.VK_NUMPAD7) & 0x8000:
                keyboard_tool.pressAndHold("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                keyboard_tool.release("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.05)
                for idx in range(self.range):
                    temPos[0] = Pos[0] - idx
                    temPos[1] = Pos[1] - idx
                    win32api.SetCursorPos((temPos[0], temPos[1]))
                    time.sleep(.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                win32api.SetCursorPos(Pos)

            elif win32api.GetAsyncKeyState(win32con.VK_NUMPAD8) & 0x8000:
                keyboard_tool.pressAndHold("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                keyboard_tool.release("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.05)
                for idx in range(self.range):
                    temPos[0] = Pos[0]
                    temPos[1] = Pos[1] - idx
                    win32api.SetCursorPos((temPos[0], temPos[1]))
                    time.sleep(.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                win32api.SetCursorPos(Pos)

            elif win32api.GetAsyncKeyState(win32con.VK_NUMPAD9) & 0x8000:
                keyboard_tool.pressAndHold("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                keyboard_tool.release("alt")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, Pos[0], Pos[1], 0, 0)
                time.sleep(.05)
                for idx in range(self.range):
                    temPos[0] = Pos[0] + idx
                    temPos[1] = Pos[1] - idx
                    win32api.SetCursorPos((temPos[0], temPos[1]))
                    time.sleep(.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, Pos[0], Pos[1], 0, 0)
                win32api.SetCursorPos(Pos)

    def rangesetting_click(self):
        print("거리설정 클릭 !")
        flag, self.range = range_set.setting(range_set())
        if flag:
            self.label_2.setText(f"현재 설정 값 : {self.range}")
        pass

    def exit_click(self):
        print("나가기 클릭")
        self.close()
        pass

    def closeEvent(self, event: QCloseEvent) -> None:
        self.exit_event.set()
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()