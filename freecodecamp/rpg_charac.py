full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string."
    elif name == "":
        return  "The character should have a name."
    elif len(name) > 10:
        return "The character name is too long."
    elif " " in name:
        return "The character name should not contain spaces."

    stats = [strength, intelligence, charisma]

    if not all(isinstance(i, int) for i in stats):
        return "All stats should be integers."
    elif not all(i >= 1 for i in stats):
        return "All stats should be no less than 1."
    elif not all(i <= 4 for i in stats):
        return "All stats should be no more than 4."
    elif sum(stats) != 7:
        return "The character should start with 7 points."

    return (
        f"{name} \n"
        f"STR {full_dot * strength + empty_dot * (10 - strength)} \n"
        f"INT {full_dot * intelligence + empty_dot * (10 - intelligence)} \n"
        f"CHA {full_dot * charisma + empty_dot * (10 - charisma)}"
    )

print(create_character(" ", 4, 2, 1))




