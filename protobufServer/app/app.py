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

@app.get('/')
def send():
    return 'Hello World!', 200

@app.post("/receive")
async def receive(request: Request):
    request_data = await request.body()
    print(f"Raw request data: {request_data}")

    iBMSRelayStatusFlags = HeliosPacket.IBMSRelayStatusFlags()
    iBMSRelayStatusFlags.ParseFromString(request_data)
    print("/receive received:")
    print(f"iBMSRelayStatusFlags.AlwaysOnSignalStatus: {iBMSRelayStatusFlags.AlwaysOnSignalStatus}")
    print(f"iBMSRelayStatusFlags.ChargeRelayEnabled: {iBMSRelayStatusFlags.ChargeRelayEnabled}")
    print(f"iBMSRelayStatusFlags.ChargerSafetyEnabled: {iBMSRelayStatusFlags.ChargerSafetyEnabled}")
    print(f"iBMSRelayStatusFlags.DischargeRelayEnabled: {iBMSRelayStatusFlags.DischargeRelayEnabled}")
    print(f"iBMSRelayStatusFlags.IsChargingSignalStatus: {iBMSRelayStatusFlags.IsChargingSignalStatus}")

    return Response(content=request_data, media_type='application/octet-stream')

@app.get('/send')
def send():
    iBMSRelayStatusFlags = HeliosPacket.IBMSRelayStatusFlags(
        AlwaysOnSignalStatus=True,
        ChargeRelayEnabled=False,
        ChargerSafetyEnabled=False,
        DischargeRelayEnabled=False,
        IsChargingSignalStatus=False,
        IsReadySignalStatus=False,
        MalfunctionIndicatorActive=False,
        MultiPurposeInputSignalStatus=False
    )

    # Encode the Protobuf message
    data = iBMSRelayStatusFlags.SerializeToString()
    response = requests.post('http://localhost:8000/receive', data=data)
    iBMSRelayStatusFlags.ParseFromString(response.content)
    print("/send reponse:")
    print(f"iBMSRelayStatusFlags.AlwaysOnSignalStatus: {iBMSRelayStatusFlags.AlwaysOnSignalStatus}")
    print(f"iBMSRelayStatusFlags.ChargeRelayEnabled: {iBMSRelayStatusFlags.ChargeRelayEnabled}")
    print(f"iBMSRelayStatusFlags.ChargerSafetyEnabled: {iBMSRelayStatusFlags.ChargerSafetyEnabled}")
    print(f"iBMSRelayStatusFlags.DischargeRelayEnabled: {iBMSRelayStatusFlags.DischargeRelayEnabled}")
    print(f"iBMSRelayStatusFlags.IsChargingSignalStatus: {iBMSRelayStatusFlags.IsChargingSignalStatus}")

    return 'Sent the Protobuf message', 200

if __name__ == '__main__':
    app.run(port=4000)
