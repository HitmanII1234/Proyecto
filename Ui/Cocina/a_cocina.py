import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDial, QDialog, QApplication, QGridLayout, QLabel, QMessageBox, QPushButton, QScrollArea, QSizePolicy, QVBoxLayout, QWidget
from PyQt5.uic import loadUi

class Cocina(QDialog):
    def __init__(self, widget, db):
        super(Cocina, self).__init__()
        self.original_widget = widget
        self.db = db
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_cocina.ui")
        loadUi(ui_a, self)

        self.scroll_area = self.findChild(QScrollArea, 'scroll_area')
        self.scroll_area.setWidgetResizable(True)

        self.content_widget = self.scroll_area.findChild(QWidget, 'scrollAreaWidgetContents')
        self.grid_layout = self.widget_order.findChild(QGridLayout, 'layout_content')

        self.grid_layout = QGridLayout(self.content_widget) #EL ERROR SE CORRIGE CUANDO DEFINIMOS EL GRID Y EL SCROLL AREA CON EL CONTENT WIDGET NUEVAMENMTE, PROBLEMAS DEL DESIGNR
        self.scroll_area.setWidget(self.content_widget)

        self.b_salir_1.clicked.connect(self.add_order)

    def add_order(self):
        order_card = QWidget()
        order_card.setStyleSheet("background-color: #f5f5f5; border-radius: 10px; padding: 15px; margin: 10px;")
        order_card.setMinimumSize(200, 150)
        
        card_layout = QVBoxLayout(order_card)
        order_details = QLabel(f"Mesa a · bn \n cc")
        order_details.setStyleSheet("font-weight: bold; color: white;")
        complete_btn = QPushButton("✓ Completar")
        card_layout.addWidget(order_details)
        card_layout.addWidget(complete_btn)

        # Añadir tarjeta al grid layout
        row = (self.grid_layout.count() // 3)
        col = self.grid_layout.count() % 3
        self.grid_layout.addWidget(order_card, row, col)
        
############################################################################################# Area de test
    def salir(self):
        from Ui.Login.a_login import Login
        mainwindow = Login(self.original_widget, self.db)
        self.original_widget.addWidget(mainwindow)
        self.original_widget.setFixedWidth(1091)
        self.original_widget.setFixedHeight(501)
        self.original_widget.setCurrentIndex(self.original_widget.currentIndex()+1)


def a4(db, widget):
    cocina_w = Cocina(widget,db)
    widget.addWidget(cocina_w)
    widget.setFixedWidth(1091)
    widget.setFixedHeight(501)
    widget.setCurrentIndex(widget.currentIndex() + 1)