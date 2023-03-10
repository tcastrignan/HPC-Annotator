# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_splash_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(893, 530)
        Form.setMinimumSize(QtCore.QSize(893, 530))
        Form.setMaximumSize(QtCore.QSize(893, 530))
        Form.setMouseTracking(False)
        Form.setWindowTitle("")
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QProgressBar {\n"
"     border: 2px solid white;\n"
"     border-radius: 5px;\n"
"     background: transparent;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgba(127,80,32,100);\n"
"    width: 20px;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 90, 891, 121))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background: transparent;\n"
"color: #ffffff;\n"
"font: 75 40pt \"Georgia\";\n"
"font-size: 48px; \n"
"font-weight: 300; \n"
"line-height: 58px;\n"
"margin: 0 0 58px;\n"
"\n"
"")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 891, 141))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background: transparent;\n"
"color: #ffffff;\n"
"font: 75 40pt \"Georgia\";\n"
"font-size: 48px; \n"
"font-weight: 300; \n"
"line-height: 58px;\n"
"margin: 0 0 58px;\n"
"\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-16, -15, 911, 531))
        self.label_3.setStyleSheet("border: None;\n"
"background-color: transparent;\n"
"background-image: url(:/root/icons/bg-splash.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(330, 440, 231, 21))
        self.label_4.setStyleSheet("color: white;\n"
"font: italic 10pt \"Georgia\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 270, 891, 111))
        self.label_5.setStyleSheet("background: transparent;\n"
"color: #ffffff;\n"
"font: 75 20pt \"Georgia\";\n"
"font-size:20px; \n"
"font-weight: 300; \n"
"line-height: 58px;\n"
"margin: 0 0 58px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.enter = QtWidgets.QPushButton(Form)
        self.enter.setGeometry(QtCore.QRect(540, 380, 151, 41))
        self.enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter.setStyleSheet("QPushButton{\n"
"background: transparent;\n"
"color: white;\n"
"font: 14pt \"Georgia\";\n"
"border: 3px solid rgba(255, 255, 255, 100);\n"
"border-radius: 10px 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(0, 0, 0, 100);\n"
"   border: 3px solid rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.enter.setObjectName("enter")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(200, 380, 151, 41))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("QPushButton{\n"
"background: transparent;\n"
"color: white;\n"
"font: 14pt \"Georgia\";\n"
"border: 3px solid rgba(255, 255, 255, 100);\n"
"border-radius: 10px 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(0, 0, 0, 100);\n"
"   border: 3px solid rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.exit.setObjectName("exit")
        self.config = QtWidgets.QPushButton(Form)
        self.config.setGeometry(QtCore.QRect(370, 380, 151, 41))
        self.config.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.config.setStyleSheet("QPushButton{\n"
"background: transparent;\n"
"color: white;\n"
"font: 14pt \"Georgia\";\n"
"border: 3px solid rgba(255, 255, 255, 100);\n"
"border-radius: 10px 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(0, 0, 0, 100);\n"
"   border: 3px solid rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.config.setObjectName("config")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.enter.raise_()
        self.exit.raise_()
        self.config.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "HPC"))
        self.label_2.setText(_translate("Form", "ANNOTATOR"))
        self.label_4.setText(_translate("Form", "Created by: Lorenzo Arcioni"))
        self.label_5.setText(_translate("Form", "Generate your own custom scripts for HPC parallel annotation"))
        self.enter.setText(_translate("Form", "Enter"))
        self.exit.setText(_translate("Form", "Exit"))
        self.config.setText(_translate("Form", "Config"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
