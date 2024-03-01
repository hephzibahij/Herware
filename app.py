from flask import Flask, request

app = Flask(_name_)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    gender = request.form.get('gender')
    organization = request.form.get('organization')
    date of birth = request.form.get('date of birth')
    why do you want to volunteer = request.form.get('why
                                                    do you want to volunteer')
    # Process the data (e.g., save to a database)
    return 'Form submitted successfully'


@app.route('/')
def index():
    return "Welcome to the Girlchild API"


if _name_ == '_main_':
    app.run()
