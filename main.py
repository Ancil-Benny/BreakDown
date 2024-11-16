import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextEdit, QToolBar, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from groq import Groq

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("simpification of concepts") 
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        main_layout = QVBoxLayout()

        # Toolbar
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: black; height: 20%; padding:10%")

        self.addToolBar(toolbar)

        # Logo
        logo = QLabel("BREAKDOWN")
        logo.setStyleSheet("color: white; font-size: 36px; font-weight: bold;")
        toolbar.addWidget(logo)

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(main_layout)

        # Input layout
        input_layout = QHBoxLayout()

       
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter your text here...")
        self.input_field.setStyleSheet("font-size: 16px; padding: 10px;")
        self.input_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        input_layout.addWidget(self.input_field)

    
        self.button = QPushButton("Submit")
        self.button.setStyleSheet("background-color: black; color: white; font-size: 18px; padding: 15px;")
        self.button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button.clicked.connect(self.call_api)
        input_layout.addWidget(self.button)

        main_layout.addLayout(input_layout)

        # Output field
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setStyleSheet("font-size: 16px; padding: 10px;")
        main_layout.addWidget(self.output_field)

   
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

    def call_api(self):
        user_input = self.input_field.text()
        if user_input:
            client = Groq(api_key="")
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama3-8b-8192",
            )
            response = chat_completion.choices[0].message.content
            self.output_field.setText(response)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())