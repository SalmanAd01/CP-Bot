import os
from commands.cf_commands import cfupcoming_contest
import discord 
import requests
from dotenv import load_dotenv


load_dotenv(".env")
# from keep_alive import keep_alive


from commands.cs_commands import csuser_info, csproblem_info, csupcoming, cspresent
from commands.cf_commands import cfuser_info, cfupcoming_contest
from commands.run import make_Token, count_problem
intents = discord.Intents.default()
intents.members = True
intents.message_content=True


client = discord.Client(intents=intents)
# client=discord.Client(Intents.)
token = None
expires_at = None





@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if msg.startswith("$Run"):
    try:
      try:
        str2=msg.split("$Input",1)[0]
        inp=msg.split("$Input ",1)[1]
        st=str2.split("$Run ",1)[1]
      except:
        st=msg.split("$Run ",1)[1]
        inp='NO INPUT'
      url="https://api.codechef.com/ide/run"
      key2=make_Token()
      headers={"Authorization":f"Bearer {key2}"}
      data={"sourceCode" : st,"language" : "PYTH 3.6","input" : inp}
      response=requests.post(url,headers=headers,json=data)
      code=response.json()
      import time
      time.sleep(2)
      url="https://api.codechef.com/ide/status?link=" +code["result"]["data"]["link"]
      headers = {"Authorization":"Bearer %s" % key2}
      response=requests.get(url,headers=headers)
      data=response.json()
      myembed=discord.Embed(title="IDE Result",discription="",color=0x444444)
      try:
        myembed.add_field(name="Input",value=data["result"]["data"]["input"],inline=False)
      except:
        myembed.add_field(name="Input",value="s",inline=False)
      try:
        myembed.add_field(name="Output",value=data["result"]["data"]["output"],inline=False)
      except:
        myembed.add_field(name="Output",value="s",inline=False)
      try:
        myembed.add_field(name="memory",value=data["result"]["data"]["memory"],inline=False)
      except:
        myembed.add_field(name="memory",value="s",inline=False)
      try:
        myembed.add_field(name="time",value=data["result"]["data"]["time"],inline=False)
      except:
        myembed.add_field(name="time",value="s",inline=False)
      await message.channel.send(embed=myembed)
    except:
      await message.channel.send("Erorr...")
  if msg.startswith("$C+Run"):
    try:
      try:
        str2=msg.split("$Input",1)[0]
        inp=msg.split("$Input ",1)[1]
        st=str2.split("$C+Run ",1)[1]
      except:
        st=msg.split("$C+Run ",1)[1]
        inp='NO INPUT'
      url="https://api.codechef.com/ide/run"
      key2=make_Token()
      headers={"Authorization":f"Bearer {key2}"}
      data={"sourceCode" : st,"language" : "C++ 4.3.2","input" : inp}
      response=requests.post(url,headers=headers,json=data)
      code=response.json()
      import time
      time.sleep(2)
      url="https://api.codechef.com/ide/status?link=" +code["result"]["data"]["link"]
      headers = {"Authorization":"Bearer %s" % key2}
      response=requests.get(url,headers=headers)
      data=response.json()
      myembed=discord.Embed(title="IDE Result",discription="",color=0x444444)
      try:
        myembed.add_field(name="Input",value=data["result"]["data"]["input"],inline=False)
      except:
        myembed.add_field(name="Input",value="s",inline=False)
      try:
        myembed.add_field(name="Output",value=data["result"]["data"]["output"],inline=False)
      except:
        myembed.add_field(name="Output",value="s",inline=False)
      try:
        myembed.add_field(name="memory",value=data["result"]["data"]["memory"],inline=False)
      except:
        myembed.add_field(name="memory",value="s",inline=False)
      try:
        myembed.add_field(name="time",value=data["result"]["data"]["time"],inline=False)
      except:
        myembed.add_field(name="time",value="s",inline=False)
      await message.channel.send(embed=myembed)
    except:
      await message.channel.send("Erorr...")
  if msg.startswith("$csupcoming"):
    try:
      await message.channel.send(embed=csupcoming())
    except:
      await message.channel.send(csupcoming())
  if msg.startswith("$cspresent"):
    try:
      await message.channel.send(embed=cspresent())
    except:
      await message.channel.send(cspresent())
  if msg.startswith("$csuser"):
    try:
      user_name=msg.split("$csuser ",1)[1]
      csuser_info(user_name)
      await message.channel.send(embed=csuser_info(user_name))
    except:
      await message.channel.send(csuser_info(user_name))
  if msg.startswith("$csproblem"):
    user_name=msg.split("$csproblem ",1)[1]
    try:
      await message.channel.send(embed=csproblem_info(user_name))
    except:
      await message.channel.send(csproblem_info(user_name))
  if msg.startswith("$cscountproblem"):
    try:
      await message.channel.send(embed=count_problem())
    except:
      await message.channel.send(count_problem())
  if msg.startswith("$help"):
    myembed=discord.Embed(title="Help Commands",description="",color=0x444444)
    myembed.add_field(name="$csupcoming",value="To Get The Info About Upcoming Codechef Contest\nEg. $csupcoming",inline=False)
    myembed.add_field(name="$cspresent",value="To Get The Info About Present Codechef Contest\nEg. $cspresent",inline=False)
    myembed.add_field(name="$csuser",value="To Get The Basic Info About Codechef User\nEg. $csuser gkcs",inline=False)
    myembed.add_field(name="$cscountproblem",value="To Get The Total Problem in CodeChef with respective of there complexity\nEg. $cscountproblem",inline=False)
    myembed.add_field(name="$csproblem",value="To Get The Info About The Problem Solved By Codechef User\nEg. $csproblem priyansh19077",inline=False)
    myembed.add_field(name="$cfuser",value="To Get The Info About The Codeforces User\nEg. $cfuser tourist",inline=False)
    myembed.add_field(name="$cfupcoming",value="To Get The Info About Upcoming Codeforces Contest\nEg. $cfupcoming",inline=False)
    myembed.add_field(name="$Run",value="""Virtual Compiler For Python\nEg.1)Without $Input\n$Run import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)\n2)With $Input\n$Run INDIA=int(input()) 
for i in range(INDIA):print('Happy Independence Day') $Input 5""",inline=False)
    myembed.add_field(name="$C+Run",value="""Virtual Compiler For C++\nEg.1)Without $Input\n$C+Run #include <iostream>
using namespace std;
int main()
{
    for (int i=0;i<5;i++)
    {
    cout<<"Hello World";
}
    return 0;
}\n2)With $Input\n$C+Run #include <iostream>
using namespace std;
int main()
{
    int a;
    cin >> a;
    for (int i=0;i<a;i++)
    {
    cout<<"Hello World";
}
    return 0;
} $Input 5""",inline=False)
    await message.channel.send(embed=myembed)
  if msg.startswith("$cfupcoming"):
    try:
      await message.channel.send(embed=cfupcoming_contest())
    except:
      await message.channel.send(cfupcoming_contest())
  if msg.startswith("$cfuser"):
    name = message.content.split("$cfuser ",1)[1]
    try:
      await message.channel.send(embed=cfuser_info(name))
    except:
      await message.channel.send(cfuser_info(name))
  if msg.startswith("$test"):
    tem=msg.split("$test ",1)[1]
    tes=tem.split("$te ",1)[1]
    await message.channel.send("Y")
# keep_alive()


client.run(os.environ.get("DISCORD_BOT_TOKEN"))

