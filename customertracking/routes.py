from flask import render_template, url_for, flash, redirect
from customertracking import app, db, bcrypt
from customertracking.forms import RegistrationForm, LoginForm
from customertracking.models import User, Customer

customers = [
    {
        'Name': 'Κώστας Παπαδημητρίου',
        'Balance': 1.345,
        'Address': 'Καποδιστρίου 64'
    },
    {
        'Name': 'Γιώργος Παπαβασιλείου',
        'Balance': 10.000,
        'Address': 'Χατζηζωγίδου 23'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', customers=customers)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f'Δημιουργήθηκε ο λογαριασμός για το χρήστη {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Εγγραφή', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Έχεις συνδεθεί επιτυχώς', 'success')
        return redirect(url_for('home'))
    else:
        flash('Αποτυχία σύνδεσης', 'danger')
    return render_template('login.html', title='Σύνδεση', form=form)
