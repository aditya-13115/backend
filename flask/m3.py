# Get Post
from flask import Flask,render_template,request
#WSGI APPLICATION
app=Flask(__name__)
'''
    it will create an instance of flask,
    which will be your WSGI application.
'''

@app.route("/")
def welcome():
    return "<html><h1>Welcome to Flask Course.</h1></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

#now we will try post request
@app.route("/form", methods=["GET"])
def form():
    return render_template('form.html')

@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method=='POST':
        name = request.form['name']
        mail = request.form['email']
        message = request.form['message']
        return f"Hello {name}!!!<br> your mail id is: {mail}<br> YOur message: {message}"
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)