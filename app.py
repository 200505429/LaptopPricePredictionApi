from flask import  Flask, render_template,request
from backEnd import backEnd
from flask_cors import CORS, cross_origin
import json

app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
@cross_origin()
def main():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    screenSize = float( request.form['screenSize'])
    screenRes = int(request.form['ScreenRes'])
    Cpu = int(request.form['CPU'])
    RAM = int(request.form['RAM'])
    weight = float(request.form['Weight'])
    touchScreen = int(request.form['Touchscreen'])
    HDD = int(request.form['HDD'])
    SSD = int(request.form['SSD'])
    SSHD = int(request.form['SSHD'])
    FStorage = int(request.form['fStorage'])
    Type = int(request.form['Type'])
    Os = int(request.form['Os'])

    back = backEnd(screenSize, screenRes, Cpu, RAM, weight, touchScreen, HDD, SSD, SSHD, FStorage, Type, Os)
    final_predicted = (round(float(back.totalPredicted[0]),2))
    response.headers.add("Access-Control-Allow-Origin", "*")  
    response =  format(final_predicted)
    return response

if __name__ == "__main__":
    app.run(debug=True)