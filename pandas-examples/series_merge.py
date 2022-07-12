"""
examples of working with pandas series
to merge to series to a data frame

Goal is to merge the following Series 
Serie 1:
0  1  3  4  6  7  9 10 12 13 17 20
Serie 2:
0  1  2  3  4  5  6  7  8  9 10 11

https://pandas.pydata.org/docs/user_guide/merging.html
Series concat on index
https://sparkbyexamples.com/pandas/pandas-combine-two-series-into-dataframe/
"""

import pandas as pd
from pandas import Series
from typing import Tuple, Dict

def create_encoder_decoder_maps(s: Series) -> Tuple[Dict, Dict]:
    origin: list = s.value_counts().index.to_list()
    origin.sort(reverse=False) # use sort so that the 0 is at the very beginning
    target: list = list(range(len(origin)))
    _encoder_map = dict(zip(origin, target)) # this code loops multiple time, there is better way to do so.
    _decoder_map = dict(zip(target, origin))
    return _encoder_map, _decoder_map

    

def main():
    serie1: Series = Series([0, 1,  3,  4,  6,  7,  9, 10, 12, 13, 17, 20], name="serie1")
    serie2: Series = Series(list(range(len(serie1))), name = "serie2")

    df = pd.concat([serie1, serie2], axis=1) # concat on idx
    print(df)


if __name__ == "__main__":
    main()