import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton,QLineEdit,QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora Simples | Lucas Henrique")
        self.setFixedSize(450,450)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display,0,0,1,5)
        self.display.setDisabled(True)
        self.setStyleSheet('background:#363636;')
        self.display.setStyleSheet(
            '*{background: #696969; color: #000;  font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


        self.addbtn(QPushButton('7'),1,0,1,1)
        self.addbtn(QPushButton('8'),1,1,1,1)
        self.addbtn(QPushButton('9'),1,2,1,1)
        self.addbtn(QPushButton('+'),1,3,1,1)
        self.addbtn(
            QPushButton('C'),1,4,1,1,
            lambda: self.display.setText(''),
            'background: #2F4F4F; color: #fff; font-weight:700;'
        )

        self.addbtn(QPushButton('4'), 2, 0, 1, 1)
        self.addbtn(QPushButton('5'), 2, 1, 1, 1)
        self.addbtn(QPushButton('6'), 2, 2, 1, 1)
        self.addbtn(QPushButton('-'), 2, 3, 1, 1)
        self.addbtn(QPushButton('c'), 2, 4, 1, 1,
                    lambda: self.display.setText(
                        self.display.text()[:-1]#apaga um
                    ),
                    'background:#2F4F4F; color:#D3D3D3; font-weight:700; '
          )

        self.addbtn(QPushButton('1 '), 3, 0, 1, 1)
        self.addbtn(QPushButton('2'), 3, 1, 1, 1)
        self.addbtn(QPushButton('3'), 3, 2, 1, 1)
        self.addbtn(QPushButton('/'), 3, 3, 1, 1)
        self.addbtn(QPushButton(''), 3, 4, 1, 1)

        self.addbtn(QPushButton('.'), 4, 0, 1, 1)
        self.addbtn(QPushButton('0'), 4, 1, 1, 1)
        self.addbtn(QPushButton(''), 4, 2, 1, 1)
        self.addbtn(QPushButton('*'), 4, 3, 1, 1)
        self.addbtn(QPushButton('='), 4, 4, 1, 1,

                    self.evaligual,
                    'background:#00FF00; color:#000000; font-weight:700;'
           )

        self.setCentralWidget(self.cw)
    def addbtn(self,btn,row,col,rowspan,colspan,funcao=None, style=None):
        self.grid.addWidget(btn,row,col,rowspan,colspan)
        btn.setStyleSheet('background-color: #696969; color:#00FFFF; font-weight:700;')

        if not funcao:
         btn.clicked.connect(
             lambda: self.display.setText(
                 self.display.text() + btn.text()
            )
         )
        else:
            btn.clicked.connect(funcao)
        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def evaligual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta Invalida!')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()