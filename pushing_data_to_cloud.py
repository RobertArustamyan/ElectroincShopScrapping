import os
import json
from firebase_admin import credentials, db, initialize_app
from dotenv import load_dotenv
load_dotenv()

cred = credentials.Certificate("electro-shops-arm-firebase-adminsdk-fznxq-e286074b55.json")
initialize_app(cred, {
    'databaseURL': os.environ.get('DataServerLink')
})

def push_data_from_json(json_file_path, key):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    ref = db.reference('/')
    ref.child(key).set(data)
    print(f"Data from '{json_file_path}' pushed to the database with key '{key}' successfully!")

json_files_with_keys = [
    {"path": "Data/3DPlanet.json", "key": "3d_planet_data"},
    {"path": "Data/MobileCenterAllData.json", "key": "mobile_center_data"},
    {"path": "Data/RedStoreAllData.json", "key": "red_store_data"},
    {"path": "Data/ZigZagAllData.json", "key": "zig_zag_data"}
]

for file_info in json_files_with_keys:
    push_data_from_json(file_info["path"], file_info["key"])
