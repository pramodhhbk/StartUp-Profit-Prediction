import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    feature1=[]
    
    features = [x for x in request.form.values()]
    
    
    if(features[0]=='New York'):
        var1=0.0
        var2=0.0
        var3=1.0
    elif(features[0]=='California'):
        var1=1.0
        var2=0.0
        var3=0.0
    else:
        var1=0.0
        var2=1.0
        var3=0.0
    
        
    features.insert(0,var1)
    features.insert(1,var2)
    features.insert(2,var3)
    features.pop(3)
    features=list(map(int,features))
    print(features)
    
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 3)

    return render_template('index.html', prediction_text='Profit Should Be Salary  $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)