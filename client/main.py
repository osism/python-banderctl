import os
import requests
import typer

from typing import List, Optional

app = typer.Typer(help="Client to manage banderctl")
version = "0.0.1"
os.environ
settings = {"api_url": os.getenv("BANDERCTL_ENDPOINT", "http://localhost")}


def perform_api_call(payload: dict):
    url = f"{settings['api_url']}/allowlist/packages"
    result = requests.post(
        url=url,
        json=payload,
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    print(url)
    return result.text


@app.command("add")
def add(
        packages: Optional[List[str]] = typer.Option(
            [], "--package", "-p", help="OPTIONAL,MULTI-USE - e.g. osism"
        )
):
    """
    Mirror pip packages from upstream

    Example call: python3 main.py add -p osism -p fastapi
    """
    payload = {
        "mode": "add",
        "packages": packages
    }
    print(perform_api_call(payload=payload))


@app.command("delete")
def delete(
        packages: Optional[List[str]] = typer.Option(
            [], "--package", "-p", help="OPTIONAL,MULTI-USE - e.g. osism"
        )
):
    """
    Remove mirrored pip packages from config

    Example call: python3 main.py delete -p osism -p fastapi
    """
    payload = {
        "mode": "delete",
        "packages": packages
    }
    print(perform_api_call(payload=payload))


@app.command("version")
def version():
    print(version)


@app.callback()
def generic(
        url: Optional[str] = typer.Option(
            "http://localhost", "-e", "--endpoint"
        )):
    settings['api_url'] = url.strip("/")


def main():
    app()


if __name__ == "__main__":
    main()
