#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
import re
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
import hashlib

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


def authenticate(username, password):
    user = mongo.db.users.find_one({"username":username})
    if user and safe_str_cmp(user['password'], hashlib.sha256(str.encode(password)).hexdigest()):
        user['_id'] = str(user['_id'])
        return User(user["id"],user["username"],user["password"])

def identity(payload):
    user_id = payload['identity']
    user = mongo.db.users.find_one({"id":user_id})
    if user != None:
        user['_id'] = str(user['_id'])
        return User(user["id"],user["username"],user["password"])
    else:
        return user

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'super-secret'

app.config["MONGO_URI"] = "mongodb://caochanhduong:bikhungha1@ds261626.mlab.com:61626/activity?retryWrites=false"
mongo = PyMongo(app)

jwt = JWT(app, authenticate, identity)


class ServerException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def convert_to_regex_constraint(constraints):
    regex_constraint_dict = {}
    for k,values in constraints.items():
        if values != []:
            list_pat = []
            for value in values:
                list_pat.append(re.compile(".*{0}.*".format(value)))
            regex_constraint_dict[k] = {"$all":list_pat}
        else:
            regex_constraint_dict[k] = values
    return regex_constraint_dict


    # def convert_to_regex_constraint(constraints):
    #     list_and_out = []
    #     list_and_in = []
    #     ele_match_obj = {}
    #     list_or = []
    #     regex_constraint_dict = {}
    #     for k,values in constraints.items():
    #         if k not in list_map_key:
    #             list_pattern = []
    #             for value in values:
    #                 list_pattern.append(re.compile(".*{0}.*".format(value)))
    #             if list_pattern != []:
    #                 list_and_out.append({k: {"$all": list_pattern}})
    #         else:
    #             for value in values:
    #                 list_and_in.append({
    #                     "$or" : [
    #                                 {
    #                                     k: {
    #                                         "$all": [re.compile(".*{0}.*".format(value))]
    #                                     }
    #                                 },
    #                                 {    
    #                                     "time_works_place_address_mapping": {
    #                                         "$all": [
    #                                                     {
    #                                                         "$elemMatch": {
    #                                                                 k: {
    #                                                                     "$all": [re.compile(".*{0}.*".format(value))]
    #                                                                 }
    #                                                         }
    #                                                     }
    #                                                 ]
    #                                     }
    #                                 }
    #                             ]
    #                 })

    #     if list_and_in != []:
    #         list_and_out.append({"$and": list_and_in})

    #     if list_and_out != []:
    #         regex_constraint_dict = {"$and":list_and_out}
    #     return regex_constraint_dict

# def convert_to_regex_constraint(constraints):
#     list_and_out = []
#     list_and_in = []
#     ele_match_obj = {}
#     list_or = []
#     for k,values in constraints.items():
#         list_pat = []
#         for value in values:
#             list_pat.append(re.compile(".*{0}.*".format(value)))
#         # regex_constraint_dict[k] = {"$all":list_pat}
#         if k not in ["works","name_place","address","time"]:
#             list_and_out.append({k:{"$all":list_pat}})
#         else:
#             list_and_in.append({k:{"$all":list_pat}})
#             ele_match_obj[k] = {"$all":list_pat}
#     if list_and_in != [] :
#         list_or = [{"$and":list_and_in},{"time_works_place_address_mapping":{"$all":[{"$elemMatch":ele_match_obj}]}}]
#         list_and_out.append({"$or" : list_or})
#     regex_constraint_dict = {"$and":list_and_out}
#     return regex_constraint_dict

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

@app.errorhandler(ServerException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/api/server-cse-assistant-admin/activities/<_id>", methods=['GET'])
@jwt_required()
def activity_detail(_id):
    print(_id)
    if _id == "" or len(_id)!=24:
        raise ServerException('invalid id', status_code=400)
    activity = mongo.db.activities.find_one({"_id":ObjectId(_id)})

    if activity != None:
        activity["_id"] = _id
        return jsonify({"message": activity})
    raise ServerException('activity not found', status_code=404)

@app.route("/api/server-cse-assistant-admin/activities/page/<page>", methods=['GET'])
@jwt_required()
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
        return jsonify({"activities": result,"total":total,"per_page":per_page,"current_page":current_page})
    raise ServerException('activity not found', status_code=404)

@app.route("/api/server-cse-assistant-admin/activities/<_id>", methods=['DELETE'])
@jwt_required()
def delete_activity(_id):
    print(_id)
    if _id == "" or len(_id)!=24:
        raise ServerException('invalid id', status_code=400)
    activity = mongo.db.activities.find_one({"_id" : ObjectId(_id)})
    
    if activity != None:
        result = mongo.db.activities.delete_one({"_id" : activity["_id"]})
        mongo.db.dictionary.delete_many({"activity_id":_id})
        return jsonify({"message": "delete success"})
    raise ServerException("activity not found", status_code=404)

@app.route("/api/server-cse-assistant-admin/activities", methods=['GET'])
@jwt_required()
def get_all_activities():
    activities = mongo.db.activities.find(limit = 10)
    result = []
    #convert _id to string
    for activity in activities:
        activity["_id"] = str(activity["_id"])
        result.append(activity)
    if activity != None:
        return jsonify({"message": result})
    raise ServerException('activities not found', status_code=404)

@app.route("/api/server-cse-assistant-admin/activities", methods=['POST'])
@jwt_required()
def add_activity():
    input_data = request.json
    if "activity" not in input_data:
        raise ServerException('activity can not be None', status_code=400)
    activity = input_data["activity"]
    
    insert_id = mongo.db.activities.insert_one(activity).inserted_id
    for key in list(activity.keys()):
        if key not in ["time_works_place_address_mapping","_id"]:
            for value in activity[key]:
                mongo.db.dictionary.insert_one({'activity_id':str(insert_id),'value':value,'type':key})
        elif key == "time_works_place_address_mapping":
            for map_obj in activity[key]:
                for key_obj in list(map_obj.keys()):
                    for value in map_obj[key_obj]:
                        mongo.db.dictionary.insert_one({'activity_id':str(insert_id),'value':value,'type':key_obj})

    if insert_id != None:
        return jsonify({"message": "insert success","id":str(insert_id)})
    raise ServerException('insert fail', status_code=400)

@app.route("/api/server-cse-assistant-admin/activities", methods=['PUT'])
@jwt_required()
def update_activity():
    input_data = request.json
    if "activity" not in input_data:
        raise ServerException('activity can not be None', status_code=400)
    activity = input_data["activity"]
    res = mongo.db.activities.find_one({"_id" : ObjectId(activity["_id"])})
    if res == None:
        raise ServerException("activity's _id not exist", status_code=400)
    mongo.db.activities.delete_one({"_id" : ObjectId(activity["_id"])})
    mongo.db.dictionary.delete_many({"activity_id":activity["_id"]})
    activity["_id"] = ObjectId(activity["_id"])
    mongo.db.activities.insert_one(activity)
    for key in list(activity.keys()):
        if key not in ["time_works_place_address_mapping","_id"]:
            for value in activity[key]:
                mongo.db.dictionary.insert_one({'activity_id':str(activity["_id"]),'value':value,'type':key})
        elif key == "time_works_place_address_mapping":
            for map_obj in activity[key]:
                for key_obj in list(map_obj.keys()):
                    for value in map_obj[key_obj]:
                        mongo.db.dictionary.insert_one({'activity_id':str(activity["_id"]),'value':value,'type':key_obj})

    return jsonify({"message":"update success"})

@app.route("/api/server-cse-assistant-admin/activities/filter/page/<page>", methods=['POST'])
@jwt_required()
def filter_activity(page):
    input_data = request.json
    if "condition" not in input_data:
        raise ServerException('condition can not be None', status_code=400)
    condition = input_data["condition"]
    regex_constraint = convert_to_regex_constraint(condition)
    total = mongo.db.activities.find(regex_constraint).count()
    per_page = 20
    current_page = int(page)
    activities = mongo.db.activities.find(regex_constraint,limit = 20,skip = per_page*(current_page - 1))

    result = []
    print(activities)
        
    for activity in activities:
        #đổi từ object id sang string và dùng id đó làm key (thay vì dùng index của mảng để làm key vì không xác định đc index)
        activity["_id"] = str(activity["_id"])
        result.append(activity)
    if result == [] :
        raise ServerException('activity not found', status_code=404)
    return jsonify({"message":"activity found","activities": result,"total":total,"per_page":per_page,"current_page":current_page})


if __name__ == '__main__':
    app.run()

