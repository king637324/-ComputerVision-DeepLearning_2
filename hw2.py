from sys import int_info
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep

import hw2_ui as ui

import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np
import glob
import imutils
import matplotlib.pyplot as plt
import os

from sklearn.decomposition import PCA

error = []

class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ####################
        #####    Q1    #####
        #################### 
        self.grid = (11, 8)
        self.ButtonQ1_1.clicked.connect(self.Q1_1)

        ####################
        #####    Q2    #####
        #################### 
        self.ButtonQ2_1.clicked.connect(self.Q2_1)
        self.ButtonQ2_2.clicked.connect(self.Q2_2)

        ####################
        #####    Q3    #####
        #################### 
        self.ButtonQ3_1.clicked.connect(self.Q3_1)
        ####################
        #####    Q4    #####
        #################### 
        self.ButtonQ4_1.clicked.connect(self.Q4_1)
        self.ButtonQ4_2.clicked.connect(self.Q4_2)


    def Q1_1(self):
        print("-------------Q1_1-------------")
        
        print("-------------Q1_1 Finsh-------------\n")
        
    def Q2_1(self):
        print("-------------Q2_1-------------")
        
        print("-------------Q2_1 Finsh-------------\n")

    def Q2_2(self):
        print("-------------Q2_2-------------")
        
        print("-------------Q2_2 Finsh-------------\n")
    
    def Q3_1(self):
        print("-------------Q3_1-------------")

        print("-------------Q3_1 Finsh-------------\n")

    def norm_image(self, image):
        image = image.copy()
        image -= np.min(image)
        image /= np.max(image)
        image *= 255.
        return np.uint8(image)

    def PCA_reconstruct(self, im):
        pca = PCA(25)
        x = im.reshape((400, -1))
        x_pca = pca.fit_transform(x)
        x_recover = pca.inverse_transform(x_pca)
        x_recover = x_recover.reshape(400, 400, 3)  #解析度
        x_recover = self.norm_image(x_recover)

        x_recover_gray = cv2.cvtColor(x_recover, cv2.COLOR_BGR2GRAY)
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        re = abs(im_gray - x_recover_gray)
        return x_recover, re.sum()
    
    def Q4_1(self):
        print("-------------Q4_1-------------")

        fig = plt.figure(figsize=(15, 4))
        for i in range(1, 15):
            plt.subplot(4, 14, i)
            
            im = cv2.imread(f'Dataset_CvDl_Hw2/Q4_Image/{i}.jpg')[:, :, ::-1]
            plt.xticks([])
            plt.yticks([])
            plt.imshow(im)

            plt.subplot(4, 14, i + 14)
            im = cv2.imread(f'Dataset_CvDl_Hw2/Q4_Image/{i}.jpg')[:, :, ::-1]
            plt.xticks([])
            plt.yticks([])
            im_re, re = self.PCA_reconstruct(im)
            plt.imshow(im_re)
            error.append(re)

            plt.subplot(4, 14, i + 28)
            im = cv2.imread(f'Dataset_CvDl_Hw2/Q4_Image/{i + 14}.jpg')[:, :, ::-1]
            plt.xticks([])
            plt.yticks([])
            plt.imshow(im)

            plt.subplot(4, 14, i + 42)
            im = cv2.imread(f'Dataset_CvDl_Hw2/Q4_Image/{i + 14}.jpg')[:, :, ::-1]
            plt.xticks([])
            plt.yticks([])
            im_re, re = self.PCA_reconstruct(im)
            plt.imshow(im_re)
            error.append(re)

        fig.text(0, 0.9, 'Original', va='center', rotation='vertical')
        fig.text(0, 0.65, 'Reconstruction', va='center', rotation='vertical')

        fig.text(0, 0.4, 'Original', va='center', rotation='vertical')
        fig.text(0, 0.15, 'Reconstruction', va='center', rotation='vertical')

        plt.tight_layout(pad=0.5)
        plt.savefig('temp.png')
        im = cv2.imread('temp.png')
        cv2.imshow("Image Reconstruction", im)
        if os.path.exists("temp.png"):
            os.remove("temp.png")
        

        print("-------------Q4_1 Finsh-------------\n")

        return

    
    def Q4_2(self):
        print("-------------Q4_2-------------")
        
        if error == []:
            self.Q4_1()
            print(error)
        else:
            print(error)

        print("-------------Q4_2 Finsh-------------\n")

        return

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())