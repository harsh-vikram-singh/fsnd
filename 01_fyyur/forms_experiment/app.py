from flask import Flask, render_template
from forms import EmployeeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ARANDondfsdfkjgrw09rgfjtwofnqroisdfvnr[pifjsdf]'


@app.route('/')
def index():
    form = EmployeeForm()
    return render_template('index.html', form=form)
