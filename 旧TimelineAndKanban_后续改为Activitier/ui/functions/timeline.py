import sys

from PySide6.QtCore import Qt, QRectF, QPoint
from PySide6.QtGui import QColor, QPainterPath
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsLineItem, QGraphicsRectItem, QPushButton, QVBoxLayout, QWidget, QMainWindow, QGraphicsItem
class Timeline(QGraphicsView):
    def __init__(self):
        super().__init__()
        
        # 禁用滚动条
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # 创建场景
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        # 画时间线
        self.timeLine = QGraphicsLineItem()
        self.timeLine.setLine(0,0,24*60*1,0)  # 修改时间线的长度以匹配分钟数，每分钟的像素长度为1
        self.timeLine.setPen(QColor(0,255,0)) # 设置时间线的颜色为绿色
        self.scene.addItem(self.timeLine)
        
        # 画时间点 
        for i in range(24*60):
            item = QGraphicsRectItem(0,0,1,5)
            item.setPos(i*1,0)
            self.scene.addItem(item)
            
        # 画紧张度轴
        self.intensityLine = QGraphicsLineItem()
        self.intensityLine.setLine(0,0,0,5*10*2)  # 修改紧张度轴的长度以匹配紧张度级别
        self.intensityLine.setPen(QColor(0,0,255)) # 设置紧张度轴的颜色为蓝色
        self.scene.addItem(self.intensityLine)
        
        # 画紧张度级别
        for i in range(1, 5*10+1):
            item = QGraphicsRectItem(0,0,5,5)
            item.setPos(0,i*10)
            self.scene.addItem(item)
            
        # 选中范围 
        self.selection = QGraphicsRectItem()
        self.selection.setPen(QColor(255,0,0))
        self.selection.setBrush(QColor(255,0,0))  # 设置矩形的填充颜色为红色
        self.selection.setFlag(QGraphicsItem.ItemIsMovable)  # 启用ItemIsMovable标志
        self.scene.addItem(self.selection)  # 添加到场景中
        
        # 按钮
        self.printButton = QPushButton("Print Time")
        self.printButton.clicked.connect(self.printTime)
        
    def mousePressEvent(self,event):
        self.origin = event.position().toPoint()  # 记录鼠标点击的位置
        
    def mouseMoveEvent(self, event):
        if self.origin is not None and self.selection.contains(event.position()):
            diff = event.position().toPoint() - self.origin  # 计算鼠标移动的距离
            self.selection.setPos(self.selection.pos() + diff)  # 移动矩形
            self.origin = event.position().toPoint()  # 更新鼠标点击的位置
        QGraphicsView.mouseMoveEvent(self, event)  # 调用父类的方法来处理事件

    def mouseReleaseEvent(self,event):
        if self.origin is not None:
            self.selection.setRect(QRectF(self.origin,event.position().toPoint()).normalized())  # 使用position().toPoint()代替pos()
            self.ensureVisible(self.selection.rect())  # 确保选中的区域总是可见的
        
    def printTime(self):
        startX = self.selection.rect().left()
        endX = self.selection.rect().right()
        startY = self.selection.rect().top()
        endY = self.selection.rect().bottom()
        startHour, startMinute = divmod(startX/1, 60)  # 将像素值转换为小时和分钟
        endHour, endMinute = divmod(endX/1, 60)  # 将像素值转换为小时和分钟
        startIntensity = startY/20  # 将像素值转换为紧张度级别
        endIntensity = endY/20  # 将像素值转换为紧张度级别
        print(f"Start Time: {startHour:02.0f}:{startMinute:02.0f} End Time: {endHour:02.0f}:{endMinute:02.0f} Start Intensity: {startIntensity:.1f} End Intensity: {endIntensity:.1f}")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    timeline = Timeline()
    
    # 创建一个主窗口
    window = QMainWindow()
    # 创建一个布局并添加你的时间线和按钮
    layout = QVBoxLayout()
    layout.addWidget(timeline)
    layout.addWidget(timeline.printButton)
    
    # 创建一个小部件，设置布局，然后设置为主窗口的中心小部件
    widget = QWidget()
    widget.setLayout(layout)
    window.setCentralWidget(widget)
    
    window.show()
    sys.exit(app.exec())