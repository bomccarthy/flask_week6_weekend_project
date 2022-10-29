from xml.sax.handler import all_properties
import requests as req

def getProd(id):
    url = f'https://fakestoreapi.com/products/{id}'
    resp = req.get(url)                 # requested URL for product by number
    if resp.ok:
        dct = resp.json()
        prod_dict = {'id': dct['id'],    # forms dictionary to be returned
            'title': dct['title'],
            'price': dct['price'],
            'description': dct['description'],
            'category': dct['category'],
            'image': dct['image'],
            'rating': dct['rating']['rate'],
            'count': dct['rating']['count']
            }
        return prod_dict
    else:
        return 'I don\'t know that Product. Is that the right Product ID?'

def getAllProdByID():
    r = req.get('https://fakestoreapi.com/products')
    dict = r.json()
    allProdDictByID = {}
    for id in dict:
        allProdDictByID[id['id']] = id['title']
    return allProdDictByID

def getAllProdByCat():
    r = req.get('https://fakestoreapi.com/products')
    dict = r.json()
    allProdDictByCat = {}
    for cat in dict:
        allProdDictByCat[cat['id']] = cat['category']
    return allProdDictByCat
