import os
import pandas as pd 
import numpy as np


class GetData(object):
    def __init__(self, path):
        self.path = path
        allfiles = [f for f in os.listdir(path) if f.endswith('.maf')]
        data = self.read_data(allfiles)
        self.patientDf = data[0]
        self.aggDf = data[1]
      
        

    def read_data(self, files:list):
        path = self.path + '/'
        Patients = {}
        allPatients = []
        for patient in files:
            patientId = patient.split('.')[0]
            patientDf = pd.read_table(path+patient)
            allpatDf = pd.read_table(path+patient, header=0, index_col=None)
            allPatients.append(allpatDf)
            Patients[patientId] = patientDf
        aggDf = pd.concat(allPatients, ignore_index=True)
        return (Patients,aggDf)

#For testing
if __name__ == '__main__':
    d = GetData('data/mafs')
    print(d.patientDf.keys())
