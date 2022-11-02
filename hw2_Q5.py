from sys import int_info
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep

import hw2Q5_ui as ui

import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np
import glob
import imutils
import matplotlib.pyplot as plt
import os

from sklearn.decomposition import PCA


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ButtonQ5_1.clicked.connect(self.Q5_1)
        self.ButtonQ5_2.clicked.connect(self.Q5_2)
        self.ButtonQ5_3.clicked.connect(self.Q5_3)
        self.ButtonQ5_4.clicked.connect(self.Q5_4)



    def Q5_1(self):
        print("-------------Q5_1-------------")
        
        print("-------------Q5_1 Finsh-------------\n")

    def Q5_2(self):
        print("-------------Q5_2-------------")
        
        print("-------------Q5_2 Finsh-------------\n")

    def Q5_3(self):
        print("-------------Q5_3-------------")
        
        print("-------------Q5_3 Finsh-------------\n")
    
    def Q5_4(self):
        print("-------------Q5_4-------------")
        
        print("-------------Q5_4 Finsh-------------\n")
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())