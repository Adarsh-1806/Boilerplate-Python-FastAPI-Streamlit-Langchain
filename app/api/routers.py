"""
Routers:
- Routers can be used to organize related endpoints into separate groups for better code organization.
- Routers can be mounted on the main application using `app.include_router(router, prefix="/prefix")`.
"""

from fastapi import APIRouter

from app.api.endpoints import healthcheck,accounts,transactions,ai
api_router = APIRouter()

api_router.include_router(accounts.router, tags=["accounts"])
api_router.include_router(ai.router,tags=["ai"])
api_router.include_router(transactions.router,tags=["transactions"])
api_router.include_router(healthcheck.router, tags=["healthcheck"])