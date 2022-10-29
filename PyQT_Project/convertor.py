from PyQt5 import QtCore, QtGui, QtWidgets


class ConvertorScheme(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(814, 460)
        self.converter_type = QtWidgets.QComboBox(Form)
        self.converter_type.setGeometry(QtCore.QRect(40, 30, 211, 50))
        self.converter_type.setObjectName("converter_type")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 150, 521, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout.setSpacing(22)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_type = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_type.sizePolicy().hasHeightForWidth())
        self.input_type.setSizePolicy(sizePolicy)
        self.input_type.setObjectName("input_type")
        self.verticalLayout.addWidget(self.input_type)
        self.input_value = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_value.sizePolicy().hasHeightForWidth())
        self.input_value.setSizePolicy(sizePolicy)
        self.input_value.setObjectName("input_edit")
        self.verticalLayout.addWidget(self.input_value)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout_2.setSpacing(22)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output_type = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_type.sizePolicy().hasHeightForWidth())
        self.output_type.setSizePolicy(sizePolicy)
        self.output_type.setObjectName("output_type")
        self.verticalLayout_2.addWidget(self.output_type)
        self.output_value = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_value.sizePolicy().hasHeightForWidth())
        self.output_value.setSizePolicy(sizePolicy)
        self.output_value.setObjectName("output_value")
        self.verticalLayout_2.addWidget(self.output_value)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))