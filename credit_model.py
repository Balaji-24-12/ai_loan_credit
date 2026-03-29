import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier

data = pd.read_csv("credit_risk_dataset.csv")

print(data.head())
print(data.info())
data = data.dropna()

label = LabelEncoder()

data["person_home_ownership"] = label.fit_transform(data["person_home_ownership"])
data["loan_intent"] = label.fit_transform(data["loan_intent"])
data["loan_grade"] = label.fit_transform(data["loan_grade"])
data["cb_person_default_on_file"] = label.fit_transform(data["cb_person_default_on_file"])

X = data.drop("loan_status", axis=1)
y = data["loan_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = XGBClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print(classification_report(y_test, predictions))

sample = [[35,50000,1,10,2,3,15000,11.5,0.3,0,12]]

prediction = model.predict(sample)

print("Loan Status:", prediction)

import pickle

pickle.dump(model, open("credit_model.pkl","wb"))

model = pickle.load(open("credit_model.pkl","rb"))