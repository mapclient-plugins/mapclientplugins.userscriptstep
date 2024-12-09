# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(600, 220)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditIdentifier)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label1)

        self.spinBoxNumberOfInputs = QSpinBox(self.configGroupBox)
        self.spinBoxNumberOfInputs.setObjectName(u"spinBoxNumberOfInputs")
        self.spinBoxNumberOfInputs.setMinimumSize(QSize(75, 0))
        self.spinBoxNumberOfInputs.setMinimum(1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBoxNumberOfInputs)

        self.label2 = QLabel(self.configGroupBox)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label2)

        self.spinBoxNumberOfOutputs = QSpinBox(self.configGroupBox)
        self.spinBoxNumberOfOutputs.setObjectName(u"spinBoxNumberOfOutputs")
        self.spinBoxNumberOfOutputs.setMinimumSize(QSize(75, 0))
        self.spinBoxNumberOfOutputs.setMinimum(1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinBoxNumberOfOutputs)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditFileLocation = QLineEdit(self.configGroupBox)
        self.lineEditFileLocation.setObjectName(u"lineEditFileLocation")

        self.horizontalLayout.addWidget(self.lineEditFileLocation)

        self.pushButtonFileChooser = QPushButton(self.configGroupBox)
        self.pushButtonFileChooser.setObjectName(u"pushButtonFileChooser")

        self.horizontalLayout.addWidget(self.pushButtonFileChooser)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure User Script", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:", None))
        self.label1.setText(QCoreApplication.translate("ConfigureDialog", u"Number of inputs:", None))
        self.label2.setText(QCoreApplication.translate("ConfigureDialog", u"Number of outputs:", None))
        self.label.setText(QCoreApplication.translate("ConfigureDialog", u"Script Path:", None))
        self.pushButtonFileChooser.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
    # retranslateUi

