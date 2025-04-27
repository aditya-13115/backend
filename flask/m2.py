from flask import Flask,render_template
#WSGI APPLICATION
app=Flask(__name__)
'''
    it will create an instance of flask,
    which will be your WSGI application.
'''

@app.route("/")
def welcome():
    return "<html><h1>Welcome to Flask Course.</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__=="__main__":
    app.run(debug=True)