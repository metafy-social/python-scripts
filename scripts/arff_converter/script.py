from scipy.io.arff import loadarff
import pandas as pd


def arff_to_csv(data, out_file_name):

    df = pd.DataFrame(loadarff(data)[0])
    df.to_csv(out_file_name, index=False)


def arff_to_excel(data, out_file_name):

    df = pd.DataFrame(loadarff(data)[0])
    df.to_excel(out_file_name, index=False)
