import json
import plotly.express as px
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import time
databaseFilePath="./training_data/Elysia.Laps.json"
packetTrainingDataPath="./training_data/Elysia.Packets.json"
def cleanData(df: pd.DataFrame):
    df = df.drop(columns=["msgType", "_id.$oid"])
    # drop rows where averagepackCurrent == NaN
    df = df.dropna(subset=["averagepackCurrent"])
    return df

# with open(databaseFilePath, "r") as f:
#     data = json.load(f)
#     df = pd.json_normalize(data)
#     cleanedDf = cleanData(df)
#     print(cleanedDf)
    # fig = px.line(cleanedDf, x="timestamp.$numberLong", y="amphours", title='Battery Usage Over Time')
    # fig.show()


# with open(packetTrainingDataPath, "r") as f:
#     start_time = time.time()
#     data = json.load(f)
#     df = pd.json_normalize(data)
#     print("JSON read time:", time.time() - start_time)
# Reading JSON
# start_time = time.time()
# jsonDF = pd.read_json(packetTrainingDataPath)
# print("JSON read time:", time.time() - start_time)

# Reading CSV
# start_time = time.time()
# df_csv = pd.read_csv('output.csv')
# print("CSV read time:", time.time() - start_time)
# table = pa.Table.from_pandas(df_csv)
# pq.write_table(table, 'output.parquet')
start_time = time.time()
df_read = pq.read_table('output.parquet').to_pandas()
print("Parquet read time:", time.time() - start_time)
start_time = time.time()
df_feather = pd.read_feather('output.feather')
print("Feather write time:", time.time() - start_time)
# df_read.to_feather('output.feather')
# df_loaded = pd.read_feather('output.feather')
# print(df_loaded.head())