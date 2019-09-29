from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode as q 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 600)
        MainWindow.setMaximumSize(QtCore.QSize(476, 600))
        MainWindow.setStyleSheet("background-color:#2C3335;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.dataLabel = QtWidgets.QLabel(self.centralwidget)
        self.dataLabel.setGeometry(QtCore.QRect(10, 50, 102, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.dataLabel.setFont(font)
        self.dataLabel.setStyleSheet("background-color:#2C3335;\n"
"color: white;")
        self.dataLabel.setObjectName("dataLabel")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(120, 10, 233, 29))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)

        self.titleLabel.setFont(font)
        self.titleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel.setStyleSheet("color:white;\n"
"background-color:#2C3335;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.data = QtWidgets.QTextEdit(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(10, 80, 451, 261))

        font = QtGui.QFont()
        font.setPointSize(11)

        self.data.setFont(font)
        self.data.setStyleSheet("background-color:white;")
        self.data.setObjectName("data")

        self.saveFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.saveFileLabel.setGeometry(QtCore.QRect(10, 380, 102, 20))

        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)

        self.saveFileLabel.setFont(font)
        self.saveFileLabel.setStyleSheet("background-color:#2C3335;\n"
"color: white;")
        self.saveFileLabel.setObjectName("saveFileLabel")
        self.saveFile = QtWidgets.QLineEdit(self.centralwidget)
        self.saveFile.setGeometry(QtCore.QRect(110, 370, 351, 41))

        font = QtGui.QFont()
        font.setPointSize(11)

        self.saveFile.setFont(font)
        self.saveFile.setStyleSheet("background-color:white;")
        self.saveFile.setObjectName("saveFile")

        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(170, 440, 121, 41))
        self.convert.setStyleSheet("background-color:#333945;")
        self.convert.setObjectName("convert")
        self.convert.clicked.connect(self.textToQR)

        self.New = QtWidgets.QPushButton(self.centralwidget)
        self.New.setGeometry(QtCore.QRect(170, 500, 121, 41))
        self.New.setStyleSheet("background-color:#333945;")
        self.New.setObjectName("New")
        self.New.clicked.connect(self.newEntry)

        MainWindow.setCentralWidget(self.centralwidget)        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QRCode Generator"))
        self.dataLabel.setText(_translate("MainWindow", "Enter the data"))
        self.titleLabel.setText(_translate("MainWindow", "QR Code Generator"))
        self.saveFileLabel.setText(_translate("MainWindow", "Save File As"))
        self.convert.setText(_translate("MainWindow", "Convert"))
        self.New.setText(_translate("MainWindow", "New"))


    def textToQR(self):
        txt = self.data.toPlainText()
        filename = self.saveFile.text()        
        qr = q.QRCode(version=1,box_size=10,border=5)        
        qr.add_data(txt)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(filename)
        print("File Converted....")

    def newEntry(self):
        self.data.clear()
        self.saveFile.clear()
        print("Cleared......")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
