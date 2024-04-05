from flask import Flask, jsonify, make_response, request, render_template
from mathematics import summation, subtraction, multiplication

app = Flask(__name__)

data = [
    {
        "id": "1",
        "first_name": "yusuf",
        "last_name": "masri"
    },
    {
        "id": "2",
        "first_name": "ibrahim",
        "last_name": "masri"
    },
    {
        "id": "3",
        "first_name": "omar",
        "last_name": "masri"
    }
]

@app.route('/')
def index():
    return jsonify({"message": "Hello World"})


@app.route("/no_content")
def no_content():
    return ({"message":"No content found"},204)

@app.route("/exp")
def index_explicit():
    resp = make_response({"message": "Hello World"})
    resp.status_code = 200
    return resp


@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of the length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
        
    except NameError:
        return {"message": "Data not found"}, 404
    
@app.route("/name_search")
def name_search():
    
    query = request.args.get("q")

    if not query:
        return {"message": "Invalid input parameter"}, 422
    
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person
        
    return ({"message": "Person not found"}, 404)

@app.route("/count")
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500
    
@app.route("/person/<id>")
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person
    return {"message": "person not found"}, 404

@app.route("/person/<id>", methods =['DELETE'])
def delete_by_id(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message":f"{id} removed"}, 200
    return {"message": f"{id} not found"}, 404



@app.route("/calculator")
def render_index_page():
    return render_template('index.html')

@app.route("/calculator/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1,num2)
    return str(result)

@app.route("/calculator/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1,num2)
    return str(result)

@app.route("/calculator/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1,num2)
    return str(result)

    
app.run(debug=1)  