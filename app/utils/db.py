# Libraries
import os
import pprint
import datetime

# Imports
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
from urllib.parse import quote_plus
from bson.objectid import ObjectId

max_stage = 5


# Functions for interacting with MongoDB
def init_db():
    # Load .env variables
    load_dotenv(find_dotenv())

    # Variables
    username = os.getenv('MONGODB_UID')
    cluster = os.getenv('MONGODB_CLUSTER_NAME')
    authSource = os.getenv('MONGODB_AUTH')
    password = quote_plus(os.getenv('MONGODB_PWD'))

    # URI string
    uri = username + ':' + password + '@' + cluster + authSource

    # Initialize MongoDB client
    client = MongoClient(uri)

    # Connect to database
    users_db = client.test

    # Define your collections
    # return users_db.users
    return users_db.test

# Find existing user in database
def find_user(user_email):

    users_collection = init_db()
    users = users_collection.find()

    for user in users:
        # Assign email
        email = user.get("email")

        # Compare email
        if email == user_email:
            return user.get("_id")
  
    return False


# Stage 0: Basic Info

# Insert user basic information
def insert_info(responses):
    users_collection = init_db()

    # Check if user already exists
    if find_user(responses["email"]):
        print("User already exists!")
        return (-1)
    
    # Assign info otherwise
    # data = {
    #     "email": responses["user_email"],
    #     "stage": 0,
    #     "firstName" : responses["firstName"],
    #     "lastName" : responses["lastName"],
    #     "uf_id" : responses["uf_id"],
    #     "classSchool" : responses["classSchool"],
    # }

    # Insert a new user into the database
    result = users_collection.insert_one(responses)
    print("User successfully added!")
    return result.inserted_id


# Stage 1: Agreement
def get_stage(user_id):
    users_collection = init_db()

    users = users_collection.find()

    for user in users:

        curr_uid = user.get("_id")

        # Compare email
        if curr_uid == user_id:
            return user.get("stage")
  
    return False


def update_stage(user_id, new_stage):
    users_collection = init_db()

    if new_stage > max_stage:
        print("Invalid update")
        return

    if get_stage(user_id) != (new_stage - 1):
        print("Invalid update")
        return
   
    query = {"_id": user_id}
    # Add data to database if it does not exist
    update = {
        "$set": {
            "stage": new_stage,
        }
    }
    result = users_collection.update_one(query, update)

    if result:
        print("success!")
        #print(result)
    else:
        print("failed!")

def user_agree(user_id):
    update_stage(user_id, 1)

# Stage 2: Demographics
def insert_demographics(responses):
    return

# Stage 3: Pre-Survey
def insert_presurvey(responses):
    return

# Stage 4: Main Survey
    # Instructions page when reloading
    # One question at a time

def insert_user_response(responses):

    _id = find_user(responses["email"])

    # Check if user already exist in db
    if (_id == -1):
        print("User already exist!")
        return

    # users_collection = init_db()
    # from bson.objectid import ObjectId
   
    # query = {"_id": _id}
    # # Add data to database if it does not exist
    # update = {
    #     "$set": {
    #         "uf_id": responses["uf_id"],
    #         "question_order": responses["question_order"],
    #         "answers": responses["answers"],
    #         "pre_survey_answers": responses["pre_survey_answers"],
    #         "post_survey_answers": responses["post_survey_answers"],
    #         "final_survey_answers": responses["final_survey_answers"],
    #         "chat_history": responses["chat_history"],
    #         "firstName" : responses["firstName"],
    #         "lastName" : responses["lastName"],
    #         "classSchool" : responses["classSchool"],
    #         "demographics" : responses["demographics"],
    #         "timestamp" : datetime.datetime.now(),
    #         "times" : responses["times"],
    #     }
    # }
    # result = users_collection.update_one(query, update)

    # if result:
    #     print("success!")
    # else:
    #     print("failed!")

# Add more functions as needed

# Stage 5: Final Survey

def update_user(user_email, updated_data):
    users_collection = init_db()
    # Update user data by email
    return users_collection.update_one({"_id": user_email}, {"$set": updated_data})

def delete_user(user_email):
    users_collection = init_db()
    # Delete a user by email
    return users_collection.delete_one({"_id": user_email})


# Main Tests
email = "a.person@ufl.edu"
firstName = "A"
lastName = "Person"
uf_id = 12345678
classSchool = "Class 1234"

user_id = ObjectId("687848a0e23ce4838ca2cd96")
# Create an empty dictionary to hold all the data
combined_data = {}

# Add each data element to the dictionary
combined_data["email"] = email
combined_data["uf_id"] = uf_id
combined_data["firstName"] = firstName
combined_data["lastName"] = lastName
combined_data["classSchool"] = classSchool
combined_data["stage"] = 0


# combined_data["question_order"] = ""
# combined_data["answers"] = ""
# combined_data["pre_survey_answers"] = ""
# combined_data["post_survey_answers"] = ""
# combined_data["final_survey_answers"] = ""
# combined_data["chat_history"] = ""
# combined_data["demographics"] = ""
# combined_data["times"] = ""



print(insert_info(combined_data))
#update_stage(user_id, 5)
#print(get_stage(user_id))
#print(type(user_id))
#print(type(find_user(email)))