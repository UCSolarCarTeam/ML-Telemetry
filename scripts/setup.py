import os

from pathnames import LAP_JSON_PATH, PACKET_JSON_PATH
from generateFeather import main as generateFeather
from generateCSV import main as generateCSV
if not os.path.exists(LAP_JSON_PATH):
  print(f"{LAP_JSON_PATH} could not be found. Please attach the volume to the container and try again.")
  exit()
if not os.path.exists(PACKET_JSON_PATH):
  print(f"{PACKET_JSON_PATH} could not be found. Please attach the volume to the container and try again.")
  exit()


generateFeather()
generateCSV()