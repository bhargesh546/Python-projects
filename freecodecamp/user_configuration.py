def add_setting(settings: dict, key_value: tuple):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, key_value: tuple):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key):
    key = key.lower()

    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings: dict):
    if not settings:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key in settings:
            result += f"{key.capitalize()}: {settings[key]}\n"
        
        return result

test_settings = {
    'theme': 'light',
    'notifications': 'enabled'
}

add_setting({'theme': 'light'}, ('volume', 'high'))

print(test_settings)

update_setting({'theme': 'light'}, ('theme', 'dark'))

print(test_settings)

delete_setting({'theme': 'light'}, 'theme')
