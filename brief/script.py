import random
import calendar
import time 
import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb+srv://JulienFuriga:5792dbb58c@katacluster.ldjhk.mongodb.net/brief?retryWrites=true&w=majority")
db = client.brief.dons




forname = ['Liam', 'Noah', 'Oliver', 'William', 'Elijah', 'James', 'Benjamin', 'Lucas', 'Mason', 'Ethan', 'Olivia', 'Emma',
         'Ava', 'Sophia', 'Isabella', 'Charlotte', 'Amelia', 'Mia', 'Harper', 'Evelyn', 'Abbey', 'Addison', 'Adal', 'Alex',
          'Ali', 'Thomas', 'Camille', 'Pereg', 'Baptiste', 'Jérémy', 'César', 'Paul', 'Pauline', 'Eva', 'Christelle', 'Patricia',
          'Julien', 'Céline', 'Gwendolyne', 'Coralie', 'Stéphanie', 'Brigitte', 'Laura', 'Clémentine', 'Clara', 'Capucine',
          'Morgane', 'Jason', 'Kevin', 'Bob', 'Théo', 'Léopold']

name=['Bokalli', 'Bonneau', 'Chaigneau', 'Cloatre', 'Furiga', 'Guillen', 'Hergoualch', 'Ibanni', 'Karfaoui', 'Le Berre',
 'Le Goff', 'Le Joncour', 'Le Moal', 'Maintier', 'Moulard', 'Petron', 'Rioual', 'Sabia', 'Verpoest',"Verdier","Costa",
 "Pinto", "Le Bazin","Violet","Drogosz","Dupont","Kermane","Le Meur","Dubois","Montiel","Stallone"]

cityList=['Brest','Rennes',"Paris","Bordeaux","Marseille",'Chateauroux',"Montelimar","Strasbourg","Lille","Nantes","Lyon","Mont de Marsan",
"Perpignan","Toulouse","Metz"]


for i in range(450):
    e=random.randrange(0,len(forname))
    f=random.randrange(0,len(name))
    g=random.randrange(0,len(cityList))
    nom = name[f]
    prenom = forname[e]
    mail = "test"
    adress = "test"
    city = cityList[g]
    state = "test"
    zipCode = "test"
    montant = random.randrange(0,100)
    date= calendar.timegm(time.gmtime())-(30000*i)
    date=datetime.fromtimestamp(date)
    donnateur = {'Name' : nom, 'Prenom' : prenom,"Mail":mail,"Adress":adress,"City":city,"State":state,"Zip":zipCode,"Montant":montant,"Date":date}
    db.insert_one(donnateur)
