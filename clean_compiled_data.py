import pandas as pd

df = pd.read_csv('./compiledData/compliedData.csv')
# count number of nan values in each column and print those with more than 0
print(df.columns)
for column in df.columns:
    if df[column].isnull().sum() > 1000:
        print(column, " has ", df[column].isnull().sum(), " nan values... Dropping column")
        # drop columns with more than 1000 nan values
        df.drop(column, axis=1, inplace=True)
print("Total rows: ", len(df))


# check the quantity of unique values in each column
for column in df.columns:
    print(column, " has ", df[column].nunique(), " unique values")

# save the cleaned data
df.to_csv('./compiledData/cleanedCompiledData.csv', index=False)