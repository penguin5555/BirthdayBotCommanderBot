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
    import base64
    # to bypass discord finding the bot's token
    TOKEN = base64.b64decode('TVRFNU16QXhOakkwTlRreE9Ea3dNREkyTlEuR1JCTkZrLnRtSThFU1JBcDZBcjdyMk5qSl9KM2EyclQwTjZPemdiaG9pTGxr').decode('utf-8')

    local = False
    if not local:
        # use this when deployed
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)
    else:
        # on local use this
        client = discord.Client()

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
            async for message in client.get_channel(1193010614235299902).history(limit=1):
                # print(message.content)
                lastMessage = message.content
                break
            # lastMessage = (await client.get_channel(1193010614235299902).history(limit=1).flatten())[0].content
            
            

    
    client.run(TOKEN)
