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


def readData(page, count):
    users = db.child(page).child(count).get()
    values = [x.val() for x in users.each()]
    keys = [x.key() for x in users.each()]
    json_data = {keys[i]: values[i] for i in range(len(values))}
    return json.dumps(json_data)


def uploadData():
    # need to be adjusted based on needed data structure
    count = 1
    # 'count' can be a global parameter
    timestamp = time.time()
    data_index = {"name": "Amy",'timestamp':timestamp,'achieve_ratio':1/2}
    data_user = {'timestamp':timestamp,'breath':[1,2,3,4,5],'label':1}
    # db.child("page_index").child(count).update(data_index)
    # db.child("page_user").child(count).update(data_user)
    db.child("page_index").child(count+1).set(data_index)
    db.child("page_user").child(count+1).set(data_user)


if __name__ == '__main__':
    readData('page_user', 1)

