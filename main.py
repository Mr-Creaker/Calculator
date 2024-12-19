from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QGroupBox
from PyQt5.QtCore  import Qt


app = QApplication([])
window = QWidget()
window.setWindowTitle("My Super App")
window.resize(300,500)
window.setStyleSheet("""QWidget {
font-family: "Times New Roman", Times, serif;
font-size: 25px;
background-color: rgb(0, 0, 0);
 color: white;
 }
                    QPushButton {
    background-color: grey;
    border: 3px solid white;
    padding:5px 25px 5px 25px;
    border-radius: 20px;
                    }
                    QPushButton:hover{
    background-color:black;
    border-radius: 10px;
 }
  QGroupBox{ border: None;}        
 """)
btn_0 = QPushButton('0')
btn_1 = QPushButton('1')
btn_2 = QPushButton('2')
btn_3 = QPushButton('3')
btn_4 = QPushButton('4')
btn_5 = QPushButton('5')
btn_6 = QPushButton('6')
btn_7 = QPushButton('7')
btn_8 = QPushButton('8')
btn_9 = QPushButton('9')

btn_eq = QPushButton("=")
btn_clear = QPushButton("C")
btn_back = QPushButton("<-")
btn_point = QPushButton(".")
btn_pl =QPushButton("+")
btn_min =QPushButton("-")
btn_mul =QPushButton("*")
btn_div = QPushButton("/")
result = QLabel("0")

line1 = QHBoxLayout()
line1.addWidget(btn_point,alignment=Qt.AlignCenter)
line1.addWidget(btn_0,alignment=Qt.AlignCenter)
line1.addWidget(btn_back,alignment=Qt.AlignCenter)
line2 = QHBoxLayout()
line2.addWidget(btn_1,alignment=Qt.AlignCenter)
line2.addWidget(btn_2,alignment=Qt.AlignCenter)
line2.addWidget(btn_3,alignment=Qt.AlignCenter)
line3 = QHBoxLayout()
line3.addWidget(btn_4,alignment=Qt.AlignCenter)
line3.addWidget(btn_5,alignment=Qt.AlignCenter)
line3.addWidget(btn_6,alignment=Qt.AlignCenter)
line4 = QHBoxLayout()
line4.addWidget(btn_7,alignment=Qt.AlignCenter)
line4.addWidget(btn_8,alignment=Qt.AlignCenter)
line4.addWidget(btn_9,alignment=Qt.AlignCenter)
box2 = QGroupBox()
box_line2 = QVBoxLayout()
box_line2.addLayout(line4)
box_line2.addLayout(line3)
box_line2.addLayout(line2)
box_line2.addLayout(line1)
box2.setLayout(box_line2)
line5 = QVBoxLayout()
line5.addWidget(btn_eq,alignment=Qt.AlignCenter)
line5.addWidget(btn_div,alignment=Qt.AlignCenter)
line5.addWidget(btn_mul,alignment=Qt.AlignCenter)
line5.addWidget(btn_pl,alignment=Qt.AlignCenter)
line5.addWidget(btn_min,alignment=Qt.AlignCenter)
line5.addWidget(btn_clear,alignment=Qt.AlignCenter)
btn_tan = QPushButton("tan")
btn_sin = QPushButton("sin")
btn_cos = QPushButton("cos")
btn_pow =QPushButton("^")
btn_sqtr =QPushButton("√")
line7 = QVBoxLayout()
line7.addWidget(btn_tan,alignment=Qt.AlignCenter)
line7.addWidget(btn_sin,alignment=Qt.AlignCenter)
line7.addWidget(btn_cos,alignment=Qt.AlignCenter)
line7.addWidget(btn_pow,alignment=Qt.AlignCenter)
line7.addWidget(btn_sqtr,alignment=Qt.AlignCenter)
box3 = QGroupBox()
box_line3 = QHBoxLayout()
box_line3.addLayout(line5)
box_line3.addLayout(line7)
box3.setLayout(box_line3)

line6 = QHBoxLayout()
line6.addWidget(box2)
line6.addWidget(box3)

box1 = QGroupBox("РЕЗУЛЬТАТ")
box_line = QHBoxLayout()
box_line.addWidget(result,alignment=Qt.AlignCenter)
box1.setLayout(box_line)


main_line = QVBoxLayout()
main_line.addWidget(box1,   stretch=3)
main_line.addLayout(line6,stretch=6)


def add_sybmol():
   button = app.sender() 
   text = result.text()
   if  text[len(text)-1] in "+-/*^√" and button.text() in "+-/*^√":
      return
   if text =="0":
      text ="" 
   result.setText(text+button.text())
btn_0.clicked.connect(add_sybmol)
btn_1.clicked.connect(add_sybmol)
btn_2.clicked.connect(add_sybmol)
btn_3.clicked.connect(add_sybmol)
btn_4.clicked.connect(add_sybmol)
btn_5.clicked.connect(add_sybmol)
btn_6.clicked.connect(add_sybmol)
btn_7.clicked.connect(add_sybmol)
btn_8.clicked.connect(add_sybmol)
btn_9.clicked.connect(add_sybmol)
btn_pl.clicked.connect(add_sybmol)
btn_min.clicked.connect(add_sybmol)
btn_mul.clicked.connect(add_sybmol)
btn_div.clicked.connect(add_sybmol)
btn_point.clicked.connect(add_sybmol)
#
btn_pow.clicked.connect(add_sybmol)
btn_sqtr.clicked.connect(add_sybmol)
#
def clear():
   result.setText("0")
btn_clear.clicked.connect(clear)

def back():
   text = result.text()
   text = text[:-1]
   if text =="":
      text ="0"
   result.setText(text)
btn_back.clicked.connect(back)


def parseSting(string):
   operatoins ="+-/*^√"
   element =""
   result = []
   for symbol in string:
      if operatoins.find(symbol) !=-1:
         result.append(element)
         result.append(symbol)
         element =""
      else:
         element+=symbol
   result.append(element)
   return result

def calculate(string):
   formula = parseSting(string)
   if formula[0] == "":
      formula[0] ="0"
   operatoins =["+-","/*","^","√"]
   for cur_operation in operatoins:
      i =0 
      while i< len(formula):
         if cur_operation.find(formula[i]) !=-1:
            operatoin = formula[i]
            first_number = float(formula[i-1])
            second_number = float(formula[i+1])
            if operatoin =="+":
               result = first_number+second_number
            if operatoin =="-":
               result = first_number-second_number
            if operatoin =="*":
               result = first_number*second_number
            if operatoin =="/":
               result = first_number/second_number
            if operatoin =="^":
               result = first_number**second_number
            if operatoin =="√":
               result = first_number*second_number**(1/2)
            del formula[i+1]
            formula[i] = str(result)
            del formula[i-1]
            i =0
         i +=1
   return formula[0]


def equal():
   formula = result.text()
   number = calculate(formula)
   result.setText(str(number))
btn_eq.clicked.connect(equal)
window.setLayout(main_line)
window.show()
app.exec_()