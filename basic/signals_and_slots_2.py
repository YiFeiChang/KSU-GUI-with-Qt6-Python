import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App 2")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)


app = QApplication(sys. argv)
window = MainWindow()
window.show()
app.exec()
