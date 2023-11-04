

import pandas as pd

def load(file_path):
  data= pd.read_csv(file_path)

  return data

if __name__ == '__main__':
  file_path=input("enter path")


  D=load(file_path)

  print(D)

