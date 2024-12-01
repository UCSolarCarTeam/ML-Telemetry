from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from main import getLapPlot, getPacketPlot 
import plotly.io as pio

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
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/lap_plot")
async def get_lap_plot():
    fig = getLapPlot()
    graphJSON = pio.to_json(fig)
    return JSONResponse(content=graphJSON)

@app.get("/packet_plot")
async def get_packet_plot():
    fig = getPacketPlot()
    graphJSON = pio.to_json(fig)
    return JSONResponse(content=graphJSON)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
