
import pandas as pd
import joblib

# Load the trained ML model
model = joblib.load("models/career_model.pkl")

# Load the feature names used during training
feature_columns = joblib.load("models/feature_columns.pkl")


def recommend_career(skills, interest):
    # Prepare user input
    user_data = pd.DataFrame(
        [[0] * len(feature_columns)],
        columns=feature_columns
    )

    for skill, value in skills.items():
        if skill in user_data.columns:
            user_data.loc[0, skill] = int(value)

    interest_column = "Interest_" + interest

    if interest_column in user_data.columns:
        user_data.loc[0, interest_column] = 1

    # Give priority to the selected interest
    if interest == "Web":
        return "Web Developer"

    elif interest == "Development":
         return "Software Developer"

    elif interest == "Analytics":
        return "Data Analyst"

    elif interest == "AI":
        return "Data Scientist"

    # Use ML model if interest is not recognized
    prediction = model.predict(user_data)

    return prediction[0]

