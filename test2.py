from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/sudh', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


@app.route('/sudh2', methods=['POST']) # for calling the API from Postman/SOAPUI
def math():
    if (request.method=='POST'):
        a =int(request.json['num'])
        b =int(request.json['num1'])
        c = int(request.json['num2'])
        result = a * b * c
        return jsonify(result)


@app.route('/sudh3', methods=['POST']) # for calling the API from Postman/SOAPUI
def math2():
    if (request.method=='POST'):
        a = request.json["name"]
        result = a + a
        return jsonify(result)


if __name__ == '__main__':
    app.run()
