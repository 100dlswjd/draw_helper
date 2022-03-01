# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_draw_helper(object):
    def setupUi(self, draw_helper):
        if not draw_helper.objectName():
            draw_helper.setObjectName(u"draw_helper")
        draw_helper.resize(218, 115)
        self.action_rangesetting = QAction(draw_helper)
        self.action_rangesetting.setObjectName(u"action_rangesetting")
        self.action_exit = QAction(draw_helper)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(draw_helper)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        draw_helper.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(draw_helper)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 218, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        draw_helper.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(draw_helper)
        self.statusbar.setObjectName(u"statusbar")
        draw_helper.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_rangesetting)

        self.retranslateUi(draw_helper)

        QMetaObject.connectSlotsByName(draw_helper)
    # setupUi

    def retranslateUi(self, draw_helper):
        draw_helper.setWindowTitle(QCoreApplication.translate("draw_helper", u"draw_helperr", None))
        self.action_rangesetting.setText(QCoreApplication.translate("draw_helper", u"\uac70\ub9ac\uc124\uc815", None))
        self.action_exit.setText(QCoreApplication.translate("draw_helper", u"\ub05d\ub0b4\uae30", None))
        self.label.setText(QCoreApplication.translate("draw_helper", u"\ud3ec\ud1a0\uc0f5 \uadf8\ub9bc \uadf8\ub9ac\uae30 \ub3c4\uc6c0 \ud504\ub85c\uadf8\ub7a8 \u314b\n"
"\ub0b4 \uc804\uc6a9\uc778\uac70\uc784", None))
        self.label_2.setText(QCoreApplication.translate("draw_helper", u"\ud604\uc7ac \uc124\uc815 \uac12 :", None))
        self.menu.setTitle(QCoreApplication.translate("draw_helper", u"\ud30c\uc77c", None))
        self.menu_2.setTitle(QCoreApplication.translate("draw_helper", u"\uc124\uc815", None))
    # retranslateUi

