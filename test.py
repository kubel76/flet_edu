import uuid


# unique_username = f"user-{uuid.uuid4()}"
unique_username = f"user-{uuid.uuid4().hex[:8]}"
print(f"Унікальне ім'я користувача: {unique_username}")

api_key = uuid.uuid4().hex
print(f"API Key: {api_key}")

mac = str(uuid.getnode()).hex
print(f'Mac is {mac}')
