from flask import Flask, render_template, request, jsonify
import joblib  
import re 
import pickle
app = Flask(__name__)

model = pickle.load(open('random_forest_model.pkl','rb'))

def is_valid_url(url):
    regex = re.compile(
        r'^(http|https|ftp)://[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')
    return re.match(regex, url)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        if is_valid_url(url):
            prediction = model.predict([url])

            return render_template('index.html', prediction=prediction)
        else:
            return render_template('index.html', error='Invalid URL')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
