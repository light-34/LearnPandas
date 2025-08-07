# Step 1: Import libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# We need:
# load_iris: to get the dataset
# train_test_split: to split into train/test sets
# StandardScaler: to normalize features (even though RandomForest doesn’t require it, it's a good habit)
# RandomForestClassifier: our model
# Metrics: for evaluation

# Step 2: Load the dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
# We convert the built-in dataset into a pandas DataFrame for easier handling.

# Step 3: Split features and target
x = df.drop('target', axis=1)
y = df['target']
#Separate the independent variables (x) from the target labels (y).

# Step 4: Split into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#Training set: used to train the model
#Test set: used to evaluate model performance
#random_state: makes the split reproducible

# Step 5: Normalize features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
#Scales features to have mean=0 and std=1.
#Important for models sensitive to scale (e.g., SVM, KNN).
#Random Forests don’t require this, but it's included for consistency.

# Step 6: Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train_scaled, y_train)
#RandomForestClassifier is used here (you could use SVM, KNN, etc.).
#Trained on the scaled training data.

# Step 7: Predict on test set
y_pred = model.predict(x_test_scaled)
#We now use the trained model to make predictions on unseen data.

# Step 8: Evaluate the model
print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')
print(f'\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}')
print(f'\nClassification Report:\n{classification_report(y_test, y_pred, target_names=iris.target_names)}')
#We assess how well the model performs using:
#Accuracy
#Confusion matrix
#Precision, recall, f1-score for each class
