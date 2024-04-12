import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    bot_token: str
    admin_id: int

settings = Settings(
    bot_token=os.getenv('TOKEN'),
    admin_id=int(os.getenv('ADMIN_ID'))
)



