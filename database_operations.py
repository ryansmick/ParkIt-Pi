import json
import http.client
import urllib.parse
import ssl
import databaseconfig

class Parse:
    def __init__(self, app_id, api_key, parse_server):
        self.APPLICATION_ID = app_id
        self.REST_API_KEY = api_key
        self.PARSE_SERVER = parse_server

    def create(self, class_name, data):
        connection = http.client.HTTPSConnection(self.PARSE_SERVER, 443, context=ssl._create_unverified_context())
        connection.connect()
        connection.request('POST', '/classes/'+class_name, json.dumps(data), {
               "X-Parse-Application-Id": self.APPLICATION_ID,
               "X-Parse-REST-API-Key": self.REST_API_KEY,
               "Content-Type": "application/json"
             })
        results = json.loads(connection.getresponse().read().decode('utf-8'))
        print (results)   # Should be 201 Created

    def retrieve(self, class_name, object_id):
        connection = http.client.HTTPSConnection(self.PARSE_SERVER, 443, context=ssl._create_unverified_context())
        connection.connect()
        connection.request('GET', '/classes/'+class_name+'/'+object_id, '', {
               "X-Parse-Application-Id": self.APPLICATION_ID,
               "X-Parse-REST-API-Key": self.REST_API_KEY,
             })
        results = json.loads(connection.getresponse().read().decode('utf-8'))
        print (results)

    def update(self, class_name, object_id, data):
        connection = http.client.HTTPSConnection(self.PARSE_SERVER, 443, context=ssl._create_unverified_context())
        connection.connect()
        connection.request('PUT', '/classes/'+class_name+'/'+object_id, json.dumps(data), {
               "X-Parse-Application-Id": self.APPLICATION_ID,
               "X-Parse-REST-API-Key": self.REST_API_KEY,
               "Content-Type": "application/json"
             })
        results = json.loads(connection.getresponse().read().decode('utf-8'))
        print (results)

    def delete(self, class_name, object_id):
        connection = http.client.HTTPSConnection(self.PARSE_SERVER, 443, context=ssl._create_unverified_context())
        connection.connect()
        connection.request('DELETE', '/classes/'+class_name+'/'+object_id, '', {
               "X-Parse-Application-Id": self.APPLICATION_ID,
               "X-Parse-REST-API-Key": self.REST_API_KEY,
             })
        results = json.loads(connection.getresponse().read().decode('utf-8'))
        print (results)

    def find_unoccupied_parking_lot(self):
        connection = http.client.HTTPSConnection(self.PARSE_SERVER, 443, context=ssl._create_unverified_context())
        params = urllib.parse.urlencode({"where":json.dumps({
               "post": {
                 "$inQuery": {
                   "where": {
                     "is_occupied": False,
                     "is_active": True
                   },
                   "className": "parking_lot"
                 }
               }
             })})
        connection.connect()
        connection.request('GET', '/classes/parking_space?%s' % params, '', {
               "X-Parse-Application-Id": self.APPLICATION_ID,
               "X-Parse-REST-API-Key": self.REST_API_KEY,
             })
        results = json.loads(connection.getresponse().read().decode('utf-8'))
        print (results)
