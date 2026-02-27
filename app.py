from flask import Flask,request, jsonify
import joblib
import numpy as np 

model= joblib.load("insurance_model.pkl")

app=Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data=request.get_json(force=True)
        input_data=np.array(data["input"]).reshape(1,-1)
        prediction=model.predict(input_data)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error":str(e)})

if __name__=="__main__":
    app.run(debug=True)