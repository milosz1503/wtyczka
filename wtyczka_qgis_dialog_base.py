# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wtyczka_qgis_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WtyczkaQGISDialogBase(object):
    def setupUi(self, WtyczkaQGISDialogBase):
        WtyczkaQGISDialogBase.setObjectName("WtyczkaQGISDialogBase")
        WtyczkaQGISDialogBase.resize(327, 180)
        self.horizontalLayoutWidget = QtWidgets.QWidget(WtyczkaQGISDialogBase)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.mMapLayerComboBox = QgsMapLayerComboBox(self.horizontalLayoutWidget)
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.verticalLayout.addWidget(self.mMapLayerComboBox)
        self.oblicz = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.oblicz.setObjectName("oblicz")
        self.verticalLayout.addWidget(self.oblicz)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(WtyczkaQGISDialogBase)
        QtCore.QMetaObject.connectSlotsByName(WtyczkaQGISDialogBase)

    def retranslateUi(self, WtyczkaQGISDialogBase):
        _translate = QtCore.QCoreApplication.translate
        WtyczkaQGISDialogBase.setWindowTitle(_translate("WtyczkaQGISDialogBase", "Wtyczka QGIS"))
        self.label.setText(_translate("WtyczkaQGISDialogBase", "Wybierz 2 punkty aby policzyć różnicę wyskości"))
        self.label_2.setText(_translate("WtyczkaQGISDialogBase", "Wybierz 3 punkty aby policzyć pole"))
        self.label_3.setText(_translate("WtyczkaQGISDialogBase", "Wybierz warstwę punktową:"))
        self.oblicz.setText(_translate("WtyczkaQGISDialogBase", "Oblicz"))

from qgsmaplayercombobox import QgsMapLayerComboBox
