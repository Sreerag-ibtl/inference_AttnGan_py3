from PyQt5.QtWidgets import (QWidget,QApplication,QMainWindow,QGridLayout,
                             QLineEdit,QLabel,QPushButton,QStackedWidget)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.widget=QWidget()
        self.le=QLineEdit()
        self.pb=QPushButton("Generate")
        self.lb1=QLabel()
        self.lb1.setScaledContents(True)
        self.lb2=QLabel()
        self.lb2.setScaledContents(True)
        self.lb3=QLabel()
        self.lb3.setScaledContents(True)
        self.pb.clicked.connect(self.generate)
        self.lo=QGridLayout(self.widget)
        self.lo.addWidget(self.le)
        self.lo.addWidget(self.pb)
        self.lo.addWidget(self.lb1)
        self.lo.addWidget(self.lb2)
        self.lo.addWidget(self.lb3)
        self.widget2=QWidget()
        self.lb=QLabel()
        self.lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.text="Text2Image"
        self.lb.setText(self.text)
        self.lo2=QGridLayout(self.widget2)
        self.pb2=QPushButton("Go")
        self.pb2.clicked.connect(self.go)
        self.lo2.addWidget(self.lb)
        self.lo2.addWidget(self.pb2)
        self.sw=QStackedWidget()
        self.sw.addWidget(self.widget2)
        self.sw.addWidget(self.widget)
        self.setCentralWidget(self.sw)
    def go(self):
        self.sw.setCurrentIndex(1)
    def generate(self):
        text=self.le.text()
        with open("../data/birds/example_captions.txt","w") as f:
            f.write(text)
        os.system("python main.py --cfg cfg/eval_bird.yml --gpu -1")
        self.pmap1=QPixmap("../models/bird_AttnGAN2/example_captions/0_s_0_g0.png")
        self.pmap2=QPixmap("../models/bird_AttnGAN2/example_captions/0_s_0_g1.png")
        self.pmap3=QPixmap("../models/bird_AttnGAN2/example_captions/0_s_0_g2.png")
        self.lb1.setPixmap(self.pmap1)
        self.lb2.setPixmap(self.pmap2)
        self.lb3.setPixmap(self.pmap3)
if __name__=="__main__":
    app=QApplication([])
    mw=MainWindow()
    mw.show()
    app.exec_()
        
