"""
This pandas demo shows how to filter pandas dataframe columns with condition


Reference:
https://stackoverflow.com/questions/37663931/selecting-columns-with-condition-on-pandas-dataframe
"""
import pandas as pd
from pandas import Series

def filter_series(s: Series, value)-> Series:
    """
    https://stackoverflow.com/a/37663969/3569768
    https://stackoverflow.com/questions/37663931/selecting-columns-with-condition-on-pandas-dataframe
    @return a single row dataframe with all positive hpo column selected
    """
    # return df[(df == value).any(1)] .iloc[0]
    # s: Series = df.iloc[0]
    return s[s == value]

def main():
    # create a data frame
    df = pd.DataFrame({'a' : [1,2,3,4], 'b' : ['hi', 'foo', 'fat', 'cat']})
    print(df)

    print((df == 'hi').any(1))

    col_conditions = (df == 'hi').any(1)
    print(df[col_conditions])

    series: Series = df[col_conditions].iloc[0]
    print(filter_series(series, 'hi').index.tolist())




if __name__ == "__main__":
    main()
