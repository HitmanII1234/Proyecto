import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDial, QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self, widget,db):
        super(Login, self).__init__()
        self.original_widget = widget  # Guardar referencia al widget
        self.db = db  # Guardar referencia a la db
        dir_l = os.path.dirname(os.path.abspath(__file__))
        ui_l = os.path.join(dir_l, "u_login.ui")
        loadUi(ui_l, self)
        self.b_login.clicked.connect(self.loginbutton)


    def loginbutton(self):
        from Classes.users import usuario
        usr = usuario(self.id_emp.text(), self.pwd_emp.text())
        if self.id_emp.text() and self.pwd_emp.text():
            a = usr.login(self.db, self.original_widget) # Referencia db y widged
            if a == True:
                QMessageBox.warning(self, "Error", "Usuario y Contraseña no coinciden")
            else:
                usr.login(self.db, self.original_widget)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass


def a1(db):
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = Login(widget,db)  # Pasar el widget y db al inicio para poder ejecutar la db en otras funciones
    widget.addWidget(mainwindow)
    widget.setFixedWidth(1091)
    widget.setFixedHeight(501)
    widget.show()
    sys.exit(app.exec_())