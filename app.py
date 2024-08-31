# All imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

# Main app objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My First App with PyQt5 yaaaay!")
main_window.resize(300, 200)

# words list
my_words = ["Hello", "Goodbye", "Test", "Javascript", "PyQt", "Code"]

# function to display words
def display_word(text):
    word = choice(my_words)
    text.setText(word)

# Create all widgets needed in app
title_text = QLabel("Random Words")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

# add event on button 1
button1.clicked.connect(lambda: display_word(text1))
button2.clicked.connect(lambda: display_word(text2))
button3.clicked.connect(lambda: display_word(text3))

master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()


# Design your layout, add your widgets to the screen
row1.addWidget(title_text, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1, alignment=Qt.AlignCenter)
row3.addWidget(button2, alignment=Qt.AlignCenter)
row3.addWidget(button3, alignment=Qt.AlignCenter)

# Set the final layout to the main window & events
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Show and execute your app
main_window.show()
app.exec_()