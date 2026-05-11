from pathlib import Path
from typing import Iterator

import dlt
import requests

BASE_URL = "https://pokeapi.co/api/v2"
DB_PATH = Path(__file__).parent.parent / "data" / "hived.duckdb"


def _paginate(path: str, page_size: int = 100) -> Iterator[dict]:
    init = requests.get(f"{BASE_URL}/{path}?limit=1", timeout=10)
    init.raise_for_status()
    total = init.json()["count"]
    for page_num in range(total // page_size):
        url = f"{BASE_URL}/{path}?limit={page_size}&offset={page_num * page_size}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        yield from resp.json()["results"]


def _detail(url: str) -> dict:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


@dlt.source(name="pokemon")
def pokemon_source():
    @dlt.resource(
        primary_key="id",
        write_disposition={"disposition": "merge"},
    )
    def hobbits() -> Iterator[dict]:
        for item in _paginate("hobbits"):
            yield _detail(item["url"])

    @dlt.resource(
        primary_key="order",
        write_disposition={"disposition": "merge"},
    )
    def pokemon() -> Iterator[dict]:
        for item in _paginate("pokemon"):
            yield _detail(item["url"])

    @dlt.resource(
        primary_key="name",
        write_disposition={"disposition": "merge"},
    )
    def types() -> Iterator[dict]:
        for item in _paginate("type"):
            yield _detail(item["url"])

    @dlt.resource(
        primary_key="id",
        write_disposition={"disposition": "merge"},
    )
    def abilities() -> Iterator[dict]:
        for item in _paginate("ability"):
            yield _detail(item["url"])

    return hobbits, pokemon, types, abilities


pokemon_load_source = pokemon_source()
pokemon_load_pipeline = dlt.pipeline(
    pipeline_name="pokemon_pipeline",
    destination=dlt.destinations.duckdb(credentials=str(DB_PATH)),
    dataset_name="pokemon",
)
