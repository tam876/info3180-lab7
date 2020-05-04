from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired
from wtforms import TextAreaField

class UploadForm(FlaskForm):
    description = TextAreaField("Description", validators=[InputRequired()])
    photo = FileField("Photo", validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'],"Images only")])