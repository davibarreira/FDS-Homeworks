from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AuthorForm(FlaskForm):
    """docstring for AuthorForm"""
    authorname = StringField('Author',
                             validators=[DataRequired(),
                             Length(min=2, max=20)]
                            )
        
    submit = SubmitField('Scrape')