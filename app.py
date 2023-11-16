
from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('strokenew.pkl', 'rb'))

@app.route("/")
def index():
    return ("Hello World")

@app.route("/result", methods=['POST'])

def result():

    data = request.form.to_dict()
    age = request.form['age']
    maritalstatus = request.form['maritalstatus']
    work_type = request.form['work_type']
    residence = request.form['residence']
    gender = request.form['gender']
    bmi = request.form['bmi']
    gluclevel = request.form['gluclevel']
    smoke = request.form['smoke']
    hypertension = request.form['hypertension']
    heart_disease = request.form['heart_disease']

    res={'Urban':1,'Rural':0}
    gen={'Female':0,'Male':1}
    msts={'Married':1,'Not married':0}
    wktype={'PrivateJob':2,'GovernmentJob':1,'SelfEmployed':3}
    smke={'Formerly-Smoked':1,'Non-Smoker':2,'Smoker':3}
    hypten={'Yes':1,'No':0}
    hrtdis={'Yes':1,'No':0}

    residence=res[residence]
    gender=gen[gender]
    maritalstatus=msts[maritalstatus]
    work_type=wktype[work_type]
    smoke=smke[smoke]
    hypertension=hypten[hypertension]
    heart_disease=hrtdis[heart_disease]

    array = [[gender,age,hypertension,heart_disease,maritalstatus,work_type,residence,gluclevel,bmi,smoke]]
    array = [np.array(array[0],dtype = 'float64')]
    pred_stroke = model.predict(array)

    result = int(pred_stroke[0])

    response = {
        'ResultNow': 'Nostroke' if result == 0 else 'Stroke'
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)










