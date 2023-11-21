from app import db
from datetime import datetime


# PROJECT TABLE
class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    site = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    # Add a foreign key relationship with the Firm table
    firm_id = db.Column(db.Integer, db.ForeignKey('firm.id'))
    firm = db.relationship('Firm', back_populates='projects')

    # Define the relationship with transactions
    transactions = db.relationship('Transaction', back_populates='project')

    def __init__(self, name, site, start_date, end_date, description, firm_id):
        self.name = name
        self.site = site
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.firm_id = firm_id

    def __repr__(self):
        return 'The Project is {}'.format(self.name)


# VENDOR TABLE
class Vendor(db.Model):
    __tablename__ = 'vendor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    address = db.Column(db.String(700), nullable=False)
    contactNbr = db.Column(db.String(20), nullable=False)

    # Define the relationship with transactions
    transactions = db.relationship('Transaction', back_populates='vendor')

    def __init__(self, name, description, address, contactNbr):
        self.name = name
        self.description = description
        self.address = address
        self.contactNbr = contactNbr

    def __repr__(self):
        return 'The Vendor is {}'.format(self.name)


# FIRM TABLE
class Firm(db.Model):
    __tablename__ = 'firm'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(700), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    gst_no = db.Column(db.String(20), nullable=False)

    # Add a relationship to projects
    projects = db.relationship('Project', back_populates='firm')
    transactions = db.relationship('Transaction', back_populates='firm')

    def __init__(self, name, address, description, gst_no):
        self.name = name
        self.address = address
        self.description = description
        self.gst_no = gst_no

    def __repr__(self):
        return 'The Firm is {}'.format(self.name)


# TRANSACTION TABLE
# TRANSACTION TABLE
class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    paymentDetails = db.Column(db.String(300), nullable=False)
    paymentDate = db.Column(db.Date, nullable=False)
    paymentType = db.Column(db.String(10), nullable=True)  # Add the paymentType column

    # ESTABLISH RELATIONSHIPS
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship('Project', back_populates='transactions')

    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    vendor = db.relationship('Vendor', back_populates='transactions')

    firm_id = db.Column(db.Integer, db.ForeignKey('firm.id'))
    firm = db.relationship('Firm', back_populates='transactions')

    def __init__(self, amount, description, paymentDetails, paymentDate, project_id, vendor_id, firm_id, paymentType):
        self.amount = amount
        self.description = description
        self.paymentDate = paymentDate
        self.paymentDetails = paymentDetails
        self.project_id = project_id
        self.vendor_id = vendor_id
        self.firm_id = firm_id
        self.paymentType = paymentType  # Set the paymentType during initialization

    def __repr__(self):
        return '{} by {} for {}'.format(self.amount, self.description, self.project.name)

