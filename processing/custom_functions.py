import datetime
import pandas as pd

def fill_pain_scale_na_with_cpc_mean(dataset):
    return (dataset['PainScale'].fillna(dataset.
                 groupby('PresentingComplaint')['PainScale'].transform("mean")))

def DOBtoAGE(dataset, DOB):

    dataset[DOB] = pd.to_datetime(dataset[DOB])

    def GetAGEfromDOB(DOB):
        currentDT = datetime.datetime.now()
        return currentDT.year - DOB.year

    dataset[DOB] = dataset[DOB].apply(GetAGEfromDOB)

    return dataset
