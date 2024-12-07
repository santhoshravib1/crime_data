import pandas as pd

FILE_PATH = 'Crime_Data_from_2020_to_Present.csv'

def findMean():
    try:
        df = pd.read_csv(FILE_PATH)
        return df['Vict Age'].mean()
    except KeyError:
        print("Error: Column 'Vict Age' not found in the file.")
        return None

def findMedian():
    try:
        df = pd.read_csv(FILE_PATH)
        return df['Vict Age'].median()
    except KeyError:
        print("Error: Column 'Vict Age' not found in the file.")
        return None

if __name__ == "__main__":
    print("Mean Vict Age:", findMean())
    print("Median Vict Age:", findMedian())

