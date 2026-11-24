import pandas as pd
import wittgenstein as lw

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("datasets/diabetes.csv")

# Features and target
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = lw.RIPPER()
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, pred)

print("Accuracy:", acc)

# Display rules
print("\nGenerated Rules:")
print(model.ruleset_)
#save model
import pickle

with open("models/diabetes_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nDiabetes model saved successfully!")