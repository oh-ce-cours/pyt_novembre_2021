from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton("Click me (please)")


def on_button_clicked():
    alert = QMessageBox()
    print("clicked")
    alert.setText("You clicked the button!")
    alert.exec_()


def on_button_released():
    print("le bouton est relaché")


def on_button_pressed():
    print("le bouton est appuyé")


button.clicked.connect(on_button_clicked)
button.released.connect(on_button_released)
button.pressed.connect(on_button_pressed)
button.show()
app.exec_()
