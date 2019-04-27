import pymongo
from bson.objectid import ObjectId

#pymongo is a library to access mongodb server

client = pymongo.MongoClient("mongodb+srv://Ak4nksha:Ak4nksha@cluster0-ieotr.gcp.mongodb.net/test?retryWrites=true")
#client is connecting to database "test"
db = client.test

# name of collection is "notes"

def addNote(title, note):
    return db.notes.insert_one({
        "title":title,
        "note":note
    }).inserted_id

# mongo will create id for each entry

def deleteNote(id):
    return db.notes.delete_one({"_id":ObjectId(id)}).deleted_count


def updateNote(id, title, note):
    return db.notes.replace_one({"_id":ObjectId(id)},{  #update syntax: find, what to replace
        "title":title,
        "note":note
    }).modified_count    

def listNote():  #to list all the notes
    return db.notes.find() 