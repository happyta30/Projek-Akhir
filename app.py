from flask import Flask, render_template, request
import numpy as np
import joblib


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    return render_template('index.html')

@app.route('/masterpeta') 
def masterpeta():
    return render_template('masterpeta.html',menu='master', submenu='peta')

@app.route('/masterprediksi') 
def masterprediksi():
    if request.method == 'GET':
        print(request.form)
        return render_template('masterprediksi.html')
    elif request.method == 'POST':
         # Get values through input bars
        model = joblib.load("../model_development/model_predict_home.pkl")
        income = request.form.get("height")
        age = request.form.get("age")
        bathroom = request.form.get("bathroom")
        bedroom = request.form.get("bedroom")
        population = request.form.get("population")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[income, age, bathroom, bedroom, population]], columns = ["income", "age", "bathroom", "bedroom", "population"])
        
        # Get prediction
        predict = model.predict(X)[0]
        
    else:
        predict = ""
        
    return render_template("masterprediksi.html", output = predict)
           
        
    #     print(dict(request.form))
    #     X_feature = dict(request.form).values()
    #     X_feature = np.array([float(x) for x in X_feature])
        
    #     X_feature = X_feature.reshape(1,-1) # satu baris unknown columns[1,2,3,4,]
    #     print(X_feature)
    #     result = model.predict(X_feature)
    #     # edit hasil disini
    #     # result = bla bla bla
    #     return render_template('masterprediksi.html', result=result )
    #      # prediction_text="The house should be sold for $ {}".format(output)
    # else:
    #     return "Unsupported Request Method"


@app.route('/masterprediksiusia') 
def masterprediksiusia():
    return render_template('masterprediksiusia.html',menu='master', submenu='prediksi')


if __name__ == "__main__":
    app.run()