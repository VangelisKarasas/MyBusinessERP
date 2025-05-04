from customertracking import db


class User(db.Model):
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
    name = db.Column(db.String(60), primary_key=True,
                     unique=True, nullable=False)
    email = db.Column(db.String(120), primary_key=True,
                      unique=True, nullable=False)
    total_balance = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),  nullable=False)

    def __repr__(self):
        return f"Πελάτης('{self.name}','{self.email}')"
