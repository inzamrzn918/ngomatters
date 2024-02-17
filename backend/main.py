from fastapi import Depends, FastAPI
import uvicorn
from src.dependencies.database import get_db
from src.routers.users import user_route

from src.core.settings import load_settings
app = FastAPI(
    docs_url="/",
    dependencies=[Depends(get_db)]
)

routers = [user_route]

[app.include_router(router) for router in routers]
 



if __name__ == "__main__":
    sets = load_settings()
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)