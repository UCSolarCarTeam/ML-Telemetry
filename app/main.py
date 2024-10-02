import json
import plotly.express as px
import pandas as pd
databaseFilePath="./training_data/Elysia.Laps.json"
def cleanData(df: pd.DataFrame):
    df = df.drop(columns=["msgType", "_id.$oid"])
    # drop rows where averagepackCurrent == NaN
    df = df.dropna(subset=["averagepackCurrent"])
    return df

with open(databaseFilePath, "r") as f:
    data = json.load(f)
    df = pd.json_normalize(data)
    cleanedDf = cleanData(df)
    print(cleanedDf)
    fig = px.line(cleanedDf, x="timestamp.$numberLong", y="amphours", title='Battery Usage Over Time')
    fig.show()
