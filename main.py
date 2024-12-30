from pathlib import Path

import pyperclip
from PySide6.QtWidgets import QApplication, QWidget

from dbkit import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.baseDir = Path(__file__).parent
        self.bind()

    def bind(self):
        self.copyButton.clicked.connect(self.copy)


    def copy(self):
        # clipboard = QApplication.clipboard()
        # clipboard.setText("test text")
        pyperclip.copy("test text")

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()
