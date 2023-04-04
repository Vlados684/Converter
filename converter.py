from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import glob
from PIL import *
from img2pdf import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        self.dir_label = QtWidgets.QLabel(MainWindow)
        self.dir_label.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.dir_label.setText("Выбрана директория: ")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 350)
        MainWindow.setStyleSheet(
            "background-color: rgb(170, 255, 255);\n"
            "background-color: rgb(237, 255, 203);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 50))
        font = QtGui.QFont()
        font.setFamily("Seagull")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(188, 185, 255);")
        self.label.setObjectName("label")

        self.button_JPG = QtWidgets.QPushButton(self.centralwidget)
        self.button_JPG.setGeometry(QtCore.QRect(30, 70, 100, 25))
        self.button_JPG.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "font: 8pt \"Seagull\";")
        self.button_JPG.setObjectName("button_JPG")

        self.button_PNG = QtWidgets.QPushButton(self.centralwidget)
        self.button_PNG.setGeometry(QtCore.QRect(30, 140, 100, 25))
        self.button_PNG.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "font: 8pt \"Seagull\";")
        self.button_PNG.setObjectName("button_PNG")

        self.button_TIFF = QtWidgets.QPushButton(self.centralwidget)
        self.button_TIFF.setGeometry(QtCore.QRect(370, 70, 100, 25))
        self.button_TIFF.setStyleSheet(
            "font: 8pt \"Seagull\";\n"
            "background-color: rgb(255, 255, 255);")
        self.button_TIFF.setObjectName("button_TIFF")

        self.button_RAW = QtWidgets.QPushButton(self.centralwidget)
        self.button_RAW.setGeometry(QtCore.QRect(370, 140, 100, 25))
        self.button_RAW.setStyleSheet(
            "font: 8pt \"Seagull\";\n"
            "background-color: rgb(255, 255, 255);")
        self.button_RAW.setObjectName("button_RAW")

        self.button_BMP = QtWidgets.QPushButton(self.centralwidget)
        self.button_BMP.setGeometry(QtCore.QRect(195, 140, 100, 25))
        self.button_BMP.setStyleSheet(
            "font: 8pt \"Seagull\";\n"
            "background-color: rgb(255, 255, 255);")
        self.button_BMP.setObjectName("button_BMP")

        self.button_GIF = QtWidgets.QPushButton(self.centralwidget)
        self.button_GIF.setGeometry(QtCore.QRect(195, 70, 100, 25))
        self.button_GIF.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "font: 8pt \"Seagull\";")
        self.button_GIF.setObjectName("button_GIF")

        self.button_convert = QtWidgets.QPushButton(self.centralwidget)
        self.button_convert.setGeometry(QtCore.QRect(50, 250, 150, 50))
        self.button_convert.setStyleSheet(
            "font: 8pt \"Seagull\";\n"
            "background-color: rgb(255, 255, 255);")
        self.button_convert.setObjectName("button_convert")

        self.button_convert_TIFF = QtWidgets.QPushButton(self.centralwidget)
        self.button_convert_TIFF.setGeometry(QtCore.QRect(300, 250, 150, 50))
        self.button_convert_TIFF.setStyleSheet(
            "font: 8pt \"Seagull\";\n"
            "background-color: rgb(255, 255, 255);")
        self.button_convert_TIFF.setObjectName("button_convert_TIFF")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.button_JPG.clicked.connect(self.choose_table_JPG)
        self.button_PNG.clicked.connect(self.choose_table_PNG)
        self.button_GIF.clicked.connect(self.choose_table_GIF)
        self.button_BMP.clicked.connect(self.choose_table_BMP)
        self.button_TIFF.clicked.connect(self.choose_table_TIFF)
        self.button_RAW.clicked.connect(self.choose_table_RAW)

        self.button_JPG.clicked.connect(self.onClick)
        self.button_PNG.clicked.connect(self.onClick)
        self.button_BMP.clicked.connect(self.onClick)
        self.button_GIF.clicked.connect(self.onClick)
        self.button_TIFF.clicked.connect(self.onClick)
        self.button_RAW.clicked.connect(self.onClick)

        self.button_convert.clicked.connect(self.converter)
        self.button_convert_TIFF.clicked.connect(self.convert_TIFF)


    def retranslateUi(self, MainWindow):
        self.setWindowIcon(QIcon('web/icon.png'))
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конвертатер в PDF"))
        self.label.setText(_translate("MainWindow", " Программа для конвертации различных файлов в формат PDF"))
        self.button_JPG.setText(_translate("MainWindow", "Файл JPG"))
        self.button_PNG.setText(_translate("MainWindow", "Файл PNG"))
        self.button_TIFF.setText(_translate("MainWindow", "Файл TIFF"))
        self.button_BMP.setText(_translate("MainWindow", "Файл BMP"))
        self.button_GIF.setText(_translate("MainWindow", "Файл GIF"))
        self.button_RAW.setText(_translate("MainWindow", "Файл RAW"))
        self.button_convert.setText(_translate("MainWindow", "Конвертировать"))
        self.button_convert_TIFF.setText(_translate("MainWindow", "Конвертировать TIFF в JPG"))



    def choose_table_files(self, file_type):
        image_files, _ = QFileDialog.getOpenFileNames(self, 'Выберите файл', os.path.expanduser("~"), f'Image files (*.{file_type})')
        if image_files:
            for image_file in image_files:
                pixmap = QPixmap(image_file)
                self.label.setPixmap(pixmap)
        self.file_type = file_type
        return image_files

    def choose_table_JPG(self):
        self.choose_table_files('jpg')
        return


    def choose_table_PNG(self):
        self.choose_table_files('png')
        return


    def choose_table_GIF(self):
        self.choose_table_files('gif')
        return


    def choose_table_BMP(self):
        self.choose_table_files('bmp')
        return


    def choose_table_TIFF(self):
        self.choose_table_files('tif')
        return


    def choose_table_RAW(self):
        self.choose_table_files('raw')
        return


    def onClick(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
        if directory:
            self.thedir = str(directory)
            print('Выбрана директория: ' + self.thedir)
            self.dir_label.setText(self.thedir)
        else:
            print('Директория не выбрана.')
        return


    def convert_TIFF(self):
        for files in glob.glob(os.path.join(self.thedir, '*.tiff')):
            name_wo_ext = os.path.splitext(files)[0]
            with Image.open(files) as im:
                rgb_convert = im.convert('RGB')
                rgb_convert.save(name_wo_ext + '.jpg')
        print("Конвертация TIFF-изображений в JPG завершена")
        return
    
    def converter(self):
        imgs = []
        for r, _, f in os.walk(self.thedir):
            for fname in f:
                if not fname.endswith((".jpg", ".png", ".bmp", ".tiff", ".tif", ".gif", ".raw")):
                    continue
                imgs.append(os.path.join(r, fname))
        pdf = canvas.Canvas(os.path.join(self.thedir, 'WORK.pdf'), pagesize=letter)
        for img_path in imgs:
            with Image.open(img_path) as img:
                width, height = img.size
                if width > height:
                    pdf.setPageSize((height, width))
                else:
                    pdf.setPageSize((width, height))
                pdf.drawImage(img_path, 0, 0, width, height)
                pdf.showPage()
        pdf.save()
        print("Конвертация в PDF завершена")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
