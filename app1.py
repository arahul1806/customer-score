from flask import Flask, request, jsonify, render_template

import pickle

app = Flask(__name__)

@app.route('/')
def my_fun():
    print('Welcome To Customer Project')
    return render_template('home.html')

@app.route('/pred', methods = ['POST'])
def cust_pred():
    
    with open ('cust_prj.pkl', 'rb') as f:
        model_ml = pickle.load(f)
        
    data = request.form
    
    print('Data is >>', data)
    
    CustomerID = eval(data['CustomerID'])
    Genre = eval(data['Genre'])
    Age = eval(data['Age'])
    Annual_Income = eval(data['Annual_Income'])
    
    pred_score = model_ml.predict([[CustomerID, Genre, Age, Annual_Income]])
    
    return jsonify({'Result' : f'The predicted score of Customer is {pred_score}'})

if __name__ == '__main__':
    
    app.run(port = 1806, debug = True)
    
    