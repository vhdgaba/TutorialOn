# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peeradviserregistration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PeerAdviserRegister(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 390)
        
        icon = QtGui.QIcon("../Resources/logo.png")
        Form.setWindowIcon(icon)
        Form.setWindowTitle("TutorialOn")
        
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_name.setObjectName("label_name")
        self.lineEdit_lastname = QtWidgets.QLineEdit(Form)
        self.lineEdit_lastname.setGeometry(QtCore.QRect(10, 80, 171, 20))
        self.lineEdit_lastname.setStatusTip("")
        self.lineEdit_lastname.setWhatsThis("")
        self.lineEdit_lastname.setAccessibleName("")
        self.lineEdit_lastname.setInputMask("")
        self.lineEdit_lastname.setText("")
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.label_program = QtWidgets.QLabel(Form)
        self.label_program.setGeometry(QtCore.QRect(290, 115, 51, 21))
        self.label_program.setObjectName("label_program")
        self.lineEdit_givenname = QtWidgets.QLineEdit(Form)
        self.lineEdit_givenname.setGeometry(QtCore.QRect(190, 80, 171, 20))
        self.lineEdit_givenname.setObjectName("lineEdit_givenname")
        self.lineEdit_middlename = QtWidgets.QLineEdit(Form)
        self.lineEdit_middlename.setGeometry(QtCore.QRect(370, 80, 171, 20))
        self.lineEdit_middlename.setObjectName("lineEdit_middlename")
        self.label_studentnumber = QtWidgets.QLabel(Form)
        self.label_studentnumber.setGeometry(QtCore.QRect(10, 115, 91, 21))
        self.label_studentnumber.setObjectName("label_studentnumber")
        self.lineEdit_studentnumber = QtWidgets.QLineEdit(Form)
        self.lineEdit_studentnumber.setGeometry(QtCore.QRect(100, 115, 171, 20))
        self.lineEdit_studentnumber.setText("")
        self.lineEdit_studentnumber.setObjectName("lineEdit_studentnumber")
        self.lineEdit_program = QtWidgets.QLineEdit(Form)
        self.lineEdit_program.setGeometry(QtCore.QRect(340, 115, 71, 20))
        self.lineEdit_program.setText("")
        self.lineEdit_program.setObjectName("lineEdit_program")
        self.lineEdit_contactnumber = QtWidgets.QLineEdit(Form)
        self.lineEdit_contactnumber.setGeometry(QtCore.QRect(370, 150, 171, 20))
        self.lineEdit_contactnumber.setText("")
        self.lineEdit_contactnumber.setObjectName("lineEdit_contactnumber")
        self.label_contactnumber = QtWidgets.QLabel(Form)
        self.label_contactnumber.setGeometry(QtCore.QRect(280, 150, 91, 21))
        self.label_contactnumber.setObjectName("label_contactnumber")
#        self.comboBox_department = QtWidgets.QComboBox(Form)
#        self.comboBox_department.setGeometry(QtCore.QRect(120, 140, 421, 22))
#        self.comboBox_department.setEditable(False)
#        self.comboBox_department.setCurrentText("")
#        self.comboBox_department.setObjectName("comboBox_department")
#        self.label_department = QtWidgets.QLabel(Form)
#        self.label_department.setGeometry(QtCore.QRect(10, 140, 101, 21))
#        self.label_department.setObjectName("label_department")
        self.pushButton_register = QtWidgets.QPushButton(Form)
        self.pushButton_register.setGeometry(QtCore.QRect(450, 340, 75, 23))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButton_register.clicked.connect(lambda: self.push_register(Form))
        self.label_organization = QtWidgets.QLabel(Form)
        self.label_organization.setGeometry(QtCore.QRect(10, 150, 91, 21))
        self.label_organization.setObjectName("label_organization")
        self.lineEdit_organization = QtWidgets.QLineEdit(Form)
        self.lineEdit_organization.setGeometry(QtCore.QRect(80, 150, 181, 20))
        self.lineEdit_organization.setText("")
        self.lineEdit_organization.setObjectName("lineEdit_organization")
        self.label_emailaddress = QtWidgets.QLabel(Form)
        self.label_emailaddress.setGeometry(QtCore.QRect(10, 185, 91, 21))
        self.label_emailaddress.setObjectName("label_emailaddress")
        self.lineEdit_emailaddress = QtWidgets.QLineEdit(Form)
        self.lineEdit_emailaddress.setGeometry(QtCore.QRect(85, 185, 181, 20))
        self.lineEdit_emailaddress.setText("")
        self.lineEdit_emailaddress.setObjectName("lineEdit_emailaddress")
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(290, 185, 91, 21))
        self.label_password.setObjectName("label_password")
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(350, 185, 190, 20))
        self.lineEdit_password.setText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 230, 531, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBox_time2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_time2.setGeometry(QtCore.QRect(220, 50, 171, 22))
        self.comboBox_time2.setObjectName("comboBox_time2")
        self.comboBox_day1 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_day1.setGeometry(QtCore.QRect(110, 20, 101, 22))
        self.comboBox_day1.setObjectName("comboBox_day1")
        self.comboBox_time1 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_time1.setGeometry(QtCore.QRect(220, 20, 171, 22))
        self.comboBox_time1.setObjectName("comboBox_time1")
        self.label_advisingschedule = QtWidgets.QLabel(self.groupBox)
        self.label_advisingschedule.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_advisingschedule.setObjectName("label_advisingschedule")
        self.comboBox_day2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_day2.setGeometry(QtCore.QRect(110, 50, 101, 22))
        self.comboBox_day2.setObjectName("comboBox_day2")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.clicked.connect(lambda: self.push_cancel(Form))


        self.retranslateUi(Form)
        self.populate_schedule()
#        self.comboBox_department.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TutorialOn"))
        self.label_name.setText(_translate("Form", "Name:"))
        self.lineEdit_lastname.setPlaceholderText(_translate("Form", "Last Name"))
        self.label_program.setText(_translate("Form", "Program:"))
        self.lineEdit_givenname.setPlaceholderText(_translate("Form", "Given Name"))
        self.lineEdit_middlename.setPlaceholderText(_translate("Form", "Middle Name"))
        self.label_studentnumber.setText(_translate("Form", "Student Number:"))
        self.label_contactnumber.setText(_translate("Form", "Contact Number:"))
#        self.label_department.setText(_translate("Form", "School/Department:"))
        self.pushButton_register.setText(_translate("Form", "Register"))
        self.label_organization.setText(_translate("Form", "Organization:"))
        self.label_emailaddress.setText(_translate("Form", "Email Address:"))
        self.label_password.setText(_translate("Form", "Password:"))
        self.label_advisingschedule.setText(_translate("Form", "Advising Schedule:"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))

    def connect_session(self, session):
        self.ses = session
        
    def populate_schedule(self):
        self.comboBox_day1.addItem('Monday')
        self.comboBox_day1.addItem('Tuesday')
        self.comboBox_day1.addItem('Wednesday')
        self.comboBox_day1.addItem('Thursday')
        self.comboBox_day1.addItem('Friday')
        self.comboBox_day1.addItem('Saturday')
        self.comboBox_day2.addItem('Monday')
        self.comboBox_day2.addItem('Tuesday')
        self.comboBox_day2.addItem('Wednesday')
        self.comboBox_day2.addItem('Thursday')
        self.comboBox_day2.addItem('Friday')
        self.comboBox_day2.addItem('Saturday')
        self.comboBox_time1.addItem('7:30-9:00')
        self.comboBox_time1.addItem('9:00-10:30')
        self.comboBox_time1.addItem('10:30-12:00')
        self.comboBox_time1.addItem('12:00-13:30')
        self.comboBox_time1.addItem('13:30-15:00')
        self.comboBox_time1.addItem('15:00-16:30')
        self.comboBox_time1.addItem('16:30-18:00')
        self.comboBox_time1.addItem('18:00-19:30')
        self.comboBox_time1.addItem('19:30-21:00')
        self.comboBox_time2.addItem('7:30-9:00')
        self.comboBox_time2.addItem('9:00-10:30')
        self.comboBox_time2.addItem('10:30-12:00')
        self.comboBox_time2.addItem('12:00-13:30')
        self.comboBox_time2.addItem('13:30-15:00')
        self.comboBox_time2.addItem('15:00-16:30')
        self.comboBox_time2.addItem('16:30-18:00')
        self.comboBox_time2.addItem('18:00-19:30')
        self.comboBox_time2.addItem('19:30-21:00')

    def push_register(self, form):
        if self.ses.register_peeradviser(self.lineEdit_studentnumber.text(), self.lineEdit_givenname.text(), self.lineEdit_middlename.text(), self.lineEdit_lastname.text(), self.lineEdit_program.text(), self.lineEdit_contactnumber.text(), self.lineEdit_organization.text(), self.lineEdit_emailaddress.text(), self.lineEdit_password.text(), self.comboBox_day1.currentText(), self.comboBox_time1.currentText(), self.comboBox_day2.currentText(), self.comboBox_time2.currentText()):
            self.smsg('Register success!')
            self.registered = True
            form.close()
        else:
            self.smsg(self.ses.errormsg)
    
    def push_cancel(self, form):
        self.registered = False
        form.close()

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
    Form = QtWidgets.QWidget()
    ui = Ui_PeerAdviserRegister()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

