from flask import Flask, request, jsonify
from predict import predict_loan

app = Flask(__name__)


# -----------------------------
# HOME ROUTE
# -----------------------------

@app.route('/')
def home():

    return jsonify({
        "message": "AI Loan Risk Analysis API Running Successfully"
    })


# -----------------------------
# PREDICTION ROUTE
# -----------------------------

@app.route('/predict', methods=['POST'])
def predict():

    try:

        # Get JSON data from request
        data = request.get_json()

        # Validate request data
        if not data:

            return jsonify({
                "success": False,
                "error": "No input data provided"
            }), 400

        # Generate prediction
        result = predict_loan(data)

        # Return response
        return jsonify({
            "success": True,
            "prediction": result["prediction"],
            "probability": result["probability"],
            "risk_level": result["risk_level"],
            "ai_insights": result["ai_insights"]
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------
# MAIN ENTRY
# -----------------------------

if __name__ == '__main__':

    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )