import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier  

# Load the dataset
data = pd.read_csv('data/Fish.csv')

# Encode Species (text) to numerical labels
le = LabelEncoder()
data['Species'] = le.fit_transform(data['Species'])

# Features and Target
X = data[['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']]
y = data['Species']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model (Random Forest example)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate on the test data
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save the model (optional -  using pickle or joblib)
import pickle
pickle.dump(model, open('fish_classifier.pkl', 'wb'))
