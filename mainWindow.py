from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtSvg
from PySide2 import QtGui
import datetime
import sys

from pathlib import Path


class greetingPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        Vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(Vbox)

        greetingLabel = QtWidgets.QLabel(self)
        greetingLabel.setFixedHeight(60)
        greetingLabel.setObjectName("greeting")

        now = datetime.datetime.now()
        morning = now.replace(hour=12, minute=0, second=0, microsecond=0)
        afternoon = now.replace(hour=17, minute=0, second=0, microsecond=0)
        evening = now.replace(hour=20, minute=0, second=0, microsecond=0)
        if now <= morning:
            greetingLabel.setText("Good morning")
        elif now <= afternoon:
            greetingLabel.setText("Good afternoon")
        elif now <= evening:
            greetingLabel.setText("Good evening")
        else:
            greetingLabel.setText("Good night")

        greetingBox = QtWidgets.QWidget(self)
        Hbox = QtWidgets.QHBoxLayout(greetingBox)
        greetingBox.setLayout(Hbox)
        icon_label = QtWidgets.QLabel(greetingBox)
        icon_label.setFixedSize(60, 60)
        with open("./coffeecup.svg", "r") as f:
            xml_data = f.read()
            icon = QtGui.QPixmap()
            _bytes = QtCore.QByteArray(xml_data.encode())
            icon.loadFromData(_bytes)
            f.close()
            del xml_data
            del _bytes
            icon_label.setPixmap(icon)
            del icon

        Hbox.setContentsMargins(7, 0, 0, 0)
        Hbox.setSpacing(0)
        Hbox.addStretch(1)
        Hbox.addWidget(icon_label)
        Hbox.addWidget(greetingLabel)
        Hbox.addStretch(1)

        Vbox.addWidget(greetingBox)


class choosePage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        quseLabel = QtWidgets.QLabel(self, text="What do you like today?")
        quseLabel.setObjectName("title")
        quseLabel.move(0, 70)
        quseLabel.setFixedWidth(640)
        quseLabel.setAlignment((QtCore.Qt.AlignHCenter |
                                QtCore.Qt.AlignVCenter))

        icon_label = QtWidgets.QLabel(self)
        icon_label.setFixedSize(60, 60)
        with open("./coffeecup.svg", "r") as f:
            xml_data = f.read()
            icon = QtGui.QPixmap()
            _bytes = QtCore.QByteArray(xml_data.encode())
            icon.loadFromData(_bytes)
            f.close()
            del xml_data
            del _bytes
            icon_label.setPixmap(icon)
            del icon
        icon_label.setGeometry(70, 150, 60, 60)

        chooseBox = QtWidgets.QComboBox(self)
        chooseBox.setGeometry(160, 155, 330, 60)
        coffee_list = ["Choose your coffee",]
        chooseBox.addItems(coffee_list)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("lanny test")
        self.setFixedSize(640, 400)

        self.setStyleSheet(Path("./main.qss").read_text())
        self.initUI()

    def initUI(self):
        #self.container =greetingPage(self)
        self.container = choosePage(self)
        self.setCentralWidget(self.container)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
