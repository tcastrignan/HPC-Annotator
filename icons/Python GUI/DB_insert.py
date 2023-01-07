from PyQt5 import  QtCore, QtGui, QtWidgets
import os
import sys
import json

from DB_insert_GUI import Ui_MainWindow

class DB_insert(QtWidgets.QMainWindow):

    def Exit(self):
        sys.exit(0)
    
    def Minimize(self):
        self.showMinimized()

    def Insert(self):
        data = {"account": [],
                "partition": []}
        with open("config.json", "r") as f:
            try:
                data = json.loads(f.read())
            except Exception as e:
                print(str(e))
            f.close()
        

        if self.window.account.text() != None: data["account"].append(self.window.account.text())
        if self.window.partition.text() != None: data["partition"].append(self.window.partition.text())

        if self.window.binary.text() != None: data["binary"]    = self.window.binary.text()
        if self.window.outfmt.text() != None: data["outfmt"]    = self.window.outfmt.text()

        with open("config.json", "w") as f:
            json.dump(data, f, indent = 4)
            f.close()
        
        msg = QtWidgets.QMessageBox(self)
        msg.setText("Data correctly stored!")
        msg.setWindowTitle("Success")
        msg.buttonClicked.connect(self.Exit)
        msg.exec_()
            

    def __init__(self):
        super(DB_insert, self).__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)

        # setting  the fixed size of window
        self.setFixedSize(540, 539)

        #Frameless splash window
        self.setWindowFlags(
            self.windowFlags() | 
            QtCore.Qt.FramelessWindowHint
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Window connections
        self.window.insert.clicked.connect(self.Insert)
        self.window.btn_close.clicked.connect(self.Exit)
        self.window.btn_minimize.clicked.connect(self.Minimize)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = DB_insert()
    main.show()
    sys.exit(app.exec_())