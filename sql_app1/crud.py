from sqlalchemy.orm import Session

from . import models , schemas


def get_course(course_id: str , db : Session):
    return db.query(models.course).filter(models.course.cid == course_id).first()

def get_student(student_id : int , db : Session):
    return db.query(models.student).filter(models.student.stid == student_id).first()

def get_lecturer(lecturer_id : int , db : Session):
    return db.query(models.lecturer).filter(models.lecturer.lid == lecturer_id).first()

def create_course(db : Session , course : schemas.course):
    db_course = models.course(cid = course.cid , cname = course.cname , department = course.department, credit = course.credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def create_student(db : Session , student : schemas.student):
    db_student = models.student(stid = student.stid , fname = student.fname , lname = student.lname, father = student.father , birth = student.birth, ids = student.ids , borncity = student.borncity, address = student.address , postalcode = student.postalcode, cphone = student.cphone , hphone = student.hphone, department = student.department , major = student.major, married = student.married , id = student.id , cid = student.cid, lids = student.lids)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_lecturer(db : Session , lecturer : schemas.lecturer):
    db_lecturer = models.lecturer(lid = lecturer.lid , fname = lecturer.fname , lname = lecturer.lname, id = lecturer.id , department = lecturer.department, major = lecturer.major , birth = lecturer.birth, borncity = lecturer.borncity , address = lecturer.address, postalcode = lecturer.postalcode , cphone = lecturer.cphone, hphone = lecturer.hphone , cid = lecturer.cid)
    db.add(db_lecturer)
    db.commit()
    db.refresh(db_lecturer)
    return db_lecturer