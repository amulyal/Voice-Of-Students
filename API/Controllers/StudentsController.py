from flask import make_response, jsonify, request, Blueprint

from Models.Models import Student
from database.Database import VOSDb

bp = Blueprint('students', __name__, url_prefix='/students')


@bp.route("", methods=['GET'])
def getStudents():
    if request.args.get('last_name') is not None:
        last_name_query = request.args.get('last_name') + '%'
        students = VOSDb.session.query(Student).filter(
            Student.last_name.like(last_name_query)).all()
    else:
        students = VOSDb.session.query(Student).all()

    response = []
    for student in students:
        response.append(student.to_json())
    return make_response(jsonify(response), 200)


@bp.route("/<int:student_id>", methods=['GET'])
def getStudent(student_id):
    if VOSDb.session.query(Student.student_id).filter_by(student_id=student_id).scalar() is None:
        return make_response(jsonify({"message": " Student not found"}), 404)

    student = VOSDb.session.query(Student).filter(Student.student_id == student_id).first()
    response = student.to_json()
    return make_response(jsonify(response), 200)


@bp.route("/<int:student_id>", methods=['PUT'])
def updateStudent(student_id):
    if VOSDb.session.query(Student.student_id).filter_by(student_id=student_id).scalar() is None:
        return make_response(jsonify({"message": "Student Not Found"}), 404)

    data = request.get_json()
    student = VOSDb.session.query(Student).filter(Student.student_id == student_id).first()
    student.first_name = data['firstName']
    student.middle_name = data['middleName']
    student.last_name = data['lastName']
    student.date_of_birth = data['dateOfBirth']
    student.birth_city = data['placeOfBirth']
    student.birth_country = data['birthCountry']
    student.email = data['email']
    student.address_line_1 = data['address1']
    student.address_line_2 = data['address2']
    student.city = data['city']
    student.pincode = data['pin']
    student.state = data['state']
    student.country = data['country']
    student.nationality = data['nationality']
    student.phone_number = data['phoneNumber']
    student.national_identification_type = data['identificationType']
    student.national_identification_number = data['identificationNumber']

    VOSDb.session.commit()
    return make_response(jsonify({"message": "Customer Updated"}), 200)


@bp.route("", methods=['POST'])
def addStudent():
    data = request.get_json()
    student = Student(data['firstName'], data['middleName'], data['lastName'], data['dateOfBirth'],
                      data['placeOfBirth'], data['birthCountry'], data['address1'],
                      data['address2'], data['email'], data['city'], data['pin'], data['state'],
                      data['country'], data['nationality'], data['phoneNumber'], data['identificationType'],
                      data['identificationNumber'])

    VOSDb.session.add(student)
    VOSDb.session.commit()
    return make_response(jsonify({"message": "Student Added"}), 201)
