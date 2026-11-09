from discord.ext import bridge, commands
from discord.ext.bridge import BridgeOption


class Limpiar(commands.Cog):
    categoria = "Administración"

    def __init__(self, bot: bridge.Bot):
        self.bot = bot

    @bridge.bridge_command(name="limpiar", description="Borra los últimos N mensajes del canal")
    @bridge.has_permissions(manage_messages=True)
    async def limpiar(self, ctx: bridge.BridgeContext, cantidad: BridgeOption(int, "Mensajes a borrar (1-100)", min_value=1, max_value=100)):
        if isinstance(ctx, bridge.BridgeExtContext):
            cantidad += 1  # incluye el propio mensaje con el comando
        else:
            await ctx.defer(ephemeral=True)
        borrados = await ctx.channel.purge(limit=cantidad)
        await ctx.respond(f"🧹 Borrados {len(borrados)} mensajes.", delete_after=5)


def setup(bot: bridge.Bot):
    bot.add_cog(Limpiar(bot))
