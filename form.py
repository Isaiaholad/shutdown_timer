from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widgg(object):
    def setupUi(self, widgg):
        widgg.setObjectName("widgg")
        widgg.resize(800, 600)

        # Setting up the color palette
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Text, QtGui.QColor(255, 0, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, QtGui.QColor(255, 85, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Window, QtGui.QColor(255, 255, 127))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, QtGui.QColor(255, 0, 0, 128))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Text, QtGui.QColor(255, 0, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, QtGui.QColor(255, 85, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor(255, 255, 127))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, QtGui.QColor(255, 0, 0, 128))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, QtGui.QColor(120, 120, 120))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, QtGui.QColor(120, 120, 120))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Base, QtGui.QColor(255, 255, 127))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Window, QtGui.QColor(255, 255, 127))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, QtGui.QColor(0, 0, 0, 128))
        widgg.setPalette(palette)
        widgg.setAutoFillBackground(True)

        # Create widgets and set their properties
        self.sdwnbtn = QtWidgets.QPushButton(widgg)
        self.sdwnbtn.setGeometry(QtCore.QRect(510, 210, 131, 61))
        font = QtGui.QFont("MS Gothic", 20)
        self.sdwnbtn.setFont(font)
        self.sdwnbtn.setObjectName("sdwnbtn")
        self.label = QtWidgets.QLabel(widgg)
        self.label.setGeometry(QtCore.QRect(30, 140, 400, 41))
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.WindowText, QtGui.QColor(255, 0, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Base, QtGui.QColor(255, 255, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, QtGui.QColor(255, 0, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Base, QtGui.QColor(255, 255, 0))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, QtGui.QColor(120, 120, 120))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Base, QtGui.QColor(85, 0, 127))
        self.label.setPalette(palette)
        font = QtGui.QFont("MS Mincho", 16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.notify = QtWidgets.QCheckBox(widgg)
        self.notify.setGeometry(QtCore.QRect(560, 280, 71, 17))
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.WindowText, QtGui.QColor(170, 85, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, QtGui.QColor(170, 85, 0))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, QtGui.QColor(120, 120, 120))
        self.notify.setPalette(palette)
        font = QtGui.QFont("Verdana", 10, weight=QtGui.QFont.Bold, italic=True)
        self.notify.setFont(font)
        self.notify.setObjectName("notify")
        self.spinBox = QtWidgets.QSpinBox(widgg)
        self.spinBox.setGeometry(QtCore.QRect(450, 140, 61, 41))
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Base, QtGui.QColor(255, 170, 127))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Base, QtGui.QColor(255, 170, 127))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Base, QtGui.QColor(255, 255, 127))
        self.spinBox.setPalette(palette)
        font = QtGui.QFont("Microsoft Himalaya", 16)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.abortbtn = QtWidgets.QPushButton(widgg)
        self.abortbtn.setGeometry(QtCore.QRect(510, 330, 131, 61))
        font = QtGui.QFont("MS Gothic", 20)
        self.abortbtn.setFont(font)
        self.abortbtn.setObjectName("abortbtn")

        # Connect slots and signals
        self.retranslateUi(widgg)
        QtCore.QMetaObject.connectSlotsByName(widgg)

    def retranslateUi(self, widgg):
        _translate = QtCore.QCoreApplication.translate
        widgg.setWindowTitle(_translate("widgg", "SHUTDOWN TIMER"))
        self.sdwnbtn.setText(_translate("widgg", "shutdown"))
        self.label.setText(_translate("widgg", "Enter Shutdown countdown in minutes"))
        self.notify.setText(_translate("widgg", "Notify"))
        self.abortbtn.setText(_translate("widgg", "Abort"))
