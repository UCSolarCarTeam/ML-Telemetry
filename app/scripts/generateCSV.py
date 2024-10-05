import pandas as pd
import json
trainingDataFolder = "./training_data"
lapTrainingDataPath=f"{trainingDataFolder}/Elysia.Laps.json"
packetTrainingDataPath=f"{trainingDataFolder}/Elysia.Packets.json"

def packetJSONToCSV(packetTrainingDF: pd.DataFrame):
  packetTrainingDF.to_csv(f'{trainingDataFolder}/Elysia.Packets.csv')

def lapJSONToCSV(lapTrainingDF: pd.DataFrame):
  lapTrainingDF.to_csv(f'{trainingDataFolder}/Elysia.Laps.csv')

with open(lapTrainingDataPath) as json_file:
  data = json.load(json_file)
  lapTrainingDF = pd.json_normalize(data)   
  lapJSONToCSV(lapTrainingDF)

with open(packetTrainingDataPath) as json_file:
  data = json.load(json_file)
  packetTrainingDF = pd.json_normalize(data)   
  packetJSONToCSV(packetTrainingDF)