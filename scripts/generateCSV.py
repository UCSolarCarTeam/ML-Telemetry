from typing import List
import pandas as pd
import json
import os

from pathnames import LAP_JSON_PATH, PACKET_JSON_PATH, TRAINING_DATA_FOLDER, LAP_FEATHER_PATH, PACKET_FEATHER_PATH

PACKET_CSV_PATH=f'{TRAINING_DATA_FOLDER}/Elysia.Packets.csv'
LAP_CSV_PATH=f'{TRAINING_DATA_FOLDER}/Elysia.Laps.csv'

def generateCSV(outputFilePath: str, inputFeatherPath = "", inputJSONPath = "", ):
  if os.path.exists(outputFilePath):
    print(f"{outputFilePath} already exists. Delete them if you want to regenerate them.")
  else:
    data = None
    if(os.path.exists(inputFeatherPath)):
        data = pd.read_feather(inputFeatherPath)
    elif os.path.exists(inputJSONPath):
      with open(inputJSONPath) as json_file:
        jsonData = json.load(json_file)
        data = pd.json_normalize(jsonData)   
    if(data is not None):
      data.to_csv(outputFilePath)
      print(f"Generated {outputFilePath}")
    else:
      print(f"Neither {inputFeatherPath} nor {inputFeatherPath} exists. Please generate them first or check that you are running this in the root.")

def main():
  generateCSV(outputFilePath=LAP_CSV_PATH, inputJSONPath=LAP_JSON_PATH, inputFeatherPath=LAP_FEATHER_PATH)
  generateCSV(outputFilePath=PACKET_CSV_PATH, inputJSONPath=PACKET_JSON_PATH, inputFeatherPath=PACKET_FEATHER_PATH)
if __name__ == "__main__":
  main()