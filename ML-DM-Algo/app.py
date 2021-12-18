from flask_cors import CORS, cross_origin

import numpy as np
from flask import Flask, request
import joblib
import json 
import pandas as pd

app = Flask(__name__)
# load the model from disk
loaded_model = joblib.load('finalized_model.sav')
sc = joblib.load('normalisation.sav')

CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/predict_api',methods=['POST'])
@cross_origin()
def predict_api():
   
    '''
    # For direct API calls trought request
    # '''
    
    #Exctracting the request data
    
    request_data = request.get_json()
    Age = request_data['Age']
    Sex = request_data['Sex']
    ChestPainType = request_data['ChestPainType']  
    RestingBP = request_data['RestingBP'] 
    Cholesterol = request_data['Cholesterol']
    FastingBS = request_data['FastingBS']
    RestingECG = request_data['RestingECG']
    MaxHR = request_data['MaxHR']
    ExerciseAngina = request_data['ExerciseAngina']
    Oldpeak = request_data['Oldpeak']
    ST_Slope = request_data['ST_Slope']
    
    #Creating an empty Test vector
    input_data = np.zeros((15,1))
    
    #Filling the test vector with test data 
    #Defining the AGE 
    input_data[7] = Age 
    
    #Defining the Sex 

    if Sex== "Male" :
        input_data[8] = 1 
    if Sex== "Female" :
        input_data[8] = 0
        
     #Defining the RestingBP
     
    input_data[9] = RestingBP

    #Defining the Cholesterol
    
    input_data[10] = Cholesterol
    
    #Defining the FastingBS
    
    input_data[11] = FastingBS
    
    #Defining the MaxHR
    
    input_data[12] = MaxHR 
    
    #Defining the ExerciseAngina
    
    
    if ExerciseAngina== "N" :
        input_data[13] = 0
    else:
        input_data[13] = 1
    

    
    #Defining the Oldpeak
    
    input_data[14] = Oldpeak
    
    #Defining the ChestPainType
    
    if ChestPainType=="ATA" :
        input_data[4] = 0
        input_data[5] = 1
        input_data[6] = 0

    if ChestPainType=="NAP" :
        input_data[4] = 0
        input_data[5] = 0
        input_data[6] = 1
    if ChestPainType=="TA" :
        input_data[4] = 0
        input_data[5] = 0
        input_data[6] = 0

    if ChestPainType=="ASY" : 
        input_data[4] = 1
        input_data[5] = 0
        input_data[6] = 0

    #Defining the RestingECG
        
    if RestingECG=="Normal" :
            input_data[2] = 0
            input_data[3] = 1
           

    if RestingECG=="ST" :
            input_data[2] = 0
            input_data[3] = 0
      

    if RestingECG=="LVH" : 
            input_data[2] = 1
            input_data[3] = 0
            
     #Defining the ST_Slope
    if ST_Slope=="Up" :
             input_data[0] = 0
             input_data[1] = 0

    if ST_Slope=="Flat" :
             input_data[0] = 0
             input_data[1] = 1

    if ST_Slope=="Down" :
             input_data[0] = 1
             input_data[1] = 0
             
    #Scaling and Testing the vector           
             
    input_data=input_data.transpose()
    input_data = sc.transform(input_data)
    pred=loaded_model.predict([input_data])
   

    result = {"result" : str(pred[0][0]) }
    json_dump = json.dumps(result)
    
   
    return json_dump



   

if __name__ == "__main__":
    app.run(debug=True)

   