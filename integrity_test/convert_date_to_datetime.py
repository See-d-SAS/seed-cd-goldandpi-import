import pandas as pd

def convert_date_to_datetime(date : str, format_list : list = ['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y']) -> bool:
    """ Converts any date format into datetime if this date is of the type present in format_list
    In:
        date : date we want to convert
        format_list : list of accepted date formats
    Results: see above
    Out: 
        converted date
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
    for fmt in format_list:
        try:
            return pd.to_datetime(date, format=fmt)
        except ValueError:
            continue
    return pd.NaT