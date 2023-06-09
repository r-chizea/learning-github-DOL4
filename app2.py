from flask import Flask, request

app = Flask(__name__)

colours = ['purple', 'black', 'gold']

contents = f'''
Hello! You have made a GET request. 
 You can also make more requests using these URLs:
 Show all colours: http://18.170.229.188:5000/showall
 show a colour: http://18.170.229.188:5000/showcolour/<colourid>
 add a colour: http://18.170.229.188:5000/addcolour
 change a colour: http://18.170.229.188:5000/changecolour/<colourid>
 delete a colour: http://18.170.229.188:5000/delcolour/<colourid>
'''

@app.route('/')
def home():
    return contents

@app.route('/showall')
def allcolours():
    return colours

@app.route('/showcolour/<colourid>')
def colourshow(colourid):
    if len(colours) <= int(colourid):
        return "Outside of data range"
    else:
        return colours[int(colourid)]

@app.route('/addcolour', methods=['GET', 'POST'])
def add_colour():
    if request.method == 'POST':
        colours.append(request.get_data())
        return "200 - OK. Your POST request has been fulfilled!"
    else:
        return "You need to use a POST HTTP method"

@app.route('/changecolour/<colourid>', methods=['GET', 'PUT'])
def colourchange(colourid):
    if request.method == 'PUT':
        if len(colours) <= int(colourid):
            return "Outside of data range"
        else:
            colours[int(colourid)] = request.get_data()
            return "200 - OK. Your PUT request has been fulfilled!"
    else:
        return 'Please submit a PUT request'

@app.route('/delcolour/<colourid>', methods=['GET','DELETE'])
def colourdel(colourid):
    if request.method == 'DELETE':
        if len(colours) <= int(colourid):
            return "Outside of data range"
        else:
            colours.pop(int(colourid))
            return "200 - OK. Your DELETE request has been fulfilled!"
    else:
        return "You need to use a DELETE HTTP method"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)