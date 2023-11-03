from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired
from app.catalog.models import Vendor  # Import Vendor model


class CreateProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    site = StringField('Site', validators=[DataRequired()])
    start_date = DateField('StartDate', validators=[DataRequired()])
    end_date = DateField('EndDate', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    firm_name = StringField('Firm Name')  # New field for Firm Name
    submit = SubmitField('Create')


class CreateVendorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    contactNbr = StringField('Contact', validators=[DataRequired()])
    submit = SubmitField('Create')


class CreateTransactionForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(CreateTransactionForm, self).__init__(*args, **kwargs)
        with current_app.app_context():
            self.vendor.choices = [(v.id, v.name) for v in Vendor.query.all()]

    amount = IntegerField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    paymentDetails = StringField('PaymentDetails', validators=[DataRequired()])
    paymentDate = DateField('PaymentDate', validators=[DataRequired()])
    vendor = SelectField('Vendor', coerce=int, validators=[DataRequired()])
    project_id = IntegerField('ProjectID', validators=[DataRequired()])

    submit = SubmitField('Create')


class CreateFirmForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    gst_no = StringField('GST Number', validators=[DataRequired()])
    submit = SubmitField('Create')
