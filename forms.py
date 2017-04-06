from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class newGuideForm(Form):
    title = StringField('Tajuk', validators=[DataRequired()])
    body = StringField('Isi', validators=[DataRequired()], widget=TextArea())
