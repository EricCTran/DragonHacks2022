import hikari
import lightbulb

token = open('famBamBotToken.txt', 'r')

tokenStr = token.read()

token.close()

bot = lightbulb.BotApp(token=tokenStr, default_enabled_guilds=(969993622697177168))

#Part 2
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started')

#Part 3
@bot.command
@lightbulb.command('ping','says pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.command('group','This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand','This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')

@bot.command
@lightbulb.option('num1','The first number', type=int)
@lightbulb.option('num2','The second number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)



bot.run()