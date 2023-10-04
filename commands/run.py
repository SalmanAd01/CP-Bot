import os
import requests
import datetime
import pytz
import discord


def make_Token():
    global token
    global expires_at
    if not token or datetime.datetime.utcnow() >= expires_at:
        url = "https://api.codechef.com/oauth/token"
        payload = {
            "grant_type": "client_credentials",
            "scope": "public",
            "client_id": os.environ.get("CODECHEF_CLIENT_ID"),
            "client_secret": os.environ.get("CODECHEF_CLIENT_SECRET"),
        }
        response = requests.post(url, json=payload)
        try:
            response = response.json().get("result", {}).get("data", {})
            token = response.get("access_token")
            expires_at = datetime.datetime.utcnow() + datetime.timedelta(
                seconds=response.get("expires_in")
            )
        except Exception as e:
            print("Code chef access token error ", e)
    return token


key = os.environ.get("CODEFORCES_API_KEY")  # CodeForcesAPIToken


def count_problem():
    try:
        myembed = discord.Embed(
            title="<:cs:875397195963199529>CodeChef Total Problem",
            discription="",
            color=0x444444,
        )
        list = ["school", "easy", "medium", "hard", "challenge", "extcontest"]
        for items in list:
            url = "https://api.codechef.com/problems/" + items
            key2 = make_Token()
            headers = {
                "Accept": "application/json",
                "authorization": "Bearer %s" % key2,
            }
            response = requests.request("GET", url, headers=headers)
            data = response.json()
            myembed.add_field(
                name=items,
                value=str(len(data["result"]["data"]["content"])),
                inline=False,
            )
            print(len(data["result"]["data"]["content"]))
        return myembed
    except:
        return "Erorr..."


def find_date(num):
    IST = pytz.timezone("Asia/Kolkata")
    seconds = num
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    days = seconds
    hours = seconds - (days * seconds_in_day)
    minutes = seconds - (days * seconds_in_day) - (hours * seconds_in_hour)
    new_sec = (
        seconds
        - (days * seconds_in_day)
        - (hours * seconds_in_hour)
        - (minutes * seconds_in_minute)
    )
    datetime_ist = datetime.datetime.now(IST)
    new_time = datetime_ist - datetime.timedelta(
        days=-days, hours=-hours, minutes=-minutes, seconds=-new_sec
    )
    temp_o = new_time.strftime("%d/%m/%Y   %H:%M:%S")
    return temp_o
