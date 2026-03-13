import pandas as pd
# Carar el dataset
def cargar_datos():
    df = pd.read_csv("empleados.csv")
    return df