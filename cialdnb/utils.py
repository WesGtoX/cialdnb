import re

def clean_phone(value):
    if not value:
        return []

    phone = re.sub(r'[^\d+\(\)+]', ' ', value)
    phone = re.sub(r'^\+\s', '+', phone)
    return phone
