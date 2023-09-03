import sys
from typing import Tuple

from PyQt5 import QtWidgets,QtCore,uic

from src.binary_converter import BinaryConverter


class MainWindow(QtWidgets.QMainWindow):

    UI_FILE:str = "src/uifiles/main.ui"
    GEOMETRY:Tuple[int,int] = (511,242)
    WINDOW_TITLE:str = "Text to Binary"

    def __init__(self,*args,**kwargs) -> None:

        super().__init__(*args,**kwargs)
        uic.loadUi(self.UI_FILE,self)

        self.setFixedSize(*self.GEOMETRY)
        self.setWindowTitle(self.WINDOW_TITLE)

        self.__find_widgets()

        self.__set_events()

    


    def __set_events(self) -> None:

        self.__btn_convert.clicked.connect(self.__btn_convert_clicked)


    def __btn_convert_clicked(self) -> None:
        
        from_text:str = self.__from_text.toPlainText()

        binary_converter = BinaryConverter(from_text)

        self.__converted_text.setText(binary_converter.binary_text)


        
        


    def __find_widgets(self) -> None:

        self.__from_text:QtWidgets.QTextEdit = self.findChild(QtWidgets.QTextEdit,"txtFrom")
        self.__converted_text = self.findChild(QtWidgets.QTextEdit,"txtTo")

        self.__btn_convert = self.findChild(QtWidgets.QPushButton,"btnConvert")


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())