from fasthtml.common import *
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

app, rt = fast_app()
env = dotenv_values(".env")

def create_route(path, file_path):
    @rt(path)
    def get():
        return FileResponse(
            file_path,
            filename=os.path.basename(file_path),
            media_type='application/octet-stream'
        )

for key in env:
    value = env[key]
    path = f"/{os.path.basename(value).lower()}"
    print(f"Creating route: {path} -> {value}")
    create_route(path, value)

serve()
