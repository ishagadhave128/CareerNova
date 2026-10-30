
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pd.read_csv("data/career_data.csv")

# Select input features and target
X = data.drop("Career", axis=1)
y = data["Career"]

# Convert text categories into numeric values
X = pd.get_dummies(X, columns=["Interest"])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Train the Machine Learning model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Check model accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Save the trained model and feature names
joblib.dump(model, "models/career_model.pkl")
joblib.dump(list(X.columns), "models/feature_columns.pkl")

print("Career Recommendation Model trained successfully!")
