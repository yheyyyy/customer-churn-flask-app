from flask import Flask, request, render_template
from input_processing import validate, format_model_inputs
from model import Model

app = Flask(__name__)
# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        errors = validate(form_input)
        if len(errors) > 0:
            print(f"Errors: {errors}")
            return render_template('index.html', errors=errors)

        model_inputs = format_model_inputs(form_input)
        prediction = Model().predict(model_inputs)
        print(f"Prediction: {prediction}")
        return render_template('index.html', prediction=prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
