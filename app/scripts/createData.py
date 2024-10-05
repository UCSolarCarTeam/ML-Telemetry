import json
import pandas as pd
trainingDataFolder = "./training_data"
lapTrainingDataPath=f"{trainingDataFolder}/Elysia.Laps.json"
packetTrainingDataPath=f"{trainingDataFolder}/Elysia.Packets.json"

def packetJSONToFeather(packetTrainingDF: pd.DataFrame):
  packetTrainingDF.to_feather(f'{trainingDataFolder}/Elysia.Packets.feather')

def lapJSONToFeather(lapTrainingDF: pd.DataFrame):
  lapTrainingDF.to_feather(f'{trainingDataFolder}/Elysia.Laps.feather')

with open(lapTrainingDataPath) as json_file:
  data = json.load(json_file)
  lapTrainingDF = pd.json_normalize(data)   
  lapJSONToFeather(lapTrainingDF)

with open(packetTrainingDataPath) as json_file:
  data = json.load(json_file)
  packetTrainingDF = pd.json_normalize(data)   
  packetJSONToFeather(packetTrainingDF)