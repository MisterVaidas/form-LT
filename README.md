# Cryptocurrency and Blockchain Course Registration App

This Flask application is designed for users to register for a cryptocurrency and blockchain course. It features a form for user input, email notifications, and a stylish interface.

## Features

- User registration form with fields for name, surname, date of birth, city, country, email address, telephone number, and knowledge level about cryptocurrencies and blockchain.
- Email notification on form submission.
- Dynamic country list populated in the form.
- Styled interface with responsive design.
- SweetAlert for displaying a stylish success message.

## Setup and Installation

To get this project up and running, follow these steps:

### Prerequisites

- Python 3.x
- Flask
- Flask-Mail
- pycountry

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repository/cryptocurrency-course-registration.git
   cd cryptocurrency-course-registration

### Set up a Virtual Environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`

```

### Install Required Packages:

```
pip install -r requirements.txt

```

### Configure Email Settings:

Set up the email configuration in `config.py` or as environment variables.

### Run the Application:

```
flask run

```

### Usage

After starting the app, navigate to `http://localhost:5000` in your web browser to access the form. Fill in the details and submit the form to see the success message.

### Deployment

For deployment instructions, refer to the Flask deployment documentation or the documentation provided by your hosting service.

### Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

### Contact

For any queries or further assistance with this project, please contact Vaidas Simkus