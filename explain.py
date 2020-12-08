#importing the discord library
import discord

#establish client
client = discord.Client()

#putting async and @client.event here lets this bit of code run whenever an event happens
#in this case, whenever the bot connects and is ready, it'll print "bot initialised" in the console for debugging purposes
@client.event
async def on_ready():
    print("Bot initialised")

@client.event
async def on_message(message): #whenever a message is recieved, it takes message as an argument to let you use it in this function
    if message.author == client.user: #if the message author is the bot itself, it wont do anything to prevent it spamming
        return
    else:
        if message.content == "poo": #if the content of the message taken in by the on_message function is "poo"
            await message.channel.send("Rude...") #need to use await here bc of async task stuff you dont really need to know about right now, basically need to use await for sending messages in an asyncronous function. It knows what channel to send to because there's stuff in the message data (the .channel.send part) that knows where the message "poo" was sent from

        if message.content.startswith("hello"): #in-built function for seeing if a message starts with the arg
            await message.channel.send("Hi there!")


client.run("NzM4OTE2NTQxMDM4NDYwOTc5.XyS3pw.BllY8tM_AvjE8JfZqLCZBI8rzRQ") #this actually runs the bot, get a token from https://discord.com/developers/applications, make an application and then make a bot in that application. Remember to add the bot to a server you own :)
