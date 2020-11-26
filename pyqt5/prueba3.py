import sys
import cv2
import numpy

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.image = None
        self.label = QLabel()
        self.initUI()

    def initUI(self):
        self.label.setText('Imagen')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('border: gray; border-style:solid; border-width: 1px;')

        btn_open = QPushButton('Abir Imagen...')
        btn_open.clicked.connect(self.abrirImagen)
        
        btn_thresh = QPushButton('Thresholding')
        btn_thresh.clicked.connect(self.Thresholding)

        top_bar = QHBoxLayout()
        top_bar.addWidget(btn_open)
        top_bar.addWidget(btn_thresh)

        root = QVBoxLayout(self)
        root.addLayout(top_bar)
        root.addWidget(self.label)

        self.resize(540, 574)
        self.setWindowTitle('Operadores Punto')

    def abrirImagen(self):
        filename, _ = QFileDialog.getOpenFileName(None, 'Buscar Imagen', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if filename:
                self.image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
                self.mostrarImagen()

                
    def Thresholding(self):
        h,w,channel=self.image.shape
        
        print(h)
        print(w)
        print(self.image.shape)
        for i in range(h):
            for j in range(w):
                if self.image[i][j][0]<60 and self.image[i][j][1]<60 and self.image[i][j][2]<60:
                    self.image[i][j]=255
                else:
                    self.image[i][j]=0
                    
        imagenaux=self.image
        cv2.imwrite('imagen1.png',imagenaux)
        
                

        '''
        if self.image is not None:
            # self.image = cv2.GaussianBlur(self.image, (5, 5), 0)
            # self.image = cv2.Canny(self.image, 100, 200)

            gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY) \
                if len(self.image.shape) >= 3 else self.image

            blur = cv2.GaussianBlur(gray, (21, 21), 0, 0)

            self.image = cv2.divide(gray, blur, scale=256)
            self.mostrarImagen()
        '''
        self.mostrarImagen()
    def mostrarImagen(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()
        
    
        self.label.setPixmap(QPixmap.fromImage(img))
        self.label.setPixmap(QPixmap(img).scaled(550, 584,Qt.KeepAspectRatio,
                                                 Qt.SmoothTransformation))
        self.resize(self.label.pixmap().size())

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())
