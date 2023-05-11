from flask import Flask

app = Flask(__name__)

contents = '''
Hello! You have made a GET request. You can also make more requests using these URLs:
'''
@app.route('/')
def home():
    return contents

@app.route('/name/<name>')
def hello_user(name):
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)