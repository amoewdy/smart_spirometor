

import pyrebase
import json
import time

config = {
    'apiKey': "AIzaSyAc6xANvMdWV2TTJA_Z0Bnb26JYxySKSS8",
    'authDomain': "smart-spirometer.firebaseapp.com",
    'databaseURL': "https://smart-spirometer.firebaseio.com",
    'projectId': "smart-spirometer",
    'storageBucket': "smart-spirometer.appspot.com",
    'messagingSenderId': "846679117231",
    'serviceAccount': "smart-spirometer-firebase-adminsdk-ntwx4-c55ff7cd43.json"
    }



# Initialize Firebase
firebase = pyrebase.initialize_app(config)


db = firebase.database()


def readData():
    pass


def uploadData():
    count = 1
    timestamp = time.time()
    data_index = {"name": "Amy",'timestamp':timestamp,'achieve_ratio':1/2}
    data_user = {'timestamp':timestamp,'breath':[1,2,3,4,5],'label':1}
    # db.child("page_index").child(count).update(data_index)
    # db.child("page_user").child(count).update(data_user)
    db.child("page_index").child(count+1).set(data_index)
    db.child("page_user").child(count+1).set(data_user)


if __name__ == '__main__':
    uploadData()

