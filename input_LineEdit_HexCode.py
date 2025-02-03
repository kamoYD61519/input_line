# PyQt5によるGUIパーツ　lineEdit 文字入力
#　16進数6桁の文字チェックを行い、color-code変数へ格納、background-color更新
import sys
from PyQt5 import QtCore as Qc, QtGui as Qg, QtWidgets as Qw    #（補足1）
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
#
#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
#from PyQt5.QtGui import QRegExpValidator
#from PyQt5.QtCore import QRegExp
from inputLineE_ui import *

class InputLineEdit(Qw.QMainWindow):

    def __init__(self,parent=None): 
        super().__init__(parent)    # 上位クラスの初期化ルーチンを呼び出す
        self.ui = Ui_MainWindow()   # importするapp.pyの中にあるUi_MainWindowsクラスのインスタンス化
        self.ui.setupUi(self)       # インスタンス・メソッドの実行

        self.setWindowTitle("カラーコード入力")

        # QLineEdit（カラーコード入力）
        self.ui.lineEdit.setPlaceholderText("6桁の16進数を入力")
        
        # 入力制限（0-9, A-F, a-f のみ）
        regex = QRegExp("^[0-9A-Fa-f]{0,6}$")
        validator = QRegExpValidator(regex, self)
        self.ui.lineEdit.setValidator(validator)

        # 確定ボタン
        self.ui.pushButton.clicked.connect(self.validate_input)
        
        # 結果表示用ラベル
        
    def validate_input(self):
        color_code = self.ui.lineEdit.text()

        # バリデーションチェック
        if len(color_code) != 6:
            self.ui.label.setText("エラー: 6桁の16進数を入力してください")
            return

        if not all(c in "0123456789ABCDEFabcdef" for c in color_code):
            self.ui.label.setText("エラー: 使用できるのは 0-9, A-F, a-f のみです")
            return

        # バリデーション成功時
        self.ui.label.setText(f"color code = #{color_code.upper()}")
        self.ui.centralwidget.setStyleSheet(f"background-color:#{color_code};\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:gray;\n"
"color:black;")

if __name__ == "__main__":
    app = Qw.QApplication(sys.argv)
    window = InputLineEdit()
    window.show()
    sys.exit(app.exec_())