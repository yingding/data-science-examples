"""
examples of working with pandas series
"""

import pandas as pd
from pandas import Series


def main():
    series: Series = Series([1, 2, 3, 3, 4, 5,5,5])
    print(series.values)
    print(series.index)
    print(series.value_counts())
    print(series.value_counts().index.to_list())
    print(chr(69))

if __name__ == "__main__":
    main()