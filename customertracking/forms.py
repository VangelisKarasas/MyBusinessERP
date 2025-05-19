from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, DateField, FieldList, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from customertracking.models import User

customers = [
    {
        'id': 1,
        'Name': 'Κώστας Παπαδημητρίου',
        'Balance': 1.345,
        'Address': 'Καποδιστρίου 64'
    },
    {
        'id': 2,
        'Name': 'Γιώργος Παπαβασιλείου',
        'Balance': 10.000,
        'Address': 'Χατζηζωγίδου 23'
    }
]

names = [(str(customer['id']) + ": " + customer['Name'])
         for customer in customers]


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Εγγραφή')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Θυμήσου με')
    submit = SubmitField('Σύνδεση')


class CustomerForm(FlaskForm):
    id = StringField('Κωδικός', validators=[DataRequired()])
    name = StringField('Επωνυμία', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    tax_number = StringField('ΑΦΜ')
    total_balance = IntegerField('Υπόλοιπο')
    submit = SubmitField('Καταχώρηση')


class DocumentLinesForm(FlaskForm):
    code = StringField(u'Κωδικός Είδους', validators=[
        DataRequired(), Length(min=2, max=25)])
    description = StringField(u'Περιγραφή Είδους', validators=[
        DataRequired(), Length(min=2, max=60)])
    brand = SelectField(u'Brand', choices=names)
    net_value = IntegerField(validators=[DataRequired()])
    vat_value = IntegerField(validators=[DataRequired()])
    gross_value = IntegerField(validators=[DataRequired()])


class DocumentForm(FlaskForm):
    document_type = SelectField(
        u'Τύπος Παρ/κού', choices=[('1', 'ΤΔΑ'), ('2', 'ΠΤΔ')], validators=[DataRequired()])
    document_code = StringField(u'Κωδικός Παραστατικού', validators=[
        DataRequired(), Length(min=2, max=25)])
    customer = SelectField(u'Πελάτης', choices=names)
    gross_value = IntegerField(validators=[DataRequired()])
    net_value = IntegerField(validators=[DataRequired()])
    vat_value = IntegerField(validators=[DataRequired()])
    registration_date = DateField(validators=[DataRequired()])
    lines = FieldList(FormField(DocumentLinesForm),
                      min_entries=5, max_entries=50)
    submit = SubmitField('Καταχώρηση')


class ItemForm(FlaskForm):
    id = StringField(u'Κωδικός Είδους', validators=[
        DataRequired(), Length(min=2, max=25)])
    description = StringField(u'Περιγραφή Είδους', validators=[
        DataRequired(), Length(min=2, max=25)])
    brand_description = SelectField(u'Brand Είδους', choices=[
                                    ('1', 'Kraft'), ('2', 'FF Group')])
    price = IntegerField()
    size = StringField(u'Μέγεθος', validators=[
        DataRequired()])
    submit = SubmitField('Καταχώρηση')
