import sys
from PyQt5.QtWidgets import *

class Calculator(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()


        layout_op = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_num = QGridLayout()
        layout_equation_sol = QFormLayout()


        label_equation = QLabel("식: ")
        label_sol = QLabel("해답: ")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")


        layout_equation_sol.addRow(label_equation, self.equation)
        layout_equation_sol.addRow(label_sol, self.solution)


        btn_plus = QPushButton("+")
        btn_min = QPushButton("-")
        btn_product = QPushButton("*")
        btn_div = QPushButton("/")


        btn_plus.clicked.connect(lambda state, operation = "+": self.btn_op_clicked(operation))
        btn_min.clicked.connect(lambda state, operation = "-": self.btn_op_clicked(operation))
        btn_product.clicked.connect(lambda state, operation = "*": self.btn_op_clicked(operation))
        btn_div.clicked.connect(lambda state, operation = "/": self.btn_op_clicked(operation))


        layout_op.addWidget(btn_plus)
        layout_op.addWidget(btn_min)
        layout_op.addWidget(btn_product)
        layout_op.addWidget(btn_div)


        btn_equal = QPushButton("=")
        btn_clear = QPushButton("Clear")
        btn_backspace = QPushButton("Backspace")


        btn_equal.clicked.connect(self.btn_equal_clicked)
        btn_clear.clicked.connect(self.btn_clear_clicked)
        btn_backspace.clicked.connect(self.btn_backspace_clicked)


        layout_clear_equal.addWidget(btn_clear)
        layout_clear_equal.addWidget(btn_backspace)
        layout_clear_equal.addWidget(btn_equal)



        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.num_btn_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_num.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_num.addWidget(number_button_dict[number], 3, 1)


        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.num_btn_clicked(num))
        layout_num.addWidget(button_dot, 3, 2)

        btn_double_zero = QPushButton("00")
        btn_double_zero.clicked.connect(lambda state, num = "00": self.num_btn_clicked(num))
        layout_num.addWidget(btn_double_zero, 3, 0)


        main_layout.addLayout(layout_equation_sol)
        main_layout.addLayout(layout_op)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_num)

        self.setLayout(main_layout)
        self.setWindowTitle("python GUI Calculator")
        self.show()




    def num_btn_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def btn_op_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def btn_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def btn_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def btn_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Calculator()
    sys.exit(app.exec_())
