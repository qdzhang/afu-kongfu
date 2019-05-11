import random
import sys
from PyQt5 import QtWidgets
from main_gui import Ui_MainWindow
from about import Ui_Dialog


class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("关于")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("骚话王阿福")
        self.ui.pushButton.clicked.connect(self.btn_clicked)
        self.ui.action_2.triggered.connect(self.about_clicked)

    def btn_clicked(self):
        with open(r'dict_cn_en.txt', 'r', encoding='utf-8') as fp:
            all_words_list = fp.readlines()

        random_index = random.randint(0, len(all_words_list))
        self.ui.textBrowser.setText(all_words_list[random_index])

    def about_clicked(self):
        self.new_dialog = AboutDialog()
        self.new_dialog.show()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
