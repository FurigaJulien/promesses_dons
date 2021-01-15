from flask import Flask, render_template, request, url_for, flash, redirect
import pymongo
import time 
from datetime import datetime
import random
import calendar


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefgh'


client = pymongo.MongoClient("mongodb+srv://JulienFuriga:5792dbb58c@katacluster.ldjhk.mongodb.net/brief?retryWrites=true&w=majority")
db = client.brief.dons



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/don', methods=('GET', 'POST'))
def don():
    if request.method == 'POST':
        nom = request.form['inputName']
        prenom = request.form['inputPrenom']
        mail = request.form['inputAddressMail']
        adress = request.form['inputAddress']
        city = request.form['inputCity']
        state = request.form['inputState']
        zipCode = request.form['inputZip']
        montant = int(request.form['inputMontant'])
        date= calendar.timegm(time.gmtime())
        date=datetime.fromtimestamp(date)
        donnateur = {'Name' : nom, 'Prenom' : prenom,"Mail":mail,"Adress":adress,"City":city,"State":state,"Zip":zipCode,"Montant":montant,"Date":date}
        db.insert_one(donnateur)

        return redirect(url_for('index'))
    return render_template('don.html')

@app.route('/promesses')
def promesses():
    posts=list(db.find({},{'Prenom':1,'Name':1,'City':1,'Montant':1,"_id":0}).sort('Montant',-1))[0:10]
    print(posts)

    return render_template('promesses.html', posts=posts[0:10])

