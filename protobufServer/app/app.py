from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import HeliosPacket_pb2 as HeliosPacket
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def send():
    return "Hello World! Navigate to localhost:8000/send and check the console!", 200


@app.post("/receive")
async def receive(request: Request):
    request_data = await request.body()
    print(f"Raw request data: {request_data}")

    payload = HeliosPacket.B3()
    payload.ParseFromString(request_data)
    print("/receive received:")
    print(f"B3.Acceleration: {payload.Acceleration}")
    print(f"B3.B3Heartbeat: {payload.B3Heartbeat}")
    print(f"B3.BrakeLightSignalStatus: {payload.BrakeLightSignalStatus}")
    print(f"B3.BrakeSwitchDigital: {payload.BrakeSwitchDigital}")
    print(
        f"B3.DaytimeRunningLightSignalStatus: {payload.DaytimeRunningLightSignalStatus}"
    )
    print(f"B3.ForwardDigital: {payload.ForwardDigital}")
    print(f"B3.HandbrakeSwitchDigital: {payload.HandbrakeSwitchDigital}")
    print(f"B3.HazardLightsInput: {payload.HazardLightsInput}")
    print(f"B3.HeadightsSwitchInput: {payload.HeadightsSwitchInput}")
    print(f"B3.HeadlightSignalStatus: {payload.HeadlightSignalStatus}")
    print(f"B3.HornSignalStatus: {payload.HornSignalStatus}")
    print(f"B3.HornSwitchDigital: {payload.HornSwitchDigital}")
    print(f"B3.LapDigital: {payload.LapDigital}")
    print(f"B3.LeftSignalInput: {payload.LeftSignalInput}")
    print(f"B3.LeftSignalStatus: {payload.LeftSignalStatus}")
    print(f"B3.MotorResetDigital: {payload.MotorResetDigital}")
    print(f"B3.NeutralDigital: {payload.NeutralDigital}")
    print(f"B3.RaceModeDigital: {payload.RaceModeDigital}")
    print(f"B3.RegenBraking: {payload.RegenBraking}")
    print(f"B3.ReverseDigital: {payload.ReverseDigital}")
    print(f"B3.RightSignalInput: {payload.RightSignalInput}")
    print(f"B3.RightSignalStatus: {payload.RightSignalStatus}")

    return Response(content=request_data, media_type="application/octet-stream")


@app.get("/send")
def send():
    payload = HeliosPacket.B3(
        Acceleration=32,
        B3Heartbeat=False,
        BrakeLightSignalStatus=False,
        BrakeSwitchDigital=True,
        DaytimeRunningLightSignalStatus=True,
        ForwardDigital=False,
        HandbrakeSwitchDigital=True,
        HazardLightsInput=False,
        HeadightsSwitchInput=False,
        HeadlightSignalStatus=True,
        HornSignalStatus=True,
        HornSwitchDigital=False,
        LapDigital=True,
        LeftSignalInput=False,
        LeftSignalStatus=False,
        MotorResetDigital=False,
        NeutralDigital=True,
        RaceModeDigital=False,
        RegenBraking=64,
        ReverseDigital=True,
        RightSignalInput=True,
        RightSignalStatus=False,
    )

    # Encode the Protobuf message
    data = payload.SerializeToString()
    response = requests.post("http://localhost:8000/receive", data=data)
    payload.ParseFromString(response.content)
    print("/send reponse:")
    print(f"Sending Payload: {payload}")

    return "Sent the Protobuf message", 200


if __name__ == "__main__":
    app.run(port=4000)
