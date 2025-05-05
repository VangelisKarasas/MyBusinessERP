from flask import render_template, url_for, flash, redirect, request
from customertracking import app, db, bcrypt
from customertracking.forms import RegistrationForm, LoginForm
from customertracking.models import User, Customer
from flask_login import login_user, current_user, logout_user, login_required

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

tasks = [
    {
        'id': '1',
        'Name': 'Κώστας Παπαδημητρίου',
        'Description': 'Τοποθέτηση μαρμάρων 30μ',
        'Cost': '1200',
        'Completion_date': '5/5/2025'
    },
    {
        'id': '2',
        'Name': 'Γιώργος Αντωνίου',
        'Description': 'Τοποθέτηση πλακάκια 30 τ.μ',
        'Cost': '1000',
        'Completion_date': '2/5/2025'
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
        #     flash('Αποτυχία σύνδεσης', 'danger')
        return render_template('login.html', title='Σύνδεση', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Λογαριασμός')


@app.route("/customers")
@login_required
def customer_list():
    return render_template('customer_list.html', customers=customers)


@app.route("/tasks")
@login_required
def task_list():
    return render_template('task_list.html', tasks=tasks)
