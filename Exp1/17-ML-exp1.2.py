import pandas as pd 
import numpy as np 
print("\n==================== 1. Series Creation ====================") 
# Series from list 
s1 = pd.Series([10, 20, 30, 40]) 
print("Series from list:\n", s1) 
# Series with custom index 
s2 = pd.Series([1, 2, 3], index=['a','b','c']) 
print("\nSeries with custom index:\n", s2)
# Series from dictionary 
s3 = pd.Series({'x': 100, 'y': 200}) 
print("\nSeries from dictionary:\n", s3)

print("\n==================== 2. DataFrame Creation ====================") 
# From dictionary 
df1 = pd.DataFrame({ 
'Name': ['Alice','Bob','Charlie'], 
'Age': [25,30,35], 
'City': ['NY','LA','Chicago'] 
}) 
print("DataFrame from dictionary:\n", df1) 
# From NumPy array 
arr = np.arange(9).reshape(3,3) 
df2 = pd.DataFrame(arr, columns=['A','B','C']) 
print("\nDataFrame from NumPy array:\n", df2) 
# From list of lists 
df3 = pd.DataFrame([[1,2],[3,4],[5,6]], columns=['X','Y']) 
print("\nDataFrame from list of lists:\n", df3) 

print("\n==================== 3. Viewing Data ====================") 
print("Head of df1:\n", df1.head(2)) 
print("Tail of df1:\n", df1.tail(2)) 
print("Columns of df1:", df1.columns) 
print("Index of df1:", df1.index) 
print("Shape of df1:", df1.shape) 
print("Info of df1:") 
print(df1.info()) 
print("Describe numeric data in df1:\n", df1.describe())

print("\n==================== 4. Selection & Indexing ====================") 
print("Select 'Name' column:\n", df1['Name']) 
print("Select multiple columns:\n", df1[['Name','City']]) 
print("Select row by loc:\n", df1.loc[1]) 
print("Select row by iloc:\n", df1.iloc[0]) 
print("Select specific element:\n", df1.loc[1,'City']) 

print("\n==================== 5. Filtering & Boolean Indexing ====================") 
print("Rows where Age > 28:\n", df1[df1['Age']>28]) 
print("Rows where City is 'NY':\n", df1[df1['City']=='NY']) 

print("\n==================== 6. Adding & Modifying Columns ====================") 
df1['Salary'] = [50000, 60000, 70000] 
print("After adding Salary:\n", df1) 
df1['AgePlus5'] = df1['Age'] + 5 
print("After modifying/adding AgePlus5:\n", df1)

print("\n==================== 7. Dropping Rows/Columns ====================") 
df_dropped = df1.drop('AgePlus5', axis=1) 
print("After dropping column AgePlus5:\n", df_dropped) 
df_dropped_row = df1.drop(0, axis=0) 
print("After dropping row 0:\n", df_dropped_row) 

print("\n==================== 8. Handling Missing Data ====================") 
df_missing = pd.DataFrame({ 
'A':[1,np.nan,3], 
'B':[4,5,np.nan] 
}) 
print("DataFrame with missing values:\n", df_missing) 
print("Drop rows with NaN:\n", df_missing.dropna()) 
print("Fill NaN with 0:\n", df_missing.fillna(0)) 
print("Check for NaN:\n", df_missing.isna()) 

print("\n==================== 9. Aggregation Functions ====================") 
print("Sum of numeric columns:\n", df1[['Age','Salary']].sum()) 
print("Mean of numeric columns:\n", df1[['Age','Salary']].mean()) 
print("Max of numeric columns:\n", df1[['Age','Salary']].max()) 
print("Min of numeric columns:\n", df1[['Age','Salary']].min()) 
print("Describe:\n", df1[['Age','Salary']].describe()) 

print("\n==================== 10. Grouping & Aggregation ====================") 
df_group = pd.DataFrame({ 
'Department':['HR','IT','HR','IT','IT'], 
'Employee':['Alice','Bob','Charlie','David','Eve'], 
'Salary':[50000,60000,55000,65000,70000] 
}) 
print("Original DataFrame:\n", df_group) 
grouped = df_group.groupby('Department')['Salary'].mean() 
print("Average salary by Department:\n", grouped)

print("\n==================== 11. Sorting ====================") 
print("Sort by Age ascending:\n", df1.sort_values('Age')) 
print("Sort by Salary descending:\n", df1.sort_values('Salary', ascending=False)) 

print("\n==================== 12. Merging / Concatenation ====================") 
df_a = pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']}) 
df_b = pd.DataFrame({'ID':[2,3,4],'Score':[90,80,70]}) 
merged_df = pd.merge(df_a, df_b, on='ID', how='outer') 
print("Merged DataFrame (outer join):\n", merged_df) 
concat_df = pd.concat([df_a, df_b], ignore_index=True) 
print("Concatenated DataFrame:\n", concat_df)

print("\n==================== 13. File I/O ====================") 
# Save to CSV 
df1.to_csv('df1.csv', index=False) 
print("DataFrame saved to 'df1.csv'") 
# Read from CSV 
df_loaded = pd.read_csv('df1.csv') 
print("Loaded DataFrame:\n", df_loaded) 
print("\nAll major Pandas functions executed successfully!") 