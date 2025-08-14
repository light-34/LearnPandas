import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def change_string_numeric(element):
    if element == 'Sunny':
        return 1
    elif element == 'Cloudy':
        return 2
    elif element == 'Raining':
        return 3

df = pd.read_excel('./M2LA8.xlsx')
k = df['Condition'].apply(change_string_numeric)
df['Condition'] = k

x = df.drop('Go?', axis=1)
y = df['Go?']

print(x)
print(y)

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)

print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')
print(f'\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}')
print(f'\nClassification Report:\n{classification_report(y_test, y_pred)}')
