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
        return render_template(
            'hello.html',
            data=data)
    if request.method == 'GET':
        return render_template(
            'hello.html',
            data=None)

if __name__ == "__main__":
    app.run()

