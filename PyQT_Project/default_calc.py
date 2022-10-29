from PyQt5 import QtCore, QtWidgets


class DefaultCalcScheme:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(953, 542)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 50, 791, 321))
        self.button_group_numbers = QtWidgets.QButtonGroup(self)
        self.button_group_words = QtWidgets.QButtonGroup(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(2, 0, 5, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_cos = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cos.sizePolicy().hasHeightForWidth())
        self.btn_cos.setSizePolicy(sizePolicy)
        self.btn_cos.setStyleSheet("font: 20pt \"Arial\";\n"
                                   "background-color: rgb(198, 198, 198);")
        self.btn_cos.setObjectName("btn_cos")
        self.gridLayout_2.addWidget(self.btn_cos, 2, 5, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 3, 2, 1, 1)
        self.btn_e = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_e.sizePolicy().hasHeightForWidth())
        self.btn_e.setSizePolicy(sizePolicy)
        self.btn_e.setStyleSheet("font: 20pt \"Arial\";\n"
                                 "background-color: rgb(198, 198, 198);")
        self.btn_e.setObjectName("btn_e")
        self.gridLayout_2.addWidget(self.btn_e, 3, 4, 1, 1)
        self.btn_sin = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sin.sizePolicy().hasHeightForWidth())
        self.btn_sin.setSizePolicy(sizePolicy)
        self.btn_sin.setStyleSheet("font: 20pt \"Arial\";\n"
                                   "background-color: rgb(198, 198, 198);")
        self.btn_sin.setObjectName("btn_sin")
        self.gridLayout_2.addWidget(self.btn_sin, 1, 5, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_2.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setStyleSheet("font: 24pt \"Arial\";\n"
                                   "background-color: rgb(248, 248, 248);")
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout_2.addWidget(self.btn_dot, 4, 2, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eq.sizePolicy().hasHeightForWidth())
        self.btn_eq.setSizePolicy(sizePolicy)
        self.btn_eq.setStyleSheet("font: 20pt \"Arial\";\n"
                                  "background-color: rgb(198, 198, 198);")
        self.btn_eq.setAutoDefault(False)
        self.btn_eq.setDefault(False)
        self.btn_eq.setFlat(False)
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout_2.addWidget(self.btn_eq, 4, 3, 1, 1)
        self.btn_history = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy)
        self.btn_history.setStyleSheet("font: 20pt \"Arial\";\n"
                                       "background-color: rgb(198, 198, 198);")
        self.btn_history.setObjectName("btn_history")
        self.gridLayout_2.addWidget(self.btn_history, 4, 5, 1, 1)
        self.btn_pi = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pi.sizePolicy().hasHeightForWidth())
        self.btn_pi.setSizePolicy(sizePolicy)
        self.btn_pi.setStyleSheet("font: 20pt \"Arial\";\n"
                                  "background-color: rgb(198, 198, 198);")
        self.btn_pi.setObjectName("btn_pi")
        self.gridLayout_2.addWidget(self.btn_pi, 4, 4, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_2.addWidget(self.btn_0, 4, 0, 1, 2)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_2.addWidget(self.btn_3, 1, 2, 1, 1)
        self.btn_pow = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pow.sizePolicy().hasHeightForWidth())
        self.btn_pow.setSizePolicy(sizePolicy)
        self.btn_pow.setStyleSheet("font: 20pt \"Arial\";\n"
                                   "background-color: rgb(198, 198, 198);")
        self.btn_pow.setObjectName("btn_ext")
        self.gridLayout_2.addWidget(self.btn_pow, 0, 4, 1, 1)
        self.btn_type = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_type.sizePolicy().hasHeightForWidth())
        self.btn_type.setSizePolicy(sizePolicy)
        self.btn_type.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_type.setStyleSheet("font: 20pt \"Arial\";\n"
                                    "background-color: rgb(255, 186, 13);")
        self.btn_type.setObjectName("btn_type")
        self.gridLayout_2.addWidget(self.btn_type, 0, 2, 1, 1)
        self.btn_bkt = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_bkt.sizePolicy().hasHeightForWidth())
        self.btn_bkt.setSizePolicy(sizePolicy)
        self.btn_bkt.setStyleSheet("font: 20pt \"Arial\";\n"
                                   "background-color: rgb(255, 186, 13);")
        self.btn_bkt.setObjectName("btn_bkt")
        self.gridLayout_2.addWidget(self.btn_bkt, 0, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_2.addWidget(self.btn_1, 1, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_2.addWidget(self.btn_2, 1, 1, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setStyleSheet("font: 20pt \"Arial\";\n"
                                     "background-color: rgb(255, 186, 13);")
        self.btn_clear.setCheckable(False)
        self.btn_clear.setAutoExclusive(False)
        self.btn_clear.setAutoDefault(False)
        self.btn_clear.setDefault(False)
        self.btn_clear.setFlat(False)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout_2.addWidget(self.btn_clear, 0, 0, 1, 1)
        self.btn_ln = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ln.sizePolicy().hasHeightForWidth())
        self.btn_ln.setSizePolicy(sizePolicy)
        self.btn_ln.setStyleSheet("font: 20pt \"Arial\";\n"
                                  "background-color: rgb(198, 198, 198);")
        self.btn_ln.setObjectName("btn_ln")
        self.gridLayout_2.addWidget(self.btn_ln, 0, 6, 1, 1)
        self.btn_arcsin = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arcsin.sizePolicy().hasHeightForWidth())
        self.btn_arcsin.setSizePolicy(sizePolicy)
        self.btn_arcsin.setStyleSheet("font: 20pt \"Arial\";\n"
                                      "background-color: rgb(198, 198, 198);")
        self.btn_arcsin.setObjectName("btn_arcsin")
        self.gridLayout_2.addWidget(self.btn_arcsin, 1, 6, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mult.sizePolicy().hasHeightForWidth())
        self.btn_mult.setSizePolicy(sizePolicy)
        self.btn_mult.setStyleSheet("font: 20pt \"Arial\";\n"
                                    "background-color: rgb(198, 198, 198);")
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout_2.addWidget(self.btn_mult, 1, 3, 1, 1)
        self.btn_log = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_log.sizePolicy().hasHeightForWidth())
        self.btn_log.setSizePolicy(sizePolicy)
        self.btn_log.setStyleSheet("font: 20pt \"Arial\";\n"
                                   "background-color: rgb(198, 198, 198);")
        self.btn_log.setObjectName("btn_log")
        self.gridLayout_2.addWidget(self.btn_log, 0, 5, 1, 1)
        self.btn_tan = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tan.sizePolicy().hasHeightForWidth())
        self.btn_tan.setSizePolicy(sizePolicy)
        self.btn_tan.setStyleSheet("font: 20pt \"Arial\";\n"
                                   "background-color: rgb(198, 198, 198);")
        self.btn_tan.setObjectName("btn_tan")
        self.gridLayout_2.addWidget(self.btn_tan, 3, 5, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_2.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_sub = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        self.btn_sub.setStyleSheet("font: 20pt \"Arial\";\n"
                                   "background-color: rgb(198, 198, 198);")
        self.btn_sub.setObjectName("btn_sub")
        self.gridLayout_2.addWidget(self.btn_sub, 2, 3, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy)
        self.btn_sqrt.setStyleSheet("font: 20pt \"Arial\";\n"
                                    "background-color: rgb(198, 198, 198);")
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout_2.addWidget(self.btn_sqrt, 2, 4, 1, 1)
        self.btn_arctan = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arctan.sizePolicy().hasHeightForWidth())
        self.btn_arctan.setSizePolicy(sizePolicy)
        self.btn_arctan.setStyleSheet("font: 20pt \"Arial\";\n"
                                      "background-color: rgb(198, 198, 198);")
        self.btn_arctan.setObjectName("btn_arctan")
        self.gridLayout_2.addWidget(self.btn_arctan, 3, 6, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setStyleSheet("font: 20pt \"Arial\";\n"
                                    "background-color: rgb(198, 198, 198);")
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout_2.addWidget(self.btn_plus, 3, 3, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fact.sizePolicy().hasHeightForWidth())
        self.btn_fact.setSizePolicy(sizePolicy)
        self.btn_fact.setStyleSheet("font: 20pt \"Arial\";\n"
                                    "background-color: rgb(198, 198, 198);")
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout_2.addWidget(self.btn_fact, 1, 4, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setStyleSheet("font: 24pt \"Arial\";\n"
                                 "background-color: rgb(248, 248, 248);")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_2.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setStyleSheet("font: 20pt \"Arial\";\n"
                                   "background-color: rgb(198, 198, 198);")
        self.btn_div.setCheckable(False)
        self.btn_div.setAutoRepeat(False)
        self.btn_div.setAutoExclusive(False)
        self.btn_div.setAutoDefault(False)
        self.btn_div.setDefault(False)
        self.btn_div.setFlat(False)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout_2.addWidget(self.btn_div, 0, 3, 1, 1)
        self.btn_arccos = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arccos.sizePolicy().hasHeightForWidth())
        self.btn_arccos.setSizePolicy(sizePolicy)
        self.btn_arccos.setStyleSheet("font: 20pt \"Arial\";\n"
                                      "background-color: rgb(198, 198, 198);")
        self.btn_arccos.setObjectName("btn_arccos")
        self.gridLayout_2.addWidget(self.btn_arccos, 2, 6, 1, 1)
        self.output_edit = QtWidgets.QLineEdit(Form)
        self.output_edit.setGeometry(QtCore.QRect(2, 0, 784, 51))
        self.output_edit.setStyleSheet("font: 28pt \"Arial\";")
        self.output_edit.setText("")
        self.output_edit.setMaxLength(32756)
        self.output_edit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.output_edit.setObjectName("output_edit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_cos.setText(_translate("Form", "cos"))
        self.btn_9.setText(_translate("Form", "9"))
        self.btn_e.setText(_translate("Form", "e"))
        self.btn_sin.setText(_translate("Form", "sin"))
        self.btn_6.setText(_translate("Form", "6"))
        self.btn_dot.setText(_translate("Form", "."))
        self.btn_eq.setText(_translate("Form", "="))
        self.btn_history.setText(_translate("Form", "history"))
        self.btn_pi.setText(_translate("Form", "π"))
        self.btn_0.setText(_translate("Form", "0"))
        self.btn_3.setText(_translate("Form", "3"))
        self.btn_pow.setText(_translate("Form", "^"))
        self.btn_type.setText(_translate("Form", "deg"))
        self.btn_bkt.setText(_translate("Form", "("))
        self.btn_1.setText(_translate("Form", "1"))
        self.btn_2.setText(_translate("Form", "2"))
        self.btn_clear.setText(_translate("Form", "C"))
        self.btn_ln.setText(_translate("Form", "ln"))
        self.btn_arcsin.setText(_translate("Form", "arcsin"))
        self.btn_mult.setText(_translate("Form", "*"))
        self.btn_log.setText(_translate("Form", "log"))
        self.btn_tan.setText(_translate("Form", "tan"))
        self.btn_4.setText(_translate("Form", "4"))
        self.btn_8.setText(_translate("Form", "8"))
        self.btn_sub.setText(_translate("Form", "-"))
        self.btn_sqrt.setText(_translate("Form", "√"))
        self.btn_arctan.setText(_translate("Form", "arctan"))
        self.btn_plus.setText(_translate("Form", "+"))
        self.btn_fact.setText(_translate("Form", "!"))
        self.btn_7.setText(_translate("Form", "7"))
        self.btn_5.setText(_translate("Form", "5"))
        self.btn_div.setText(_translate("Form", "/"))
        self.btn_arccos.setText(_translate("Form", "arccos"))
        self.button_group_numbers.addButton(self.btn_0)
        self.button_group_numbers.addButton(self.btn_1)
        self.button_group_numbers.addButton(self.btn_2)
        self.button_group_numbers.addButton(self.btn_3)
        self.button_group_numbers.addButton(self.btn_4)
        self.button_group_numbers.addButton(self.btn_5)
        self.button_group_numbers.addButton(self.btn_6)
        self.button_group_numbers.addButton(self.btn_7)
        self.button_group_numbers.addButton(self.btn_8)
        self.button_group_numbers.addButton(self.btn_9)
        self.button_group_numbers.addButton(self.btn_plus)
        self.button_group_numbers.addButton(self.btn_div)
        self.button_group_numbers.addButton(self.btn_mult)
        self.button_group_numbers.addButton(self.btn_sub)
        self.button_group_numbers.addButton(self.btn_pow)
        self.button_group_numbers.addButton(self.btn_dot)
        self.button_group_words.addButton(self.btn_fact)
        self.button_group_words.addButton(self.btn_sqrt)
        self.button_group_words.addButton(self.btn_sin)
        self.button_group_words.addButton(self.btn_cos)
        self.button_group_words.addButton(self.btn_tan)
        self.button_group_words.addButton(self.btn_arcsin)
        self.button_group_words.addButton(self.btn_arccos)
        self.button_group_words.addButton(self.btn_arctan)
        self.button_group_words.addButton(self.btn_log)
        self.button_group_words.addButton(self.btn_ln)