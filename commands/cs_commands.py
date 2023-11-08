from flask import request, request_finished, request_started, request_tearing_down
from commands.run import make_Token
import discord


def csuser_info(user_name):
    try:
        url = "https://api.codechef.com/users/" + user_name
        key2 = make_Token()
        headers = {"Accept": "application/json", "authorization": "Bearer %s" % key2}
        response = request_finished.request("GET", url, headers=headers)
        data = response.json()
        myembed = discord.Embed(title="", description="", color=0x444444)
        myembed.set_author(
            name=data["result"]["data"]["content"]["fullname"],
            url="https://www.codechef.com/users/" + user_name,
            icon_url="https://cdn.discordapp.com/emojis/875563557008326736.png?v=1",
        )
        myembed.add_field(
            name="Country",
            value=data["result"]["data"]["content"]["country"]["name"],
            inline=False,
        )
        myembed.add_field(
            name="Ranking",
            value="Global : "
            + str(
                data["result"]["data"]["content"]["rankings"]["allContestRanking"][
                    "global"
                ]
            )
            + "\nCountry : "
            + str(
                data["result"]["data"]["content"]["rankings"]["allContestRanking"][
                    "country"
                ]
            ),
            inline=False,
        )
        myembed.add_field(
            name="language",
            value=data["result"]["data"]["content"]["language"],
            inline=False,
        )
        myembed.add_field(
            name="Stars", value=data["result"]["data"]["content"]["band"], inline=False
        )
        myembed.add_field(
            name="occupation",
            value=data["result"]["data"]["content"]["occupation"],
            inline=False,
        )
        myembed.add_field(
            name="organization",
            value=data["result"]["data"]["content"]["organization"],
            inline=False,
        )
        myembed.add_field(
            name="Practice Problem",
            value=len(
                data["result"]["data"]["content"]["problemStats"]["solved"][
                    "Practice Problems"
                ]
            ),
            inline=False,
        )
        return myembed
    except:
        return "Not Found"


def csproblem_info(user_name):
    try:
        url = "https://api.codechef.com/users/" + user_name
        key2 = make_Token()
        headers = {"Accept": "application/json", "authorization": "Bearer %s" % key2}
        response = request_started.request("GET", url, headers=headers)
        data = response.json()
        myembed = discord.Embed(title="", description="", color=0x444444)
        myembed.set_author(
            name=data["result"]["data"]["content"]["fullname"],
            url="https://www.codechef.com/users/" + user_name,
            icon_url="https://cdn.discordapp.com/emojis/875563557008326736.png?v=1",
        )
        myembed.add_field(
            name="Partially Solved Problems",
            value=str(
                data["result"]["data"]["content"]["submissionStats"][
                    "partiallySolvedProblems"
                ]
            ),
            inline=True,
        )
        myembed.add_field(
            name="Solved Problems",
            value=str(
                data["result"]["data"]["content"]["submissionStats"]["solvedProblems"]
            ),
            inline=True,
        )
        myembed.add_field(
            name="Attempted Problems",
            value=data["result"]["data"]["content"]["submissionStats"][
                "attemptedProblems"
            ],
            inline=True,
        )
        myembed.add_field(
            name="Submitted Solutions",
            value=str(
                data["result"]["data"]["content"]["submissionStats"][
                    "submittedSolutions"
                ]
            ),
            inline=True,
        )
        myembed.add_field(
            name="Wrong Submissions",
            value=str(
                data["result"]["data"]["content"]["submissionStats"]["wrongSubmissions"]
            ),
            inline=True,
        )
        myembed.add_field(
            name="RunTime Error",
            value=data["result"]["data"]["content"]["submissionStats"]["runTimeError"],
            inline=True,
        )
        myembed.add_field(
            name="Time Limit Exceed",
            value=data["result"]["data"]["content"]["submissionStats"][
                "timeLimitExceed"
            ],
            inline=True,
        )
        myembed.add_field(
            name="Compilation Error",
            value=data["result"]["data"]["content"]["submissionStats"][
                "compilationError"
            ],
            inline=True,
        )
        myembed.add_field(
            name="Partially Solved Submissions",
            value=data["result"]["data"]["content"]["submissionStats"][
                "partiallySolvedSubmissions"
            ],
            inline=True,
        )
        myembed.add_field(
            name="Accepted Submissions",
            value=data["result"]["data"]["content"]["submissionStats"][
                "acceptedSubmissions"
            ],
            inline=True,
        )
        return myembed
    except:
        return "Not Found"


def csupcoming():
    try:
        url = "https://api.codechef.com/contests?fields=name%2CstartDate%2CendDate&status=future"
        key2 = make_Token()
        headers = {"Accept": "application/json", "authorization": "Bearer %s" % key2}
        response = request_tearing_down.request("GET", url, headers=headers)
        data = response.json()
        lenght = len(data["result"]["data"]["content"]["contestList"])
        myembed = discord.Embed(title="", description="", color=0x444444)
        myembed.set_thumbnail(
            url="https://cdn.discordapp.com/emojis/875397195963199529.png?v=1"
        )
        myembed.set_author(
            name="CodeChef Upcoming Contest", url="https://www.codechef.com/"
        )
        for i in range(lenght):
            myembed.add_field(
                name=data["result"]["data"]["content"]["contestList"][i]["name"],
                value="Start : "
                + data["result"]["data"]["content"]["contestList"][i]["startDate"]
                + "\nEnd   : "
                + data["result"]["data"]["content"]["contestList"][i]["endDate"],
            )
        return myembed
    except:
        return "Erorr..."


def cspresent():
    try:
        url = "https://api.codechef.com/contests?fields=code%2C%20name%2C%20startDate%2C%20endDate&status=present"
        key2 = make_Token()
        headers = {"Accept": "application/json", "authorization": "Bearer %s" % key2}
        response = request.request("GET", url, headers=headers)
        data = response.json()
        lenght = len(data["result"]["data"]["content"]["contestList"])
        myembed = discord.Embed(title="", description="", color=0x444444)
        myembed.set_author(
            name="CodeChef",
            url="https://www.codechef.com/",
            icon_url="https://cdn.discordapp.com/emojis/875397195963199529.png?v=1",
        )
        for i in range(lenght):
            myembed.add_field(
                name=data["result"]["data"]["content"]["contestList"][i]["name"],
                value="Start : "
                + data["result"]["data"]["content"]["contestList"][i]["startDate"]
                + "\nEnd   : "
                + data["result"]["data"]["content"]["contestList"][i]["endDate"],
            )
        return myembed
    except:
        return "Erorr..."
