import json
import pandas as pd
import os
from pathnames import LAP_JSON_PATH, PACKET_JSON_PATH, TRAINING_DATA_FOLDER

PACKET_FEATHER_PATH=f"{TRAINING_DATA_FOLDER}/Elysia.Packets.feather"
LAP_FEATHER_PATH=f"{TRAINING_DATA_FOLDER}/Elysia.Laps.feather"
def packetJSONToFeather(packetTrainingDF: pd.DataFrame):
  packetTrainingDF.to_feather(PACKET_FEATHER_PATH)

def lapJSONToFeather(lapTrainingDF: pd.DataFrame):
  lapTrainingDF.to_feather(LAP_FEATHER_PATH)


def main():
  if os.path.exists(PACKET_FEATHER_PATH) :
    print(f"{PACKET_FEATHER_PATH} already exists. Delete them if you want to regenerate them.")
  else:
    with open(LAP_JSON_PATH) as json_file:
      data = json.load(json_file)
      lapTrainingDF = pd.json_normalize(data)   
      lapJSONToFeather(lapTrainingDF)

  if os.path.exists(LAP_FEATHER_PATH):
    print(f"{LAP_FEATHER_PATH} already exists. Delete them if you want to regenerate them.")
  else:
    with open(PACKET_JSON_PATH) as json_file:
      data = json.load(json_file)
      packetTrainingDF = pd.json_normalize(data)   
      packetJSONToFeather(packetTrainingDF)


if __name__ == "__main__":
  main()