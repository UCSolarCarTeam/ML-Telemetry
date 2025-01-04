from io import BytesIO
import json
import boto3
import plotly.io as pio
import plotly.express as px
import pandas as pd
import numpy as np

s3 = boto3.client('s3')
bucket_name = 'justin-ml-bucket' 
file_key = 'Elysia.Packets.feather'

def cleanPacketData(df: pd.DataFrame):
    cols_with_missing = [col for col in df.columns if df[col].isnull().all()]
    df = df.drop(cols_with_missing, axis=1)

    constant_columns = []
    for col in df.columns:
        if isinstance(df[col][0], (list, np.ndarray)):
            continue
        if(df[col].nunique() == 1):
            constant_columns.append(col)

    df= df.drop(columns=constant_columns, axis=1)
    return df


def generateCorrelationMatrix(df: pd.DataFrame):
    correlation_matrix = df.corr(numeric_only=True)
    return px.imshow(correlation_matrix, title="Correlation Matrix for Helios Data")

def analyzePacketData(df: pd.DataFrame):
    cleanedDF = cleanPacketData(df)
    return generateCorrelationMatrix(cleanedDF)

def lambda_handler(event, context):
    try: 
        response = s3.get_object(Bucket=bucket_name, Key=file_key) 
        file_content = response['Body'].read() 
        buffer = BytesIO(file_content)
        packetDataDF = pd.read_feather(buffer)
        figure = analyzePacketData(packetDataDF)
        return { 'statusCode': 200, 'body': json.dumps(pio.to_json(figure))} 
    except Exception as e: 
      return { 'statusCode': 500, 'body': json.dumps(str(e))}