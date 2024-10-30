import plotly.express as px
import pandas as pd
import numpy as np

packetTrainingDataPath = "../training_data/Elysia.Packets.feather"
lapTrainingDataPath = "../training_data/Elysia.Laps.feather"

def cleanLapData(df: pd.DataFrame):
    # TODO: Add more cleaning steps when packet structure is finalized.
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


def cleanPacketData(df: pd.DataFrame):
    # TODO: Add more cleaning steps when packet structure is finalized.
    #drop columns with null or empty values
    cols_with_missing = [col for col in df.columns if df[col].isnull().all()]
    df = df.drop(cols_with_missing, axis=1)

    #drop columns which are all constant; they have no variance so correlation will be undefined/NaN
    constant_columns = []
    for col in df.columns:
        #nunique doesn't work on lists or numpy arrays, which KeyMotor, MPPT, MotorDetails, and MotorFaults are. 
        if isinstance(df[col][0], (list, np.ndarray)):
            continue
        #check if the column has only one unique value
        if(df[col].nunique() == 1):
            constant_columns.append(col)

    df= df.drop(columns=constant_columns, axis=1)
    return df

def generateCorrelationMatrix(df: pd.DataFrame):
    correlation_matrix = df.corr(numeric_only=True)
    print(correlation_matrix)
    fig = px.imshow(correlation_matrix, title="Correlation Matrix for Helios Data")
    fig.show()
    return fig

def analyzePacketData(df: pd.DataFrame):
    cleanedDf = cleanPacketData(df)
    print(cleanedDf.head())
    return generateCorrelationMatrix(cleanedDf)

def analyzeLapData(df: pd.DataFrame):
    cleanedDF = cleanLapData(df)
    print(cleanedDF.head())
    return generateCorrelationMatrix(cleanedDF)

def main():
    # lapDataDF = pd.read_feather(lapTrainingDataPath)
    # return analyzeLapData(lapDataDF)
    packetDataDF = pd.read_feather(packetTrainingDataPath)
    return analyzePacketData(packetDataDF)

if __name__ == "__main__":
    main()

