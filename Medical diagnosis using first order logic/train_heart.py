import pandas as pd
import wittgenstein as lw

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Load Dataset
data = pd.read_csv("datasets/heart.csv")

# Features and Target
X = data.drop("target", axis=1)
y = data["target"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# RIPPER Model
model = lw.RIPPER()

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy :", accuracy)

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nGenerated Rules")
print(model.ruleset_)
#save model
import pickle

with open("models/heart_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nHeart model saved successfully!")