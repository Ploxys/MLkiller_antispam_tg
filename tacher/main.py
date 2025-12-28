import numpy as np
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import RidgeClassifier
from datetime import datetime, timedelta
from pymongo import MongoClient
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import Ridge

client = MongoClient()
db = client['burgerdefenser']
neuro_base = db.neuro_base
request = neuro_base.find({})
text = []
status = []
text_def = []
status_def = []
for r in request:
    text.append(r["text"])
    status.append(r["status"])
    if r["status"] == 2:
        status_def.append(1)
    else:
        status_def.append(0)

print("base:" + str(len(text)))
texts = text
texts_labels = status
text_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('scaler', StandardScaler(with_mean=False)),
    ('clf', RandomForestRegressor(n_estimators=2900,bootstrap=False,n_jobs=9))
])
fight = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', GradientBoostingRegressor(n_estimators=8000,criterion="squared_error"))
    ])
#text_clf = Pipeline([
#    ('tfidf', TfidfVectorizer()),
#    ('clf', RandomForestClassifier(criterion="entropy",n_estimators=2900,max_depth=350,bootstrap=False,n_jobs=9))
#])
#craken = Pipeline([
#   ('tfidf', TfidfVectorizer()),
#   ('clf', GradientBoostingClassifier(n_estimators=3500, learning_rate=0.5,max_depth=600, random_state=0,max_features=0.4)) #criterion entropy
#])
neuro_fighter = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('scaler', StandardScaler(with_mean=False)),
    ('clf', MLPClassifier(activation="logistic",max_iter=148,learning_rate="invscaling",n_iter_no_change=20,hidden_layer_sizes=[(256),(256)]))])
apofes = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', RidgeClassifier())
])
frost_plus = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', Ridge())])

print("Обучаем RidgeClassifier")
apofes = apofes.fit(texts,texts_labels)
filename = '/home/burger/MLkiller/datasets/RidgeClassifier.sav'
pickle.dump(apofes, open(filename, 'wb'))

print("Обучаем RidgeRegressor")
apofes = frost_plus.fit(texts,texts_labels)
filename = '/home/burger/MLkiller/datasets/RidgeRegressor.sav'
pickle.dump(apofes, open(filename, 'wb'))

print("Обучаем GradientBoostingRegressor")
apofes = fight.fit(texts,texts_labels)
filename = '/home/burger/MLkiller/datasets/GradientBoostingRegressor.sav'
pickle.dump(apofes, open(filename, 'wb'))

print("Обучаем MLPClassifier")
neuro_fighter.fit(texts, texts_labels)
filename = '/home/burger/MLkiller/datasets/MLPClassifier.sav'
pickle.dump(neuro_fighter, open(filename, 'wb'))

print("Обучаем RandomForestRegressor")
text_clf.fit(texts, status_def)
filename = '/home/burger/MLkiller/datasets/RandomForestRegressor.sav'
pickle.dump(text_clf, open(filename, 'wb'))
#print("Обучаем GradientBoostingClassifier")
#filename = 'GradientBoostingClassifier.sav'
#craken.fit(texts, texts_labels)
#pickle.dump(craken, open(filename, 'wb'))

#filename1 = 'GradientBoostingClassifier.sav'
#loaded_model = pickle.load(open(filename, 'rb'))
#res = loaded_model.predict([input("text: ")])
#print(res[0])
