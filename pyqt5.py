import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ola Pizza") #using the setWindowTitle() method to pass a title to our window
        self.setGeometry(700, 100, 500, 500)
        self.setWindowIcon(QIcon("/home/Ola/python_lab/java-not-found-error-message.png"))


        label = QLabel("Hello", self)  #we use the label module to input and style our content
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0, 0, 100, 100)
        label.setStyleSheet("color: blue;"
                            "background: green;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;"
                            )
        

        label.setAlignment(Qt.AlignTop)   #VERTICALLY TOP ALIGNMENT
        label.setAlignment(Qt.AlignVCenter)   #VERTICALLY Centre ALIGNMENT

        label.setAlignment(Qt.AlignRight)   #Horizontal Right ALIGNMENT





    
def main():
    app = QApplication(sys.argv) #creating an app object from the class Qapplication and pass in system arguements sys.argv
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #to display the window on our screen


if __name__ == "__main__":
    main()