import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import tensorflow as tf

def mmscaler(x): # Avoid requiring us to import sklearn, since we only need it for minmax scaling
    x_scaled = (x-np.amin(x))/(np.amax(x)-np.amin(x))
    return x_scaled

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = tf.keras.models.load_model('predictor.h5')

def getLogsum(x0,x1,x2,x3,x4,x5):
    # Verify all inputs are correct, if not, it probably means a field enterred was empty
    if type(x0)==np.float64 and type(x1)==np.float64 and type(x2)==np.float64 and type(x3)==np.float64 and type(x4)==np.float64 and type(x5)==np.float64:
        xs = [x0,x1,x2,x3,x4,x5]
        logsum = 0
        for x in xs:
            if x>0:
                logsum += np.log1p(x)
            elif x<0:
                logsum += -(np.log1p(-x))
            else:
                logsum += 0
        return logsum
    else:
        print('Error in getting logsum, one of the elements is either empty, or not a float. Returning -1 to frontend.')
        return jsonify(-1)

@app.route('/', methods=['GET'])
@cross_origin()
def pred():
    if request.method=='GET':
        try:
            fields = ['limitbal','gender','education','marriage','age',
                'pay0','pay1','pay2','pay3','pay4','pay5',
                'billamt1','billamt2','billamt3','billamt4','billamt5','billamt6',
                'payamt1','payamt2','payamt3','payamt4','payamt5','payamt6']
            c=0
            x=np.zeros((1,27))
            x[0,0]=30001
            for idx,field in enumerate(fields): # Build the input argument using index c for each column of the field
                c+=1
                if c==12:
                    paylogsum = getLogsum(x[0,6],x[0,7],x[0,8],x[0,9],x[0,10],x[0,11]) # Get logsum (feature engineering on the fly)
                    x[0,c] = paylogsum
                    c+=1
                if c==19:
                    billlogsum = getLogsum(x[0,13],x[0,14],x[0,15],x[0,16],x[0,17],x[0,18])
                    x[0,c] = billlogsum
                    c+=1
                if request.args.get(field)=='': # Flask requests the field input by user in the frontend, if it's empty, return -1
                    print(f'pred(): Detected missing field: {field} , returning -1 to frontend.') # And handle the display on the frontend.
                    return jsonify(-1)
                else:
                    x[0,c]=float(request.args.get(field)) # Otherwise transform the input field to a float and use it for prediction
                if c==25: ### SPECIAL CASE: c never gets to 26 since we're iterating through fields, so handle payamtlogsum here!!! Must be after the if,else statement
                    payamtlogsum = getLogsum(x[0,20],x[0,21],x[0,22],x[0,23],x[0,24],x[0,25])
                    x[0,26] = payamtlogsum
                    c+=1
            min_max_scaled = mmscaler(x)
            p = (model.predict(min_max_scaled.reshape(1,-1)))[0][0] * 100
            print(p)
            return jsonify(p)
        except RuntimeError as e:
            return ('Error occured during model prediction : '+e)
    else:
        return 'Error occured during prediction : Request method is not a GET method'

# # TODO Remove tests

@app.route('/test')
def test():
    return "This is a test"

@app.route('/testml')
def testml():
    x = np.random.randint(8, size=(1, 27))
    x[0,1] = 1
    x[0,2] = 1
    x[0,3] = 1
    x[0,4] = 1
    min_max_scaled = mmscaler(x)
    p = (model.predict(min_max_scaled.reshape(1,-1)))[0][0] * 100
    print(p)
    print(jsonify(p))
    return ("predicted"+str(p))

if __name__=="__main__":
    app.run(debug=True)