import json
from pathlib import Path


DATA_FILES = {
    f"sip_{version.replace('.', '_')}_{name.lower()}": (
        f"src/docs/diginstroom/sip/{version}/_data/{filename}.json"
    )
    for version in ("2.1", "3.0")
    for name, filename in (
        ("basic", "BASIC_PROFILE"),
        ("bibliographic", "BIBLIOGRAPHIC_PROFILE"),
        ("film", "FILM_PROFILE"),
        ("general", "GENERAL"),
        ("material_artwork", "MATERIAL_ARTWORK_PROFILE"),
    )
}


def define_env(env):
    root = Path(__file__).parent
    for name, path in DATA_FILES.items():
        env.variables[name] = json.loads((root / path).read_text(encoding="utf-8"))
