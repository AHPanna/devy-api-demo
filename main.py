#!/usr/bin/env python

##
#   Demo Purpose Usage, using a https api server todo some test to the front-end.
##


# data json format : which the rela server should send back
##
#   Details of data retrieved from
#
#
##
searchData = {  "id": "2145",
                "Items": {
                    "1": {
                        "id": "1",
                        "title": "IPhone 7 Plus cassé",
                        "nom": "reda",
                        "email": "reda@devy-france.fr",
                        "phone": "032488659",
                        "categories": "Telephonie",
                        "description": "Je cherche à réparer mon iPhone. L’écran de protection est cassé, batterie faibles besoin de changer la batterie, bluetooth HS et wifi 2.5 foncttionnel.",
                        "lieu": "Béthune, France",
                        "dateAjouter": "30/08/2020, 12:56",
                        "images": ["https://img2.leboncoin.fr/ad-large/3e4a21185615215abb3b88597534748e4ea9d705.jpg",
                                   "https://img0.leboncoin.fr/ad-large/0ccfe703df77eb8a89846fad1e7c8eaf87beb188.jpg",
                                   "https://img5.leboncoin.fr/ad-large/bfc58705bd5f2560217953824c8c3528c3cd5308.jpg"],
                    },
                    "2": {
                        "id": "2",
                        "title": "Ecran dell 23 pouces ne marche plus",
                        "nom": "Mehdidu75",
                        "email": "Mehdidu75@email.com",
                        "phone": "066569878",
                        "categories": "Informatique",
                        "description": "J'ai verser de l'eau sur mon ecran du coups, mon ecran chauffe beaucoups et apres 1h d'utilisation l'ecran devient jaune rouges et s'éteint, les pins du port vga sont cassé.",
                        "lieu": "Lille, France",
                        "dateAjouter": "15/05/2020, 15:00",
                        "images": ["https://img6.leboncoin.fr/ad-large/c6e92a4459272112f30a0ca693fe150f4d3180ef.jpg",
                                   "https://img6.leboncoin.fr/ad-large/79428d7dc8653953341544e960c98cdde016d181.jpg",
                                   "https://img7.leboncoin.fr/ad-large/301068eb4caf9c89c8c25cff3cee6e9648c98319.jpg"],
                    },
                    "3": {
                        "id": "3",
                        "title": "Frigo combiné Samsung Fuite de gaz.",
                        "nom": "DavidZax",
                        "email": "DavidZax@gmail.com",
                        "phone": "066588957",
                        "categories": "Electromenager",
                        "description": "Mon frigo samsung combiné, elle a une fuite de gaz, la partie congel ne fonctionne pas, pertes de froid, les tiroirs trop remplis ont formé des sillons dans l'appareil.",
                        "lieu": "Saint-Paul-en-Jarez, France",
                        "dateAjouter": "22/08/2020, 18:45",
                        "images": ["https://img5.leboncoin.fr/ad-large/c208ba1124b9fb407baadc283e60aac89247c804.jpg",
                                   "https://img1.leboncoin.fr/ad-large/bced2dd7455e22a153956b3228a5888fdab166b2.jpg",
                                   "https://img3.leboncoin.fr/ad-large/b0c0cafe3a9ac5d559656f16784208dd0cea49cd.jpg"],
                    },
                },
                "Response": "true",
            }


# Use flask 
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



# debug purpose
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

# this will return only item info : json object
@app.route('/id/<uniqueItem>', methods=['GET', 'POST'])
def sendItem(uniqueItem):
    return "uniqueItem {}!".format(uniqueItem)


# this will return list of items info searched : json object
@app.route('/find/<listItems>', methods=['GET', 'POST'])
def findItem(listItems):
    return "listItems {}!".format(listItems)


@app.route('/index', methods=['GET', 'POST'])
@cross_origin()
def index():
    return jsonify(searchData)

@app.route('/cookies', methods=['GET', 'POST'])
@cross_origin()
def cookies():
    
    print(dir(request.cookies))
    print(type(request.cookies.values))
    #return request.cookies.get('token')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081')
