import random

from discord.ext import bridge, commands
from discord.ext.bridge import BridgeOption


class Dado(commands.Cog):
    categoria = "Juego"

    def __init__(self, bot: bridge.Bot):
        self.bot = bot

    @bridge.bridge_command(name="dado", description="Tira un dado de N caras")
    async def dado(self, ctx: bridge.BridgeContext, caras: BridgeOption(int, "Número de caras (por defecto 6)", min_value=2) = 6):
        await ctx.respond(f"🎲 Ha salido un **{random.randint(1, max(caras, 2))}** (d{caras})")


def setup(bot: bridge.Bot):
    bot.add_cog(Dado(bot))
