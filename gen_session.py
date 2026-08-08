from pyrogram import Client

api_id = input("Enter your API_ID: ").strip()
api_hash = input("Enter your API_HASH: ").strip()

with Client("session_gen", api_id=int(api_id), api_hash=api_hash, in_memory=True) as app:
    session_string = app.export_session_string()

print("\n" + "="*60)
print("YOUR STRING_SESSION:")
print("="*60)
print(session_string)
print("="*60)
