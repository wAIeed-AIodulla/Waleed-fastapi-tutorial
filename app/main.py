from fastapi import FastAPI
from router import router as process_router

#FastAPI supports minimal coding, to the point where
#The line below creates an API
app = FastAPI()

#This line then includes a process router to the api,
#allowing us to route data to correct endpoints
app.include_router(process_router)
