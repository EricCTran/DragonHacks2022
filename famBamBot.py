import hikari

token = open('famBamBotToken.txt', 'r')

tokenStr = token.read()

token.close()

bot = hikari.GatewayBot(token=tokenStr)
bot.run()