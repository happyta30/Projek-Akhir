from flask import Flask, render_template, request
# import numpy as np
import joblib
import pandas as pd


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    return render_template('index.html')

@app.route('/masterpeta', methods=['GET','POST']) 
def masterpeta():
    if request.method == 'GET':
        print(request.form)
        return render_template('masterpeta.html')
    if request.method == 'POST':
        return render_template('masterpeta.html',menu='master', submenu='peta')


@app.route('/masterprediksi', methods=['GET','POST']) 
def masterprediksi():
    if request.method == 'GET':
        print(request.form)
        return render_template('masterprediksi.html')
    elif request.method == 'POST':
         # Get values through input bars
        model, std_scaler  = joblib.load("model_development/model_predict_home_price.pkl")
        income = request.form.get("income")
        age = request.form.get("age")
        bathroom = request.form.get("bathroom")
        bedroom = request.form.get("bedroom")
        population = request.form.get("population")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[income, age, bathroom, bedroom, population]], columns = ["income", "age", "bathroom", "bedroom", "population"])
        X_scaled = std_scaler.fit_transform(X)
        
        # Get prediction
        predict_price = round(model.predict(X_scaled)[0],2)      
    else:
        predict_price = ""    
    return render_template("masterprediksi.html", output = predict_price)


@app.route('/masterprediksiusia', methods=['GET','POST']) 
def masterprediksiusia():
    if request.method == 'GET':
        print(request.form)
        return render_template('masterprediksiusia.html')
    elif request.method == 'POST':
         # Get values through input bars
        model2 = joblib.load("model_development/model_predict_home_age.pkl")
        income = request.form.get("income")
        bathroom = request.form.get("bathroom")
        bedroom = request.form.get("bedroom")
        population = request.form.get("population")
        price = request.form.get("price")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[income, bathroom, bedroom, population, price]], columns = ["income", "bathroom", "bedroom", "population", "price"])
        
        # Get prediction
        predict_age = round(model2.predict(X)[0])      
    else:
        predict_age = ""   
    return render_template("masterprediksiusia.html", output_age = predict_age)


if __name__ == "__main__":
    app.run()