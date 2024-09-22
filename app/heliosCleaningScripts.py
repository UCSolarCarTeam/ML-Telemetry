from sklearn.preprocessing import StandardScaler
import pandas as pd
import sqlite3
import json
import numpy as np
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

def readPacketData(connectionURL: str):

    conn = sqlite3.connect('database.sqlite')

    query = 'SELECT * FROM packetData LIMIT 100;'


    def parsed_json(json_str):
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return None
        
    df = pd.read_sql_query(query, conn)

    parsed_data = df['data'].apply(parsed_json).apply(pd.json_normalize)
    conn.close()
    return parsed_data

def cleanData(parsed_data: pd.DataFrame):
    cleaned_df = pd.concat(parsed_data.tolist(),ignore_index=True)
    numerical_df = cleaned_df.select_dtypes(np.number)

    outliers = {}
    for column in numerical_df.columns:
        Q1 = numerical_df[column].quantile(0.25)
        Q3 = numerical_df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        column_outliers = numerical_df[(numerical_df[column] < lower_bound) | (numerical_df[column] > upper_bound)]
        outliers[column] = column_outliers[column].tolist()

    #remove the outliers
    for column, outlier_values in outliers.items():
        cleaned_df = cleaned_df[~cleaned_df[column].isin(outlier_values)]

    # Normalize/Scale the data
    scaler = StandardScaler()
    numerical_columns = cleaned_df.select_dtypes(include=[np.number]).columns
    cleaned_df[numerical_columns] = scaler.fit_transform(cleaned_df[numerical_columns])

    return cleaned_df

def main():
    databaseConnection = "database.sqlite"
    packetData = readPacketData(databaseConnection)
    cleanedDf = cleanData(packetData)
    print(cleanedDf)

main()
