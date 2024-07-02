from flask import Flask, render_template, request, url_for
from joblib import load
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the saved model
model = load('model.joblib')

# Example route to handle predictions
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Example: Read input values from the HTML form
    age = float(request.form['age'])
    bp = float(request.form['bp'])
    sg = float(request.form['sg'])
    al = float(request.form['al'])
    su = float(request.form['su'])
    rbc = request.form['rbc']  # Example dropdown with options in HTML form
    pc = request.form['pc']    # Example dropdown with options in HTML form
    pcc = request.form['pcc']  # Example dropdown with options in HTML form
    ba = request.form['ba']    # Example dropdown with options in HTML form
    bgr = float(request.form['bgr'])
    bu = float(request.form['bu'])
    sc = float(request.form['sc'])
    sod = float(request.form['sod'])
    pot = float(request.form['pot'])
    hemo = float(request.form['hemo'])
    pcv = int(request.form['pcv'])
    wc = int(request.form['wc'])
    rc = float(request.form['rc'])  # Convert to float, not int
    htn = request.form['htn']    # Example dropdown with options in HTML form
    dm = request.form['dm']      # Example dropdown with options in HTML form
    cad = request.form['cad']    # Example dropdown with options in HTML form
    appet = request.form['appet']  # Example dropdown with options in HTML form
    pe = request.form['pe']      # Example dropdown with options in HTML form
    ane = request.form['ane']    # Example dropdown with options in HTML form

    # Create a dictionary to store input data
    data = {
        'age': [age],
        'bp': [bp],
        'sg': [sg],
        'al': [al],
        'su': [su],
        'rbc': [rbc],
        'pc': [pc],
        'pcc': [pcc],
        'ba': [ba],
        'bgr': [bgr],
        'bu': [bu],
        'sc': [sc],
        'sod': [sod],
        'pot': [pot],
        'hemo': [hemo],
        'pcv': [pcv],
        'wc': [wc],
        'rc': [rc],
        'htn': [htn],
        'dm': [dm],
        'cad': [cad],
        'appet': [appet],
        'pe': [pe],
        'ane': [ane]
    }

    # Create a DataFrame from the input data dictionary
    df = pd.DataFrame(data)

    # Apply label encoding to categorical columns if needed
    categorical_cols = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
    label_encoders = {}
    for col in categorical_cols:
        label_encoders[col] = LabelEncoder()
        df[col] = label_encoders[col].fit_transform(df[col].astype(str))

    # Make predictions using the loaded model
    prediction = model.predict(df)

    if prediction == 2:
        result = 'Based on the test results, it appears that you have not Chronic Kidney Disease'

    else:
        result = 'Based on the test results, it appears that you have Chronic Kidney Disease.'


    # Return the prediction result to the frontend
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
