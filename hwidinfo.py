import os
import hikari
import lightbulb

# Create a new bot instance with the given token and settings
bot = lightbulb.BotApp(
    token="YourTokenHere",
    default_enabled_guilds=YOUR_GUILD_ID_HERE,
    help_slash_command=True,
    intents=hikari.Intents.ALL
)

# Define a command that allows the bot to say something
@bot.command()
@lightbulb.option("text", "The text you want the bot to say")
@lightbulb.command("say", "Make the bot say something")
@lightbulb.implements(lightbulb.SlashCommand)
async def say_command(ctx: lightbulb.SlashContext) -> None:
    # Respond with the text provided by the user
    await ctx.respond(ctx.options.text)

# Define a command that returns the ping of the bot
@bot.command()
@lightbulb.command("ping", "Returns the bot's current latency")
async def ping_command(ctx: lightbulb.Context) -> None:
    # Get the current latency of the bot
    latency = int(bot.latency * 1000)
    # Send a message with the current latency
    await ctx.respond(f"Pong! Current latency is {latency}ms.")

# Define a command that returns information about the server
@bot.command()
@lightbulb.command("serverinfo", "Returns information about the server")
async def serverinfo_command(ctx: lightbulb.Context) -> None:
    # Get information about the server
    guild = ctx.get_guild()
    name = guild.name
    description = guild.description
    member_count = guild.member_count
    # Send a message with the server information
    await ctx.respond(f"Server Name: {name}\nDescription: {description}\nMember Count: {member_count}")

# Start the bot
bot.run()