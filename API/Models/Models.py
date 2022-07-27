import datetime

from flask_sqlalchemy import SQLAlchemy
from dateutil import parser
from datetime import datetime
from database import Database
db = Database.VOSDb


class Student(db.Model):
    __tablename__ = "student"
    __table_args__ = {"schema": "public"}
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    nationality = db.Column(db.String(50))
    birth_city = db.Column(db.String(50))
    birth_country = db.Column(db.String(50))
    phone_number = db.Column(db.String(10))
    email_address = db.Column(db.String(100))
    address_line_1 = db.Column(db.String(100))
    address_line_2 = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    pincode = db.Column(db.Integer)
    national_identification_type = db.Column(db.String(50))
    national_identification_number = db.Column(db.String(50))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(self, first_name, middle_name, last_name, date_of_birth, birth_city, birth_country, address_line_1,
                 address_line_2, email_address, city, pincode, state, country, nationality, phone_number,
                 national_identification_type,
                 national_identification_number):
        self.first_name = first_name,
        self.middle_name = middle_name,
        self.last_name = last_name,
        self.date_of_birth = date_of_birth,
        self.birth_city = birth_city,
        self.birth_country = birth_country,
        self.email_address = email_address,
        self.address_line_1 = address_line_1,
        self.address_line_2 = address_line_2,
        self.city = city,
        self.pincode = pincode,
        self.state = state,
        self.country = country,
        self.nationality = nationality,
        self.phone_number = phone_number,
        self.national_identification_type = national_identification_type,
        self.national_identification_number = national_identification_number,
        self.date_created = datetime.now()

    def to_json(self):
        return {
            "studentId": self.student_id,
            "firstName": self.first_name,
            "middleName": self.middle_name,
            "lastName": self.last_name,
            "dateOfBirth": self.date_of_birth,
            "placeOfBirth": self.birth_city,
            "birthCountry": self.birth_country,
            "email": self.email_address,
            "address1": self.address_line_1,
            "address2": self.address_line_2,
            "city": self.city,
            "pin": self.pincode,
            "state": self.state,
            "country": self.country,
            "nationality": self.nationality,
            "phoneNumber": self.phone_number,
            "identificationType": self.national_identification_type,
            "identificationNumber": self.national_identification_number,
            "dateCreated": self.date_created,
            "dateModified": self.date_modified
        }


class Parent(db.Model):
    __tablename__ = "parent"
    __table_args__ = {'schema': 'public'}
    student_id = db.Column(db.Integer, db.ForeignKey('Student.student_id'), primary_key=True)
    father_first_name = db.Column(db.String(50))
    father_middle_name = db.Column(db.String(50))
    father_last_name = db.Column(db.String(50))
    mother_first_name = db.Column(db.String(50))
    mother_middle_name = db.Column(db.String(50))
    mother_last_name = db.Column(db.String(50))
    parent_contact_number = db.Column(db.String(10))
    parent_email_address = db.Column(db.String(100))

#     def __init__(self, student_id, father_first_name, father_middle_name, father_last_name, mother_first_name,
#                  mother_middle_name, mother_last_name, parent_contact_number, parent_email_address):
#         self.student_id = student_id,
#         self.father_first_name = father_first_name,
#         self.father_middle_name = father_middle_name,
#         self.father_last_name = father_last_name,
#         self.mother_first_name = mother_first_name,
#         self.mother_middle_name = mother_middle_name,
#         self.mother_last_name = mother_last_name,
#         self.parent_contact_number = parent_contact_number,
#         self.parent_email_address = parent_email_address
#
#     def to_json(self):
#         return {
#             "studentId": self.student_id,
#             "fatherFirstName": self.father_first_name,
#             "fatherMiddleName": self.father_middle_name,
#             "fatherLastName": self.father_last_name,
#             "motherFirstName": self.mother_first_name,
#             "motherMiddleName": self.mother_middle_name,
#             "motherLastName": self.mother_last_name,
#             "parentContactNumber": self.parent_contact_number,
#             "parentEmail": self.parent_contact_number
#         }
#
# class Guardian(db.Model):
#     __tablename__ = "guardian"
#     __table_args__ = {'schema': 'public'}
#     student_id = db.column(db.Integer, db.ForeignKey('Student.student_id'), primary_key=True)
#     guardian_first_name = db.Column(db.String(50))
#     guardian_middle_name = db.Column(db.String(50))
#     guardian_last_name = db.Column(db.String(50))
#     guardian_contact_number = db.Column(db.String(10))
#     guardian_email_address = db.Column(db.String(100))
#
#     def __init__(self, student_id, guardian_first_name, guardian_middle_name, guardian_last_name,
#                  guardian_contact_number, guardian_email_address):
#         self.student_id = student_id,
#         self.guardian_first_name = guardian_first_name,
#         self.guardian_middle_name = guardian_middle_name,
#         self.guardian_last_name = guardian_last_name,
#         self.guardian_contact_number = guardian_contact_number,
#         self.guardian_email_address = guardian_email_address
#
#     def to_json(self):
#         return {
#             "studentId": self.student_id,
#             "guardianFirstName": self.guardian_first_name,
#             "guardianMiddleName": self.guardian_middle_name,
#             "guardianLastName": self.guardian_last_name,
#             "guardianContactNumber": self.guardian_contact_number,
#             "guardianEmail": self.guardian_email_address
#         }



    # class Branch(db.Model):
#     __tablename__ = "branch"
#     __table_args__ = {'schema': 'public'}
#     branch_id = db.column(db.Integer, primary_key=True)
#     branch_name = db.Column(db.String(50))
#     degree = db.Column(db.String(50))
#     duration = db.Column(db.Integer)
#
#
# class Board(db.Model):
#     __tablename__ = "board"
#     __table_args__ = {'schema': 'public'}
#     board_id = db.column(db.Integer, primary_key=True)
#     board_type = db.Column(db.String(50))
#
#
# class AllocationCategory(db.Model):
#     __tablename__ = "allocation_category"
#     __table_args__ = {'schema': 'public'}
#     category_id = db.column(db.Integer, primary_key=True)
#     category_name = db.Column(db.String(50))
#
#
# class AdmissionTypes(db.Model):
#     __tablename__ = "admission_types"
#     __table_args__ = {'schema': 'public'}
#     type_id = db.column(db.Integer, primary_key=True)
#     type_name = db.Column(db.String(50))
#
#
# class Application(db.Model):
#     __tablename__ = "application"
#     __table_args__ = {'schema': 'public'}
#     application_id = db.column(db.Integer, primary_key=True)
#     student_id = db.column(db.Integer, db.ForeignKey('Student.student_id'))
#     board_id = db.column(db.Integer, db.ForeignKey('Board.board_id'))
#     board_roll_number = db.Column(db.String(20))
#     highschool_percentage_marks = db.Column(db.Float)
#     highschool_cgpa = db.Column(db.Float)
#     pu_qualification = db.Column(db.String(50))
#     pu_roll_number = db.Column(db.String(20))
#     pu_college_name = db.Column(db.String(50))
#     pu_percentile = db.Column(db.Float)
#     pu_gpa = db.Column(db.Float)
#     admission_type_id = db.Column(db.Integer, db.ForeignKey('AdmissionTypes.type_id'))
#     cet_comedk_id = db.Column(db.String(20))
#     cet_comedk_rank =  db.Column(db.Integer)
#     parent_or_guardian =
#     admission_acceptance =
#     year_of_joining =  db.Column(db.Integer)
#     branch_id = db.Column(db.Integer, db.ForeignKey('Branch.branch_id'))
#     allocation_category_id =  db.Column(db.Integer, db.ForeignKey('AllocationCategory.category_id'))
