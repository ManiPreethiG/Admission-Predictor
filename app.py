from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your machine learning model
with open(r'C:\Users\Dell\Documents\flaskApp\model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    gre_score = float(request.form['gre_score'])
    toefl_score = float(request.form['toefl_score'])
    university_rating = float(request.form['university_rating'])
    sop_strength = float(request.form['sop_strength'])
    lor_strength = float(request.form['lor_strength'])
    cgpa = float(request.form['cgpa'])
    research_exp = float(request.form['research_exp'])

    # Prepare the input array in the correct format
    input_data = np.array([[gre_score, toefl_score, university_rating, sop_strength, lor_strength, cgpa, research_exp]])

    # Use the loaded model to make predictions
    prediction = model.predict(input_data)[0]

    # Return the result as a percentage
    return f"Your admission success percentage is: {round((prediction*100),2)}%"

if __name__ == '__main__':
    app.run(debug=True)
