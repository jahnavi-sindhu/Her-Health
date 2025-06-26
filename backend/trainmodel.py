import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib  # For saving the model

# Load dataset
df = pd.read_csv('PCOS_data.csv')  # Replace with the actual CSV filename

# Assuming df is your dataframe and these are your features and target
top_features = ['Follicle No. (R)', 'Follicle No. (L)', 'Cycle length(days)', 'AMH(ng/mL)', 'BMI']
target_column = 'PCOS (Y/N)'  # Replace with your actual target column name if different

# Select features and target
X = df[top_features]
y = df[target_column]

# Drop rows with missing values
X = X.apply(pd.to_numeric, errors='coerce').dropna()
y = y.loc[X.index]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest model
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train_scaled, y_train)

# Predictions
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

# Evaluation
print("Train Accuracy:", accuracy_score(y_train, y_train_pred))
print("Test Accuracy:", accuracy_score(y_test, y_test_pred))
print("Classification Report:\n", classification_report(y_test, y_test_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_test_pred))

# Save model and scaler
joblib.dump(model, "random_forest_pcos_model.pkl")
joblib.dump(scaler, "scaler.pkl")
