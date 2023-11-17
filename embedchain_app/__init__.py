import os

os.environ["OPENAI_API_KEY"] = ""

from embedchain.apps.app import App

from embedchain.config import (AppConfig, BaseEmbedderConfig, BaseLlmConfig,
                               ChromaDbConfig)
from embedchain.config.vectordb.base import BaseVectorDbConfig

from embedchain.embedchain import EmbedChain
from embedchain.embedder.base import BaseEmbedder
from embedchain.embedder.openai import OpenAIEmbedder

from embedchain.llm.base import BaseLlm
from embedchain.llm.openai import OpenAILlm

from embedchain.vectordb.base import BaseVectorDB
from embedchain.vectordb.chroma import ChromaDB

def create_embedchain_app(collection_name: str, app_id: str = None):
    chroma_config = ChromaDbConfig(
        collection_name=collection_name,
        dir="db",
        host="db",
        port="8000",
    )

    db = ChromaDB(
        config=chroma_config
    )

    if app_id == str():
        app_id = "ecairn-app-1"

    app_config = AppConfig(
        id=app_id, # used for history
        log_level="INFO",
        collect_metrics=False
    )

    llm_config = BaseLlmConfig(
        number_documents=5,
        model="gpt-4-1106-preview"
    )

    llm = OpenAILlm(
        config=llm_config
    )

    embedder_config = BaseEmbedderConfig(
      model="text-embedding-ada-002"
    )

    embedder = OpenAIEmbedder(
        config=embedder_config
    )

    app = App(
        config=app_config,
        db=db,
        llm=llm,
        embedder=embedder
    )

    return app
