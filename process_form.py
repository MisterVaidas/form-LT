from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
from config import email_user, email_password
import pycountry

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.ionos.co.uk'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = email_user
app.config['MAIL_PASSWORD'] = email_password
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            name = request.form['name']
            surname = request.form['surname']
            date_of_birth = request.form['dateOfBirth']
            city = request.form['city']
            country = request.form['country']
            email_address = request.form['email']
            telephone_number = request.form['telephone']
            knowledge = request.form['knowledge']

            msg = Message('New Course Registration', sender='admin@ledgerfield.io', recipients=['admin@ledgerfield.io'])
            msg.body = (
                f"New registration:\n"
                f"Name: {name}\n"
                f"Surname: {surname}\n"
                f"Date of Birth: {date_of_birth}\n"
                f"City: {city}\n"
                f"Country: {country}\n"
                f"Email: {email_address}\n"
                f"Telephone: {telephone_number}\n"
                f"Knowledge Level: {knowledge}"
            )

            mail.send(msg)
            return 'Registration successful!'
        except Exception as e:
            print(f"An error occurred: {e}")

            return 'An error occurred during registration. Please try again later.'

    else:
        countries = [country.name for country in pycountry.countries]
        return render_template('index.html', countries=countries)
    
if __name__ == '__main__':
    app.run(debug=True)
