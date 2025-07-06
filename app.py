"""
from flask import Flask, render_template, request
#to input file into flask, we need two modules flask_wtf and wtforms to the installed using pip and import here for use as below
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

#to build the form upload, we would crrate a class

class UploadFileForm(FlaskForm): #inherits from the imported Flaskform above
    file = FileField("File", validators=[InputRequired()]) #creating an input variables using the imported FileField above
    submit = SubmitField("Upload File") #creating an input variables using the imported submitField above.

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data #first grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "File has been uploaded"
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

    
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/upload', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        return render_template('index.html')
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
