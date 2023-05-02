import sys
from PyQt5.QtWidgets import *

class Calculator(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_op = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_num = QGridLayout()
        layout_equation_sol = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("식: ")
        label_sol = QLabel("해답: ")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_sol.addRow(label_equation, self.equation)
        layout_equation_sol.addRow(label_sol, self.solution)

        ### 사칙연상 버튼 생성
        btn_plus = QPushButton("+")
        btn_min = QPushButton("-")
        btn_product = QPushButton("*")
        btn_div = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        btn_plus.clicked.connect(lambda state, operation = "+": self.btn_op_clicked(operation))
        btn_min.clicked.connect(lambda state, operation = "-": self.btn_op_clicked(operation))
        btn_product.clicked.connect(lambda state, operation = "*": self.btn_op_clicked(operation))
        btn_div.clicked.connect(lambda state, operation = "/": self.btn_op_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_op.addWidget(btn_plus)
        layout_op.addWidget(btn_min)
        layout_op.addWidget(btn_product)
        layout_op.addWidget(btn_div)

        ### =, clear, backspace 버튼 생성
        btn_equal = QPushButton("=")
        btn_clear = QPushButton("Clear")
        btn_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        btn_equal.clicked.connect(self.btn_equal_clicked)
        btn_clear.clicked.connect(self.btn_clear_clicked)
        btn_backspace.clicked.connect(self.btn_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(btn_clear)
        layout_clear_equal.addWidget(btn_backspace)
        layout_clear_equal.addWidget(btn_equal)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
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

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.num_btn_clicked(num))
        layout_num.addWidget(button_dot, 3, 2)

        btn_double_zero = QPushButton("00")
        btn_double_zero.clicked.connect(lambda state, num = "00": self.num_btn_clicked(num))
        layout_num.addWidget(btn_double_zero, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_sol)
        main_layout.addLayout(layout_op)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_num)

        self.setLayout(main_layout)
        self.setWindowTitle("python GUI Calculator")
        self.show()

    #################
    ### functions ###
    #################
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
