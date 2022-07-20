from flask import  Flask, render_template,request
from backEnd import backEnd
from flask_cors import CORS, cross_origin

import json

app= Flask(__name__)
CORS(app)  # This makes the CORS feature cover all routes in the app
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})


@app.route('/')

def main():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
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
    
    return format(final_predicted)

if __name__ == "__main__":
    app.run(debug=False)
