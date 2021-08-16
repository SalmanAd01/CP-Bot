import discord 
import requests
import datetime
import pytz
from keep_alive import keep_alive
client=discord.Client()
token = None
expires_at = None
def make_Token():
  global token
  global expires_at
  if not token or datetime.datetime.utcnow() >= expires_at:
    url = "https://api.codechef.com/oauth/token"
    payload = {"grant_type":"client_credentials" , 
    "scope":"public",
    "client_id":#CodeChefClient_id,
    "client_secret":#CodeChefClient_secret,
    }
    response  = requests.post(url, json=payload)
    try:
      response = response.json().get('result',{}).get('data', {})
      token = response.get('access_token')
      expires_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=response.get('expires_in'))
    except Exception as e:
      print("Code chef access token error ", e)
  return token
key=#CodeForcesAPIToken
def csuser_info(user_name):
  try:
    url="https://api.codechef.com/users/"+user_name
    key2=make_Token()
    headers = {"Accept":"application/json","authorization":"Bearer %s" % key2}
    response = requests.request("GET",url,headers=headers)
    data=response.json()
    myembed=discord.Embed(title="",description="",color=0x444444)
    myembed.set_author(name=data["result"]["data"]["content"]["fullname"],url="https://www.codechef.com/users/"+user_name,icon_url="https://cdn.discordapp.com/emojis/875563557008326736.png?v=1")
    myembed.add_field(name="Country",value=data["result"]["data"]["content"]["country"]["name"],inline=False)
    myembed.add_field(name="Ranking",value="Global : "+str(data["result"]["data"]["content"]["rankings"]["allContestRanking"]["global"])+"\nCountry : "+str(data["result"]["data"]["content"]["rankings"]["allContestRanking"]["country"]),inline=False)
    myembed.add_field(name="language",value=data["result"]["data"]["content"]["language"],inline=False)
    myembed.add_field(name="Stars",value=data["result"]["data"]["content"]["band"],inline=False)
    myembed.add_field(name="occupation",value=data["result"]["data"]["content"]["occupation"],inline=False)
    myembed.add_field(name="organization",value=data["result"]["data"]["content"]["organization"],inline=False)
    myembed.add_field(name="Practice Problem",value=len(data["result"]["data"]["content"]["problemStats"]["solved"]["Practice Problems"]),inline=False)
    return (myembed)
  except:
    return ("Not Found")
def csproblem_info(user_name):
  try:
    url="https://api.codechef.com/users/"+user_name
    key2=make_Token()
    headers = {"Accept":"application/json","authorization":"Bearer %s" % key2}
    response = requests.request("GET",url,headers=headers)
    data=response.json()
    myembed=discord.Embed(title="",description="",color=0x444444)
    myembed.set_author(name=data["result"]["data"]["content"]["fullname"],url="https://www.codechef.com/users/"+user_name,icon_url="https://cdn.discordapp.com/emojis/875563557008326736.png?v=1")
    myembed.add_field(name="Partially Solved Problems",value=str(data["result"]["data"]["content"]["submissionStats"]["partiallySolvedProblems"]),inline=True)
    myembed.add_field(name="Solved Problems",value=str(data["result"]["data"]["content"]["submissionStats"]["solvedProblems"]),inline=True)
    myembed.add_field(name="Attempted Problems",value=data["result"]["data"]["content"]["submissionStats"]["attemptedProblems"],inline=True)
    myembed.add_field(name="Submitted Solutions",value=str(data["result"]["data"]["content"]["submissionStats"]["submittedSolutions"]),inline=True)
    myembed.add_field(name="Wrong Submissions",value=str(data["result"]["data"]["content"]["submissionStats"]["wrongSubmissions"]),inline=True)
    myembed.add_field(name="RunTime Error",value=data["result"]["data"]["content"]["submissionStats"]["runTimeError"],inline=True)
    myembed.add_field(name="Time Limit Exceed",value=data["result"]["data"]["content"]["submissionStats"]["timeLimitExceed"],inline=True)
    myembed.add_field(name="Compilation Error",value=data["result"]["data"]["content"]["submissionStats"]["compilationError"],inline=True)
    myembed.add_field(name="Partially Solved Submissions",value=data["result"]["data"]["content"]["submissionStats"]["partiallySolvedSubmissions"],inline=True)
    myembed.add_field(name="Accepted Submissions",value=data["result"]["data"]["content"]["submissionStats"]["acceptedSubmissions"],inline=True)
    return (myembed)
  except:
    return ("Not Found")
def csupcoming():
  try:
    url="https://api.codechef.com/contests?fields=name%2CstartDate%2CendDate&status=future"
    key2=make_Token()
    headers = {"Accept":"application/json","authorization":"Bearer %s" % key2}
    response = requests.request("GET",url,headers=headers)
    data=response.json()
    lenght=len(data["result"]["data"]["content"]["contestList"])
    myembed=discord.Embed(title="",description="",color=0x444444)
    myembed.set_thumbnail(url="https://cdn.discordapp.com/emojis/875397195963199529.png?v=1")
    myembed.set_author(name="CodeChef Upcoming Contest",url="https://www.codechef.com/")
    for i in range (lenght):
      myembed.add_field(name=data["result"]["data"]["content"]["contestList"][i]["name"],value="Start : "+data["result"]["data"]["content"]["contestList"][i]["startDate"]+"\nEnd   : "+data["result"]["data"]["content"]["contestList"][i]["endDate"])
    return (myembed)
  except:
    return ("Erorr...")
def cspresent():
  try:
    url="https://api.codechef.com/contests?fields=code%2C%20name%2C%20startDate%2C%20endDate&status=present"
    key2=make_Token()
    headers = {"Accept":"application/json","authorization":"Bearer %s" % key2}
    response = requests.request("GET",url,headers=headers)
    data=response.json()
    lenght=len(data["result"]["data"]["content"]["contestList"])
    myembed=discord.Embed(title="",description="",color=0x444444)
    myembed.set_author(name="CodeChef",url="https://www.codechef.com/",icon_url="https://cdn.discordapp.com/emojis/875397195963199529.png?v=1")
    for i in range (lenght):
      myembed.add_field(name=data["result"]["data"]["content"]["contestList"][i]["name"],value="Start : "+data["result"]["data"]["content"]["contestList"][i]["startDate"]+"\nEnd   : "+data["result"]["data"]["content"]["contestList"][i]["endDate"])
    return (myembed)
  except:
    return ("Erorr...")
def count_problem():
  try:
    myembed=discord.Embed(title="<:cs:875397195963199529>CodeChef Total Problem",discription="",color=0x444444)
    list=["school","easy","medium","hard","challenge","extcontest"]
    for items in list:
      url="https://api.codechef.com/problems/"+items
      key2=make_Token()
      headers = {"Accept":"application/json","authorization":"Bearer %s" % key2}
      response = requests.request("GET",url,headers=headers)
      data=response.json()
      myembed.add_field(name=items,value=str(len(data["result"]["data"]["content"])),inline=False)
      print(len(data["result"]["data"]["content"]))
    return (myembed)
  except:
    return ("Erorr...")
def cfuser_info(user_name):
  try:
    url="https://codeforces.com/api/user.info?handles="+user_name
    headers = {"Accept":"application/json","authorization":"Bearer %s" % key}
    response = requests.request("GET",url,headers=headers)
    data=response.json()
    myembed= discord.Embed(title="",discription="",color=0x444444)
    try:
      myembed.set_author(name=data["result"][0]["firstName"]+" "+data["result"][0]["lastName"],url="https://codeforces.com/profile/"+user_name)
      myembed.set_thumbnail(url=data["result"][0]["titlePhoto"])
    except:
      myembed.set_author(name="Name is not set")
    try:
      myembed.add_field(name="country",value=data["result"][0]["country"],inline=False)
    except:
      myembed.add_field(name="country",value="Not Set",inline=False)
    try:
      myembed.add_field(name="rating",value=data["result"][0]["rating"],inline=False)
    except:
      myembed.add_field(name="rating",value=0,inline=False)
    try:
      myembed.add_field(name="friendOfCount",value=data["result"][0]["friendOfCount"],inline=False)
    except:
      myembed.add_field(name="friendOfCount",value=0,inline=False)
    try:
      myembed.add_field(name="Rank",value=data["result"][0]["maxRank"],inline=False)
    except:
      myembed.add_field(name="Rank",value=0,inline=False)
    try:
      myembed.add_field(name="organization",value=data["result"][0]["organization"],inline=False)
    except:
      myembed.add_field(name="organization",value="Not Set",inline=False)
    return (myembed)
  except:
    return ("Erorr...")
def find_date(num):
  IST = pytz.timezone('Asia/Kolkata')
  seconds = num
  seconds_in_day = 60 * 60 * 24
  seconds_in_hour = 60 * 60
  seconds_in_minute = 60

  days = seconds
  hours = (seconds - (days * seconds_in_day))
  minutes = (seconds - (days * seconds_in_day) - (hours *seconds_in_hour))
  new_sec=seconds-(days*seconds_in_day)-(hours*seconds_in_hour)-(minutes*seconds_in_minute)
  datetime_ist = datetime.datetime.now(IST)
  new_time = datetime_ist - datetime.timedelta(days=-days,hours=-hours, minutes=-minutes,seconds=-new_sec)
  temp_o=new_time.strftime("%d/%m/%Y   %H:%M:%S")
  return (temp_o)
def cfupcoming_contest():
  try:
    url="https://codeforces.com/api/contest.list?"
    headers = {"Accept":"application/json","authorization":"Bearer %s" % key}
    response=requests.request("GET",url,headers=headers)
    data=response.json()
    myembed=discord.Embed(title="Codeforces Upcoming Contest",discription="",color=0x444444)
    myembed.set_thumbnail(url="https://cdn.discordapp.com/emojis/875617364681555968.png?v=1")
    for i in range(4):
      str1=data["result"][i]["relativeTimeSeconds"]
      myembed.add_field(name=data["result"][i]["name"],value=find_date(str1*-1),inline=False)
    return (myembed)
  except:
    return ("Erorr..")
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
    myembed=discord.Embed(Title="Help Commands",description="",color=0x444444)
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
keep_alive()

client.run(#Bot_Token)
