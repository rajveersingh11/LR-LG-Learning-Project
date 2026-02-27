import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from mysql_db import engine

df = pd.read_csv("C:\\Users\\rajve\\OneDrive\\Desktop\\lrlg\\covid_toy.csv")

df["fever"] = df["fever"].fillna(df["fever"].mean())

X = df.drop(columns=["has_covid"])
y = df["has_covid"]

le = LabelEncoder()
for col in X.select_dtypes(include=["object"]).columns:
    X[col] = le.fit_transform(X[col])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
logistic = LogisticRegression()    

logistic.fit(x_train, y_train)
y_pred = logistic.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
import joblib
joblib.dump(logistic, "covid_model.pkl")
