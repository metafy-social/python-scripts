import pandas as pd 

def makeExcel():
    df = pd.read_csv('Path to your CSV file.csv')
    # index and header can be set True or False accoring to needs
    df.to_excel('Path where save as Excel file.xlsx', index=False, header=True)
    print('Converted Successfuly')

if __name__ == "__main__":
    makeExcel()