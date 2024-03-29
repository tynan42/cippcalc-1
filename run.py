import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import formcheck
import cippcalc

app = Flask(__name__)
#app.config.from_object('config')

@app.route('/')
def start_html():
    design_condition = 'Fully Deteriorated'
    submitted_data={
        'design_condition':'Fully Deteriorated', 'location':'Highway'
        }
    return render_template('index.html',return_vars=submitted_data)

@app.route('/', methods=['GET', 'POST'])
def run_cippcalc():
    input = {}
    hard_error_msg = None
    soft_error_msg = None
    errors = formcheck.ErrorValidation(request.form)
    warnings = formcheck.WarningValidation(request.form)
    if request.method == 'POST' and errors.validate():
        for k in request.form.keys():
            input[k] = request.form[k]
        warnings.validate()
        soft_error_msg = warnings.errors
        if soft_error_msg:
            soft_errors = {}
            for j in soft_error_msg.keys():
                soft_errors[j] = request.form[j]
    else:
        warnings.validate()
        hard_error_msg = errors.errors
        for key, value in hard_error_msg.items():
            if 'Not a valid float value' in value:
                hard_error_msg[key] = ['Not a valid number.']
        soft_error_msg = warnings.errors
        
    if hard_error_msg is None:
        thickness, flow_change, submitted_data = cippcalc.LM_run(input)
        thickness = str(thickness)
        if flow_change == -100:
            flow_message = None
            soft_error_msg['flowwarn'] = ['Check design inputs, liner thickness is greater than pipe diameter.']
        elif flow_change > 0:
            flow_message = str(abs(round(flow_change)))+'% increase in flow capacity at 2/3 full'
        elif flow_change == 0:
            flow_message = 'No change in flow capacity at 2/3 full'
        else:
            flow_message = str(abs(round(flow_change)))+'% decrease in flow capacity at 2/3 full'
        return render_template('index.html', thickness=thickness, flow_change=flow_message, return_vars=submitted_data, warning=soft_error_msg, messages=soft_error_msg)
    else:
        submitted_data = request.form
        return render_template('index.html', thickness='Error', return_vars=submitted_data, error=hard_error_msg, warning=soft_error_msg, messages=soft_error_msg )

if __name__ == '__main__':
    #app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)