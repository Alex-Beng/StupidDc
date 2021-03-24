from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired

from app import photos

class AddClothesForm(FlaskForm):
    title = StringField(u'您的新衣裳叫啥好呢')
    photo = FileField(u'图片', validators=[
        FileRequired(u'你还没有选择图片！'),
        FileAllowed(['jpg', 'png', 'jpeg'], u'只能上传图片！')])
    submit = SubmitField(u'提交')
