
## Author: I-En Wu, Lateefat Kalejaya, Pin-Kuang Lai*

# ------------------------------------------- Package Import ------------------------------------------- #

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# -------------------------------- Read the SAPSCM.csv file from DeepSP -------------------------------- #

dataset_test = pd.read_csv('SAPSCM.csv')

# -------------------------------- Features Selection and Transformation ------------------------------- #

feature_ACSINS = dataset_test[['SAP_pos_CDRH1', 'SAP_pos_CDRL3', 'SCM_pos_CDRH1','SCM_neg_CDR']]
feature_AS = dataset_test[['SAP_pos_CDRH2','SCM_pos_CDRL2','SCM_pos_CDRL3','SCM_neg_CDRL3']]
feature_BVP = dataset_test[['SAP_pos_CDRH1','SAP_pos_CDRH3','SCM_pos_CDR','SCM_neg_CDRH3']]
feature_CIC = dataset_test[['SAP_pos_CDRL2', 'SAP_pos_CDRL3', 'SAP_pos_Lv','SCM_neg_CDR']]
feature_CSI = dataset_test[['SAP_pos_CDRL1', 'SAP_pos_Lv', 'SCM_pos_CDRH2','SCM_neg_CDRL2']]
feature_ELISA = dataset_test[['SAP_pos_CDRH3', 'SCM_pos_CDR','SCM_neg_CDR']]
feature_HIC = dataset_test[['SAP_pos_CDRL3', 'SAP_pos_CDR','SAP_pos_Hv','SCM_pos_CDRH3']]
feature_HEK = dataset_test[['SAP_pos_CDRH2','SAP_pos_CDRL3','SCM_pos_Lv','SCM_neg_Lv']]
feature_PSR = dataset_test[['SAP_pos_Lv', 'SCM_pos_CDRH2', 'SCM_neg_CDRL2']]
feature_SGAC = dataset_test[['SAP_pos_CDRH1', 'SAP_pos_CDRL3', 'SCM_neg_CDRH2','SCM_neg_Lv']]
feature_SMAC = dataset_test[['SAP_pos_CDR', 'SAP_pos_Fv', 'SCM_neg_CDRL2','SCM_neg_Fv']]
feature_Tm = dataset_test[['SAP_pos_CDRH1', 'SAP_pos_CDRH2', 'SCM_pos_CDRH3']]

sc = StandardScaler()

X_ACSINS = feature_ACSINS.values
X_AS = feature_AS.values
X_BVP = feature_BVP.values
X_CIC = feature_CIC.values
X_CSI = feature_CSI.values
X_ELISA = feature_ELISA.values
X_HIC = feature_HIC.values
X_HEK = feature_HEK.values
X_PSR = feature_PSR.values
X_SGAC = feature_SGAC.values
X_SMAC = feature_SMAC.values
X_Tm = feature_Tm.values

X_ACSINS = sc.fit_transform(X_ACSINS)
X_AS = sc.fit_transform(X_AS)
X_BVP = sc.fit_transform(X_BVP)
X_CIC = sc.fit_transform(X_CIC)
X_CSI = sc.fit_transform(X_CSI)
X_ELISA = sc.fit_transform(X_ELISA)
X_HIC = sc.fit_transform(X_HIC)
X_HEK = sc.fit_transform(X_HEK)
X_PSR = sc.fit_transform(X_PSR)
X_SGAC = sc.fit_transform(X_SGAC)
X_SMAC = sc.fit_transform(X_SMAC)
X_Tm = sc.fit_transform(X_Tm)

# -------------------------------- Predictive Model Import ------------------------------- #

ACSINS_SVR_model = joblib.load('Trained_model/ACSINS_SVR_model.joblib')
AS_LR_model = joblib.load('Trained_model/AS_LR_model.joblib')
BVP_KNN_model = joblib.load('Trained_model/BVP_KNN_model.joblib')
CIC_KNN_model = joblib.load('Trained_model/CIC_KNN_model.joblib')
CSI_SVR_model = joblib.load('Trained_model/CSI_SVR_model.joblib')
ELISA_KNN_model = joblib.load('Trained_model/ELISA_KNN_model.joblib')
HEK_KNN_model = joblib.load('Trained_model/HEK_KNN_model.joblib')
HIC_SVR_model = joblib.load('Trained_model/HIC_SVR_model.joblib')
PSR_SVR_model = joblib.load('Trained_model/PSR_SVR_model.joblib')
SGAC_SVR_model = joblib.load('Trained_model/SGAC_SVR_model.joblib')
SMAC_KNN_model = joblib.load('Trained_model/SMAC_KNN_model.joblib')
Tm_KNN_model = joblib.load('Trained_model/Tm_KNN_model.joblib')

# --------------------------- Biophysical Properties Prediction -------------------------- #

ACSINS_transformed,AS,BVP,CIC_transformed,CSI_transformed,ELISA,HIC,HEK,PSR,SGAC_transformed,SMAC_transformed,Tm =[],[],[],[],[],[],[],[],[],[],[],[]

for index,row in dataset_test.iterrows():

  feature_ACSINS = X_ACSINS[index]
  prediction_ACSINS = ACSINS_SVR_model.predict(feature_ACSINS.reshape(1,-1))
  feature_AS = X_AS[index]
  prediction_AS = AS_LR_model.predict(feature_AS.reshape(1,-1))
  feature_BVP = X_BVP[index]
  prediction_BVP = BVP_KNN_model.predict(feature_BVP.reshape(1,-1))
  feature_CIC = X_CIC[index]
  prediction_CIC = CIC_KNN_model.predict(feature_CIC.reshape(1,-1))
  feature_CSI = X_CSI[index]
  prediction_CSI = CSI_SVR_model.predict(feature_CSI.reshape(1,-1))
  feature_ELISA = X_ELISA[index]
  prediction_ELISA = ELISA_KNN_model.predict(feature_ELISA.reshape(1,-1))
  feature_HIC = X_HIC[index]
  prediction_HIC = HIC_SVR_model.predict(feature_HIC.reshape(1,-1))
  feature_HEK = X_HEK[index]
  prediction_HEK = HEK_KNN_model.predict(feature_HEK.reshape(1,-1))
  feature_PSR = X_PSR[index]
  prediction_PSR = PSR_SVR_model.predict(feature_PSR.reshape(1,-1))
  feature_SGAC = X_SGAC[index]
  prediction_SGAC = SGAC_SVR_model.predict(feature_SGAC.reshape(1,-1))
  feature_SMAC = X_SMAC[index]
  prediction_SMAC = SMAC_KNN_model.predict(feature_SMAC.reshape(1,-1))
  feature_Tm = X_Tm[index]
  prediction_Tm = Tm_KNN_model.predict(feature_Tm.reshape(1,-1))

  ACSINS_transformed.append(prediction_ACSINS)
  AS.append(prediction_AS)
  BVP.append(prediction_BVP)
  CIC_transformed.append(prediction_CIC)
  CSI_transformed.append(prediction_CSI)
  ELISA.append(prediction_ELISA)
  HIC.append(prediction_HIC)
  HEK.append(prediction_HEK)
  PSR.append(prediction_PSR)
  SGAC_transformed.append(prediction_SGAC)
  SMAC_transformed.append(prediction_SMAC)
  Tm.append(prediction_Tm)

# ------------------------------- Result Sheet Generation ------------------------------ #
  
Name = dataset_test[['Name']].to_numpy()
data = np.column_stack((Name,ACSINS_transformed,AS,BVP,CIC_transformed,CSI_transformed,ELISA,HIC,HEK,PSR,SGAC_transformed,SMAC_transformed,Tm))
np.savetxt('Prediction_Result.csv', data, delimiter=',', fmt='%s', header='Name,ACSINS_transformed,AS,BVP,CIC_transformed,CSI_transformed,ELISA,HIC,HEK,PSR,SGAC_transformed,SMAC_transformed,Tm', comments='')
