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
import datetime
from time_normalizer import convert_atom_time
from constants import list_intent, list_placeholder_message
import random
def compound2unicode(text):
  #https://gist.github.com/redphx/9320735`
  text = text.replace("\u0065\u0309", "\u1EBB")    # ẻ
  text = text.replace("\u0065\u0301", "\u00E9")    # é
  text = text.replace("\u0065\u0300", "\u00E8")    # è
  text = text.replace("\u0065\u0323", "\u1EB9")    # ẹ
  text = text.replace("\u0065\u0303", "\u1EBD")    # ẽ
  text = text.replace("\u00EA\u0309", "\u1EC3")    # ể
  text = text.replace("\u00EA\u0301", "\u1EBF")    # ế
  text = text.replace("\u00EA\u0300", "\u1EC1")    # ề
  text = text.replace("\u00EA\u0323", "\u1EC7")    # ệ
  text = text.replace("\u00EA\u0303", "\u1EC5")    # ễ
  text = text.replace("\u0079\u0309", "\u1EF7")    # ỷ
  text = text.replace("\u0079\u0301", "\u00FD")    # ý
  text = text.replace("\u0079\u0300", "\u1EF3")    # ỳ
  text = text.replace("\u0079\u0323", "\u1EF5")    # ỵ
  text = text.replace("\u0079\u0303", "\u1EF9")    # ỹ
  text = text.replace("\u0075\u0309", "\u1EE7")    # ủ
  text = text.replace("\u0075\u0301", "\u00FA")    # ú
  text = text.replace("\u0075\u0300", "\u00F9")    # ù
  text = text.replace("\u0075\u0323", "\u1EE5")    # ụ
  text = text.replace("\u0075\u0303", "\u0169")    # ũ
  text = text.replace("\u01B0\u0309", "\u1EED")    # ử
  text = text.replace("\u01B0\u0301", "\u1EE9")    # ứ
  text = text.replace("\u01B0\u0300", "\u1EEB")    # ừ
  text = text.replace("\u01B0\u0323", "\u1EF1")    # ự
  text = text.replace("\u01B0\u0303", "\u1EEF")    # ữ
  text = text.replace("\u0069\u0309", "\u1EC9")    # ỉ
  text = text.replace("\u0069\u0301", "\u00ED")    # í
  text = text.replace("\u0069\u0300", "\u00EC")    # ì
  text = text.replace("\u0069\u0323", "\u1ECB")    # ị
  text = text.replace("\u0069\u0303", "\u0129")    # ĩ
  text = text.replace("\u006F\u0309", "\u1ECF")    # ỏ
  text = text.replace("\u006F\u0301", "\u00F3")    # ó
  text = text.replace("\u006F\u0300", "\u00F2")    # ò
  text = text.replace("\u006F\u0323", "\u1ECD")    # ọ
  text = text.replace("\u006F\u0303", "\u00F5")    # õ
  text = text.replace("\u01A1\u0309", "\u1EDF")    # ở
  text = text.replace("\u01A1\u0301", "\u1EDB")    # ớ
  text = text.replace("\u01A1\u0300", "\u1EDD")    # ờ
  text = text.replace("\u01A1\u0323", "\u1EE3")    # ợ
  text = text.replace("\u01A1\u0303", "\u1EE1")    # ỡ
  text = text.replace("\u00F4\u0309", "\u1ED5")    # ổ
  text = text.replace("\u00F4\u0301", "\u1ED1")    # ố
  text = text.replace("\u00F4\u0300", "\u1ED3")    # ồ
  text = text.replace("\u00F4\u0323", "\u1ED9")    # ộ
  text = text.replace("\u00F4\u0303", "\u1ED7")    # ỗ
  text = text.replace("\u0061\u0309", "\u1EA3")    # ả
  text = text.replace("\u0061\u0301", "\u00E1")    # á
  text = text.replace("\u0061\u0300", "\u00E0")    # à
  text = text.replace("\u0061\u0323", "\u1EA1")    # ạ
  text = text.replace("\u0061\u0303", "\u00E3")    # ã
  text = text.replace("\u0103\u0309", "\u1EB3")    # ẳ
  text = text.replace("\u0103\u0301", "\u1EAF")    # ắ
  text = text.replace("\u0103\u0300", "\u1EB1")    # ằ
  text = text.replace("\u0103\u0323", "\u1EB7")    # ặ
  text = text.replace("\u0103\u0303", "\u1EB5")    # ẵ
  text = text.replace("\u00E2\u0309", "\u1EA9")    # ẩ
  text = text.replace("\u00E2\u0301", "\u1EA5")    # ấ
  text = text.replace("\u00E2\u0300", "\u1EA7")    # ầ
  text = text.replace("\u00E2\u0323", "\u1EAD")    # ậ
  text = text.replace("\u00E2\u0303", "\u1EAB")    # ẫ
  text = text.replace("\u0045\u0309", "\u1EBA")    # Ẻ
  text = text.replace("\u0045\u0301", "\u00C9")    # É
  text = text.replace("\u0045\u0300", "\u00C8")    # È
  text = text.replace("\u0045\u0323", "\u1EB8")    # Ẹ
  text = text.replace("\u0045\u0303", "\u1EBC")    # Ẽ
  text = text.replace("\u00CA\u0309", "\u1EC2")    # Ể
  text = text.replace("\u00CA\u0301", "\u1EBE")    # Ế
  text = text.replace("\u00CA\u0300", "\u1EC0")    # Ề
  text = text.replace("\u00CA\u0323", "\u1EC6")    # Ệ
  text = text.replace("\u00CA\u0303", "\u1EC4")    # Ễ
  text = text.replace("\u0059\u0309", "\u1EF6")    # Ỷ
  text = text.replace("\u0059\u0301", "\u00DD")    # Ý
  text = text.replace("\u0059\u0300", "\u1EF2")    # Ỳ
  text = text.replace("\u0059\u0323", "\u1EF4")    # Ỵ
  text = text.replace("\u0059\u0303", "\u1EF8")    # Ỹ
  text = text.replace("\u0055\u0309", "\u1EE6")    # Ủ
  text = text.replace("\u0055\u0301", "\u00DA")    # Ú
  text = text.replace("\u0055\u0300", "\u00D9")    # Ù
  text = text.replace("\u0055\u0323", "\u1EE4")    # Ụ
  text = text.replace("\u0055\u0303", "\u0168")    # Ũ
  text = text.replace("\u01AF\u0309", "\u1EEC")    # Ử
  text = text.replace("\u01AF\u0301", "\u1EE8")    # Ứ
  text = text.replace("\u01AF\u0300", "\u1EEA")    # Ừ
  text = text.replace("\u01AF\u0323", "\u1EF0")    # Ự
  text = text.replace("\u01AF\u0303", "\u1EEE")    # Ữ
  text = text.replace("\u0049\u0309", "\u1EC8")    # Ỉ
  text = text.replace("\u0049\u0301", "\u00CD")    # Í
  text = text.replace("\u0049\u0300", "\u00CC")    # Ì
  text = text.replace("\u0049\u0323", "\u1ECA")    # Ị
  text = text.replace("\u0049\u0303", "\u0128")    # Ĩ
  text = text.replace("\u004F\u0309", "\u1ECE")    # Ỏ
  text = text.replace("\u004F\u0301", "\u00D3")    # Ó
  text = text.replace("\u004F\u0300", "\u00D2")    # Ò
  text = text.replace("\u004F\u0323", "\u1ECC")    # Ọ
  text = text.replace("\u004F\u0303", "\u00D5")    # Õ
  text = text.replace("\u01A0\u0309", "\u1EDE")    # Ở
  text = text.replace("\u01A0\u0301", "\u1EDA")    # Ớ
  text = text.replace("\u01A0\u0300", "\u1EDC")    # Ờ
  text = text.replace("\u01A0\u0323", "\u1EE2")    # Ợ
  text = text.replace("\u01A0\u0303", "\u1EE0")    # Ỡ
  text = text.replace("\u00D4\u0309", "\u1ED4")    # Ổ
  text = text.replace("\u00D4\u0301", "\u1ED0")    # Ố
  text = text.replace("\u00D4\u0300", "\u1ED2")    # Ồ
  text = text.replace("\u00D4\u0323", "\u1ED8")    # Ộ
  text = text.replace("\u00D4\u0303", "\u1ED6")    # Ỗ
  text = text.replace("\u0041\u0309", "\u1EA2")    # Ả
  text = text.replace("\u0041\u0301", "\u00C1")    # Á
  text = text.replace("\u0041\u0300", "\u00C0")    # À
  text = text.replace("\u0041\u0323", "\u1EA0")    # Ạ
  text = text.replace("\u0041\u0303", "\u00C3")    # Ã
  text = text.replace("\u0102\u0309", "\u1EB2")    # Ẳ
  text = text.replace("\u0102\u0301", "\u1EAE")    # Ắ
  text = text.replace("\u0102\u0300", "\u1EB0")    # Ằ
  text = text.replace("\u0102\u0323", "\u1EB6")    # Ặ
  text = text.replace("\u0102\u0303", "\u1EB4")    # Ẵ
  text = text.replace("\u00C2\u0309", "\u1EA8")    # Ẩ
  text = text.replace("\u00C2\u0301", "\u1EA4")    # Ấ
  text = text.replace("\u00C2\u0300", "\u1EA6")    # Ầ
  text = text.replace("\u00C2\u0323", "\u1EAC")    # Ậ
  text = text.replace("\u00C2\u0303", "\u1EAA")    # Ẫ
  return text

def extract_special_character_and_url(input_string):
    # lọc sơ các bài đăng
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    hash_tag_pattern = '(#([^ ])*)'
    breakline_pattern = '(\n(\n| )+)'
    specialBreakline_pattern = '([-—^*_+ ]([-—^*_+ ])+)'
    dot_pattern = '(\.\.\.(\.)+)'
    specialChar_pattern = '((:\)+)|(:D+)|(:\(+)|(:\'\(+)|(:P+)|(O:\))|(3:\))|(o.O+)|(;\)+)|(:\/ )|(>:O)|(:O+)|(-_+-)|(:\*)|(^_+^)|(8-\)+)|(8\|+)|(>:\(+)|(:v+)|(:3+)|(\(y\))|(<\(\"\))|(\(^^^\))|(==+)|(:\|\])|(:poop:)|(:putnam:)|(<3+)|(●)|(☐)|(→)|(🚀)|(▶))'
    input_string = re.sub(emoj,'',input_string)
    input_string = re.sub(hash_tag_pattern,'',input_string)
    input_string = re.sub(breakline_pattern,'',input_string)
    input_string = re.sub(specialBreakline_pattern,'',input_string)
    input_string = re.sub(dot_pattern,'',input_string)
    input_string = re.sub(specialChar_pattern,'',input_string)

    #bat email truoc vi email trong do co link
    first_corpus=input_string
    email_pattern=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
    list_email=re.findall(email_pattern,input_string)
    if list_email!=[]:
        for x in list_email:
            input_string=input_string.replace(x,'‱',1)
    url_pattern_http='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)\,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    list_url_http=re.findall(url_pattern_http,input_string)
    if list_url_http!=[]:
        for x in list_url_http:
            input_string=input_string.replace(x,'⌫',1)
    url_pattern_no_http='(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+'
    list_url_no_http=re.findall(url_pattern_no_http,input_string)
    if list_url_no_http!=[]:
        for x in list_url_no_http:
            input_string=input_string.replace(x,'₪',1)

    input_string=input_string.replace('•','')
    input_string = re.sub('[\{\}\_=\+\#\$\%\~\`\'\|\<\>\"\“”…*\^]','',input_string)
    input_string = re.sub('[\,]',' , ',input_string)
    input_string = re.sub('[\.]',' . ',input_string)
    input_string = re.sub('[\:]',' : ',input_string)
    input_string = re.sub('[\-]',' - ',input_string)
    input_string = re.sub('[\?]',' ? ',input_string)
    input_string = re.sub('[\!]',' ! ',input_string)
    input_string = re.sub('[\(]',' ( ',input_string)
    input_string = re.sub('[\)]',' ) ',input_string)
    input_string = re.sub('[\&]',' & ',input_string)
    input_string = re.sub('[\[]',' [ ',input_string)
    input_string = re.sub('[\]]',' ] ',input_string)
    input_string = re.sub('[\@]',' @ ',input_string)
    input_string = re.sub('[\;]',' ; ',input_string)
    input_string=input_string.replace('\\ud','')
    input_string=input_string.replace('\\uc','')
    input_string=input_string.replace('\\','')
    token_list = input_string.split(" ")
    while '' in token_list:
        token_list.remove('')
    input_string=' '.join(token_list).lower()
    result=''
    http_idx=0
    no_http_idx=0
    email_idx=0
    for i in range(0,len(input_string)):
        if input_string[i] not in ['⌫','₪','‱']:
            result+=input_string[i]
        elif input_string[i]=='⌫':
            result+=list_url_http[http_idx]
            http_idx=http_idx+1
        elif input_string[i]=='₪':
            if no_http_idx<len(list_url_no_http):
                result+=list_url_no_http[no_http_idx]
                no_http_idx=no_http_idx+1
            else:
                print("---------------------------error corpus")
                print("---------------------------error first corpus")
        elif input_string[i]=='‱':
            result+=list_email[email_idx]
            email_idx=email_idx+1
    return result


def preprocess_message(message):
    if isinstance(message,str):
        message = message.lower()
        message = message.replace(',', ' , ')
        message = message.replace('.', ' . ')
        message = message.replace('!', ' ! ')
        message = message.replace('&', ' & ')
        message = message.replace('?', ' ? ')
        message = message.replace('-', ' - ')
        message = message.replace('(', ' ( ')
        message = message.replace(')', ' ) ')
        message = compound2unicode(message)
        list_token = message.split(' ')
        while '' in list_token:
            list_token.remove('')
        message = ' '.join(list_token)
    return message

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
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)

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

@app.route("/api/server-cse-assistant-admin/filter-corpus", methods=['POST'])
@jwt_required()
def filter_corpus():
    input_data = request.json
    if "corpus" not in input_data:
        raise ServerException('corpus can not be None', status_code=400)
    corpus = input_data['corpus']
    processed_corpus = extract_special_character_and_url(corpus)
    response = jsonify({"processed_corpus": processed_corpus})
    response.headers.add('Access-Control-Allow-Origin', '*')
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
        response = jsonify({"message": activity})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
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
        response = jsonify({"activities": result,"total":total,"per_page":per_page,"current_page":current_page})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
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
        mongo.db.suggest_messages.delete_many({"activity_id":_id})
        response = jsonify({"message": "delete success"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
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
        response = jsonify({"message": result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    raise ServerException('activities not found', status_code=404)

@app.route("/api/server-cse-assistant-admin/activities", methods=['POST'])
@jwt_required()
def add_activity():
    input_data = request.json
    if "activity" not in input_data:
        raise ServerException('activity can not be None', status_code=400)
    activity = input_data["activity"]
    ## chuẩn hóa trước khi insert
    for key in list(activity.keys()):
        if key not in ["time_works_place_address_mapping","_id","time"]:
            for i in range(len(activity[key])):
                activity[key][i] = preprocess_message(activity[key][i])
        elif key == "time_works_place_address_mapping":
            for j in range(len(activity[key])):
                for key_obj in list(activity[key][j].keys()):
                    for i in range(len(activity[key][j][key_obj])):
                        activity[key][j][key_obj][i] = preprocess_message(activity[key][j][key_obj][i])
                        
    insert_id = mongo.db.activities.insert_one(activity).inserted_id
    if activity['name_activity'] not in [[], None]:
        #thêm 5 câu suggest cho mỗi tên hoạt động
        for j in range(5):
            for name_activity in activity['name_activity']:
                random_placeholder_message_index = random.randint(0,len(list_placeholder_message) - 1)
                if list_placeholder_message[random_placeholder_message_index].find("mùa hè xanh") != -1:
                    suggest_message_insert = list_placeholder_message[random_placeholder_message_index].replace("mùa hè xanh",name_activity)
                    intent_insert = list_intent[random_placeholder_message_index]
                    mongo.db.suggest_messages.insert_one({'activity_id':str(insert_id),'message':suggest_message_insert,'intent':intent_insert})
    
    
    
    for key in list(activity.keys()):
        if key not in ["time_works_place_address_mapping","_id","time"]:
            for value in activity[key]:
                mongo.db.dictionary.insert_one({'activity_id':str(insert_id),'value':value,'type':key})
        elif key == "time_works_place_address_mapping":
            for map_obj in activity[key]:
                for key_obj in list(map_obj.keys()):
                    if key_obj != "time":
                        for value in map_obj[key_obj]:
                            mongo.db.dictionary.insert_one({'activity_id':str(insert_id),'value':value,'type':key_obj})

    if insert_id != None:
        response = jsonify({"message": "insert success","id":str(insert_id)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    raise ServerException('insert fail', status_code=400)

@app.route("/api/server-cse-assistant-admin/activities-ner", methods=['POST'])
@jwt_required()
def add_activity_ner():
    input_data = request.json
    if "activity" not in input_data:
        raise ServerException('activity can not be None', status_code=400)
    activity = input_data["activity"]
    ## chuẩn hóa trước khi insert
    for key in list(activity.keys()):
        if key not in ["time_works_place_address_mapping","_id","time"]:
            for i in range(len(activity[key])):
                activity[key][i] = preprocess_message(activity[key][i])
        elif key == "time":
            result_time_int = []
            for i in range(len(activity[key])):
                preprocess_time_int = convert_atom_time(preprocess_message(activity[key][i]))
                if preprocess_time_int != None:
                    result_time_int.append(preprocess_time_int)
            activity[key] = result_time_int
        elif key == "time_works_place_address_mapping":
            for j in range(len(activity[key])):
                for key_obj in list(activity[key][j].keys()):
                    if key_obj != "time":
                        for i in range(len(activity[key][j][key_obj])):
                            activity[key][j][key_obj][i] = preprocess_message(activity[key][j][key_obj][i])
                    else:
                        result_time_obj_int = []
                        for i in range(len(activity[key][j][key_obj])):
                            preprocess_time_obj_int = convert_atom_time(preprocess_message(activity[key][j][key_obj][i]))
                            if preprocess_time_obj_int != None:
                                result_time_obj_int.append(preprocess_time_obj_int)
                        activity[key][j][key_obj] = result_time_obj_int

                        
    insert_id = mongo.db.activities.insert_one(activity).inserted_id
    if activity['name_activity'] not in [[], None]:
        #thêm 5 câu suggest cho mỗi tên hoạt động
        for j in range(5):
            for name_activity in activity['name_activity']:
                random_placeholder_message_index = random.randint(0,len(list_placeholder_message) - 1)
                if list_placeholder_message[random_placeholder_message_index].find("mùa hè xanh") != -1:
                    suggest_message_insert = list_placeholder_message[random_placeholder_message_index].replace("mùa hè xanh",name_activity)
                    intent_insert = list_intent[random_placeholder_message_index]
                    mongo.db.suggest_messages.insert_one({'activity_id':str(insert_id),'message':suggest_message_insert,'intent':intent_insert})
    
    for key in list(activity.keys()):
        if key not in ["time_works_place_address_mapping","_id","time"]:
            for value in activity[key]:
                mongo.db.dictionary.insert_one({'activity_id':str(insert_id),'value':value,'type':key})
        elif key == "time_works_place_address_mapping":
            for map_obj in activity[key]:
                for key_obj in list(map_obj.keys()):
                    if key_obj != "time":
                        for value in map_obj[key_obj]:
                            mongo.db.dictionary.insert_one({'activity_id':str(insert_id),'value':value,'type':key_obj})

    if insert_id != None:
        response = jsonify({"message": "insert success","id":str(insert_id)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    raise ServerException('insert fail', status_code=400)

@app.route("/api/server-cse-assistant-admin/activities", methods=['PUT'])
@jwt_required()
def update_activity():
    input_data = request.json
    if "activity" not in input_data:
        raise ServerException('activity can not be None', status_code=400)
    activity = input_data["activity"]

    ## chuẩn hóa trước khi update
    for key in list(activity.keys()):
        if key not in ["time_works_place_address_mapping","_id"]:
            for i in range(len(activity[key])):
                print(activity[key][i])
                activity[key][i] = preprocess_message(activity[key][i])
        elif key == "time_works_place_address_mapping":
            for j in range(len(activity[key])):
                for key_obj in list(activity[key][j].keys()):
                    for i in range(len(activity[key][j][key_obj])):
                        activity[key][j][key_obj][i] = preprocess_message(activity[key][j][key_obj][i])


    res = mongo.db.activities.find_one({"_id" : ObjectId(activity["_id"])})
    if res == None:
        raise ServerException("activity's _id not exist", status_code=400)
    mongo.db.activities.delete_one({"_id" : ObjectId(activity["_id"])})
    mongo.db.dictionary.delete_many({"activity_id":activity["_id"]})
    mongo.db.suggest_messages.delete_many({"activity_id":activity["_id"]})
    if activity['name_activity'] not in [[], None]:
        #thêm 5 câu suggest cho mỗi tên hoạt động
        for j in range(5):
            for name_activity in activity['name_activity']:
                random_placeholder_message_index = random.randint(0,len(list_placeholder_message) - 1)
                if list_placeholder_message[random_placeholder_message_index].find("mùa hè xanh") != -1:
                    suggest_message_insert = list_placeholder_message[random_placeholder_message_index].replace("mùa hè xanh",name_activity)
                    intent_insert = list_intent[random_placeholder_message_index]
                    mongo.db.suggest_messages.insert_one({'activity_id':activity["_id"],'message':suggest_message_insert,'intent':intent_insert})
    
    
    activity["_id"] = ObjectId(activity["_id"])
    mongo.db.activities.insert_one(activity)
    for key in list(activity.keys()):
        if key not in ["time_works_place_address_mapping","_id","time"]:
            for value in activity[key]:
                mongo.db.dictionary.insert_one({'activity_id':str(activity["_id"]),'value':value,'type':key})
        elif key == "time_works_place_address_mapping":
            for map_obj in activity[key]:
                for key_obj in list(map_obj.keys()):
                    if key_obj != "time":
                        for value in map_obj[key_obj]:
                            mongo.db.dictionary.insert_one({'activity_id':str(activity["_id"]),'value':value,'type':key_obj})
    response = jsonify({"message":"update success"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/api/server-cse-assistant-admin/valid-token", methods=['GET'])
@jwt_required()
def valid_token():
    response = jsonify({"message":"token valid"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/api/server-cse-assistant-admin/activities/filter/page/<page>", methods=['POST'])
@jwt_required()
def filter_activity(page):
    input_data = request.json
    if "condition" not in input_data:
        raise ServerException('condition can not be None', status_code=400)
    condition = input_data["condition"]
    for key in list(condition.keys()):
        for i in range(len(condition[key])):
            condition[key][i] = preprocess_message(condition[key][i])
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
    response = jsonify({"message":"activity found","activities": result,"total":total,"per_page":per_page,"current_page":current_page})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(port=8000)

