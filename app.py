from flask import Flask, jsonify, request
from code import getprediction
app=Flask(__name__)
@app.route("/predict-alphabet", methods=["POST"])
def predict_data():
    image = request.files.get("alphabet")
    prediction = getprediction(image)
    return jsonify({
        "rediction":prediction
    }),200
if __name__=="__main__":
    app.run(debug=True)