from PySide6.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem,QGraphicsTextItem,QGraphicsItem,
                               QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget,QGraphicsLineItem)
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QColor, QBrush,QPen
from random import randint

class MovableRect(QGraphicsRectItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.previous_pos = None
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setPen(QPen(QColor(0, 0, 0), 2))  # Set the initial border color to black

    def mousePressEvent(self, event):
        self.previous_pos = self.pos()
        self.setPen(QPen(QColor(255, 255, 0), 2))  # Set the border color to yellow when selected
        super().mousePressEvent(event)
    def mouseReleaseEvent(self, event):
        if self.previous_pos != self.pos():
            self.update_text()
        super().mouseReleaseEvent(event)
    def hoverLeaveEvent(self, event):
        if not self.isSelected():
            self.setPen(QPen(Qt.NoPen))  # Reset the border color when not selected
        super().hoverLeaveEvent(event)
    
    def update_text(self):
        intensity_start = self.x() / self.scene().width() * 5
        intensity_end = (self.x() + self.rect().width()) / self.scene().width() * 5
        time_start = QTime(0, 0).addSecs(self.y() / self.scene().height() * 24 * 60 * 60).toString("HH:mm")
        time_end = QTime(0, 0).addSecs((self.y() + self.rect().height()) / self.scene().height() * 24 * 60 * 60).toString("HH:mm")
        self.text.setPlainText(f"Intensity: {intensity_start:.1f}-{intensity_end:.1f}\nTime: {time_start}-{time_end}")
        print(self.text)
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
        self.view.setFixedSize(self.width() / 2,self.height())  # Limit the width of self.view
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.view.scale(0.96, 0.96) #终于调好画布大小不用拖拽显示啦！
        self.layout.addWidget(self.view)

        self.generate_button.clicked.connect(self.generate_rectangle)
        # Draw x and y axes
        self.draw_axes()

        # Set the height ratio of each part in the layout
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 1)
        self.layout.setStretch(2, 1)
        self.layout.setStretch(3, 4)
        

    def draw_axes(self):
        # Clear the axes
        for item in self.scene.items():
            if isinstance(item, QGraphicsLineItem) or isinstance(item, QGraphicsTextItem):
                self.scene.removeItem(item)

        # Draw reference line
        reference_line = QGraphicsLineItem(0, self.scene.height() / 2, self.scene.width(), self.scene.height() / 2)
        reference_line.setPen(QPen(QColor(255, 0, 0), 2))  # Set the color to red and the width to 2
        self.scene.addItem(reference_line)


        # Draw x axis
        x_axis = QGraphicsLineItem(0, self.scene.height(), self.scene.width(), self.scene.height())
        x_axis.setPen(QPen(QColor(0, 0, 255)))
        #self.scene.addItem(x_axis)

        # Draw y axis
        y_axis = QGraphicsLineItem(0, 0, 0, self.scene.height())
        y_axis.setPen(QPen(QColor(255, 0, 0)))
        #self.scene.addItem(y_axis)

        # Draw x axis ticks (every 0.1 intensity)
        for i in range(1, 51):
            x = i * self.scene.width() / 50
            tick = QGraphicsLineItem(x, self.scene.height(), x, self.scene.height() - 10)

            # Add labels every 0.5 intensity
            if i % 5 == 0:
                label = QGraphicsTextItem(f"{i * 0.1:.1f}")
                label.setPos(x, self.scene.height() - 20)
                self.scene.addItem(label)

                # Emphasize the tick with a darker color
                tick.setPen(QPen(QColor(235, 200, 141)))
            else:
                tick.setPen(QPen(QColor(0, 0, 255)))

            self.scene.addItem(tick)

        # Draw y axis ticks (every hour)
        for i in range(24):
            y = self.scene.height() - i * self.scene.height() / 24
            tick = QGraphicsLineItem(0, y, 10, y)
            tick.setPen(QPen(QColor(255, 0, 0)))
            self.scene.addItem(tick)

            # Add labels every hour
            label = QGraphicsTextItem(f"{24-i:02d}:00")
            label.setPos(20, y-10)
            self.scene.addItem(label)

            # Emphasize the tick with a darker color
            tick.setPen(QPen(QColor(128, 0, 0)))
    

    def resizeEvent(self, event):
        super().resizeEvent(event)  # Call the parent class's resizeEvent method
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.draw_axes()  # Redraw axes when the window is resized
        # Update text for all MovableRect items
        for item in self.scene.items():
            if isinstance(item, MovableRect):
                item.update_text()
                print("item.update_text()")    
        
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
        
        
      
        

    

if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()