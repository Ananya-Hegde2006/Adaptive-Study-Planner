import firebase_admin
from firebase_admin import credentials, db

try:
    cred = credentials.Certificate("adaptivestudyplanner-firebase-adminsdk-fbsvc-749e8d705d.json")
    firebase_url = "https://adaptivestudyplanner-default-rtdb.asia-southeast1.firebasedatabase.app/"

    firebase_admin.initialize_app(cred, {
        'databaseURL': firebase_url
    })

    print("✅ Firebase connected successfully!")

except Exception as e:
    print("❌ Firebase connection failed!")
    print(e)
