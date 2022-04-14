from fastapi import Request
from fastapi.responses import JSONResponse
from meowpi.utils.errors import UserAlreadyCreated, UserNotFoundError, DatabaseUpdateError




def setup_exception_handlers(app):

    @app.exception_handler(UserNotFoundError)
    async def not_found_exception_handler(request: Request, exc: UserNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"message": f"User not found"},
        )

    @app.exception_handler(UserAlreadyCreated)
    async def alread_created_exc_handler(request: Request, exc: UserAlreadyCreated):
        return JSONResponse(
            status_code=400,
            content={"message": f"Username is already being used"}
        )
    
    @app.exception_handler(DatabaseUpdateError)
    async def database_update_exc_handler(request: Request, exc: DatabaseUpdateError):
        return JSONResponse(
            status_code=502,
            content={"message": f"Services currently unavailable"}
        )
