import pyperclip, re

phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

# Creating email regex.

mail_re = re.compile(r'''(
                [a-zA-Z0-9_]+   # Username
                @               # '@' symbol
                [a-zA-Z0-9.]+   # Domain name
                (\.[a-zA-Z]{2,4})            
                )''', flags=re.VERBOSE)

# Finding matches in clipboard text.
text = str(pyperclip.paste())

matches = []

for match in phone_re.finditer(text):
    g = match.groups()

    phone = f"{g[1]}-{g[3]}-{g[5]}"
    if g[7]:
        phone += f" x{g[8]}"
    
    matches.append(phone)

matches.extend(m.group(1) for m in mail_re.finditer(text))

# Copying results to the clipboard.

if matches:
    result = '\n'.join(matches)
    pyperclip.copy(result)
    print('Copied to clipboard:')
    print(result)
else:
    print('No phone numbers or email addresses found.')
