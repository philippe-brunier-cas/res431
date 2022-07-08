import pandas as pd

def MapTable(datafile,header_file):
    header = pd.read_csv(os.path.join(os.getcwd(),'mapping',header_file),sep=';')
    
    df = pd.read_csv(datafile, sep=';',
                     # dtype = header.data_type.values,
                     )
    
    df = df.set_axis(header.col_name, axis=1, inplace=False)
    
    #drop delle colonne non interessanti
    to_use = header[header.grab != 0].col_name
    return df[to_use]
