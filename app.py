from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, PlainTextResponse
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from typing_extensions import Annotated

from utils import VerifyToken

from datetime import datetime
import pandas as pd
from prophet import Prophet

app = FastAPI(
    title="Sales prediction API",
    description="""An API that utilises a Machine Learning model to create json data with sales and apply a model of prediction""",
    version="1.0.0", debug=True)

auth = VerifyToken()

@app.get("/", response_class=PlainTextResponse)
async def running():
  note = """
Sales prediction API 🙌🏻

Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
  return note

favicon_path = 'favicon.png'
@app.get('/favicon.png', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.post("/prophet")
async def insights(request: Request):
    data = await request.json()
    df = pd.DataFrame(data)
    df['OrderDate'] = df['OrderDate'].apply(lambda x: datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(x) - 2))
    df = df.rename(columns={"OrderDate": "ds", "Revenue":"y"})
    print(df.head())
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)
    print(forecast.head())
    return forecast.to_json(orient='records')