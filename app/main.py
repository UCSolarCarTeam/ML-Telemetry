import plotly.express as px
import pandas as pd
packetTrainingDataPath="./training_data/Elysia.Packets.feather"
lapTrainingDataPath="./training_data/Elysia.Laps.feather"
def cleanLapData(df: pd.DataFrame):
    # TODO: Add more cleaning steps when packet structure is finalized.
    df = df.drop(columns=["msgType", "_id.$oid", "averagepackCurrent.$numberDouble", "timestamp.$numberLong"])
    df = df.dropna(subset=["averagepackCurrent"])
    return df

def cleanPacketData(df: pd.DataFrame):
    # TODO: Add more cleaning steps when packet structure is finalized.
    df = df.drop(columns=["Battery.FanSpeed", "Battery.FanVoltage", "Battery.BMSRelayStatusFlags.MalfunctionIndicatorActive", "Battery.RequestedFanSpeed"])
    return df
def generateCorrelationMatrix(df: pd.DataFrame):
    correlation_matrix = df.corr( numeric_only=True)
    print(correlation_matrix)
    fig = px.imshow(correlation_matrix)
    fig.show()
    return correlation_matrix
def analyzePacketData(df: pd.DataFrame):
    cleanedDf = cleanPacketData(df)
    print(cleanedDf.head())
    generateCorrelationMatrix(cleanedDf)
def analyzeLapData(df: pd.DataFrame):
    cleanedDF = cleanLapData(df)
    print(cleanedDF.head())
    generateCorrelationMatrix(cleanedDF)
lapDataDF = pd.read_feather(lapTrainingDataPath)
analyzeLapData(lapDataDF)
packetDataDF = pd.read_feather(packetTrainingDataPath)
analyzePacketData(packetDataDF)