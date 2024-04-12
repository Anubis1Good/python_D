import os
from dotenv import load_dotenv

load_dotenv()

ADMIN = os.getenv('ADMIN_ID')
print(ADMIN)