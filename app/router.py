from fastapi import APIRouter

import endpoint

#Router instance
router = APIRouter()

#The prefix is the very important in that it designates the endpoint
router.include_router(endpoint.router, prefix="/events", tags=["events"])
