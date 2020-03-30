#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)


app.config["MONGO_URI"] = "mongodb://caochanhduong:bikhungha1@ds261626.mlab.com:61626/activity?retryWrites=false"
mongo = PyMongo(app)


def msg(code, mess=None):
    if code == 200 and mess is None:
        return jsonify({"code": 200, "value": True})
    return jsonify({"code": code, "message": mess}), code


# In[14]:
@app.route('/')
def index():
    return """<h1>CSE Assistant</h1>"""


@app.errorhandler(404)
def url_error(e):
    print("---------------------")
    return msg(404, "cao chánh dương")


@app.errorhandler(500)
def server_error(e):
    return msg(500, "SERVER ERROR")


@app.route("/api/server-cse-assistant-admin/activities/<_id>", methods=['GET'])
def activity_detail(_id):
    print(_id)
    if _id == "" or len(_id)!=24:
        return msg(400, "invalid id")
    activity = mongo.db.activities.find_one({"_id":ObjectId(_id)})

    if activity != None:
        activity["_id"] = _id
        return jsonify({"code": 200, "message": activity})
    return jsonify({"code":404,"message":"activity not found"})

@app.route("/api/server-cse-assistant-admin/activities/page/<page>", methods=['GET'])
def activities_page(page):
    print(page)
    total = mongo.db.activities.count()
    per_page = 20
    current_page = int(page)
    activities = mongo.db.activities.find(limit = 20,skip = per_page*(current_page - 1))
    result = []
    #convert _id to string
    for activity in activities:
        activity["_id"] = str(activity["_id"])
        result.append(activity)
    if activity != None:
        return jsonify({"code": 200, "users": result,"total":total,"per_page":per_page,"current_page":current_page})
    return jsonify({"code":404,"users": [],"total":0,"per_page":per_page,"current_page":current_page})

@app.route("/api/server-cse-assistant-admin/activities/<_id>", methods=['DELETE'])
def delete_activity(_id):
    print(_id)
    if _id == "" or len(_id)!=24:
        return msg(400, "invalid id")
    activity = mongo.db.activities.find_one({"_id" : ObjectId(_id)})
    
    if activity != None:
        result = mongo.db.activities.delete_one({"_id" : activity["_id"]})
        return jsonify({"code": 200, "message": "delete success"})
    return jsonify({"code":404,"message":"activity not found"})

@app.route("/api/server-cse-assistant-admin/activities", methods=['GET'])
def get_all_activities():
    activities = mongo.db.activities.find(limit = 10)
    result = []
    #convert _id to string
    for activity in activities:
        activity["_id"] = str(activity["_id"])
        result.append(activity)
    if activity != None:
        return jsonify({"code": 200, "message": result})
    return jsonify({"code":404,"message":"activities not found"})

@app.route("/api/server-cse-assistant-admin/activities", methods=['POST'])
def add_activity():
    input_data = request.json
    if "activity" not in input_data:
        return jsonify({"code": 400, "message":"activity can not be None"})
    activity = input_data["activity"]
    result = mongo.db.activities.insert_one(activity)
    if result != None:
        return jsonify({"code": 200, "message": "insert success"})
    return jsonify({"code":400,"message":"insert fail"})

@app.route("/api/server-cse-assistant-admin/activities", methods=['PUT'])
def update_activity():
    input_data = request.json
    if "activity" not in input_data:
        return jsonify({"code": 400, "message":"activity can not be None"})
    activity = input_data["activity"]
    res = mongo.db.activities.find_one({"_id" : ObjectId(activity["_id"])})
    if res == None:
        return jsonify({"code":400,"message":"activity's _id not exist"})
    
    mongo.db.activities.delete_one({"_id" : ObjectId(activity["_id"])})
    activity["_id"] = ObjectId(activity["_id"])
    mongo.db.activities.insert_one(activity)
    return jsonify({"code":200,"message":"update success"})


if __name__ == '__main__':
    app.run()

