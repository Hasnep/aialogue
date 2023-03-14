import os

import uvicorn  # type: ignore

if __name__ == "__main__":
    uvicorn.run(
        "aialogue:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 80)),
    )
