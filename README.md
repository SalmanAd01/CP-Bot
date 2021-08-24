# CP-Bot
- It's A Discord Bot Made For The Competitive Programmers. That will Help To Track The New Events on CodeChef And CodeForces And A Virtual Compiler For C++ and Python To Test the programs And Much More. 
## Badges
[![python-version](https://img.shields.io/badge/Python-v3.9.6-blue)](https://www.python.org/downloads/)

[![Discord](https://img.shields.io/badge/Bot-Discord-blue)](https://discord.com/developers/docs/game-sdk/applications)

[![CodeChefApi](https://img.shields.io/badge/CodeChef-API-blue)](https://developers.codechef.com/)

[![CodeForcesApi](https://img.shields.io/badge/CodeForces-API-blue)](https://codeforces.com/apiHelp)

[![UptimeRobot](https://img.shields.io/badge/UptimeRobot-Monitoring-blue)](https://uptimerobot.com/)

![Twitter](https://img.shields.io/twitter/url?color=Black&label=Twitter&style=social&url=https%3A%2F%2Ftwitter.com%2FAdhikariSalman%3Fs%3D09) 
 
[![LinkedIn](https://img.shields.io/badge/in-LinkedIn-blue)](https://www.linkedin.com/in/salman-adhikari-a938911bb)

## Features 
- Easy To Search The User's Info On CodeChef And CodeForces
- Easy To Track The Current And Upcoming Events On CodeChef And CodeForces
- Easy To See The Total Problems On CodeChef.
- Virtual Compiler Of Python And C++.
## How To Invite 
1) Paste The Link In The Browser Link:https://discord.com/api/oauth2/authorize?client_id=870861541862408252&permissions=0&scope=bot
2) Select The Server From The Drope Down List On Which You Wanted To Invite The Bot

![Screenshot (430)](https://user-images.githubusercontent.com/80933048/129594982-711df30d-4503-4644-b290-20b8d5d92bb1.png)<br>

3) Click On Authorize Button

![Screenshot (432)](https://user-images.githubusercontent.com/80933048/129595176-cd107395-1936-4046-b83d-a477d5d2df1e.png)


## How To Use
- $csupcoming : This Command Is Used To Know The Upcoming Events With The Starting And End Date Of CodeChef
```bash
$csupcoming
```

![Screenshot (446)](https://user-images.githubusercontent.com/80933048/130434301-715d7abf-f318-4156-a828-edfeec2cf10a.png)
- $cspresent : This Command Is Used To Know The Present Events With The Starting And End Date Of CodeChef
```bash
$cspresent
```
![Screenshot (445)](https://user-images.githubusercontent.com/80933048/130434351-9bb09220-91e8-45e4-9b76-7df4d07ec55c.png)
- $csuser : This Command Is Used To Know The Basic Information of a user In Codechef. It takes the username as a parameters
```bash
$csuser user_name
```
![Screenshot (411)](https://user-images.githubusercontent.com/80933048/129573492-754c266a-7b08-45ee-a927-46d8f96cb159.png)
- $cscountproblem : This Command Is Used To Get The Total Problem in CodeChef with respective of there complexity.
```bash
$cscountproblem
```
![Screenshot (414)](https://user-images.githubusercontent.com/80933048/129574442-36ce2c7a-cf86-42fb-ad6f-3d02024264dc.png)
- $csproblem : This Command Is Used To Get The Overall Submission status Solve By The User.It takes the user_name as a parameters.
```bash
$csproblem user_name
```
![Screenshot (416)](https://user-images.githubusercontent.com/80933048/129589635-6f6c7b86-cb0b-42a9-95d2-9609acd22dba.png)
- $cfuser : This Command Is Used To Know The Basic Information of a user In CodeForces. It takes the username as a parameters
```bash
$cfuser user_name
```
![Screenshot (418)](https://user-images.githubusercontent.com/80933048/129589970-2ffd1524-d7ec-40fb-9ee7-28f3d12d36e2.png)
- $cfupcoming : This Command Is Used To Know The Upcoming Events With The Starting And End Date Of CodeForces.
```bash
$cfupcoming
```
![Screenshot (444)](https://user-images.githubusercontent.com/80933048/130434388-b8aa83c9-ae4c-406d-b48e-63f4efcb7b53.png)
- $run : This Command Is Used To Run The Python Node.js and C++ Code It can Be Run With or Without Input.
1) Without $input
~~~
$run
```Extension_name
Write_Code
```
~~~
2) With $input
~~~
$run
```Extension_name
Write_Code
```
$input
```
Write_Input
```
~~~
- Note: For Python Extension_name is py For Node.js It's js And For C++ It's c++ 
## Demonstration Of $run command
- For Python
1) Without $input
~~~
$run
```py
import json
x={
"name":"Jhon",
"age":30,
"city":"New York"
}
y=json.dumps(x)
print (y) 
```
~~~

![Screenshot (452)](https://user-images.githubusercontent.com/80933048/130610916-40daf4c5-48f1-42c3-9cc3-b1e1405e30a3.png)
2) With $input
~~~
$run
```py
a = input()
b = input()
x = float(a) + float(b)
print(x)
```
$input
```
3
5
```
~~~

![Screenshot (450)](https://user-images.githubusercontent.com/80933048/130609755-cf0ab4a4-133c-45ab-9749-9f272c24a2c1.png)

- Note: Since It's A Discord Bot And Discord Will Not Allow To Send The Message That Having More Than 2000 Charecters.So Take That In consideration while using $Input
## How To Get The Api's
1) CodeForces
- To Get The Api Of CodeForces Is Simple You Just Need To Login With Your Account Then Click of API Button You Will Find Your Api Token here : https://codeforces.com/settings/api
- Click On Add Api Key
![Screenshot (435)](https://user-images.githubusercontent.com/80933048/129596054-52b99975-07fd-44b7-9dbb-4a7c83d71516.png)<br>

2) CodeChef
- To Get The Api of CodeChef You Need To Mail Them At api@codechef.com and Convey for what purpose you need there api
- Then They Will Send One Form You Need To Fill That Form And Wait. Then You Will Get Mail From There Side And Now You Will Be Able To Get The API Token 
- Documentation https://developers.codechef.com/#grant-types
## Contributor
<a href="https://github.com/kunal097">
  <img src="https://avatars.githubusercontent.com/u/23140769?v=4&s=50">
</a>





