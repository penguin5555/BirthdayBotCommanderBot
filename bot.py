import discord
import responses

lastMessage = 'Awaiting further data ... wait one minute'

async def sendMessage(message, userMessage, dm):
    global lastMessage

    try:
        response = responses.handleMessage(userMessage, lastMessage)
        await message.author.send(response) if dm else await message.channel.send(response)
    except Exception as e:
        e = e

def runBot():
    global lastMessage
    import os
    TOKEN = os.environ.get('TOKEN')

    print(TOKEN)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    # client = discord.Client()

    # dont change on_ready - thats the way it works
    @client.event
    async def on_ready():
        print('Bot running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            # make sure the bot talks to other ppl, not recursively to itself
            return 
        
        username = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel) 
        
        if channel == 'bot-commands':
            if '$sudo' in userMessage:
                await sendMessage(message, userMessage, dm=False)
        else:
            global lastMessage
            # the next bday data
            lastMessage = (await client.get_channel(1193010614235299902).history(limit=1).flatten())[0].content
            
            

    
    client.run(TOKEN)
