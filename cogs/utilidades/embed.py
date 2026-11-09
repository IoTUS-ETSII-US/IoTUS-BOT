import discord
from discord.ext import bridge, commands
from discord.ext.bridge import BridgeOption

import config


class Embed(commands.Cog):
    categoria = "Utilidades"

    def __init__(self, bot: bridge.Bot):
        self.bot = bot

    @bridge.bridge_command(name="embed", description="Envía un mensaje embed")
    @bridge.has_permissions(manage_messages=True)
    async def embed(
        self,
        ctx: bridge.BridgeContext,
        titulo: BridgeOption(str, "Título del embed"),
        descripcion: BridgeOption(str, "Contenido del embed"),
        color: BridgeOption(str, "Color en hex, p. ej. #ff0000", required=False) = None,
        canal: BridgeOption(discord.TextChannel, "Canal destino (por defecto, el actual)", required=False) = None,
    ):
        """Uso: $embed "título" "descripción" [#color] [#canal]"""
        try:
            colour = int(color.lstrip("#"), 16) if color else config.EMBED_COLOR
        except ValueError:
            return await ctx.respond("Color inválido. Usa formato hex, p. ej. `#ff0000`.", ephemeral=True)

        embed = discord.Embed(title=titulo, description=descripcion, color=colour)
        embed.set_footer(text=f"Enviado por {ctx.author.display_name}")
        destino = canal or ctx.channel
        await destino.send(embed=embed)
        await ctx.respond(f"Embed enviado a {destino.mention}.", ephemeral=True)


def setup(bot: bridge.Bot):
    bot.add_cog(Embed(bot))
