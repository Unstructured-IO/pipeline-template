#####################################################################
# THIS FILE IS AUTOMATICALLY GENERATED BY UNSTRUCTURED API TOOLS.
# DO NOT MODIFY DIRECTLY
#####################################################################


from fastapi import FastAPI, Request, status
import logging
import os

from .process_file import router as process_file_router
from .process_text import router as process_text_router


app = FastAPI(
    title="Unstructured Pipeline API",
    description="""""",
    version="1.0.0",
    docs_url="/{{ cookiecutter.pipeline_family }}/docs",
    openapi_url="/{{ cookiecutter.pipeline_family }}/openapi.json",
)

allowed_origins = os.environ.get("ALLOWED_ORIGINS", None)
if allowed_origins:
    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins.split(","),
        allow_methods=["OPTIONS", "POST"],
        allow_headers=["Content-Type"],
    )

app.include_router(process_file_router)
app.include_router(process_text_router)


# Filter out /healthcheck noise
class HealthCheckFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("/healthcheck") == -1


logging.getLogger("uvicorn.access").addFilter(HealthCheckFilter())


@app.get("/healthcheck", status_code=status.HTTP_200_OK, include_in_schema=False)
def healthcheck(request: Request):
    return {"healthcheck": "HEALTHCHECK STATUS: EVERYTHING OK!"}