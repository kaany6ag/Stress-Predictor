import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Starting program...")

data = {
    'study_hours': [2, 3, 5, 1, 4, 6, 2, 7, 3, 5],
    'sleep_hours': [7, 6, 5, 8, 6, 4, 7, 3, 6, 5],
    'stress_level': [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['study_hours', 'sleep_hours']]
y = df['stress_level']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

result = model.predict([[6,4]])
print("Prediction for (study=6, sleep=4):", result)

print("Program finished successfully!")