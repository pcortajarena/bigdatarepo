from . import preprocess as p

def clean_data(df):
    df = df.copy()
    return p.common_clean_data(df)