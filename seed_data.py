from app import app
from models import db, Student, Lecturer, Course, Enrollment

lecturers_data = [
    {'lecturer_number': 'LEC001', 'first_name': 'James',   'last_name': 'Smith',   'email': 'james.smith@university.edu',   'department': 'Computer Science'},
    {'lecturer_number': 'LEC002', 'first_name': 'Sarah',   'last_name': 'Johnson', 'email': 'sarah.johnson@university.edu', 'department': 'Mathematics'},
    {'lecturer_number': 'LEC003', 'first_name': 'Emily',   'last_name': 'Williams','email': 'emily.williams@university.edu','department': 'Software Engineering'},
]

courses_data = [
    {'course_code': 'CS101',  'title': 'Introduction to Programming', 'credits': 6, 'lecturer_number': 'LEC001'},
    {'course_code': 'CS201',  'title': 'Data Structures',             'credits': 6, 'lecturer_number': 'LEC001'},
    {'course_code': 'MATH101','title': 'Calculus I',                   'credits': 5, 'lecturer_number': 'LEC002'},
    {'course_code': 'SE301',  'title': 'Software Engineering',        'credits': 6, 'lecturer_number': 'LEC003'},
    {'course_code': 'SE302',  'title': 'Software Testing & QA',       'credits': 5, 'lecturer_number': 'LEC003'},
]

with app.app_context():
    Enrollment.query.delete()
    Course.query.delete()
    Lecturer.query.delete()
    Student.query.delete()
    db.session.commit()

    for data in lecturers_data:
        db.session.add(Lecturer(**data))
    db.session.commit()

    for data in courses_data:
        lecturer = Lecturer.query.filter_by(lecturer_number=data.pop('lecturer_number')).first()
        db.session.add(Course(lecturer_id=lecturer.id, **data))
    db.session.commit()

    print("Seed data inserted successfully.")
    print(f"  Lecturers:   {Lecturer.query.count()}")
    print(f"  Courses:     {Course.query.count()}")
