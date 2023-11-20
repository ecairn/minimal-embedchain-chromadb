from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from embedchain_app import create_embedchain_app

import chromadb
# settings way
settings = chromadb.Settings(chroma_server_host="db", chroma_server_http_port=8000)
chroma_client = chromadb.Client(settings)

router = APIRouter(
    prefix="/api/v1/queries",
    tags=["queries"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
def query(collection_name: str, question: str, app_id: str, call_gpt: bool = False):
    embedchain_app = create_embedchain_app(collection_name, app_id)

    # get answer
    dry_run = not call_gpt
    answer = embedchain_app.chat(question, dry_run=dry_run)

    data = { "answer": answer }

    return JSONResponse(content={"data": data}, status_code=200)
