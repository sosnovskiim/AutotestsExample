def mask_string(value: str) -> str:
    if not value:
        return value
    if len(value) <= 3:
        return "***"
    return value[0] + "*" * (len(value) - 2) + value[-1]
