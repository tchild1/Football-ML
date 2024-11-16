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


# now sum all columns that are identical except end in q1 q2 q3 q4 and then create a new column for each with x_total

# first create a list of columns that end in q1 q2 q3 q4
quarter_columns = []
for column in df.columns:
    if column.endswith('q1') or column.endswith('q2') or column.endswith('q3') or column.endswith('q4'):
        quarter_columns.append(column)

# now sum the columns that are identical except end in q1 q2 q3 q4
for column in df.columns:
    if column.endswith('q1'):
        column_name = column[:-2]
        print("Summing ", column_name)
        df[column_name + 'total'] = df[column] + df[column[:-1] + '2'] + df[column[:-1] + '3'] + df[column[:-1] + '4']


# save the cleaned data
df.to_csv('./compiledData/cleanedCompiledData.csv', index=False)