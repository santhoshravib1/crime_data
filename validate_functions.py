import pandas as pd

FILE_PATH = 'Crime_Data_from_2020_to_Present.csv'

def checkVictSex():
    try:
        df = pd.read_csv(FILE_PATH)
        column = 'Vict Sex'

        if df[column].isnull().any():
            return False
        elif not set(df[column].dropna().unique()).issubset({'M', 'F'}):
            return False
        else:
            return True
    except KeyError:
        print(f"Error: Column '{column}' not found in the file.")
        return False

def checkVictAge():
    try:
        df = pd.read_csv(FILE_PATH)
        column = 'Vict Age'

        if df[column].isnull().any():
            return False
        elif not df[column].dropna().between(1, 100).all():
            return False
        else:
            return True
    except KeyError:
        print(f"Error: Column '{column}' not found in the file.")
        return False

