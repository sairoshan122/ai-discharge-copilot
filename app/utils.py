
import pandas as pd

def load_patients(path):
    return pd.read_csv(path, encoding='utf-8')

def load_knowledge(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
