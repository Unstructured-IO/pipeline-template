#####################################################################
# THIS FILE IS AUTOMATICALLY GENERATED BY UNSTRUCTURED API TOOLS.
# DO NOT MODIFY DIRECTLY
#####################################################################


from fastapi import FastAPI, Request, status

from .process_file import router as process_file_router
from .process_text import router as process_text_router


app = FastAPI(
    title="Unstructured Pipeline API",
    description="""""",
    version="1.0.0",
    docs_url="/{{ cookiecutter.pipeline_family }}/docs",
)

app.include_router(process_file_router)
app.include_router(process_text_router)


@app.get("/healthcheck", status_code=status.HTTP_200_OK, include_in_schema=False)
def healthcheck(request: Request):
    return {"healthcheck": "HEALTHCHECK STATUS: EVERYTHING OK!"}
