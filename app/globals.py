VITE_ROUTES = (
    "/",
    "/login",
    "/logout",
    "/clients",
    "/system",
    "/account",
    "/install",
)

AVAILABLE_SERVICES = {
    "smtp": {
        "username": {"type": str, "required": True},
        "password": {"type": str, "required": True},
        "server": {"type": str, "required": True},
        "port": {"type": int, "required": True},
    },
    "zepto": {
        "sender": {"type": str, "required": True},
        "api_url": {"type": str, "required": True},
        "token": {"type": str, "required": True},
    },
    "get_address": {
        "api_key": {"type": str, "required": True},
        "administration_key": {"type": str, "required": False},
    },
}
