from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/') 
def home():
    return render_template('home.html') 

@app.route('/input') 
def tambahdata():
    return render_template('inputdata.html') 

@app.route('/list') 
def listdata():
    return render_template('listdata.html') 

@app.route('/login') 
def loginmhs():
    return render_template('loginmhs.html') 



if __name__ == "__main__":
    app.run(debug=True)