import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import datetime
import random

class KDSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KDS - Sistema de Cocina")
        self.setGeometry(100, 100, 1200, 800)
        
        # Configuración de la UI
        self.init_ui()
        
        # Simular recepción de órdenes
        self.start_order_simulator()

    def init_ui(self):
        # Widget principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Notificación de nuevos pedidos
        self.notification_label = QLabel("ESPERANDO PEDIDOS...")
        self.notification_label.setStyleSheet("font-size: 24px; color: white; background-color: orange; padding: 10px;")
        
        # Área de scroll para las órdenes
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        # Widget para contener las órdenes en una cuadrícula
        self.orders_container = QWidget()
        self.grid_layout = QGridLayout(self.orders_container)
        self.scroll_area.setWidget(self.orders_container)
        
        # Diseño principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(self.notification_label)
        main_layout.addWidget(self.scroll_area)
        

    def add_order(self, order_data):
        """Añade una orden como una tarjeta en una cuadrícula."""
        order_card = QWidget()
        order_card.setStyleSheet("background-color: #2c2c2c; border-radius: 10px; padding: 15px; margin: 10px;")
        card_layout = QVBoxLayout(order_card)
        
        # Detalles de la orden
        order_details = QLabel(f"Mesa {order_data['table']} · {order_data['items']}\n{order_data['timestamp']}")
        order_details.setStyleSheet("font-weight: bold; color: white;")
        
        # Botón para marcar como completada
        complete_btn = QPushButton("✓ Completar")
        complete_btn.clicked.connect(lambda: self.mark_order_completed(order_card))
        
        card_layout.addWidget(order_details)
        card_layout.addWidget(complete_btn)
        
        # Añadir la tarjeta a la cuadrícula (distribuidas en 3 columnas)
        row = (self.grid_layout.count() // 3)
        col = self.grid_layout.count() % 3
        self.grid_layout.addWidget(order_card, row, col)
        
        # Actualizar notificación
        self.notification_label.setText("NUEVO PEDIDO RECIBIDO!")
        QTimer.singleShot(3000, lambda: self.notification_label.setText("ESPERANDO PEDIDOS..."))

    def mark_order_completed(self, widget):
        """Elimina la tarjeta de la cuadrícula."""
        widget.deleteLater()

    def start_order_simulator(self):
        """Simula la recepción de órdenes cada 3 segundos."""
        self.timer = QTimer()
        self.timer.timeout.connect(self.generate_mock_order)
        self.timer.start(3000)

    def generate_mock_order(self):
        """Genera una orden de ejemplo."""
        tables = [1, 2, 3, 4]
        items = ["Hamburguesa", "Pizza", "Ensalada", "Tacos"]
        order_data = {
            "table": random.choice(tables),
            "items": random.choice(items),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        self.add_order(order_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KDSWindow()
    window.show()
    sys.exit(app.exec_())