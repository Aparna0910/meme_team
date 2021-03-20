from flask import Flask,request, render_template, Response, jsonify,redirect,url_for,session
import base64
import keras
from keras.models import load_model
import re
from final_prediction import *
import numpy as np

scores=[]
users=[]
loginattempts=[]


app = Flask(__name__)
app.secret_key = 'your secret key'



@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    """This function serves the login page and accepts form responses"""
    msg = ''
    firstmsg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        k=-1
        for d in users:
            if d['username'] == username and d['password'] == password :
                k=users.index(d)
        if k>=0:
            session['loggedin'] = True
            session['id'] = k
            session['username'] = users[k]['username']
            msg = 'Hey'+' '+username+' '+'!'
            if users[k]['games']==0 :
                firstmsg= 'Click on Proceed To Game to play your first Game'
            return render_template('index.html', msg=msg,firstmsg=firstmsg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/home',endpoint= 'home')
def get_to_home():
    return render_template('index.html')

@app.route('/logout')
def logout():
    """Logout function"""
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    print(session)
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    """Registration function"""
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form \
            and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if any(d['username'] == username and d['email'] == email for d in users):
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        elif not ((any(x.isupper() for x in password) and any(x.islower() for x in password)
                   and any(x.isdigit() for x in password) and len(password) >= 12)):
            msg = 'Password must contain atleast one uppercase character' \
                  ', one lower case character, one digit and atleast 12 characters'
        else:
            user={'username':username,'password':password,'email':email,'previousscore':0,'totalscore':0,'games':0}
            print(user)
            users.append(user)
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)




@app.route('/getphoto',endpoint='getphoto',methods=['GET','POST'])
def getimage():
    msg=""
    if request.method=='POST':
       msg="Succesful!"
       print(msg)
       img=request.form["base64image"]
       print (img)
       print(type(img))
       print(type(base64.b64decode(img)))
       img = img.replace("data:image/jpeg;base64,","")
       decodeit = open('new.jpeg', 'wb')
       decodeit.write(base64.b64decode((img)))
       decodeit.close()
       if msg=="Succesful!":
            score=get_prediction('static/18c218328ebc77db0bfea4027648adee.jpg','new.jpeg')
            scores.append(score.item())
            print(type(score))
            print(score)
            print(score.item())
            print(scores)
            print("round 1")
            #if (score!= None):
            #    print("Moving to next round")
            #    msg="done"

       #return render_template('round2.html')

    return render_template('round1.html')

@app.route('/getphoto2', endpoint='getphoto2',methods=['GET','POST'])
def getimage2():
    msg=""
    if request.method=='POST':
       msg="Succesful!"
       print(msg)
       img=request.form["base64image"]
       print (img)
       print(type(img))
       print(type(base64.b64decode(img)))
       img = img.replace("data:image/jpeg;base64,","")
       decodeit = open('new.jpeg', 'wb')
       decodeit.write(base64.b64decode((img)))
       decodeit.close()
       if msg=="Succesful!":
        score=get_prediction('static/maxresdefault.jpg','new.jpeg')
        scores.append(score.item())
        print(type(score))
        print(score)
        print(score.item())
        print(scores)
        print("round 2")
        #return render_template('round3.html')
    return render_template('round2.html')

@app.route('/getphoto3',endpoint='getphoto3',methods=['GET','POST'])
def getimage3():
    msg=""
    if request.method=='POST':
       msg="Succesful!"
       print(msg)
       img=request.form["base64image"]
       print (img)
       print(type(img))
       print(type(base64.b64decode(img)))
       img = img.replace("data:image/jpeg;base64,","")
       decodeit = open('new.jpeg', 'wb')
       decodeit.write(base64.b64decode((img)))
       decodeit.close()
       if msg=="Succesful!":
        score=get_prediction('static/Culture-Success-Meme-Kid.jpg','new.jpeg')
        scores.append(score.item())
        print(type(score))
        print(score)
        print(score.item())
        print(scores)
        print("round 3")
        #return render_template('round4.html')
    return render_template('round3.html')

@app.route('/getphoto4',endpoint='getphoto4',methods=['GET','POST'])
def getimage4():
    msg=""
    if request.method=='POST':
       msg="Succesful!"
       print(msg)
       img=request.form["base64image"]
       print (img)
       print(type(img))
       print(type(base64.b64decode(img)))
       img = img.replace("data:image/jpeg;base64,","")
       decodeit = open('new.jpeg', 'wb')
       decodeit.write(base64.b64decode((img)))
       decodeit.close()
       if msg=="Succesful!":
        score=get_prediction('static/Confused.jpeg','new.jpeg')
        scores.append(score.item())
        print(type(score))
        print(score)
        print(score.item())
        print(scores)
        print("round 4")
        #return render_template('round4.html')
    return render_template('round4.html')

@app.route('/results',endpoint='results')
def gen_result():
    result=0
    print("The scores are:",scores)
    for i in scores:
        result=result + i
    print(session['id'])
    users[session['id']]['previousscore']=result
    users[session['id']]['totalscore'] = users[session['id']]['totalscore'] + result
    users[session['id']]['games'] = users[session['id']]['games']+1
    scores.clear()
    print(users)
    return render_template('final.html',result = result)




if __name__ == '__main__':
    app.run(debug=True)