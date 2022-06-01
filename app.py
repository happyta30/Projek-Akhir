from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    return render_template('index.html')

@app.route('/masterpeta') 
def masterpeta():
    return render_template('masterpeta.html',menu='master', submenu='peta')

@app.route('/masterprediksi') 
def masterprediksi():
        # result = bla bla bla
    return render_template('masterprediksi.html',menu='master', submenu='prediksi')

@app.route('/masterprediksiusia') 
def masterprediksiusia():
    return render_template('masterprediksiusia.html',menu='master', submenu='prediksi')


if __name__ == "__main__":
    app.run()