from typing import Any

AVAILABLE_PRODUCT_FEATURES: list[dict[str, Any]] = [
    {
        "description": "Create playlists of certain session recordings to easily find and watch them again in the future.",
        "key": "recordings_playlists",
        "limit": 5,
        "name": "Recording playlists",
        "note": None,
        "unit": None,
    },
    {
        "description": "Restrict access to data within the organization to only those who need it.",
        "key": "team_collaboration",
        "limit": None,
        "name": "Dashboard permissions",
        "note": None,
        "unit": None,
    },
]
