from sklearn.preprocessing import StandardScaler
import pandas as pd
def prepocesamiento(df):
    #Separar features y target
    X = df.drop("churn", axis=1)
    y = df["churn"]
    #Escalado
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y

