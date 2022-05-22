from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello", methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        print(request.form.get('name'))
        data = {'message': request.form.get('name')}
        return render_template('hello.html', data=data)
    if request.method == 'GET':
        return render_template('hello.html', data=None)

@app.route("/hello_form")
def hello_from():
    return render_template('hello_form.html', data=None)

@app.route("/hello_result", methods=['POST'])
def hello_result():
    #model = .....
    #employee_age = request.form.get('age')
    #employee_years_with_company = request.form.get('years_with_company')
    #input = [employee_age, employee_years_with_company]
    #result = model.predict(input)
    data = {'message': request.form.get('name') }
    return render_template('hello_result.html', data=data)

if __name__ == "__main__":
    app.run()

