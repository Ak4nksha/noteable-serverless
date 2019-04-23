import pymongo

#pymongo is a library to access mongodb server

client = pymongo.MongoClient("mongodb+srv://Ak4nksha:Ak4nksha@cluster0-ieotr.gcp.mongodb.net/test?retryWrites=true")
#client is connecting to database "test"
db = client.test

# name of collection is "notes"

def addNote(title, note):
    return db.notes.insert_one({
        "title":title,
        "note":note
    })

# mongo will create id for each entry

def deleteNote(id):
    return db.notes.remove({"_id":id})


def updateNote(id, title, note):
    return db.notes.replace({"_id":id},{  #update syntax: find, what to replace
        "title":title,
        "note":note
    })    

def listNote():  #to list all the notes
    return db.notes.find() 