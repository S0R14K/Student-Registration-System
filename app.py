from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.exc import IntegrityError
from config import Config
from models import db, Student, Lecturer, Course, Enrollment
from forms import StudentForm, LecturerForm, CourseForm, EnrollmentForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
csrf = CSRFProtect(app)


def lecturer_choices():
    return [
        (lecturer.id, f"{lecturer.full_name()} ({lecturer.lecturer_number})")
        for lecturer in Lecturer.query.order_by(Lecturer.last_name).all()
    ]


def student_choices():
    return [
        (student.id, f"{student.full_name()} ({student.student_number})")
        for student in Student.query.order_by(Student.last_name).all()
    ]


def course_choices():
    return [
        (course.id, f"{course.title} ({course.course_code})")
        for course in Course.query.order_by(Course.title).all()
    ]


@app.route('/')
def index():
    stats = {
        'students': Student.query.count(),
        'lecturers': Lecturer.query.count(),
        'courses': Course.query.count(),
        'enrollments': Enrollment.query.count(),
    }
    return render_template('index.html', stats=stats)


@app.route('/students')
def student_list():
    search = request.args.get('search', '').strip()
    if search:
        students = Student.query.filter(
            (Student.first_name.ilike(f'%{search}%')) |
            (Student.last_name.ilike(f'%{search}%')) |
            (Student.student_number.ilike(f'%{search}%'))
        ).order_by(Student.last_name).all()
    else:
        students = Student.query.order_by(Student.last_name).all()
    return render_template('students/list.html', students=students, search=search)


@app.route('/students/add', methods=['GET', 'POST'])
def student_add():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            student_number=form.student_number.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            date_of_birth=form.date_of_birth.data,
        )
        try:
            db.session.add(student)
            db.session.commit()
            flash('Student created successfully!', 'success')
            return redirect(url_for('student_list'))
        except IntegrityError:
            db.session.rollback()
            flash('Student number or email already exists.', 'danger')
    return render_template('students/form.html', form=form, title='Add Student')


@app.route('/students/<int:student_id>')
def student_detail(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('students/detail.html', student=student)


@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def student_edit(student_id):
    student = Student.query.get_or_404(student_id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.student_number = form.student_number.data
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.email = form.email.data
        student.date_of_birth = form.date_of_birth.data
        try:
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('student_detail', student_id=student.id))
        except IntegrityError:
            db.session.rollback()
            flash('Student number or email already exists.', 'danger')
    return render_template('students/form.html', form=form, title='Edit Student')


@app.route('/students/<int:student_id>/delete', methods=['POST'])
def student_delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully.', 'success')
    return redirect(url_for('student_list'))

@app.route('/lecturers')
def lecturer_list():
    search = request.args.get('search', '').strip()
    if search:
        lecturers = Lecturer.query.filter(
            (Lecturer.first_name.ilike(f'%{search}%')) |
            (Lecturer.last_name.ilike(f'%{search}%')) |
            (Lecturer.lecturer_number.ilike(f'%{search}%'))
        ).order_by(Lecturer.last_name).all()
    else:
        lecturers = Lecturer.query.order_by(Lecturer.last_name).all()
    return render_template('lecturers/list.html', lecturers=lecturers, search=search)


@app.route('/lecturers/add', methods=['GET', 'POST'])
def lecturer_add():
    form = LecturerForm()
    if form.validate_on_submit():
        lecturer = Lecturer(
            lecturer_number=form.lecturer_number.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            department=form.department.data,
        )
        try:
            db.session.add(lecturer)
            db.session.commit()
            flash('Lecturer created successfully!', 'success')
            return redirect(url_for('lecturer_list'))
        except IntegrityError:
            db.session.rollback()
            flash('Lecturer number or email already exists.', 'danger')
    return render_template('lecturers/form.html', form=form, title='Add Lecturer')


@app.route('/lecturers/<int:lecturer_id>')
def lecturer_detail(lecturer_id):
    lecturer = Lecturer.query.get_or_404(lecturer_id)
    return render_template('lecturers/detail.html', lecturer=lecturer)


@app.route('/lecturers/<int:lecturer_id>/edit', methods=['GET', 'POST'])
def lecturer_edit(lecturer_id):
    lecturer = Lecturer.query.get_or_404(lecturer_id)
    form = LecturerForm(obj=lecturer)
    if form.validate_on_submit():
        lecturer.lecturer_number = form.lecturer_number.data
        lecturer.first_name = form.first_name.data
        lecturer.last_name = form.last_name.data
        lecturer.email = form.email.data
        lecturer.department = form.department.data
        try:
            db.session.commit()
            flash('Lecturer updated successfully!', 'success')
            return redirect(url_for('lecturer_detail', lecturer_id=lecturer.id))
        except IntegrityError:
            db.session.rollback()
            flash('Lecturer number or email already exists.', 'danger')
    return render_template('lecturers/form.html', form=form, title='Edit Lecturer')


@app.route('/lecturers/<int:lecturer_id>/delete', methods=['POST'])
def lecturer_delete(lecturer_id):
    lecturer = Lecturer.query.get_or_404(lecturer_id)
    db.session.delete(lecturer)
    db.session.commit()
    flash('Lecturer deleted successfully.', 'success')
    return redirect(url_for('lecturer_list'))

@app.route('/courses')
def course_list():
    search = request.args.get('search', '').strip()
    if search:
        courses = Course.query.filter(
            (Course.course_code.ilike(f'%{search}%')) |
            (Course.title.ilike(f'%{search}%'))
        ).order_by(Course.title).all()
    else:
        courses = Course.query.order_by(Course.title).all()
    return render_template('courses/list.html', courses=courses, search=search)


@app.route('/courses/add', methods=['GET', 'POST'])
def course_add():
    form = CourseForm()
    form.lecturer_id.choices = lecturer_choices()
    if form.validate_on_submit():
        course = Course(
            course_code=form.course_code.data,
            title=form.title.data,
            credits=form.credits.data,
            lecturer_id=form.lecturer_id.data,
        )
        try:
            db.session.add(course)
            db.session.commit()
            flash('Course created successfully!', 'success')
            return redirect(url_for('course_list'))
        except IntegrityError:
            db.session.rollback()
            flash('Course code already exists.', 'danger')
    return render_template('courses/form.html', form=form, title='Add Course')


@app.route('/courses/<int:course_id>')
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('courses/detail.html', course=course)


@app.route('/courses/<int:course_id>/edit', methods=['GET', 'POST'])
def course_edit(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)
    form.lecturer_id.choices = lecturer_choices()
    if form.validate_on_submit():
        course.course_code = form.course_code.data
        course.title = form.title.data
        course.credits = form.credits.data
        course.lecturer_id = form.lecturer_id.data
        try:
            db.session.commit()
            flash('Course updated successfully!', 'success')
            return redirect(url_for('course_detail', course_id=course.id))
        except IntegrityError:
            db.session.rollback()
            flash('Course code already exists.', 'danger')
    return render_template('courses/form.html', form=form, title='Edit Course')


@app.route('/courses/<int:course_id>/delete', methods=['POST'])
def course_delete(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('Course deleted successfully.', 'success')
    return redirect(url_for('course_list'))

@app.route('/enrollments')
def enrollment_list():
    enrollments = Enrollment.query.order_by(Enrollment.registration_date.desc()).all()
    return render_template('enrollments/list.html', enrollments=enrollments)


@app.route('/enrollments/add', methods=['GET', 'POST'])
def enrollment_add():
    form = EnrollmentForm()
    form.student_id.choices = student_choices()
    form.course_id.choices = course_choices()
    if form.validate_on_submit():
        existing = Enrollment.query.filter_by(
            student_id=form.student_id.data,
            course_id=form.course_id.data
        ).first()
        if existing:
            flash('This student is already enrolled in this course.', 'warning')
        else:
            enrollment = Enrollment(
                student_id=form.student_id.data,
                course_id=form.course_id.data,
            )
            db.session.add(enrollment)
            db.session.commit()
            flash('Enrollment registered successfully!', 'success')
            return redirect(url_for('enrollment_list'))
    return render_template('enrollments/form.html', form=form, title='Register Enrollment')


@app.route('/enrollments/<int:enrollment_id>/drop', methods=['POST'])
def enrollment_drop(enrollment_id):
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    db.session.delete(enrollment)
    db.session.commit()
    flash('Enrollment dropped successfully.', 'success')
    return redirect(url_for('enrollment_list'))

if __name__ == '__main__':
    app.run(debug=True)
