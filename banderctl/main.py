import configparser
import uvicorn

from fastapi import FastAPI
from .settings import settings

app = FastAPI()
base_url = settings.base_url
config_location = settings.config_location


@app.post("/allowlist/packages")
async def root(payload: dict) -> dict:
    mode = payload["mode"]  # can either be 'add' or 'delete'
    payload_packages = payload["packages"]

    config = configparser.ConfigParser()
    config.read(config_location)
    config_package_list = config["allowlist"]["packages"].split("\n")

    if mode == "add":
        result = list(set(config_package_list + payload_packages))
    if mode == "delete":
        result = list(set(config_package_list).difference(set(payload_packages)))
    result = sorted(result)
    result = "\n".join(result)
    config["allowlist"]["packages"] = result

    with open(config_location, "w") as configfile:
        config.write(configfile)

    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=6000, log_level="info")
