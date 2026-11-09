import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "$"
GUILD_IDS = [int(g) for g in os.getenv("GUILD_IDS", "").split(",") if g.strip()] or None
EMBED_COLOR = 0x5865F2
