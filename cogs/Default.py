from urllib.parse import urlencode
from youtube_dl import YoutubeDL
import pytube as pyt
from discord.ext import commands
from discord.utils import get
import urllib.parse
import discord
import re

bot = commands.Bot(command_prefix='-')

class Default(commands.Cog):

    @bot.command(aliases=['ytD'])
    async def ytDownload(ctx, *, search):
        author = ctx.message.author

        embed = discord.Embed(title="", description=f'{author.mention} Sedang Me-Download video.........', color=discord.Color.blue())
        await ctx.send(embed=embed, delete_after=5)

        query_string = urllib.parse.urlencode({'search_query': search})
        html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
        search_content = html_content.read().decode()
        search_results = re.findall(r'\/watch\?v=\w+', search_content)
        x_url = 'https://www.youtube.com' + search_results[0]

        video_Download = pyt.YouTube(x_url)

        videos = video_Download.streams.filter(progressive=True)
        try:
            await ctx.send(file=discord.File(videos[2].download(r'D:\Users\USER\Downloads_D\Pytube_Download\Discord')))
        except:
            embed = discord.Embed(title="", description="File terlalu besar untuk di upload", color=discord.Color.red())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Default(bot))