from fastapi import FastAPI
from fastapi.responses import JSONResponse

import plotly.io as pio
import plotly.express as px
from fastapi.middleware.cors import CORSMiddleware
from main import main

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


@app.get("/plot")
async def get_plot():

    # df = px.data.iris()
    # fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig = main()
    graphJSON = pio.to_json(fig)
    return JSONResponse(content=graphJSON)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
