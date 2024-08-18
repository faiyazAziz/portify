import pyrebase

config = {
    "apiKey": "AIzaSyCoF5PNReaxKYCh82dqMev9CJURQoK8DXw",
    "authDomain": "fir-63517.firebaseapp.com",
    "projectId": "fir-63517",
    "storageBucket": "fir-63517.appspot.com",
    "messagingSenderId": "84354516481",
    "appId": "1:84354516481:web:a37e114b3b5edf3f87e200",
    "measurementId": "G-MNHYVGGWR8",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
