from flask import flask ,render_template,request
app =flask(__name__)
@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')
@app.route("/confirm",methods=['POST','GET'])
def register():
    if request.method=='POST':
        n=request.form.get('name')
        n=request.form.get('age')
        n=request.form.get('city')
        return render_template('confirm.html',name=n,age=a,city=c)
    if __name__==__name__:
        app.run(debug=True)