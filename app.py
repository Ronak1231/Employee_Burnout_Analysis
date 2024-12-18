import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
from flask import Flask, render_template, request
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess the data
df = pd.read_excel("employee_burnout.xlsx")

# Handle missing values
df['Mental Fatigue Score'] = df['Mental Fatigue Score'].fillna(df['Mental Fatigue Score'].mean())
df['Burn Rate'] = df['Burn Rate'].fillna(df['Burn Rate'].mean())
df['Resource Allocation'] = df['Resource Allocation'].fillna(df['Resource Allocation'].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Encode categorical variables
le = LabelEncoder()
for col in ['Gender', 'Company Type', 'WFH Setup Available']:
    df[col] = le.fit_transform(df[col])

# Feature selection
features = ['Gender', 'Company Type', 'WFH Setup Available', 'Designation', 'Resource Allocation', 'Mental Fatigue Score']
target = 'Burn Rate'
X = df[features]
y = df[target]

# Normalize features
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save the model and scaler
pickle.dump(model, open('linear_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

# Flask app setup
app = Flask(__name__)

# Folder to save generated visualization images
visualization_folder = 'static/images/visualizations'
os.makedirs(visualization_folder, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html', mse=mse, r2=r2)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the model and scaler
        model = pickle.load(open('linear_model.pkl', 'rb'))
        scaler = pickle.load(open('scaler.pkl', 'rb'))

        # Extract features from form input
        gender = int(request.form['gender'])
        company_type = int(request.form['company_type'])
        wfh_setup = int(request.form['wfh_setup'])
        designation = int(request.form['designation'])
        resource_allocation = float(request.form['resource_allocation'])
        mental_fatigue_score = float(request.form['mental_fatigue_score'])

        # Create input dataframe
        new_data = pd.DataFrame({
            'Gender': [gender],
            'Company Type': [company_type],
            'WFH Setup Available': [wfh_setup],
            'Designation': [designation],
            'Resource Allocation': [resource_allocation],
            'Mental Fatigue Score': [mental_fatigue_score]
        })

        # Normalize input data
        new_data_scaled = scaler.transform(new_data)

        # Predict Burn Rate
        prediction = model.predict(new_data_scaled)[0]
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}", mse=mse, r2=r2)

    return render_template('index.html', prediction_text=f"Predicted Burn Rate: {prediction:.2f}", mse=mse, r2=r2)

@app.route('/visualizations')
def visualizations():
    # Generate visualizations dynamically
    visualizations = [
        ("mental_vs_resource.png", mental_vs_resource),
        ("resource_vs_fatigue.png", resource_vs_fatigue),
        ("burn_wfh_designation.png", burn_wfh_designation),
        ("resource_distribution.png", resource_distribution),
        ("mental_fatigue_vs_burn.png", mental_fatigue_vs_burn),
    ]
    for filename, plot_func in visualizations:
        filepath = os.path.join(visualization_folder, filename)
        plot_func(filepath)
    return render_template('visualization.html', visualizations=visualizations)

def mental_vs_resource(filepath):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Mental Fatigue Score', y='Resource Allocation', hue='Gender', data=df)
    plt.title('Mental Fatigue vs Resource Allocation by Gender')
    plt.xlabel('Mental Fatigue Score')
    plt.ylabel('Resource Allocation')
    plt.savefig(filepath)
    plt.close()

def resource_vs_fatigue(filepath):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Resource Allocation', y='Mental Fatigue Score', hue='Company Type', data=df)
    plt.title('Resource Allocation vs Mental Fatigue Score by Company Type')
    plt.xlabel('Resource Allocation')
    plt.ylabel('Mental Fatigue Score')
    plt.savefig(filepath)
    plt.close()

def burn_wfh_designation(filepath):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Designation', y='Burn Rate', hue='WFH Setup Available', data=df)
    plt.title('Burn Rate by WFH Setup and Designation')
    plt.xlabel('Designation')
    plt.ylabel('Burn Rate')
    plt.savefig(filepath)
    plt.close()

def resource_distribution(filepath):
    plt.figure(figsize=(10, 6))
    sns.histplot(x='Resource Allocation', hue='Gender', data=df, element='step')
    plt.title('Resource Allocation Distribution by Gender')
    plt.xlabel('Resource Allocation')
    plt.ylabel('Count')
    plt.savefig(filepath)
    plt.close()

def mental_fatigue_vs_burn(filepath):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Mental Fatigue Score', y='Burn Rate', hue='Gender', data=df)
    plt.title('Mental Fatigue Score vs Burn Rate')
    plt.xlabel('Mental Fatigue Score')
    plt.ylabel('Burn Rate')
    plt.savefig(filepath)
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)
