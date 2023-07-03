import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QCheckBox,QSpinBox
from PyQt5 import uic
from form import Ui_widgg

class widgg(QWidget,Ui_widgg):
    def __init__(self):
        super(widgg, self).__init__()
        self.setupUi(self)
        
        self.spnbx=self.findChild(QSpinBox,"spinBox")
        self.sdwnbtn.clicked.connect(self.sdwnbtnfctn)
        self.abortbtn.clicked.connect(self.abortbtnfctn)

    def sdwnbtnfctn(self):
        self.secs=int(self.spnbx.text())
        y=0+int(self.secs)*60
        if self.notify.isChecked() is True:
            subprocess.call('shutdown -s -t {}'.format(y))
        elif self.notify.isChecked() is False:
            subprocess.call('shutdown -s -t {} -c " " '.format(y))
    def abortbtnfctn(self):
        subprocess.call("shutdown -a")
if __name__ == "__main__":
    app = QApplication([])
    widget = widgg()
    widget.show()
    app.exec_()
