from dateutil.parser import parse
import numpy as np

def common_clean_data(df):
    if isinstance(df['time'][0], str):
        df['time'] = df.time.apply(lambda time: parse(time))
    df['year'] = df.time.apply(lambda time: time.timetuple().tm_year)
    df['yday'] = df.time.apply(lambda time: time.timetuple().tm_yday)
    df['hour'] = df.time.apply(lambda time: time.timetuple().tm_hour)
    df['sin_hour'] = df.hour.apply(lambda hour: np.sin(np.pi*hour/12))
    df['sin_month'] = df.time.apply(lambda time: np.sin(np.pi*time.timetuple().tm_mon/12))
    
    df.drop(['time'], axis=1, inplace=True)
    return df