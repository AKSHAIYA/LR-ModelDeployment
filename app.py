import pandas as pd
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("pipe.pkl")

@app.route('/')
def hi():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print(request.form.values())
    inp = [i for i in request.form.values()]
    
    try:
        if not isinstance(float(inp[2]), float):
            mess = "Please enter valid input"
            return render_template('index.html', prediction = mess)
    except:
        mess = "Please enter valid input"
        return render_template('index.html', prediction = mess)

    test = {"Item_Type":inp[0],"Outlet_Type":inp[1],"Item_MRP":float(inp[2])}
    print(test)
    test_df = pd.DataFrame([test])
    print(test_df)
    res = model.predict(test_df)
    print(res[0])
    #return str(res[0])
    if isinstance(res[0], float):
        mess = "Sale Price of the item is {} ".format(str(res[0]))
    else:
        mess = "Please enter valid input"
    return render_template('index.html', prediction = mess)


if __name__ == "__main__":
    app.run(port = 4000, debug = True)