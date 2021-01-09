# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IMayProtoShow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import IMayFunctions

Full_logo = "full_logo.png"
Globe_logo = "globe_logo.png"
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget_1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_1.setObjectName("listWidget_1")
        self.gridLayout_2.addWidget(self.listWidget_1, 1, 0, 1, 3)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_2.addWidget(self.listWidget_2, 2, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("IMay Neural Network")
        self.gridLayout_2.addWidget(self.comboBox, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.addDirectory = QtWidgets.QToolButton(self.centralwidget)
        self.addDirectory.setObjectName("addDirectory")
        self.gridLayout_2.addWidget(self.addDirectory, 0, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../IMayGui/Directory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.deleteButton)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NextButton)
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setObjectName("CancelButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CancelButton)
        self.DeleteAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteAllButton.setObjectName("DeleteAllButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DeleteAllButton)
        self.gridLayout_2.addLayout(self.formLayout, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(Full_logo))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 26))
        self.menubar.setObjectName("menubar")
        self.menuIMay_prototype = QtWidgets.QMenu(self.menubar)
        self.menuIMay_prototype.setObjectName("menuIMay_prototype")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuIMay_prototype.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.deleteButton.clicked.connect(lambda: self.delete_class_dia())
        self.toolButton.clicked.connect(lambda: self.directory_dialog())
        self.addDirectory.clicked.connect(lambda: self.add_directory())
        self.NextButton.clicked.connect(lambda: self.create_directory())
        self.CancelButton.clicked.connect(lambda: self.close_dialog())
        self.DeleteAllButton.clicked.connect(lambda: self.delete_all())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMay"))
        MainWindow.setWindowIcon(QtGui.QIcon(Globe_logo))
        self.addDirectory.setText(_translate("MainWindow", "+"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.DeleteAllButton.setText(_translate("MainWindow", "Delete All"))

    def close_dialog(self):
        close_message = QtWidgets.QMessageBox()
        close_message.setWindowIcon(QtGui.QIcon(Globe_logo))
        close_message.setWindowTitle("Continue?")
        close_message.setText("You sure you want to close?")
        close_message.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        close_message.setIcon(QtWidgets.QMessageBox.Question)
        ret = close_message.exec()

        #result = QtWidgets.QMessageBox.question(None,"Continue?", "You sure you want to close?",
                                                #QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if ret == QtWidgets.QMessageBox.Yes:
            QtCore.QCoreApplication.instance().quit()

    def directory_dialog(self):
       #path_to_directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Directory", "F:\Senior_2")
        path_to_directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Directory")
        self.lineEdit.setText(path_to_directory)

    def add_directory(self):
        path_to_directory = self.lineEdit.text()
        self.listWidget_1.addItem(path_to_directory)
        self.create_class_dia()

    def create_class_dia(self):
        class_dia, result = QtWidgets.QInputDialog.getText(MainWindow, "Class Name", "Input Class Name")
        if result:
            self.listWidget_2.addItem(class_dia)

    def delete_class_dia(self):
        index = self.listWidget_1.currentRow()
        item1 = self.listWidget_1.takeItem(index)
        item2 = self.listWidget_2.takeItem(index)
        self.listWidget_1.removeItemWidget(item1)
        self.listWidget_2.removeItemWidget(item2)

    def delete_all(self):
        self.listWidget_1.clear()
        self.listWidget_2.clear()

    def zip_directories(self):
        paths = []
        labels = []
        for index in range(self.listWidget_1.count()):
            paths.append(self.listWidget_1.item(index).text())
            labels.append(self.listWidget_2.item(index).text())
            #IMayFunctions.zip_files(self.listWidget_1.item(index).text(), self.listWidget_2.item(index).text())

        IMayFunctions.zip_files(paths, labels)

    def finish_dialog(self):
        finish_message = QtWidgets.QMessageBox()
        finish_message.setWindowIcon(QtGui.QIcon(Globe_logo))
        finish_message.setWindowTitle("Finished")
        finish_message.setText("Program has finished")
        finish_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        finish_message.setIcon(QtWidgets.QMessageBox.Information)
        ret = finish_message.exec()

    def create_directory(self):
        project_name, result = QtWidgets.QInputDialog.getText(MainWindow, "Project Name", "Input Project Name")
        if result:
            IMayFunctions.create_directory(project_name)
        else:
            print("fail")

        paths = []
        labels = []
        for index in range(self.listWidget_1.count()):
            paths.append(self.listWidget_1.item(index).text())
            labels.append(self.listWidget_2.item(index).text())

        IMayFunctions.copy_directory(paths, labels, project_name)
        IMayFunctions.zip_files(project_name, project_name)
        IMayFunctions.remove_directory(project_name)
        self.finish_dialog()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
