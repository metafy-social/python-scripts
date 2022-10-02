import pandas as pd 
import os,json

def csv_to_json():
    file = input("Enter csv path: ")
    df = pd.read_csv(file)
    name=os.path.basename(file).replace("csv","json")
    data =df.to_dict("r")
    with open(file,'w') as f:
        json.dump(df, d)
    
    print(f"file saved at {name}")


csv_to_json()