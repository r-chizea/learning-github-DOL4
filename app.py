from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return 'Hello Internet!'

@app.route('/name')
def hello_user():
    name = 'Rob'
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)