import discord
from discord.ext import bridge, commands

import config


class Ayuda(commands.Cog):
    categoria = "Utilidades"

    def __init__(self, bot: bridge.Bot):
        self.bot = bot

    @bridge.bridge_command(name="help", description="Muestra todos los comandos disponibles")
    async def help(self, ctx: bridge.BridgeContext):
        embed = discord.Embed(
            title="Ayuda de IoTUS-BOT",
            description=f"Usa `{config.PREFIX}comando` o `/comando`.",
            color=config.EMBED_COLOR,
        )
        categorias: dict[str, list[str]] = {}
        for cog in self.bot.cogs.values():
            for c in cog.get_commands():
                if not isinstance(c, bridge.BridgeCommand):
                    continue  # cada comando bridge se registra 3 veces (prefijo, slash y bridge)
                texto = f"`{config.PREFIX}{c.name}` · {c.description or c.help or 'Sin descripción'}"
                categorias.setdefault(getattr(cog, "categoria", cog.qualified_name), []).append(texto)
        for nombre, lineas in sorted(categorias.items()):
            embed.add_field(name=nombre, value="\n".join(sorted(lineas)), inline=False)
        await ctx.respond(embed=embed)


def setup(bot: bridge.Bot):
    bot.add_cog(Ayuda(bot))
