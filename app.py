from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"
    

@app.route("/test",methods=["POST"])
def first_json():
    my_json = request.get_json()
    get_id = my_json.get("id")
    model_result = 0

    return jsonify(id=get_id,flag=model_result)
    
app.run(host="0,0,0,0")