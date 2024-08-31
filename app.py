# All imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

# Main app objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My First App with PyQt5 yaaaay!")
main_window.resize(200, 300)

# Create all widgets needed in app
title_text = QLabel("Random Words")
text1 = QLabel("Vietnam")
text2 = QLabel("?")
text3 = QLabel("goodbye")

button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()


# Design your layout, add your widgets to the screen

# Set the final layout to the main window & events

# Show and execute your app
main_window.show()
app.exec_()