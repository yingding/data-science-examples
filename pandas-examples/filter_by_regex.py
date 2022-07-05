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

    # replace all string value with its first char
    repl = lambda m: m.group(0)[:1]
    rep_df = df["b"].str.replace('.*', repl, regex=True)
    print(rep_df)

    # replace all string value with int value
    repl = lambda s: ord(s[:1]) - ord('a')
    rep_df = df["b"].transform(repl)
    print(rep_df)

    # test series isin for int list
    s = pd.Series([1, 2, 3, 4, 5, 6], name='animal')
    idx = s.isin([1, 2])
    print(idx)




if __name__ == "__main__":
    main()
