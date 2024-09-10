from sklearn.preprocessing import StandardScaler
import pandas as pd
import sqlite3
import json

conn = sqlite3.connect('app/database.sqlite')

cursor = conn.cursor()

query = 'SELECT * FROM packetData LIMIT 1;'


def parsed_json(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None
    
df = pd.read_sql_query(query, conn)

df_packetData = df["data"]

parsed_data = df['data'].apply(parsed_json).apply(pd.json_normalize)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

conn.close()

cleaned_df = pd.concat(parsed_data.tolist(),ignore_index=True)



# #Function to anaylze the intial data to identify any inconsistencies or anomalies
# def analyze_data_initial(data):
#     print(data[:5])
#     print(data.describe())
#     print(data.isnull().sum())

# #Function to handle missing values, outliers and normalize the data
# def clean_data(data):
    
#     #Handling missing values
#     cleaned_data = data.fillna(data.median())

#     #Handling outliers: removing values beyond 3 standard deviations
#     for col in cleaned_data.columns:
#         mean = clean_data[col].mean()
#         std = clean_data[col].std()
#         cleaned_data = clean_data[(clean_data[col] > mean - 3*std) & (clean_data[col] < mean + 3*std)]
    
#     #Normalizing/Scaling the data
#     scaler = StandardScaler()
#     cleaned_data = scaler.fit_transform(cleaned_data)
    
#     return cleaned_data

# analyze_data_initial(example_data)
# cleaned_data = clean_data(example_data)
# print(cleaned_data)
