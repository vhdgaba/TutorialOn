# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adviseelistdialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from BusinessLogic.Advisee import Advisee
from UserInterface.evaluation import Ui_Evaluation
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdviseeDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
    
        icon = QtGui.QIcon("../Resources/logo.png")
        Dialog.setWindowIcon(icon)
        Dialog.setWindowTitle("TutorialOn")
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 30, 341, 211))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_logout = QtWidgets.QPushButton(Dialog)
        self.pushButton_logout.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_logout.clicked.connect(lambda: self.push_logout(Dialog))
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.clicked.connect(lambda: self.push_cancel(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TutorialOn"))
        self.pushButton_logout.setText(_translate("Dialog", "Logout"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))

    def connect_session(self, session):
        self.ses = session
        self.updatelist()
        
    def updatelist(self):
        self.listWidget.clear()
        for adv in self.ses.advisees:
            self.listWidget.addItem('{} - {}, {} {}'.format(adv.studentnumber, adv.lastname, adv.firstname, adv.middlename))
   
    def push_logout(self, Dialog):
        user_sn = self.listWidget.currentItem().text().split(' ')[0]
        if self.ses.logout_advisee(user_sn):
            Evaluation = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
            ui = Ui_Evaluation()
            ui.setupUi(Evaluation)
            ui.connect_session(self.ses)
            Evaluation.exec_()
            evaluation = 25
            Advisee(*self.ses.get_advisee(user_sn)).time_out(evaluation)
            self.smsg('Logout success!')
            self.updatelist()
            Dialog.close()
        else:
            self.smsg(self.ses.errormsg)
        
    def push_cancel(self, Dialog):
        self.loggedout = False
        Dialog.close()     
        
    def smsg(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('TutorialOn')
        icon = QtGui.QIcon("../Resources/logo.png")
        msg.setWindowIcon(icon)
        msg.setText(message)
        msg.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdviseeDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

