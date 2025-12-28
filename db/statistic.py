from pymongo import MongoClient
import datetime
client = MongoClient()
db = client['burgerdefenser']
stat = db.statistic

def set_stat(system,proc):
    request = stat.find_one({"date": str(datetime.datetime.now().date())})
    print(request)
    if request == None:
        globalis = {
                "sub-zero": 0,
                "hotaru": 0,
                "frost": 0,
                "frost_plus": 0,
                "obsh_proc": 0,
                "date": str(datetime.datetime.now().date())}
        post_id = stat.insert_one(globalis).inserted_id
    else:
        if system == "sub_zero":
            result = db.statistic.update_many({'date': str(datetime.datetime.now().date())},
                {'$set': {'sub-zero': request["sub-zero"] + 1,
                "obsh_proc": request["obsh_proc"] + proc}})
        if system == "hotaru":
            result = db.statistic.update_many({'date': str(datetime.datetime.now().date())},
                {'$set': {'hotaru': request["hotaru"] + 1}})
        if system == "frost":
            result = db.statistic.update_many({'date': str(datetime.datetime.now().date())},
                {'$set': {'frost': request["frost"] + 1}})   
        if system == "frost_plus":
            result = db.statistic.update_many({'date': str(datetime.datetime.now().date())},
                {'$set': {'frost_plus': request["frost_plus"] + 1,
                "obsh_proc": request["obsh_proc"] + proc}})