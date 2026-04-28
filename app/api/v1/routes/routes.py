from fastapi import APIRouter

from app.api.v1.routes.auth_routes import router as auth_router
from app.api.v1.routes.board_routes import router as board_router
from app.api.v1.routes.section_routes import router as section_router
from app.api.v1.routes.ticket_routes import router as ticket_router
from app.api.v1.routes.invite_routes import router as invite_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(board_router)
api_router.include_router(section_router)
api_router.include_router(ticket_router)
api_router.include_router(invite_router)
