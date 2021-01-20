from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
#import MySQLdb
#import pymongo
#import mysql.connector
#import mysql.connector as sql
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('model1.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Pclass = int(request.form['Pclass'])
        Age= float(request.form['Age'])
        SibSp=int(request.form['SibSp'])
        Parch=int(request.form['Parch'])
        Fare=float(request.form['Fare'])
        Sex=request.form['Sex']
        if(Sex=='Male'):
            Sex_Male=1
        else:
            Sex_Male=0

        Embarked=request.form['Embarked']
        if(Embarked == 'S'):
            Embarked_S = 1
            Embarked_Q = 0
        elif(Embarked == 'Q'):
            Embarked_S = 0
            Embarked_Q = 1
        else:
            Embarked_S = 0
            Embarked_Q = 0
        prediction=model.predict([[Pclass,Age,SibSp,Parch,Fare,Sex_Male,Embarked_Q,Embarked_S]])
        output=int(prediction)
        

        #import MySQLdb
        #con=MySQLdb.connect('localhost','root','rajathvirat','students')
        #cursor=con.cursor()
        #sql='insert into titanic(pclass,age,sibsp,parch,fare,sex,embarked,result) values (%s,%s,%s,%s,%s,%s,%s,%s)'
        #val=[Pclass,Age,SibSp,Parch,Fare,Sex,Embarked,output]
        #cursor.execute(sql,val)
        #con.commit()

#--------------using mongo db--------------------------

        #import pymongo
        #client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        #mydb=client['titanic']
        #collection=mydb.titanicdata
        #record={"pclass":Pclass,"age":Age,"sibsp":SibSp,"parch":Parch,"fare":Fare,"sex":Sex,"embarked":Embarked,"result":output}
        #collection.insert_one(record)
        
        
        if output==0:
            return render_template('index.html',prediction_text="This person Not Survived in Disaster",color="red")
        else:
            return render_template('index.html',prediction_text="This person Survived in Disaster",color="green")

        

    else:
        return render_template('index.html')

#@app.route("/dead", methods=['POST'])
#def dead():
    #if request.method=='POST':




        #import MySQLdb
       # con=MySQLdb.connect(host='localhost',user='root',password='rajathvirat',database='students')
       # cursor=con.cursor()
        #cursor.execute('Select * from titanic where result=0')
        #dead=cursor.fetchall()
        #print(type(dead))
        #con.close()

#---------------------using mongo db---------------------------
        #client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        #mydb=client['titanic']
        #collection=mydb.titanicdata
        #dead=collection.find({"result":"0"})

    #return render_template('ans.html',output=dead)

#@app.route("/survived", methods=['POST'])
#def survived():
    #if request.method=='POST':

        # 2 ways of coonecting to mysql work bench

        #con=MySQLdb.connect(host='localhost',user='root',password='rajathvirat',database='students')
        con=sql.connect(host='localhost',user='root',password='rajathvirat',database='students')

        #con=mysql.connector.connect(host='localhost',user='root',password='rajathvirat',database='students') 
        #cursor=con.cursor()
        #cursor.execute('Select * from titanic where result=1')
        #sur=cursor.fetchall()
        #print(sur)
        #con.close()

#---------------------------------using mongo db----------------------------
        #client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        #mydb=client['titanic']
        #collection=mydb.titanicdata
        #sur=collection.find({"result":1})
        #print(sur)
        

    #return render_template('ans.html',output=sur)            
           

if __name__=="__main__":
    app.run(debug=True)

