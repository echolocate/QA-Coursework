from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, DateField, IntegerField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ygjuyewjdjddfwwopkgssjkjsjfhyw35ytytn'

class BasicForm(FlaskForm):
    dob = DateField('Date of birth', format='%Y-%m-%d')
    fav_no = IntegerField('Favorite number')
    fav_food = SelectField("Favorite food", choices=[
        ("pizza", "Pizza"), 
        ("spaghetti", "Spaghetti"), 
        ("chilli", "Chilli")
    ])
    submit = SubmitField('Enter details')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        dob = form.dob.data
        fav_no = form.fav_no.data
        fav_food = form.fav_food.data

        if len(dob) == 0 or len(fav_no) == 0 or len(fav_food) == 0:
            message = "Please fill in ALL fields"
        else:
            message = f'Thank you, username is {dob} {fav_no} {fav_food}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')