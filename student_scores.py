import pandas as pd
dict1 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Score': [85, 92, 78, 90]}
df = pd.DataFrame(dict1)
print("Original DataFrame:")
print(df)
average_score = df['Score'].mean()
print("\nAverage Score:", average_score)
sorted_df = df.sort_values(by='Score', ascending=False)
print("\nDataFrame sorted by Score in descending order:")
print(sorted_df)


#837D-6F5A. 