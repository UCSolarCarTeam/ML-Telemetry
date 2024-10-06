import pandas as pd
import json
import os

from pathnames import LAP_JSON_PATH, PACKET_JSON_PATH, TRAINING_DATA_FOLDER

PACKET_CSV_PATH=f'{TRAINING_DATA_FOLDER}/Elysia.Packets.csv'
LAP_CSV_PATH=f'{TRAINING_DATA_FOLDER}/Elysia.Laps.csv'

def packetJSONToCSV(packetTrainingDF: pd.DataFrame):
  packetTrainingDF.to_csv(PACKET_CSV_PATH)

def lapJSONToCSV(lapTrainingDF: pd.DataFrame):
  lapTrainingDF.to_csv(LAP_CSV_PATH)

def main():
  if os.path.exists(PACKET_CSV_PATH):
    print(f"{PACKET_CSV_PATH} already exists. Delete them if you want to regenerate them.")
  else:
    with open(LAP_JSON_PATH) as json_file:
      data = json.load(json_file)
      lapTrainingDF = pd.json_normalize(data)   
      lapJSONToCSV(lapTrainingDF)

  if(os.path.exists(LAP_CSV_PATH)):
    print(f"{LAP_CSV_PATH} already exists. Delete them if you want to regenerate them.")
  else:
    with open(PACKET_JSON_PATH) as json_file:
      data = json.load(json_file)
      packetTrainingDF = pd.json_normalize(data)   
      packetJSONToCSV(packetTrainingDF)

if __name__ == "__main__":
  main()