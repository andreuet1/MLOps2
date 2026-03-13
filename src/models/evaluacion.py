import json
from xml.parsers.expat import model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from datetime import datetime
 
 
def evaluacion(model, X_test, y_test):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"metrics_{timestamp}.json"
 
 
    predictions = model.predict(X_test)
 
    #accuracy = accuracy_score(y_test, predictions)
 
    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
        "f1_score": f1_score(y_test, predictions)
    }
 
    with open(filename, "w") as f:
        json.dump(metrics, f, indent=4)
   
    return metrics
 