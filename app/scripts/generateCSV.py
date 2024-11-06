from typing import List
import pandas as pd
import json
import os

from pathnames import LAP_JSON_PATH, PACKET_JSON_PATH, TRAINING_DATA_FOLDER, LAP_FEATHER_PATH, PACKET_FEATHER_PATH

PACKET_CSV_PATH=f'{TRAINING_DATA_FOLDER}/Elysia.Packets.csv'
LAP_CSV_PATH=f'{TRAINING_DATA_FOLDER}/Elysia.Laps.csv'

def generatePacketCSV():
  if os.path.exists(PACKET_CSV_PATH):
    print(f"{PACKET_CSV_PATH} already exists. Delete them if you want to regenerate them.")
  else:
    data = None
    if(os.path.exists(PACKET_FEATHER_PATH)):
        data = pd.read_feather(PACKET_FEATHER_PATH)
    elif os.path.exists(PACKET_JSON_PATH):
      with open(PACKET_JSON_PATH) as json_file:
        jsonData = json.load(json_file)
        data = pd.json_normalize(jsonData)   
    if(data is not None):
      data.to_csv(PACKET_CSV_PATH)
    else:
      print(f"Neither {PACKET_JSON_PATH} nor {PACKET_FEATHER_PATH} exists. Please generate them first or check that you are running this in the root.")

def generateLapCSV():
  if(os.path.exists(LAP_CSV_PATH)):
    print(f"{LAP_CSV_PATH} already exists. Delete them if you want to regenerate them.")
  else:
    data = None
    if(os.path.exists(LAP_FEATHER_PATH)):
        data = pd.read_feather(LAP_FEATHER_PATH)
    elif(os.path.exists(LAP_JSON_PATH)):
      with open(LAP_JSON_PATH) as json_file:
        jsonData = json.load(json_file)
        data = pd.json_normalize(jsonData)   
    if(data is not None):
      data.to_csv(LAP_CSV_PATH)
    else:
      print(f"Neither {LAP_JSON_PATH} nor {LAP_FEATHER_PATH} exists. Please generate them first or check that you are running this in the root.")

def main():
  generateLapCSV()
  generatePacketCSV()

if __name__ == "__main__":
  main()