from pymongo import MongoClient
client = MongoClient()
db = client['burgerdefenser']
reports = db.reports
neuro = db.neuro_base
request = reports.find({})
for r in request:
    print(str(r["text"]) + "\n")
    if input("Y/N") == "Y":
        globalis = {"text": r["text"],
                    "status": 2}
        post_id = neuro.insert_one(globalis).inserted_id
        db.reports.delete_one({"text": r["text"]})
    else:
        db.reports.delete_one({"text": r["text"]})