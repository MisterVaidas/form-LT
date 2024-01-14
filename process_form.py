from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import os
import pycountry
import random

def generate_reference_number():
    return 'LF' + str(random.randint(100000, 999999))

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.ionos.co.uk'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER', 'default_email_user')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD', 'default_email_password')

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
            
            reference_number = generate_reference_number()

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
                f"Knowledge Level: {knowledge}\n"
                f"Reference number: {reference_number}"
            )
            
            
            
            html_content = render_template('email_template.html', reference_number=reference_number)
            
            user_msg = Message('Registracijos patvirtinimas', 
                               sender='admin@ledgerfield.io', 
                               recipients=[email_address])
            user_msg.html = html_content
            mail.send(user_msg)

            mail.send(msg)
            # return 'Registration successful!'
            return render_template('index.html', success=True, ref_number=reference_number)
        except Exception as e:
            print(f"An error occurred: {e}")

            return 'An error occurred during registration. Please try again later.'

    else:
        countries = [country.name for country in pycountry.countries]
        return render_template('index.html', success=False, countries=countries)
    
@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.run(debug=False)
    
