def handleMessage(message, lastBdayData):
    message = message.lower()
    if message == '$sudo next-bday':
        return lastBdayData
    
    else:
        return '`help - run the command $sudo next-bday`'
    


    