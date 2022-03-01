# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'range_set_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_range_set(object):
    def setupUi(self, range_set):
        if not range_set.objectName():
            range_set.setObjectName(u"range_set")
        range_set.resize(140, 74)
        self.gridLayout = QGridLayout(range_set)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(range_set)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(range_set)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_ok = QPushButton(range_set)
        self.btn_ok.setObjectName(u"btn_ok")

        self.verticalLayout.addWidget(self.btn_ok)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(range_set)

        QMetaObject.connectSlotsByName(range_set)
    # setupUi

    def retranslateUi(self, range_set):
        range_set.setWindowTitle(QCoreApplication.translate("range_set", u"0", None))
        self.label.setText(QCoreApplication.translate("range_set", u"\uac70\ub9ac \uc124\uc815:", None))
        self.btn_ok.setText(QCoreApplication.translate("range_set", u"\ud655\uc778\uc694~", None))
    # retranslateUi

