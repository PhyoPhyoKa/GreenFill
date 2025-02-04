from wtforms import Form, StringField, EmailField, PasswordField,SubmitField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length


class CreateUserForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(message='Invalid Email Address'), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8, message="Passwords must be at least 8 characters."),
                                          validators.DataRequired()])
    submit = SubmitField('Sign Up')


class LogInForm(Form):
    email = EmailField('Email', [validators.Email(message='Invalid Email Address'), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Log in')


class UpdatePasswordForm(Form):
    current_password = PasswordField('Current Password', [validators.DataRequired()])
    new_password = PasswordField('New Password', [validators.Length(min=8,
                                                                    message="Passwords must be at least 8 characters."),
                                                  validators.DataRequired()])
    confirm_password = PasswordField('Confirm New Password', [validators.DataRequired(),
                                                              validators.EqualTo('new_password', message='Password must match.'),])
    submit = SubmitField('Update Password')