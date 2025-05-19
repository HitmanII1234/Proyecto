import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

class Recepcion(QDialog):
    def __init__(self, widget, db, c_name):
        super(Recepcion, self).__init__()
        self.original_widget = widget  # Guardar referencia al widget
        self.db = db  # Guardar referencia a la db
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_recepcion.ui")
        loadUi(ui_a, self)
        self.color=['#589f37','#cca20c','#a12000']
        self.color_sub=['#5eaa3b','#d6ab0d','#ad2500']
        self.color_sub2=['#6cc644','#f6c40f','#bd2c00']
        self.encargado_name.setText(c_name)

        self.Reservaciones.hide()
        self.Reservaciones_2.hide()
        self.Reservaciones_3.hide()
        self.Reservaciones_4.hide()
        self.cargar_mesas()
        self.act_table()

        self.m_1.clicked.connect(lambda: self.upd_mesa(1, db))
        self.m_2.clicked.connect(lambda: self.upd_mesa(2, db))
        self.m_3.clicked.connect(lambda: self.upd_mesa(3, db))
        self.m_4.clicked.connect(lambda: self.upd_mesa(4, db))
        self.m_5.clicked.connect(lambda: self.upd_mesa(5, db))
        self.m_6.clicked.connect(lambda: self.upd_mesa(6, db))
        self.m_7.clicked.connect(lambda: self.upd_mesa(7, db))
        self.m_8.clicked.connect(lambda: self.upd_mesa(8, db))
        self.m_9.clicked.connect(lambda: self.upd_mesa(9, db))
        self.m_10.clicked.connect(lambda: self.upd_mesa(10, db))
        self.m_11.clicked.connect(lambda: self.upd_mesa(11, db))
        self.m_12.clicked.connect(lambda: self.upd_mesa(12, db))
        self.m_13.clicked.connect(lambda: self.upd_mesa(13, db))
        self.m_14.clicked.connect(lambda: self.upd_mesa(14, db))
        self.m_15.clicked.connect(lambda: self.upd_mesa(15, db))
        self.m_16.clicked.connect(lambda: self.upd_mesa(16, db))
        self.m_17.clicked.connect(lambda: self.upd_mesa(17, db))
        self.m_18.clicked.connect(lambda: self.upd_mesa(18, db))
        self.m_19.clicked.connect(lambda: self.upd_mesa(19, db))
        self.m_20.clicked.connect(lambda: self.upd_mesa(20, db))
        self.m_21.clicked.connect(lambda: self.upd_mesa(21, db))

        self.b_agregar_resv_2.clicked.connect(self.agregar_resv)
        self.b_editar_resv_3.clicked.connect(self.edt_resv)
        self.b_eliminar_resv_4.clicked.connect(self.delete_resv)

        self.b_salir_1.clicked.connect(self.salir)


    def agregar_resv(self):
        if not all([self.resv_2_name.text(), self.resv_2_cant.text(), self.resv_2_fecha.text(), self.resv_2_hora.text()]):
            QMessageBox.warning(self, "Búsqueda vacía", "Por favor, complete todos los campos.")
            return
        try:
            self.db.dbcursor.execute("INSERT INTO Users.mesas_resv (nombre, cantidad, fecha, hora) VALUES (%s, %s, %s, %s);", (self.resv_2_name.text(), self.resv_2_cant.text(), self.resv_2_fecha.text(), self.resv_2_hora.text()))
            self.db.commit()
            self.act_table()
            self.Reservaciones_2.hide()
            self.Reservaciones.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", "No se pudo agregar la reservación. Verifique los datos")
            return

    def edt_resv(self):
        if not all(self.resv_3_codigo.text()):
            QMessageBox.warning(self, "Búsqueda vacía", "Por favor, introduzca un codigo.")
        try:
            campos = []
            values = [] 
            if not self.resv_3_name.text().strip() == '':
                a1 = "nombre = %s"
                campos.append(a1)
                values.append(self.resv_3_name.text().strip())
            if not self.resv_3_cantidad.text().strip() == '':
                a2 = "cantidad = %s"
                campos.append(a2)
                values.append(self.resv_3_cantidad.text().strip())
            if not self.resv_3_fecha.text().strip() == '':
                a3 = "fecha = %s"
                campos.append(a3)
                values.append(self.resv_3_fecha.text().strip())
            if not self.resv_3_hora.text().strip() == '':
                a4 = "hora = %s"
                campos.append(a4)
                values.append(self.resv_3_hora.text().strip())
            
            campos_clause = ", ".join(campos)
            values.append(self.resv_3_codigo.text())
            try:
                self.db.dbcursor.execute(f"UPDATE Users.mesas_resv SET {campos_clause} WHERE id_resv = %s;", values)
                self.db.commit()
                self.act_table()
                self.act_table()
                self.Reservaciones_3.hide()
                self.resv_3_codigo.clear()
                self.resv_3_name.clear()
                self.resv_3_cantidad.clear()
                self.resv_3_fecha.clear()
                self.resv_3_hora.clear()
            except:
                QMessageBox.warning(self, "Error", "Verifique los campos.")
        except:
            QMessageBox.warning(self, "Error", "Verifique los campos")

    def delete_resv(self):
        if not self.resv_4_codigo.text():
            QMessageBox.warning(self, "Búsqueda vacía", "Por favor, introduzca un codigo.")
        try:
            code = int(self.resv_4_codigo.text())
            self.db.dbcursor.execute("DELETE FROM Users.mesas_resv WHERE id_resv = %s;", (code,))
            self.db.commit()
            self.act_table()
            self.Reservaciones_4.hide()
            self.resv_4_codigo.clear()
        except:
            QMessageBox.warning(self, "Error", "No se pudo eliminar la reservación. Verifique los datos")

    def act_table(self):
        try:
            self.resv_widget.setRowCount(0)
            self.db.dbcursor.execute("SELECT id_resv, nombre, cantidad, fecha, hora FROM Users.mesas_resv")
            data = self.db.dbcursor.fetchall()
            self.resv_widget.setRowCount(len(data))
            for n, row in enumerate(data):
                for m, item in enumerate(row):
                    self.resv_widget.setItem(
                        n, m, QtWidgets.QTableWidgetItem(str(item)))
            self.resv_widget.resizeColumnsToContents()
        except:
            QMessageBox.warning(self, "Error", "Error en la funcion act_table")
            return

    def upd_mesa(self, n, db):
        button = getattr(self, f'm_{n}')
        style = button.styleSheet()
        current_color = style.split("QPushButton {background-color:")[1].split(";")[0].strip()
        next_color = self.color[(self.color.index(current_color) + 1) % len(self.color)]
        next_color_sub = self.color_sub[(self.color.index(current_color) + 1) % len(self.color)]
        next_color_sub2 = self.color_sub2[(self.color.index(current_color) + 1) % len(self.color)]
        style_n = style.replace("QPushButton {background-color: "+current_color+';', "QPushButton {background-color: "+next_color+';')
        style_nsub = style_n.replace("QPushButton:hover {background-color: "+self.color_sub[self.color.index(current_color) % len(self.color)]+';', "QPushButton:hover {background-color: "+next_color_sub+';')
        style_nsub2 = style_nsub.replace("QPushButton:pressed {background-color: "+self.color_sub2[self.color.index(current_color) % len(self.color)]+';', "QPushButton:pressed {background-color: "+next_color_sub2+';')
        db.dbcursor.execute("UPDATE Users.mesas SET v1 = %s, v2 = %s, v3 = %s WHERE mesa = %s;", (next_color, next_color_sub, next_color_sub2, button.text()))
        db.commit()

        button.setStyleSheet(style_nsub2)

    def cargar_mesas(self):
        self.db.dbcursor.execute("SELECT v1 FROM Users.mesas")
        data = self.db.dbcursor.fetchall()
        for n in range(len(data)):
            dat = str(data[n])
            if dat == (f"('{self.color[0]}',)"):
                c = self.color[0]
                c_sub= self.color_sub2[0]
                c_sub2 = self.color[0]
            elif dat == (f"('{self.color[1]}',)"):
                c = self.color[1]
                c_sub = self.color_sub[1]
                c_sub2 = self.color_sub2[1]
            else:
                c = self.color[2]   
                c_sub = self.color_sub[2]
                c_sub2 = self.color_sub2[2]

            button = getattr(self, f'm_{n+1}')
            style = button.styleSheet()
            style_n = style.replace("QPushButton {background-color: #589f37;", "QPushButton {background-color: "+c+';')
            style_nsub = style_n.replace("QPushButton:hover {background-color: #5eaa3b;", "QPushButton:hover {background-color: "+c_sub+';')
            style_nsub2 = style_nsub.replace("QPushButton:pressed {background-color: #6cc644;", "QPushButton:pressed {background-color: "+c_sub2+';')
            button.setStyleSheet(style_nsub2)

    def salir(self):
        from Ui.Login.a_login import Login
        mainwindow = Login(self.original_widget, self.db)
        self.original_widget.addWidget(mainwindow)
        self.original_widget.setFixedWidth(1091)
        self.original_widget.setFixedHeight(501)
        self.original_widget.setCurrentIndex(self.original_widget.currentIndex()+1)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass



def a2(db, widget, c_name):
    recep_w = Recepcion(widget, db, c_name)
    widget.addWidget(recep_w)
    widget.setFixedWidth(1091)
    widget.setFixedHeight(501)
    widget.setCurrentIndex(widget.currentIndex() + 1)
