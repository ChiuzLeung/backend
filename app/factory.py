from app.models import Teacher

class TeacherFactory():

    def __init__(self):
        pass

    def createTeacher(self):
        pass

class CCNUTeacher(Teacher):

    def __init__(self):
        self.school = "ccnu"


class WUSTeacher(Teacher):

    def __init__(self):
        self.school = "wust"

class CCNUTeacherFactory(TeacherFactory):

    def __init__(self):
        pass

    def createTeacher(self):
        return CCNUTeacher()


class WUSTTeacherFactory(TeacherFactory):

    def __init__(self):
        pass

    def createTeacher(self):
        return WUSTeacher()


if __name__ == '__main__':
    ctf = CCNUTeacherFactory()
    ct = ctf.createTeacher()
    ct.set_name("张老师")
    ct.set_sex("女")
    ct.set_research_direction("大数据")
    ct.set_photo("balabala")
    ct.set_birth(50)
    print(ct)


    wtf = WUSTTeacherFactory()
    wt = wtf.createTeacher()
    wt.set_name("李老师")
    wt.set_sex("男")
    wt.set_research_direction("云计算")
    wt.set_photo("哈哈哈")
    wt.set_birth("35")
    print(wt)
