from pathlib import Path

import discord
from discord.ext import bridge

import config

intents = discord.Intents.default()
intents.message_content = True  # necesario para los comandos con prefijo ($)

bot = bridge.Bot(
    command_prefix=config.PREFIX,
    intents=intents,
    help_command=None,  # usamos nuestro propio comando help
    debug_guilds=config.GUILD_IDS,
)


def load_cogs() -> None:
    """Carga todos los cogs de cogs/<categoria>/<archivo>.py automáticamente."""
    for path in sorted(Path("cogs").glob("*/[!_]*.py")):
        bot.load_extension(".".join(path.with_suffix("").parts))


@bot.event
async def on_ready():
    print(f"Conectado como {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Game(name=f"{config.PREFIX}help | /help"))


if __name__ == "__main__":
    if not config.TOKEN:
        raise SystemExit("Falta DISCORD_TOKEN en el archivo .env")
    load_cogs()
    bot.run(config.TOKEN)
