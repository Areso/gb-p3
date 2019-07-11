from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QTextEdit, QWidget, QAction, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap


class AddressBook(QWidget):
    def __init__(self, parent=None):
        super(AddressBook, self).__init__(parent)

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()

        addressLabel = QLabel("Address:")
        self.addressText = QTextEdit()

        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0, Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Simple Address Book")


class Effects(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Effects, self).__init__(parent)
        self.MainWidget = MainWidget(self)

        self.setCentralWidget(self.MainWidget)
        self.setWindowTitle("Simple Address Book")

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Открыть файл')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')


class Image3(QWidget):
    def __init__(self, parent=None):
        super(Image3, self).__init__(parent)
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("image.png")
        print(type(pixmap))
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Example')
        self.show()


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.AddressBook = AddressBook(self)
        self.Image3 = Image3(self)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.AddressBook, 0, 1)
        mainLayout.addWidget(self.Image3, 1, 1)

        self.setLayout(mainLayout)

        self.move(300, 200)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Example')
        self.show()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    addressBook = Effects()
    addressBook.show()

    sys.exit(app.exec_())