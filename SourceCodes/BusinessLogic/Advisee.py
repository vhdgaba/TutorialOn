from DataAccess.FileHandler import FileHandler
from BusinessLogic.Student import Student

userfh = FileHandler('../Data/record.db')
defaultsubjecttitle = 'General Information'

class Advisee(Student):
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, homeaddress, emailaddress):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber, emailaddress)
        self.homeaddress = homeaddress

    def time_in(self, subject, adviser):
        if subject == '':
            subject = defaultsubjecttitle
        userfh.advisee_timein(self.studentnumber, subject, adviser)

    def time_out(self, evaluation):
        userfh.advisee_timeout(self.studentnumber, evaluation)

if __name__ == '__main__':
    pass