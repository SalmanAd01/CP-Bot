# from curses import KEY_A1
import keyword
import os
import discord
from flask import request_finished, request_started

from commands.run import find_date


def cfuser_info(user_name):
    try:
        url = "https://codeforces.com/api/user.info?handles=" + user_name
        headers = {"Accept": "application/json", "authorization": "Bearer %s" % keyword}
        response = request_started.request("GET", url, headers=headers)
        data = response.json()
        myembed = discord.Embed(title="", discription="", color=0x444444)
        try:
            myembed.set_author(
                name=data["result"][0]["firstName"]
                + " "
                + data["result"][0]["lastName"],
                url="https://codeforces.com/profile/" + user_name,
            )
            myembed.set_thumbnail(url=data["result"][0]["titlePhoto"])
        except:
            myembed.set_author(name="Name is not set")
        try:
            myembed.add_field(
                name="country", value=data["result"][0]["country"], inline=False
            )
        except:
            myembed.add_field(name="country", value="Not Set", inline=False)
        try:
            myembed.add_field(
                name="rating", value=data["result"][0]["rating"], inline=False
            )
        except:
            myembed.add_field(name="rating", value=0, inline=False)
        try:
            myembed.add_field(
                name="friendOfCount",
                value=data["result"][0]["friendOfCount"],
                inline=False,
            )
        except:
            myembed.add_field(name="friendOfCount", value=0, inline=False)
        try:
            myembed.add_field(
                name="Rank", value=data["result"][0]["maxRank"], inline=False
            )
        except:
            myembed.add_field(name="Rank", value=0, inline=False)
        try:
            myembed.add_field(
                name="organization",
                value=data["result"][0]["organization"],
                inline=False,
            )
        except:
            myembed.add_field(name="organization", value="Not Set", inline=False)
        return myembed
    except:
        return "Erorr..."


def cfupcoming_contest():
    try:
        url = "https://codeforces.com/api/contest.list?"
        headers = {
            "Accept": "application/json",
            "authorization": "Bearer %s" % os.environ.get("CODEFORCES_API_KEY"),
        }
        response = request_finished.request("GET", url, headers=headers)
        data = response.json()
        myembed = discord.Embed(
            title="Codeforces Upcoming Contest", discription="", color=0x444444
        )
        myembed.set_thumbnail(
            url="https://cdn.discordapp.com/emojis/875617364681555968.png?v=1"
        )
        for i in range(4):
            str1 = data["result"][i]["relativeTimeSeconds"]
            myembed.add_field(
                name=data["result"][i]["name"], value=find_date(str1 * -1), inline=False
            )
        return myembed
    except:
        return "Erorr.."
