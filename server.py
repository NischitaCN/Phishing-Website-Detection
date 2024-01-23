from flask import Flask, render_template, request
import sys
import subprocess
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        # dec = subprocess.check_output([sys.executable, "test.py", url])       
        p = subprocess.Popen("python test.py "+url, stdout=subprocess.PIPE, shell=True)
        dec, err = p.communicate()  
        return dec
    else:
        return("")

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)