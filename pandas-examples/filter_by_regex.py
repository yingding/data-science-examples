"""
Reference:
https://stackoverflow.com/questions/15325182/how-to-filter-rows-in-pandas-by-regex
"""
import pandas as pd

def main():
    # create a data frame
    df = pd.DataFrame({'a' : [1,2,3,4], 'b' : ['hi', 'foo', 'fat', 'cat']})
    print(df)

    # select all row with column b begins with f
    filtered_df = df[df.b.str.contains("^f.*")]
    print(filtered_df)

    # select all row with column b doesn't begins with f
    filtered_df = df[~df.b.str.contains("^f.*")]
    print(filtered_df)

    # select all row with column b doesn't begins with f
    filtered_df = df[~df["b"].str.contains("^f.*")]
    print(filtered_df)

if __name__ == "__main__":
    main()
