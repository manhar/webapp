from flask import Flask, redirect, url_for, request,render_template, make_response
from flask_wtf import Form
from wtforms import TextField
from werkzeug.utils import secure_filename
from forms   import ContactForm

app = Flask(__name__)

app.secret_key = 'development key'

'''
Set target path for upload files as well as max file size
'''

app.config['UPLOAD_FOLDER']="\\WDMyCloudEX2\ashmt"
#app.config['MAX_CONTENT_PATH']="1024"


@app.route('/upload')
def upload():
   return render_template('upload.html')
   
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
      if request.method == 'POST':
            user = request.form['nm']
      resp = make_response(render_template('readcookie.html'))
      resp.set_cookie('userID', user)
   
      return resp


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route('/login',methods = ['POST', 'GET'])
def login():
       
       if request.method == 'POST':
            user = request.form['nm']
            return redirect(url_for('success',name = user))
       else: 
            user = request.args.get('nm')
            return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)