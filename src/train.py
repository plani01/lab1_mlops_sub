import joblib
import os
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def run_training(): 
    """
    Train the model
    """
    # Read the training data 
    #dataset = pd.read_csv('data/IRIS.csv')

    column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
                'acceleration', 'model_year', 'origin', 'car_name']

    df = pd.read_csv('data/auto-mpg.data', 
                 sep='\s+',  # whitespace separator
                 names=column_names,
                 na_values='?')
    
    # Filling Null entries with the mean:
    df['horsepower']=df['horsepower'].fillna(df['horsepower'].mean())

    # split into features and target 
    y = df['mpg'].to_numpy()
    X = df.drop(columns=['mpg', 'car_name'], axis=-1)#.to_numpy()

    # Split into labels and targets
    # X = dataset.drop("species", axis=1).copy()
    # y = dataset["species"].copy()

    # Create train and test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=26)

    # Training the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    model.feature_names = X.columns

    # Persist the trained model
    if not os.path.exists("../model"):
        os.makedirs("../model")
    joblib.dump(model, "../model/model.pkl")

if __name__ == "__main__":
    run_training()
