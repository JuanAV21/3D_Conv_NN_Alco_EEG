import pandas as pd
import numpy as np
import glob

class loadData:
    def __init__(self, cwd):
        self.files = glob.glob(cwd)
        print("Done")
        
    def forward(self, alco_limit = 233):
        
        self.matrix = []
        self.a_Matrix = []
        self.c_Matrix = []
        self.annotations = []
        
        df = pd.read_csv(self.files[0])
        self.channels = pd.unique(df["sensor position"])
        length = len(self.files)
           
        aLimit = 0
        for indx in range(length):
            df = pd.read_csv(self.files[indx])
            sensorData = []
            for ch in self.channels:
                temp = df.loc[df["sensor position"] == ch]
                sensorData.append(temp["sensor value"].tolist())
            if df.iloc[0, 5] == 'c':
                self.c_Matrix.append(sensorData)
                self.annotations.append(0)
            else: 
                if aLimit <= alco_limit:
                    self.a_Matrix.append(sensorData)
                    self.annotations.append(1)
                    aLimit += 1
            self.matrix.append(sensorData)
        print("Done with forward")
