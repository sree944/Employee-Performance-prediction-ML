from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas

app=Flask(__name__)
model = pickle.load(open('xgboost_model.pkl','rb'))

@app.route( "/" )
def about():
    return render_template( 'home.html')

@app.route ( "/about")
def home():
    return render_template('about.html')

@app.route ( "/predict")
def homel() :
    return render_template( 'predict.html')

@app.route ( "/submit")
def home2():
    return render_template( 'submit.html')

@app.route( "/pred", methods=['POST'])
def predict():
    try:
        quarter =request.form[ 'quarter']
        department =request.form[ 'department']
        day =request.form[ 'day']
        team =request.form[ 'team']
        targeted_productivity= request.form['targeted_productivity']
        smv=request.form[ 'smv']
        over_time= request.form[ 'Over_time']
        incentive= request.form[ 'Incentive']
        idle_time =request.form[ 'idle_time']
        idle_men =request.form[ 'idle_men']
        no_of_style_change =request.form[ 'style_change']
        no_of_workers=request.form['No. Worker']
        month =request.form[ 'month']
        wip = 1039.0
        missing_feature_2 = 0
        missing_feature_4 = 0
        missing_feature_5 = 0
        missing_feature_6 = 0
        missing_feature_3 = 0
        total= [[int(quarter), int(department), int(day), int(team),
        float (targeted_productivity),float(smv), int(over_time), int(incentive),
        float(idle_time), int (idle_men), int(no_of_style_change), float (no_of_workers), int(month),
        wip, missing_feature_2,
        missing_feature_3, missing_feature_4,
        missing_feature_5, missing_feature_6]]
        
        print(total)
        prediction = model.predict(total)
        print(prediction)
        if prediction <=0.3:
            text = 'The employee is averagely productive. '
        elif prediction >0.3 and prediction <=0.8:
            text = 'The employee is medium productive'
        else:
            text ='The employee is Highly productive'
        return render_template('submit.html',prediction_text=text)
    except Exception as e:
        return render_template('submit.html',prediction_text="An error occurred: Invalid Input")

if __name__ =="__main__":
    app.run(debug=True)
    
    