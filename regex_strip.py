import re

def regex_strip(text, chars=None):
    if chars:
        chars = re.escape(chars)
        pattern = f"^[{chars}]+|[{chars}]+$"
        return re.sub(pattern, "", text)

    return re.sub(r"^\s+|\s+$", "", text)