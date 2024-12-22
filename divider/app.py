from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Server töötab!"

@app.route('/divide', methods=['GET'])
def divide():
    try:
        x = float(request.args.get('x', 0))
        y = float(request.args.get('y', 0))
        
        if y == 0:
            return jsonify({"error": "You can't divide by 0!"})
            
        result = x / y
        return jsonify({"result": result})
        
    except ValueError:
        return jsonify({"error": "Please provide valid numbers"})

if __name__ == '__main__':
    app.run(debug=True, port=8080) 