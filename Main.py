from discord.ext import commands

bot = commands.Bot(command_prefix='-')


def main():
    @bot.event
    async def on_ready():
        print(f'{bot.user} has successfully connected to Discord!')

    bot.load_extension("cogs.Music") # chage to cogs.Default if you want to download video yt in discord


if __name__ == '__main__':
   main()
        
bot.run('Your_Discord_Token')
