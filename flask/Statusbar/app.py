from flask import Flask, request, jsonify
from uuid import uuid1,uuid4
import os, json, pytz
from datetime import date,datetime,timedelta
import pandas as pd

db={}
db_filename="db.json"

#create the object of the flask
app=Flask(__name__)

#check wheather db.json exists in the directory or not
if os.path.exists(db_filename):
    with open(db_filename,'r') as f:
        db=json.load(f)
else:
    db={
        
    }
    with open(db_filename,'w+') as f:
        json.dump(db,f,indent=4)

#signup function
@app.route("/signup",methods=['POST'])
def signup():
    if request.method=='POST':
        name=request.form['name']
        username=request.form['username']
        password=request.form['password']
        status=''

        user_dict={
            'name':name,
            'password':password,
            'username':username,
            'status':status
        }
        
        if username not in db:
            db[username]=user_dict

            with open(db_filename,'r+') as f:
                f.seek(0)
                json.dump(db,f,indent=4)
            return "User added successfully"
        else:
            return "User already exists"
    else:
        return "Method not allowed"

#login user
@app.route("/login",methods=['POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username in db:
            if db[username]['password']==password:
                response={
                    "message":"Login Successful",
                    "Logged in as":username
                }
                
                return response
            else:
                return "Invalid username or password"

#post status
@app.route('/add_status',methods=['POST'])
def add_status():
    username=request.form['username']
    status=request.form['status']

    if username in db:
        if db[username]['status']=='':
            db[username]['status']=status
            with open(db_filename,'r+') as f:
                json.dump(db,f,indent=4)
            return 'status posted'
        else:
            return 'status present already please modify'
    else:
        return 'please signup'

#update status
@app.route('/update_status', methods=['PUT'])
def update_status():
    username=request.form['username']
    status=request.form('status')
    if db[username]['status']!='':
        db[username]['status']=status
        with open(db_filename, 'r+') as f:
            json.dump(db, f, indent=4 )
        return 'status updated succesfully'
    else:
        return 'status not present, please post'



#delete status

#get status

#run the flask
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)