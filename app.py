from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Herware API"

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    gender = request.form.get('gender')
    organization = request.form.get('organization')
    date of birth = request.form.get('date of birth')
    why do you want to volunteer = request.form.get('why do you want to volunteer')
    # Process the data (e.g., save to a database)
    return f'Form submitted successfully with name: {name} and email: {email}'

if __name__ == '__main__':
    app.run(debug=True)
