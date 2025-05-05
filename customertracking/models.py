from customertracking import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),
                         unique=True, nullable=False)
    email = db.Column(db.String(120),
                      unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    customers = db.relationship('Customer', backref='constructor', lazy=True)

    def __repr__(self):
        return f"Χρήστης('{self.username}','{self.email}')"


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60),
                     unique=True, nullable=False)
    email = db.Column(db.String(120),
                      unique=True, nullable=False)
    total_balance = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),  nullable=False)

    tasks = db.relationship('Task', backref='customer', lazy=True)

    def __repr__(self):
        return f"Πελάτης('{self.name}','{self.email}')"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customer.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    analytical_description = db.Column(db.String(max))
    price = db.Column(db.Integer, nullable=True)
    total_balance = db.Column(db.Integer, nullable=True)
    finish_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"Εργασία ('{self.description}' που ολοκληρώθηκε στις '{self.finish_date}' με αξία '{self.price}')"
