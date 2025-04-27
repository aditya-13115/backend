#jinja template & variable rule 
from flask import Flask,render_template,request , redirect,url_for
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



@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method=='POST':
        name = request.form['name']
        mail = request.form['email']
        message = request.form['message']
        return f"Hello {name}!!!<br> your mail id is: {mail}<br> YOur message: {message}"
    return render_template('form.html')

'''
#variable rule
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is " +score 
    #by default the value passed above is a str value.
    #@app.route('/success/<int:score>') this is saying we only accept the value as an int, for this you will have to type cast while concating.
    # like return "The marks you got is " +str(score) 
    '''


@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res="pass"
    else:
        res="fail"
    
    return render_template('result.html',results=res,score=score)


'''
    Jinja2 template engine
    ways to get the data:

    {{ }} : expression to print output in html
    {%...%} : conditions, for and while loops
    {#.....#} : this is for comments
'''
@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score>=50:
        res="pass"
    else:
        res="fail"
    
    exp = {'score':score,'res':res}
    
    return render_template('result1.html',results=exp)


 #now using if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('results2.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submit2',methods=['POST','GET'])
def submit2():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
        return redirect(url_for('successres',score=total_score))

    return render_template('getresult.html')




if __name__=="__main__":
    app.run(debug=True)