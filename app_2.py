from flask import Flask, jsonify

app = Flask(__name__)

tutorials = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'idi': 3,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('//tutorials', methods=['GET'])
def get_task():
    return jsonify({'tutorials': tutorials})
    
if __name__ == '__main__':
    app.run(debug=True)
