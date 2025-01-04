from io import BytesIO
import json
import boto3
import plotly.io as pio
import plotly.express as px
import pandas as pd
s3 = boto3.client('s3')
bucket_name = 'justin-ml-bucket' 
file_key = 'Elysia.Laps.feather'

def cleanLapData(df: pd.DataFrame):
    df = df.drop(
        columns=[
            "msgType",
            "_id.$oid",
            "averagepackCurrent.$numberDouble",
            "timestamp.$numberLong",
        ]
    )
    df = df.dropna(subset=["averagepackCurrent"])
    return df

def generateCorrelationMatrix(df: pd.DataFrame):
    correlation_matrix = df.corr(numeric_only=True)
    return px.imshow(correlation_matrix, title="Correlation Matrix for Helios Data")

def analyzeLapData(df: pd.DataFrame):
    cleanedDF = cleanLapData(df)
    return generateCorrelationMatrix(cleanedDF)

def lambda_handler(event, context):
    try: 
        response = s3.get_object(Bucket=bucket_name, Key=file_key) 
        file_content = response['Body'].read() 
        buffer = BytesIO(file_content)
        lapDataDF = pd.read_feather(buffer)
        figure = analyzeLapData(lapDataDF)
        return { 'statusCode': 200, 'body': json.dumps(pio.to_json(figure))} 
    except Exception as e: 
      return { 'statusCode': 500, 'body': json.dumps(str(e))}