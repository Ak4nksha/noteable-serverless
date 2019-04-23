import json
import ast
from db import addNote, deleteNote, listNote, updateNote

def all(event, context):
    items = []
    for item in listNote():
        item["_id"] = str(item["_id"])[10:-2]
        items.append(item)
    body = {
       "notes": items
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def save(event, context):
    data = eval(eval(event)['body'])
    return {
        "statusCode": 200,
        "body": addNote(data['title'], data['note'])
    }

def edit(event, context):
    data = eval(eval(event)['body'])
    return {
        "statusCode": 200,
        "body": updateNote(data['id'], data['title'], data['note'])
    }

def remove(event, cotext):
    data = json.loads(event.body)
    return {
        "statusCode": 200,
        "body": deleteNote(data.id)
    }

