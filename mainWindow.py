from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtSvg
from PySide2 import QtGui
import datetime
import sys

from pathlib import Path
import sqlite3 as sqlite3
import logging


class greetingPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        greetingLabel = QtWidgets.QLabel(self)
        greetingLabel.setFixedHeight(60)
        greetingLabel.setObjectName("greeting")

        now = datetime.datetime.now()
        morning = now.replace(hour=12, minute=0, second=0, microsecond=0)
        afternoon = now.replace(hour=17, minute=0, second=0, microsecond=0)
        evening = now.replace(hour=20, minute=0, second=0, microsecond=0)
        if now <= morning:
            greetingLabel.setText("Good morning.")
        elif now <= afternoon:
            greetingLabel.setText("Good afternoon.")
        elif now <= evening:
            greetingLabel.setText("Good evening.")
        else:
            greetingLabel.setText("Good night.")

        icon_label = QtWidgets.QLabel(self)
        icon_label.setFixedSize(60, 60)
        with open("./_icons/coffeecup.svg", "r") as f:
            xml_data = f.read()
            icon = QtGui.QPixmap()
            _bytes = QtCore.QByteArray(xml_data.encode())
            icon.loadFromData(_bytes)
            f.close()
            del xml_data
            del _bytes
            icon_label.setPixmap(icon)
            del icon

        next_label = QtWidgets.QLabel(self)
        with open("./_icons/nextlabel.svg", "r") as f:
            xml_data = f.read()
            icon = QtGui.QPixmap()
            _bytes = QtCore.QByteArray(xml_data.encode())
            icon.loadFromData(_bytes)
            f.close()
            del xml_data
            del _bytes
            next_label.setPixmap(icon)
            del icon

        next_text = QtWidgets.QLabel(self, text="Start!")
        next_text.setObjectName("info")

        greet_hbox = QtWidgets.QWidget(self)
        greet_hbox.setFixedSize(640, 100)
        greet_hbox.move(0, 130)
        greet_hlayout = QtWidgets.QHBoxLayout()
        greet_hbox.setLayout(greet_hlayout)

        greet_hlayout.addStretch(1)
        greet_hlayout.addWidget(icon_label)
        greet_hlayout.addWidget(greetingLabel)
        greet_hlayout.addStretch(1)

        # greetingLabel.move(210, 135)
        # icon_label.move(130, 130)

        next_label.move(580, 340)
        next_text.move(520, 345)

        next_text.mouseReleaseEvent = lambda event, page_index=1: self.parent.changePage(
            page_index, event)


class choosePage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        icon_label = QtWidgets.QLabel(self)
        icon_label.setFixedSize(60, 60)
        with open("./_icons/coffeecup.svg", "r") as f:
            xml_data = f.read()
            icon = QtGui.QPixmap()
            _bytes = QtCore.QByteArray(xml_data.encode())
            icon.loadFromData(_bytes)
            f.close()
            del xml_data
            del _bytes
            icon_label.setPixmap(icon)
            del icon
        icon_label.setGeometry(90, 140, 60, 60)

        chooseBox = QtWidgets.QComboBox(self)
        chooseBox.setGeometry(190, 145, 330, 60)
        chooseBox.setObjectName("coffee_box")
        # TODO: connect to db
        coffee_list = ["Choose your coffee",]
        chooseBox.addItems(coffee_list)

        create_label = QtWidgets.QLabel(
            self, text="Not Found? Create a new one")
        create_label.setObjectName("hint")
        create_label.move(20, 360)

        next_label = QtWidgets.QLabel(self)
        with open("./_icons/nextlabel.svg", "r") as f:
            xml_data = f.read()
            icon = QtGui.QPixmap()
            _bytes = QtCore.QByteArray(xml_data.encode())
            icon.loadFromData(_bytes)
            f.close()
            del xml_data
            del _bytes
            next_label.setPixmap(icon)
            del icon

        next_text = QtWidgets.QLabel(self, text="Next")
        next_text.setObjectName("info")
        next_label.move(580, 340)
        next_text.move(520, 345)

        create_label.mouseReleaseEvent = lambda event, page_index=2: self.parent.changePage(
            page_index, event)


class newCoffePage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        # region label object
        hint_label = QtWidgets.QLabel(
            self, text="Tell me about your new coffee")
        hint_label.setObjectName("title")
        hint_label.setFixedWidth(640)
        hint_label.move(0, 20)
        hint_label.setAlignment(QtCore.Qt.AlignHCenter)

        name_label = QtWidgets.QLabel(self, text="Name:")
        name_label.setObjectName("info")
        name_label.move(100, 100)

        brand_label = QtWidgets.QLabel(self, text="Brand:")
        brand_label.setObjectName("info")
        brand_label.move(100, 160)

        weight_label = QtWidgets.QLabel(self, text="Weight:")
        weight_label.setObjectName("info")
        weight_label.move(100, 220)

        price_label = QtWidgets.QLabel(self, text="Price:")
        price_label.setObjectName("info")
        price_label.move(100, 280)
        # endregion
        # region input object
        self.name_input = QtWidgets.QLineEdit(self)
        self.name_input.setFixedSize(300, 40)
        self.name_input.move(210, 100)

        self.brand_input = QtWidgets.QLineEdit(self)
        self.brand_input.setFixedSize(300, 40)
        self.brand_input.move(210, 160)

        self.weight_input = QtWidgets.QLineEdit(self)
        self.weight_input.setFixedSize(180, 40)
        self.weight_input.move(210, 220)

        self.weight_box = QtWidgets.QComboBox(self)
        self.weight_box.setFixedSize(115, 40)
        self.weight_box.move(395, 220)
        weight_list = ["lb", "g",]
        self.weight_box.addItems(weight_list)
        self.weight_box.setObjectName("currency_box")

        self.price_input = QtWidgets.QLineEdit(self)
        self.price_input.setFixedSize(180, 40)
        self.price_input.move(210, 280)

        self.price_box = QtWidgets.QComboBox(self)
        self.price_box.setFixedSize(115, 40)
        self.price_box.move(395, 280)
        cur_list = ["TWD", "CNY",]
        self.price_box.addItems(cur_list)
        self.price_box.setObjectName("currency_box")
        # endregion

        next_label = QtWidgets.QLabel(self)
        with open("./_icons/nextlabel.svg", "r") as f:
            xml_data = f.read()
            icon = QtGui.QPixmap()
            _bytes = QtCore.QByteArray(xml_data.encode())
            icon.loadFromData(_bytes)
            f.close()
            del xml_data
            del _bytes
            next_label.setPixmap(icon)
            del icon

        next_text = QtWidgets.QLabel(self, text="Next")
        next_text.setObjectName("info")
        next_label.move(580, 340)
        next_text.move(520, 345)

        back_label = QtWidgets.QLabel(self)
        with open("./_icons/backlabel.svg", "r") as f:
            xml_data = f.read()
            icon = QtGui.QPixmap()
            _bytes = QtCore.QByteArray(xml_data.encode())
            icon.loadFromData(_bytes)
            f.close()
            del xml_data
            del _bytes
            back_label.setPixmap(icon)
            del icon

        back_text = QtWidgets.QLabel(self, text="Back")
        back_text.setObjectName("info")
        back_label.move(20, 340)
        back_text.move(70, 345)

        next_text.mouseReleaseEvent = self.insert_new_coffee
        back_text.mouseReleaseEvent = lambda event, page_index=1: self.parent.changePage(
            page_index, event)

    def insert_new_coffee(self, event):
        try:
            conn = sqlite3.connect("simon's_coffee.db")
            sql = "insert into coffee_table (coffee_name, brand_name, weight, weight_unit,price,currency_unit) VALUES(?,?,?,?,?,?);"
            val = (self.name_input.text(), self.brand_input.text(), float(self.weight_input.text(
            )), self.weight_box.currentText(), float(self.price_input.text()), self.price_box.currentText())
            conn.execute(sql, val)
            conn.commit()
            conn.close()
            self.parent.changePage(1, event)
        except:
            logging.error('Connetion error!')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("lanny test")
        self.setFixedSize(640, 400)

        self.setStyleSheet(Path("./main.qss").read_text())
        self.initUI()

    def initUI(self):
        self.container = QtWidgets.QWidget(self)
        self.stack_layout = QtWidgets.QStackedLayout()
        self.container.setLayout(self.stack_layout)
        self.setCentralWidget(self.container)

        self.stack_layout.addWidget(greetingPage(self))
        self.stack_layout.addWidget(choosePage(self))
        self.stack_layout.addWidget(newCoffePage(self))

    def initDB(self):
        try:
            conn = sqlite3.connect("simon's_coffee.db")
            sql = "CREATE TABLE if not exists coffee_table (cid INTEGER primary key AUTOINCREMENT, coffee_name char(30) NOT NULL, brand_name char(30) NULL, weight FLOAT NOT NULL,price INT FLOAT NULL,weight_unit char(10),currency_unit char(10));"
            conn.execute(sql)
            conn.commit()
            conn.close()
        except:
            logging.error('Connetion error!')

    def changePage(self, page_index, eve):
        self.stack_layout.setCurrentIndex(page_index)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
