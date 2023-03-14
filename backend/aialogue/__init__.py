import os
from typing import Dict, List

import openai
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from aialogue.dialogue_generator import DialogueGenerator
from aialogue.utils import get_logger, get_static_folder_path


# Pydantic classes
class GenerateRequestBody(BaseModel):
    names: List[str]
    keywords: List[str]


# Constants
load_dotenv()
OPEN_AI_API_KEY = os.environ["OPEN_AI_API_KEY"]
STATIC_FOLDER_PATH = get_static_folder_path()
MODEL_NAME = "gpt-3.5-turbo"
logger = get_logger(__name__)

# Set up dialogue generator
openai.api_key = OPEN_AI_API_KEY
dialogue_generator = DialogueGenerator(MODEL_NAME)

# Create FastAPI app
app = FastAPI()


# Route for index page
@app.get("/")
async def get_index_page():
    return FileResponse(STATIC_FOLDER_PATH / "index.html")


# Route for dialogue generator
@app.post("/generate")
async def generate(request_body: GenerateRequestBody) -> Dict[str, str]:
    logger.info("Received generate request with body: `%s`.", request_body)
    names = request_body.names[0], request_body.names[1]
    return {
        "dialogue": dialogue_generator.generate_dialogue(names, request_body.keywords)
    }


# Mount static files
app.mount("/", StaticFiles(directory=STATIC_FOLDER_PATH), name="static")
