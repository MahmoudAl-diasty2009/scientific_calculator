import sys
import math
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class ScientificCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scientific Calculator")
        self.resize(400, 500)
        self.setStyleSheet("background-color: #0a1a2f;")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("Arial", 20))
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #fff8d6;
                color: #000;
                border: 6px solid #FFD700;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        self.layout.addWidget(self.display)

        buttons = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "*"],
            ["0", ".", "/", "sqrt"],
            ["pow", "sin", "cos", "tan"],
            ["C", "=", "Quit"]
        ]

        for row in buttons:
            row_layout = QHBoxLayout()
            for btn_text in row:
                btn = QPushButton(btn_text)
                btn.setFont(QFont("Arial", 14, QFont.Bold))
                btn.setFixedHeight(50)
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #FFD700;
                        color: #0a1a2f;
                        border-radius: 8px;

                    }
                    QPushButton:hover {
                        background-color: #ffeb66;
                    }
                """)
                btn.clicked.connect(self.on_button_click)
                row_layout.addWidget(btn)
            self.layout.addLayout(row_layout)

    def on_button_click(self):
        sender = self.sender().text()

        if sender == "C":
            self.display.clear()

        elif sender == "Quit":
            self.close()

        elif sender == "=":
            try:
                expr = self.display.text()

                if "sqrt" in expr:
                    num = float(expr.replace("sqrt", ""))
                    result = math.sqrt(num)

                elif "pow" in expr:
                    parts = expr.replace("pow", "").split(",")
                    base = float(parts[0])
                    exp = float(parts[1])
                    result = math.pow(base, exp)

                elif "sin" in expr:
                    num = float(expr.replace("sin", ""))
                    result = math.sin(math.radians(num))

                elif "cos" in expr:
                    num = float(expr.replace("cos", ""))
                    result = math.cos(math.radians(num))

                elif "tan" in expr:
                    num = float(expr.replace("tan", ""))
                    rad = math.radians(num)
                    cos_value = math.cos(rad)
                    if abs(cos_value) < 1e-10:
                        result = "Error"
                    else:
                        result = math.tan(rad)
                else:
                    result = eval(expr)

                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")

        else:
            self.display.setText(self.display.text() + sender)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ScientificCalculator()
    win.show()
    sys.exit(app.exec())
