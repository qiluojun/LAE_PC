from PySide6.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem,
                               QVBoxLayout,QGraphicsItem, QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QBrush
from random import randint




class MovableRect(QGraphicsRectItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.previous_pos = None

    def mousePressEvent(self, event):
        self.previous_pos = self.pos()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.previous_pos != self.pos():
            print("矩形已移动")
        super().mouseReleaseEvent(event)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)  # Set the initial size of the window
        self.layout = QVBoxLayout(self)

        self.width_layout = QHBoxLayout()
        self.width_label = QLabel('宽度(%):', self)
        self.width_input = QLineEdit('50', self)
        self.width_layout.addWidget(self.width_label)
        self.width_layout.addWidget(self.width_input)

        self.height_layout = QHBoxLayout()
        self.height_label = QLabel('高度(%):', self)
        self.height_input = QLineEdit('50', self)
        self.height_layout.addWidget(self.height_label)
        self.height_layout.addWidget(self.height_input)

        self.generate_button = QPushButton('生成', self)

        self.layout.addLayout(self.width_layout)
        self.layout.addLayout(self.height_layout)
        self.layout.addWidget(self.generate_button)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)

        self.layout.addWidget(self.view)

        self.generate_button.clicked.connect(self.generate_rectangle)

    def generate_rectangle(self):
        width_ratio = float(self.width_input.text()) / 100
        height_ratio = float(self.height_input.text()) / 100
        width = self.view.width() * width_ratio
        height = self.view.height() * height_ratio
        rect = MovableRect(0, 0, width, height)
        #rect.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        rect.setPos((self.view.width() - width) / 2, self.view.height() * 0.7 - height / 2)  # Set the rectangle in the middle bottom of the view
        rect.setFlag(QGraphicsRectItem.ItemIsMovable)  # Make the rectangle movable
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255), 127)  # Create a random semi-transparent color
        rect.setBrush(QBrush(color))  # Set the color of the rectangle
        self.scene.addItem(rect)
    def resizeEvent(self, event):
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())



if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()