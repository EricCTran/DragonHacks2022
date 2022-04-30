import hikari

token = open('famBamBotToken.txt', 'r')

tokenStr = token.read()

token.close()

bot = hikari.GatewayBot(token=tokenStr)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started')

bot.run()