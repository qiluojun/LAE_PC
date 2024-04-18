from PySide6.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem,QGraphicsTextItem,QGraphicsItem,
                               QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget)
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QColor, QBrush,QPen
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
            self.update_text()
        super().mouseReleaseEvent(event)
    def update_text(self):
        intensity_start = self.x() / self.scene().width() * 5
        intensity_end = (self.x() + self.rect().width()) / self.scene().width() * 5
        time_start = QTime(0, 0).addSecs(self.y() / self.scene().height() * 24 * 60 * 60).toString("HH:mm")
        time_end = QTime(0, 0).addSecs((self.y() + self.rect().height()) / self.scene().height() * 24 * 60 * 60).toString("HH:mm")
        self.text.setPlainText(f"Intensity: {intensity_start:.1f}-{intensity_end:.1f}\nTime: {time_start}-{time_end}")
        
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
        #固定画布大小
       
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.layout.addWidget(self.view)

        self.generate_button.clicked.connect(self.generate_rectangle)
        # Draw x and y axes
        self.draw_axes()
        
    def draw_axes(self):
        # Clear the scene
        self.scene.clear()

        # Draw x axis
        x_axis = self.scene.addLine(0, self.scene.height(), self.scene.width(), self.scene.height(), QPen(QColor(0, 0, 255)))
        # Draw y axis
        y_axis = self.scene.addLine(0, 0, 0, self.scene.height(), QPen(QColor(255, 0, 0)))

        # Draw x axis ticks
        for i in range(1, 51):
            x = i * self.scene.width() / 50
            tick = self.scene.addLine(x, self.scene.height(), x, self.scene.height() - 10, QPen(QColor(0, 0, 255)))

        # Draw y axis ticks (every minute)
        for i in range(24 * 60):
            y = i * self.scene.height() / (24 * 60)
            tick = self.scene.addLine(0, y, 10, y, QPen(QColor(255, 0, 0)))

    def resizeEvent(self, event):
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.draw_axes()  # Redraw axes when the window is resized
            
        
    def generate_rectangle(self):
        width_ratio = float(self.width_input.text()) / 100
        height_ratio = float(self.height_input.text()) / 100
        width = self.view.width() * width_ratio
        height = self.view.height() * height_ratio
        rect = MovableRect(0, 0, width, height)
        #rect.setFlag(QGraphicsItem.ItemPositionChange)  # Set the flag
        rect.setPos((self.view.width() - width) / 2, self.view.height() * 0.7 - height / 2)  # Set the rectangle in the middle bottom of the view
        rect.setFlag(QGraphicsRectItem.ItemIsMovable)  # Make the rectangle movable
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255), 127)  # Create a random semi-transparent color
        rect.setBrush(QBrush(color))  # Set the color of the rectangle

        # Create a QGraphicsTextItem to display the intensity and time
        text = QGraphicsTextItem(f"", rect)
        rect.text = text

        self.scene.addItem(rect)
        rect.update_text()
        self.scene.addItem(text)
        

    

if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()