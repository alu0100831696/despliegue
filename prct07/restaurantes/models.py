from __future__ import unicode_literals

from django.db import models
import json
# Create your models here.
from django.conf import settings
test_ = settings.CLIENT.testadd
restaurants_ = settings.CLIENT.test.restaurants

class Restaurantes():
   
    def showRestaurants(self):
        restaurant=restaurants_.find({},{'name':1,'cuisine':1,'borough':1,'_id':0,'restaurant_id':1})
        data={'data':[]}
        for i in restaurant:
            data['data'].append(i)
        return json.dumps(data)
   
    def addRestaurant(self,data):
        name=data['nombre']
        cuisine=data['cocina']
        borough=data['ciudad']
        restaurant_id=restaurants_.find({},{'_id':0,'restaurant_id':1}).sort('restaurant_id',-1)
        restaurant_id=str(int(restaurant_id[0]['restaurant_id']) +1)
        restaurants_.insert({'name':name,'cuisine':cuisine,'borough':borough,'restaurant_id':restaurant_id})
        
        return restaurants_.find_one({'restaurant_id':str(restaurant_id)},{'_id':0})
    
    def delRestaurants(self,id):
        
        restaurants_.remove({'restaurant_id':id})
    
    def modifyRestaurant(self,data):
        restaurant_id=data['id_restaurante']
        name=data['nombre']
        borough=data['ciudad']
        cuisine=data['cocina']
        restaurants_.update_one({'restaurant_id': restaurant_id},{'$set':{'name':name,'cuisine':cuisine,'borough':borough}})
        
        return restaurants_.find_one({'restaurant_id': restaurant_id},{'name':1,'cuisine':1,'borough':1,'_id':0,'restaurant_id':1})