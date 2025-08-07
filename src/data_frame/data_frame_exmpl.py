import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('../A_Demo/diabetes.csv')

x = df.drop('Outcome', axis=1)
y = df['Outcome']

#Splits the data: 80% for training, 20% for testing. random_state=42 ensures the same split each time (for reproducibility).
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#StandardScaler scales the data to have mean = 0 and std dev = 1.
#Helps algorithms like KNN perform better (distance-based models are sensitive to scale).
scaler = StandardScaler()
x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.transform(x_test)

#Creates a KNN model with k=20 (uses 20 nearest neighbors).
#Trains the model using scaled training data.
model = KNeighborsClassifier(n_neighbors=20)
model.fit(x_train_scaler, y_train)

#Makes predictions for the test dataset using the trained model.
y_pred = model.predict(x_test_scaler)

print(f'Accuracy : {accuracy_score(y_test, y_pred):.2f}')
print(f'\nConfusion Matrix:\n {confusion_matrix(y_test, y_pred)}')
print(f'\nClassification Report:\n {classification_report(y_test, y_pred)}')

#Loops from k = 1 to k = 20:
#Trains a new KNN model for each k.
#Predicts and prints the accuracy.
#Helps find the best k value for the dataset.
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train_scaler, y_train)
    acc = accuracy_score(y_test, knn.predict(x_test_scaler))
    print(f'K={k} -> Accuracy={acc:.2f}')


