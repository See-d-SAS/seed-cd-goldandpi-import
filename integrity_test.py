# import numpy as np
import pandas as pd
from isa4ai_library_pc.unitary_software_functions.convert_date_to_datetime.V0_0_0.convert_date_to_datetime import convert_date_to_datetime

def integrity_test(data : pd.DataFrame) -> bool:
    """ Performs an integrity test on the data
    The following conditions must be met:
        Management of NaN None, N/A, etc 
        Date format management
        Respecting formats
    In: 
        data : input data
    Results: see above
    Out: 
        True if 
    Version: 0 
        Version's description:
        Author: Matthieu Grondin
    Release: 0
        Release's description:
        Author: Matthieu Grondin
    Tag: 0
        Tag's evolution description:
        Author: Matthieu Grondin
    """
    nan_values_to_replace = ['NaN', 'NULL', 'None', 'N/A']
    # data.replace(nan_values_to_replace, np.nan, inplace = True)
    data_dates = data.applymap(convert_date_to_datetime)
    
    null_dates = data_dates.isna().mean()
    columns_to_watch_dates = null_dates[(null_dates<1) & (null_dates>0.7)].index.tolist()
    if columns_to_watch_dates:
        raise ValueError(f"Date format error in column(s) '{','.join(columns_to_watch_dates)}', index {data_dates.index[data_dates[columns_to_watch_dates].isna().any(axis = 1)]}")
    
    columns_to_watch_none = data.isin(nan_values_to_replace).any()
    columns_to_watch_none = columns_to_watch_none[columns_to_watch_none].index.tolist()
    if columns_to_watch_none:
        raise ValueError(f"Different types of None in the columns {','.join(columns_to_watch_none)}")
    return True