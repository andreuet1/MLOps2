from sklearn.ensemble import RandomForestClassifier
def entrenamiento(X_train, y_train):
    #Entrenamiento del modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model    