from fastapi import Request
from fastapi.responses import JSONResponse
from nest.core import PyNestFactory, Module
from .app_controller import AppController
from .app_service import AppService
from src.trips.trips_module import TripsModule
from starlette.requests import Request
from fastapi import HTTPException

bearer_token = "PU=-r)i7{1ldp-rh(J'B#i\!P.8il2w[D!W*dvH.S2-[9x#vPsBGxol6Xje3-Gza"

@Module(
    imports=[TripsModule],
    controllers=[AppController],
    providers=[AppService],
)
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="This is my PyNest app.",
    title="PyNest Application",
    version="1.0.0",
    debug=True,
)

@app.http_server.middleware("http")
async def dispatch(request: Request, call_next):
    try:
        auth_header = request.headers.get('Authorization')
        if not (auth_header is None or auth_header.split(" ")[1] != bearer_token):
            response = await call_next(request)
            return response
        else:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except Exception as exc:
        return JSONResponse(status_code=500, content={'error': str(exc)})

http_server = app.get_server()
