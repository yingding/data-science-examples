"""
examples of working with pandas series
to encode the series value with tranformations

Goal is to encode the following Series 
0  1  3  4  6  7  9 10 12 13 17 20

to 

0  1  2  3  4  5  6  7  8  9 10 11

and also to decode it later.
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
    origin_series: Series = Series([0, 1,  3,  4,  6,  7,  9, 10, 12, 13, 17, 20])
    encoder, decoder = create_encoder_decoder_maps(origin_series)
   
    print(encoder)
    print(decoder)

    # replace the value in series
    encoded_series = origin_series.map(encoder)
    decoded_series = encoded_series.map(decoder)
    print(f"origin  series: {origin_series.values}")
    print(f"encoded series: {encoded_series.values}")
    print(f"decoded series: {decoded_series.values}")

    print(decoded_series)

if __name__ == "__main__":
    main()