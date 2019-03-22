import preprocess as p
from sklearn.preprocessing import LabelEncoder

def clean_data(df):
    encoder = LabelEncoder()
    
    col_to_encode = ["inverter_mfg","inverter_model","module_mfg","module_model","module_tech","inverter_mfg"]
    
    for col in col_to_encode:
      df[col] = df[col].fillna('undefined')
      df[col] = encoder.fit_transform(df[col].astype(str))

    return p.common_clean_data(df)
