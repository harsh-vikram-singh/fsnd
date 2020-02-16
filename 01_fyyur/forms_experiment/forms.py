from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class EmployeeForm(FlaskForm):
    name = StringField('employee_name', validators=[DataRequired()])
    designation = StringField('employee_designation',
                              validators=[DataRequired()])
    manager = SelectField('employee_manager', validators=[DataRequired],
                          choices=[
        ('CEO', 'CEO'),
        ('CMO', 'Marketing Head'),
        ('CSO', 'Sales Head')
    ])
    submit = SubmitField('submit_data')
