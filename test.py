import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('ODI0NzI5NjExMjc5NjYzMjA0.YJnDOg.U5PUWNVhJsOqF2LD8ZEQ3_H7jDs')
