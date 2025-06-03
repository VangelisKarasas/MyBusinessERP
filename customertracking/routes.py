from flask import render_template, url_for, flash, redirect, request
from customertracking import app, db, bcrypt
from customertracking.forms import RegistrationForm, LoginForm, DocumentForm, DocumentLinesForm, CustomerForm, ItemForm
from customertracking.models import User, Customer, Item
from flask_login import login_user, current_user, logout_user, login_required
from customertracking.dbtest import customers, tasks, items, last_sales, documents


# customers = customers
tasks = tasks
# items = items
last_sales = last_sales


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
        flash('Αποτυχία σύνδεσης', 'danger')
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
    customers = Customer.query.filter_by(user_id=current_user.id).all()
    return render_template('customer_list.html', customers=customers)


@app.route("/tasks")
@login_required
def task_list():
    return render_template('task_list.html', tasks=tasks)


@app.route("/items")
@login_required
def item_list():
    items = Item.query.all()
    return render_template('item_list.html', items=items)


@app.route("/documents")
@login_required
def document_list():
    return render_template('document_list.html', documents=documents)


@app.route("/customer_account/ΚώσταςΠαπαδημητρίου")
@login_required
def customer_account():
    return render_template('customer_account.html', last_sales=last_sales)


@app.route("/customer_account/<int:id>", methods=['GET', 'POST'])
@login_required
def customer_account_dep(id):
    customer = Customer.query.filter_by(id=id).first_or_404()
    return render_template('customer_account.html', customer=customer, last_sales=last_sales)


@app.route("/document_registry", methods=['GET', 'POST'])
@login_required
def document_register():
    form = DocumentForm()
    items = Item.query.with_entities(Item.description).distinct().all()
    suggestions = [i.description for i in items]
    if form.validate_on_submit():
        # Access document fields
        doc_type = form.document_type.data
        doc_code = form.document_code.data
        customer = form.customer.data

        # Access lines
        for line in form.lines.entries:
            line_data = line.data
            print("Line:", line_data)  # Save to DB or process

        flash('Καταχωρήθηκε επιτυχώς!', 'success')
        return redirect(url_for('document_register'))

    return render_template("document_registry.html", form=form, suggestions=suggestions)


@app.route("/customer_registry", methods=['GET', 'POST'])
@login_required
def customer_register():
    form = CustomerForm()
    if form.validate_on_submit():
        # Access document fields
        customer = Customer(id=form.id.data, name=form.name.data, email=form.email.data,
                            tax_number=form.tax_number.data, total_balance=form.total_balance.data, user_id=current_user.id)
        db.session.add(customer)
        db.session.commit()
        flash('Καταχωρήθηκε επιτυχώς!', 'success')
        return redirect(url_for('customer_register'))

    return render_template("customer_registry.html", form=form)


@app.route("/item_registry", methods=['GET', 'POST'])
@login_required
def item_register():
    form = ItemForm()
    if form.validate_on_submit():
        # Access document fields
        item = Item(brand=form.brand_description.data, description=form.description.data,
                    size=form.size.data, price=form.price.data)
        db.session.add(item)
        db.session.commit()
        flash('Καταχωρήθηκε επιτυχώς!', 'success')
        return redirect(url_for('item_register'))

    return render_template("item_registry.html", form=form)
