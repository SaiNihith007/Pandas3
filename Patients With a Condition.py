import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    #sol1
    # result = []

    # for i in range(len(patients)):
    #     patient_id = patients['patient_id'][i]
    #     patient_name = patients['patient_name'][i]
    #     conditions = patients['conditions'][i]

    #     for condition in conditions.split():
    #         if condition.startswith('DIAB1'):
    #             result.append([patient_id,patient_name,conditions])
    #             break

    # return pd.DataFrame(result, columns =['patient_id','patient_name','conditions']) 

    #sol2
    # patients = patients[patients['conditions'].str.startswith('DIAB1')|
    #                     patients['conditions'].str.contains(' DIAB1') ] 
    # return patients      

    #sol3
    return patients[patients['conditions'].str.contains( r"(^|\s)DIAB1", regex =True)]                     
    