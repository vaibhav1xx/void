from app.version import APP_NAME, VERSION, CODENAME, STATUS


def startup():
    print("=" * 50)
    print(f"{APP_NAME} Systems Online")
    print("=" * 50)
    print(f"Version  : {VERSION}")
    print(f"Codename : {CODENAME}")
    print(f"Status   : {STATUS}")
    print("=" * 50)
    print("Awaiting Instructions...")