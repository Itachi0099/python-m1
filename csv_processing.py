import pandas as pd 
df = pd.read_csv('students.csv')
# Display the original DataFrame
print("Original DataFrame:")
print(df)
filtered_df = df[df['Score'] >= 85]
print("\nFiltered DataFrame (Score >= 85):")
print(filtered_df)

#students who passed 
if 'Passed' not in df.columns:
    df['Passed'] = df['Score'] >= 85
passed_df = df[df['Passed'] == True]
print("\nStudents who passed:")
print(passed_df)

# select only name+score 
passed_df [["Name", "Score"]]

final_df = passed_df[["Name", "Score"]]
final_df.to_csv('passed_students.csv', index=False)