import pandas as pd


data = {'rocket' :['Falcon 1', 'Falcon 9', 'Falcon Heavy', 'Falcon Heavy Block5'], 'launches':[89,100,4,2]}

df = pd.DataFrame(data)


# Select and print the 'rocket' column.

print(df['rocket'])

#Filter the DataFrame for rockets with more than 5 launches.

launch5_df = df[df['launches'] >= 5]
#print(launch5_df)


# Add a new column for 'success_rate'.

df['success_rate'] = [0.2,0.94,0.45, 1]

print(df)