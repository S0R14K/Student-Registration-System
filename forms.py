from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, IntegerField,
                     SelectField, SubmitField)
from wtforms.validators import DataRequired, Email, NumberRange, Length


class StudentForm(FlaskForm):
    student_number = StringField('Student Number',
                                 validators=[DataRequired(), Length(max=20)])
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(max=50)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(max=120)])
    date_of_birth = DateField('Date of Birth',
                              validators=[DataRequired()])
    submit = SubmitField('Save')


class LecturerForm(FlaskForm):
    lecturer_number = StringField('Lecturer Number',
                                  validators=[DataRequired(), Length(max=20)])
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(max=50)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(max=120)])
    department = StringField('Department',
                             validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Save')


class CourseForm(FlaskForm):
    course_code = StringField('Course Code',
                              validators=[DataRequired(), Length(max=20)])
    title = StringField('Title',
                        validators=[DataRequired(), Length(max=150)])
    credits = IntegerField('Credits',
                           validators=[DataRequired(),
                                       NumberRange(min=1, message='Credits must be positive.')])
    lecturer_id = SelectField('Lecturer', coerce=int,
                              validators=[DataRequired()])
    submit = SubmitField('Save')


class EnrollmentForm(FlaskForm):
    student_id = SelectField('Student', coerce=int,
                             validators=[DataRequired()])
    course_id = SelectField('Course', coerce=int,
                            validators=[DataRequired()])
    submit = SubmitField('Register')
