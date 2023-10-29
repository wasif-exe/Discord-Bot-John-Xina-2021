import discord
import asyncio
import requests
import uuid
from datetime import datetime
from discord.ext import commands
from startTimer import startTimer
from webserver import keep_alive
import json
import os
import random
import praw

user_agent = "Blaze_4098 V.1"
reddit = praw.Reddit(
  client_id = "7Y9FRZ27msc-jwmPZBLp_Q",
  client_secret = os.environ['secret_reddit'],
  user_agent = user_agent
)

client = commands.Bot(command_prefix = '_')
client.remove_command("help")
no = random.randint(1,5)
owner = '𝕱𝖊 乂 𝕭𝖑𝖆𝖟𝖊#1107'
global msgmin,msghour,msgday
global today
today = datetime.now()


mainshop = [{"name":"Watch","price":100,"description":"Time"},
{"name":"Laptop","price":5000,"description":"Post Memes"},
{"name":"PC","price":10000,"description":"Post Memes But More Efficiently Than The Laptop"},
{"name":"Gaming_PC","price":80000,"description":"Post Memes At The Speed Of Light And Play Games"},
{"name":"Gun","price":12000,"description":"For Bank Robbery"},
{"name":"mask","price":100,"description":"Hide Your Face During A Bank Robbery"}
]

subred = ["AdviceAnimals","MemeEconomy","ComedyCemetery","dankmemes","PrequelMemes","terriblefacebookmemes","PewdiepieSubmissions","funny","teenagers/","deepfriedmemes","surrealmemes","nukedmemes","bigbangedmemes","wackytictaks","bonehurtingjuice","shittyadviceanimals","wholesomememes","raimimemes","historymemes","okbuddyretard","comedyheaven"]


killlist = ["dies from dabbing too hard","dies due to lack of friends.","pinged b1nzy","tried to get famous on YouTube by live-streaming something dumb. Skydiving while chained to a fridge.","was walking normally when out of the corner of their eye they saw someone do a bottle flip and dab causing {member} to have a stroke.","tried to play in the street...","has some bad chinese food, and pays the ultimate price."," dies from just being a bad, un-likeable dude."]

spank = ["https://c.tenor.com/5ropePOLZV4AAAAC/bad-beat.gif","https://c.tenor.com/4RIbgFCLRrUAAAAd/rikka-takanashi-bad-girl.gif","https://c.tenor.com/uER90n0laEEAAAAC/anime-spanking.gif","https://c.tenor.com/CAesvxP0KyEAAAAd/shinobu-kocho-giyuu-tomioka.gif","https://c.tenor.com/WNnO4lxUMVQAAAAC/anime-school-girl.gif","https://c.tenor.com/qhdaIdgiV78AAAAC/anime-spank.gif","https://c.tenor.com/B5oC9lACJ9kAAAAC/anime-spank.gif","https://c.tenor.com/zlM4Im2DJO4AAAAC/spank-spanked.gif","https://c.tenor.com/gScnebhgJn4AAAAC/taritari-anime-spank.gif","https://c.tenor.com/WN-vExb3SlgAAAAC/anime-schoolgirl.gif","https://c.tenor.com/eyIeo_JX_akAAAAC/anime-spanking.gif","https://c.tenor.com/LMKZH2bDKHsAAAAC/spank-anime.gif","https://c.tenor.com/0Nm1Udc_giwAAAAC/spank-spanking.gif","https://c.tenor.com/lNyexavajUEAAAAd/anime-spanking.gif"]

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = "Chill Cooldown Breh If Dont Want Coolown Buy The Premium Version Of John Xina"
        await ctx.send(msg)

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.group(invoke_without_command=True)
async def help(ctx):
    embedVar = discord.Embed(title="Help",description ="Use _help <command> for extended information on a command.",color=ctx.author.color)
    embedVar.add_field(name="Moderation", value = "kicks,bans,mutes,purges")
    embedVar.add_field(name="Money Game",value="Just Another Banking Game But This Time With More Fun")

    await ctx.send(embed = embedVar)

@help.command()
async def moderation(ctx):
    embedVar = discord.Embed(title = "Moderation",description="")
    embedVar.add_field(name = "_purge", value = "Usage : _purge [No. Of Lines]", inline = True)
    embedVar.add_field(name = "_mute", value = "Usage : _mute [persons name]", inline = True )
    embedVar.add_field(name = "_kick", value = "Usage : _kick [persons name] [reason]", inline = True)
    embedVar.add_field(name = "_ban", value = "Usage : _ban [persons name] [reason]", inline = True)

    await ctx.send(embed = embedVar)

@help.command(aliases=["kick"])
async def kicks(ctx):
    embedVar = discord.Embed(title = "_kick",description="Usage : _kick [persons name] [reason]")
    embedVar.add_field(name = "_kick", value = "Kicks The Person From The Server")

    await ctx.send(embed = embedVar)

@help.command(aliases=["ban"])
async def bans(ctx):
    embedVar = discord.Embed(title = "_ban",description="Usage : _ban [person name] [reason]")
    embedVar.add_field(name = "_ban", value = "Bans The Person From The Server")
    embedVar.add_field(name = "_unban", value = "Unbans The Person From The Server")

    await ctx.send(embed = embedVar)

@help.command(aliases=["mute"])
async def mutes(ctx):
    embedVar = discord.Embed(title = "_mute",description="Usage : _mute [person name] [reason]")
    embedVar.add_field(name = "_mute", value = "Mutes The Person But The Person Can Read Chat But Cannot Send Messages.")
    embedVar.add_field(name = "_unmute", value = "Unmutes The Person.")

    await ctx.send(embed = embedVar)

@help.command(aliases=["purge"])
async def purges(ctx):
    embedVar = discord.Embed(title = "_purge",description="Usage : _purge [No. Of Lines]")
    embedVar.add_field(name = "_purge", value = "Delets The No Of Messages Entered.")

    await ctx.send(embed = embedVar)

@client.event
async def on_ready():
    print("Bot Is Now Logged In")
    await client.change_presence(activity=discord.Streaming(name="𝕱𝖊 乂 𝕭𝖑𝖆𝖟𝖊#1107 Making Me", url='https://www.twitch.tv/blaze_4098'))

@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 2)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await client.process_commands(message)


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embedVar = discord.Embed(title="Hello Everyone", description="Thank You For Adding Me To This 🔥 Server", color = 0x206694 )
            embedVar.set_author(name="𝕱𝖊 乂 𝕭𝖑𝖆𝖟𝖊#1107", icon_url="https://cdn.discordapp.com/avatars/808744592928276500/e06af42518a7a427a15f0af0f108469f.webp?size=1024")
            embedVar.add_field(name="_help", value="For All The Other Commands For This Bot", inline=False)
            embedVar.set_thumbnail(url="https://c.tenor.com/8qwY5r9GhksAAAAC/john-cena.gif")
            embedVar.timestamp = datetime.datetime.utcnow()
            embedVar.set_footer(text = "Salute Sensei Jinping", icon_url = "https://api.time.com/wp-content/uploads/2016/02/gettyimages-481066721.jpg")
            embedVar.set_image(url="https://i.ytimg.com/vi/qBVNzVp10gQ/maxresdefault.jpg")
            await channel.send(embed=embedVar)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@client.command(aliases=[])
async def add(ctx,no1, no2):
  sum = no1 + no2
  await ctx.send(f"By my calculation on adding {no1} and {no2} you get **{sum}**")
  
@client.command(aliases=["lvl"])
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are at level {lvl}!')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is at level {lvl}! Congrats on wasting '+lvl*20+' minutes of your lifes time.')

@client.command()
async def poll(ctx, question, option1=None, option2=None):
  if option1==None and option2==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```{question}```\n**1️⃣ = Yes**\n**2️⃣ = No**")
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
  elif option1==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```{question}```\n**1️⃣ = Yes**\n**2️⃣ = No**")
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
  elif option2==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```{question}```\n**1️⃣ = {option1}**\n**2️⃣ = No**")
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
  else:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```{question}```\n**1️⃣ = {option1}**\n**2️⃣ = {option2}**")
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')

@client.command()
async def embed(ctx):

    embedVar = discord.Embed(title="Hello Everyone", description="Thank You For Adding Me To This 🔥 Server", color = 0x206694 )
    embedVar.set_author(name="𝕱𝖊 乂 𝕭𝖑𝖆𝖟𝖊#1107", icon_url="https://cdn.discordapp.com/avatars/808744592928276500/e06af42518a7a427a15f0af0f108469f.webp?size=1024")
    embedVar.add_field(name="_help", value="For All The Other Commands For This Bot", inline=False)
    embedVar.set_thumbnail(url="https://c.tenor.com/8qwY5r9GhksAAAAC/john-cena.gif")
    embedVar.timestamp = datetime.datetime.utcnow()
    embedVar.set_footer(text = "Salute Sensei Jinping", icon_url = "https://api.time.com/wp-content/uploads/2016/02/gettyimages-481066721.jpg")
    embedVar.set_image(url="https://i.ytimg.com/vi/qBVNzVp10gQ/maxresdefault.jpg")
    await ctx.channel.send(embed=embedVar)

@client.command()
async def say(ctx, *,content:str):
  await ctx.send(content+"           -"+ctx.message.author.name)

@client.command(aliases=["ech"])
async def echo(ctx, *, content:str):
    await ctx.send(content)
    await ctx.message.delete()

@client.command()
async def invite(ctx):
  embedVar = discord.Embed(title="Invite Link",description= "https://discord.com/api/oauth2/authorize?client_id=856763955825737729&permissions=8&scope=bot",color = 0x206694 )
  
  await ctx.send(embed=embedVar)


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx,amount=2):
    await ctx.channel.purge(limit = amount+1)

@client.command()
async def fpurge_no_mercy(ctx,amount=2):
    await ctx.channel.purge(limit = amount+2)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx,member:discord.Member,*,reason=""):
    await member.send("Too Uncool For The Server")
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx,member:discord.Member,*,reason=""):
    await member.send("Too Uncool For The Server")
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name+" Has Been UnBanned!")
            return
    await ctx.send(member+" was not found")

@client.command()
async def funban_no_mercy(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name+" Has Been UnBanned!")
            await ctx.message.delete()
            return
    await ctx.send(member+" was not found")
    await ctx.message.delete()

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")

@client.command()
async def fmute_no_mercy(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

@client.command()
async def funmute_no_mercy(ctx,member:discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await member.send(f" you have unmutedd from: - {ctx.guild.name}")
    embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
    await ctx.send(embed=embed)

@client.command(aliases=["bal"])
@commands.cooldown(1,3,commands.BucketType.user)
async def balance(ctx,member:discord.Member = None):
    if member == None:
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        credit_score = users[str(user.id)]["credit_score"]
        if credit_score <= 0:
          await ctx.author.send(file = discord.File('videos/credit.mp4'))
        embedVar = discord.Embed(title=f"{ctx.author.name}'s balance", color = discord.Color.red())
        embedVar.add_field(name = "Wallet Balance",value = wallet_amt)
        embedVar.add_field(name = "Bank balance",value = bank_amt)
        embedVar.add_field(name = "Credit Score",value = credit_score)
        await ctx.send(embed=embedVar)
    else:
        await open_account(member)
        user = member
        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        credit_score = users[str(user.id)]["credit_score"]
        embedVar = discord.Embed(title=f"{member.name}'s balance", color = discord.Color.red())
        embedVar.add_field(name = "Wallet Balance",value = wallet_amt)
        embedVar.add_field(name = "Bank Balance",value = bank_amt)
        embedVar.add_field(name = "Credit Score",value = credit_score)
        await ctx.send(embed=embedVar)




@client.command()
@commands.cooldown(1,30,commands.BucketType.user)
async def beg(ctx):
    users = await get_bank_data()
    user = ctx.author
    earnings = random.randint(1,500)

    await ctx.send(f"WOAW someone just gave u {earnings} coins!!" )



    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@client.command(aliases=["dep"])
@commands.cooldown(1,3,commands.BucketType.user)
async def deposit(ctx, amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please Enter Amount")
        return
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("You Are Not Rich Enough")
        return
    if amount<0:
        await ctx.send("Hahaha Nice Try U Can't Break Me. I Am Made Up Of Chinese Flesh")
        return
    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"You Deposited {amount} Coin's")


@client.command(aliases=["with"])
@commands.cooldown(1,3,commands.BucketType.user)
async def withdraw(ctx, amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please Enter Amount")
        return
    bal = await update_bank(ctx.author)
    if amount == "0":
        amount = bal[1]
    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("You Are Not Rich Enough")
        return
    if amount<0:
        await ctx.send("Hahaha Nice Try U Can't Break Me. I Am Made Up Of Chinese Flesh")
        return
    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"You Withdrew {amount} Coin's")



@client.command(aliases=["share"])
@commands.cooldown(1,15,commands.BucketType.user)
async def send(ctx,member:discord.Member , amount = None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("Please Enter Amount")
        return
    bal = await update_bank(ctx.author)
    if amount == "all":
        amount = bal[0]
    amount = int(amount)

    if amount<0:
        await ctx.send("Hahaha Nice Try U Can't Break Me. I Am Made Up Of Chinese Flesh")
        return
    await update_bank(ctx.author,-1*amount)
    await update_bank(member ,amount)

    await ctx.send(f"You Gave {amount} Coin's To {member}")

@client.command(aliases=["slot"])
@commands.cooldown(1,5,commands.BucketType.user)
async def slots(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please Enter Amount")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("You Are Not Rich Enough")
        return
    if amount<0:
        await ctx.send("Hahaha Nice Try U Can't Break Me. I Am Made Up Of Chinese Flesh")
        return

    final = []
    for i in range(3):
        a = random.choice(["🍌","🍓","🍋"])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author,2*amount)
        await ctx.send("Noice U Won Double Amount You Bet")
        await ctx.send(f"{2*amount} Has Been Added To Your Wallet")
        if final[0] == final[1] == final[2]:
            await update_bank(ctx.author,5*amount)
            await ctx.send("Noice U Won 5'Times The Amount You Bet")
            await ctx.send(f"{5*amount} Has Been Added To Your Wallet")
    else:
        await ctx.send("You Lost RIP")
        await ctx.send(f"{-1*amount} Has Been Reduced From Your Wallet")
        await update_bank(ctx.author,-1*amount)


@client.command()
@commands.cooldown(1,5,commands.BucketType.user)
async def bet(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please Enter Amount")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("You Are Not Rich Enough")
        return
    if amount<0:
        await ctx.send("Hahaha Nice Try U Can't Break Me. I Am Made Up Of Chinese Flesh")
        return

    choice = random.randint(1,6)
    rolled = random.randint(1,6)

    if choice == rolled-1 or choice == rolled+1:
        await update_bank(ctx.author,3*amount)
        await ctx.send("Noice U Won 3 Times The Amount You Bet")
        await ctx.send(f"{3*amount} Has Been Added To Your Wallet")
    if choice == rolled:
            await update_bank(ctx.author,5*amount)
            await ctx.send("Noice U Won 5'Times The Amount You Bet")
            await ctx.send(f"{5*amount} Has Been Added To Your Wallet")
    if choice == rolled-2 or choice == rolled+2:
        await update_bank(ctx.author,2*amount)
        await ctx.send("Noice U Won Double Amount You Bet")
        await ctx.send(f"{2*amount} Has Been Added To Your Wallet")
    else:
        await update_bank(ctx.author,-1*amount)


@client.command()
@commands.cooldown(1,25,commands.BucketType.user)

async def rob(ctx,member:discord.Member):
    await open_account(ctx.author)
    await open_account(member)

    bal = await update_bank(member)


    if bal[0]<250:
        await ctx.send("It's Not Worth To Rob Him He Is Very Poor")
        return
    earnings = random.randrange(0,bal[0])

    await update_bank(ctx.author,earnings)
    await update_bank(member , -1*earnings)

    await ctx.send(f"You Robbed {member}'s {earnings} Coin's!")

@client.command(aliases=["bankrob"])
async def heist(ctx,member:discord.Member):
    await open_account(ctx.author)
    await open_account(member)

    bal = await update_bank(member)
    bala = await update_bank(ctx.author)


    chance = random.randint(1,10)
    if bala[0] >= 2000:
        if chance < 5:

            if bal[1]<250:
                await ctx.send("It's Not Worth To Bank Rob Him He Is Very Poor")
                return
            abc = bal[1]/2
            earnings = random.randrange(0,int(abc))

            await update_bank(ctx.author,earnings)
            await update_bank(member , -1*earnings, "bank")

            await ctx.send(f"You Robbed {member}'s Bank And   Earned {earnings} Coin's!")

        else:
            await ctx.send("Bank Robbery Was Unsuccesful And You Were Caught!. You Had To Pay 2000 To Get Out.")

            await update_bank(ctx.author,-2000)
    else:
        await ctx.send("You Should Have At Least 2000 To Bank Rob")




@client.command()
async def shop(ctx):
    embedVar =  discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        embedVar.add_field(name = name,value = f"{price} | {desc}")
    await ctx.send(embed=embedVar)


@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("IDK What U Talkin Bout It Aint Here")
            return
        if res[1]==2:
            await ctx.send("You Are Not That Rich To Buy It.")
            free =  random.randint(1,1000)
            if free == 1:
                earnings = amount
                await update_bank(ctx.author,earnings)
                return
            return

    await ctx.send(f"You Just Bought {item} For {amount}")

@client.command(aliases=["inv"])
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    embedVar = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        embedVar.add_field(name = name, value = amount)
    await ctx.send(embed=embedVar)






@client.command()
async def ask(ctx, *, member: discord.Member = None):
    if not member:member=ctx.message.author
    payload = {
	     "model": "gpt-3.5-turbo",
	     "messages": [
		     {
			     "role": "user",
			      "content": ctx.message
		      }
	       ]}
    headers = {
	     "content-type": "application/json",
	     "X-RapidAPI-Key": "79f0ca8f3bmsh3a3fdf409334f64p155147jsn4626dbc6c557",
	     "X-RapidAPI-Host": "openai80.p.rapidapi.com"
    }

    response = requests.post("https://openai80.p.rapidapi.com/chat/completions", json=payload, headers=headers)

    await ctx.send(response.json())
  
  
    




@client.command(aliases=["mem"])
@commands.cooldown(1,3,commands.BucketType.user)
async def meme(ctx):
    global no
    no = random.randint(1,5)
    sr = random.randint(0,20)
    for submission in reddit.subreddit(subred[sr]).hot(limit=no):
        no += 1
        title = submission.title
        score = submission.score
        imgurl = submission.url

        if score >= 50:
            meme(ctx)

    if (str(imgurl.find(".png" or ".gif" or ".jpeg"))):
        embedVar = discord.Embed(title=title , description="", color = 0x206694 )
        embedVar.set_image(url=imgurl)
        embedVar.set_footer(text = f"👍 {score}")
        await ctx.send(embed = embedVar)

    else:
        meme(ctx)


@client.command(aliases=["av", "pfp"])
async def avatar(ctx, *, member: discord.Member = None):
    if not member:member=ctx.message.author

    message = discord.Embed(title=str(member), color=discord.Colour.red())
    message.set_image(url=member.avatar_url)
    

    await ctx.send(embed=message)

@client.command(aliases=["ndrop"])
@commands.cooldown(1,2,commands.BucketType.user)
async def nitro(ctx):
    nitro = rndnitro()
    await ctx.send(f"https://discord.gift/{nitro}")

@client.command(aliases=["gaytest","gaychck","gaychk"])
async def gaycheck(ctx,member:discord.Member=None):
  if member == None:
    message = await ctx.send('Testing (5%)done')
    await asyncio.sleep(1)
    await message.edit(content="Testing (23%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (30%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (57%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (74%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (99%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (101%)done")
    await asyncio.sleep(1)
    await ctx.send('jk its done and ...')
    await ctx.send(f"Congragulations {ctx.author.name} U Are Gae")
    await ctx.send(file=discord.File('videos/gae.mp4'))

  if member == owner:
    await ctx.send('My Owner Is Pure Straight Go Fk Other Gays')
  
  else:
    message = await ctx.send('Testing (5%)done')
    await asyncio.sleep(1)
    await message.edit(content="Testing (23%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (30%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (57%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (74%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (99%)done")
    await asyncio.sleep(1)
    await message.edit(content="Testing (101%)done")
    await asyncio.sleep(1)
    await ctx.send('jk its done and ...')
    await ctx.send(f'Congragulations {member} Is Gae')
    await ctx.send(file=discord.File('videos/gae.mp4'))



@client.command(aliases=["slp"])
async def slap(ctx,member:discord.Member=None):
  response = requests.get('https://shiro.gg/api/images/slap')
  slapurl = response.json()['url']
  if member == None:
    embedVar = discord.Embed(title=f"Sheeesh {ctx.author} slap's themself hard af",color=0x206694)
    embedVar.set_image(url=slapurl)

  else:
    embedVar = discord.Embed(title=f"Sheeesh {ctx.author} slap's {member} hard af",color=0x206694)
    embedVar.set_image(url=slapurl)
  
  await ctx.send(embed=embedVar)

@client.command(aliases=["pnch"])
async def punch(ctx,member:discord.Member=None):
  response = requests.get('https://shiro.gg/api/images/punch')
  punchurl = response.json()['url']
  if member == None:
    embedVar = discord.Embed(title=f"Sheeesh {ctx.author} punch's themself hard af",color=0x206694)
    embedVar.set_image(url=punchurl)

  else:
    embedVar = discord.Embed(title=f"Sheeesh {ctx.author} punch's {member} hard af",color=0x206694)
    embedVar.set_image(url=punchurl)
  
  await ctx.send(embed=embedVar)

@client.command(aliases=["pt"])
async def pat(ctx,member:discord.Member=None):
  response = requests.get('https://shiro.gg/api/images/pat')
  punchurl = response.json()['url']
  if member == None:
    embedVar = discord.Embed(title=f"Awww {ctx.author} pat's themself what a bit*h",color=0x206694)
    embedVar.set_image(url=punchurl)

  else:
    embedVar = discord.Embed(title=f"Awww {ctx.author} pat's {member} what a simp",color=0x206694)
    embedVar.set_image(url=punchurl)
    
  
  await ctx.send(embed=embedVar)
  

@client.command()
async def cry(ctx,member:discord.Member=None):
  
  response = requests.get('https://shiro.gg/api/images/cry')
  cryurl = response.json()['url']
  if member == None:
    embedVar = discord.Embed(title=f"{ctx.author} is crying ;( ",color=0x206694)
  
  else:
    embedVar = discord.Embed(title=f"{member} is crying",color=0x206694)

  embedVar.set_image(url=cryurl)
  await ctx.send(embed=embedVar)

@client.command(aliases=["qt"])
async def quote(ctx):
  colr = random.randint(0, 0xffffff)
  response = requests.get('https://animechan.vercel.app/api/random')
  animename = response.json()["anime"]
  character = response.json()["character"]
  quote = response.json()["quote"]
  embedVar = discord.Embed(title=f"Anime - **{animename}**",color = colr)
  embedVar.add_field(name = f"*{character}*-",value = quote)
  await ctx.send(embed=embedVar)

@client.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def mult(ctx,*,content:str):
  await ctx.message.delete()
  for x in range(2):
    await ctx.send(content)
  embedVar=discord.Embed(title="_mult",description="",color=discord.Color.random())
  embedVar.add_field(name="_mult5",value="Types The String 5 Times",inline=True)
  embedVar.add_field(name="_mult10",value="Types The String 10 Times",inline=True)
  embedVar.add_field(name="_mult15",value="Types The String 15 Times",inline=True)
  embedVar.add_field(name="_mult20",value="Types The String 20 Times",inline=True)
  embedVar.add_field(name="_mult25",value="Types The String 25 Times",inline=True)
  embedVar.add_field(name="_mult50",value="Types The String 50 Times",inline=True)
  embedVar.add_field(name="_mult75",value="Types The String 75 Times",inline=True)
  embedVar.add_field(name="_mult100",value="Types The String 100 Times",inline=True)
  embedVar.set_image(url="https://i.ytimg.com/vi/ZCjMibBBy7I/maxresdefault.jpg")
  await ctx.send(embed=embedVar)


@client.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def mult5(ctx,*,content:str):
  await ctx.message.delete()
  global last
  global date_time
  global text
  text = content
  date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
  last = ctx.author
  
  for x in range(5):
    await ctx.send(content)

@client.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def mult10(ctx,*,content:str):
  await ctx.message.delete()
  global last
  global text
  text = content
  global date_time
  date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
  last = ctx.author

  for x in range(10):
    await ctx.send(content)

@client.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def mult15(ctx,*,content:str):
  await ctx.message.delete()
  global last
  global text
  text = content
  global date_time
  date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
  last = ctx.author
  
  for x in range(15):
    await ctx.send(content)

@client.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def mult20(ctx,*,content:str):
  await ctx.message.delete()
  global last
  global text
  text = content
  global date_time
  date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
  last = ctx.author
  
  for x in range(20):
    await ctx.send(content)

@client.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def mult25(ctx,*,content:str):
  await ctx.message.delete()
  global last
  global text
  text = content
  global date_time
  date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
  last = ctx.author
  for x in range(25):
    await ctx.send(content)

@client.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def mult50(ctx,*,content:str):
  await ctx.message.delete()
  global last
  global text
  text = content
  global date_time
  date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
  last = ctx.author
 
  await ctx.send("https://c.tenor.com/CWgfFh7ozHkAAAAC/rick-astly-rick-rolled.gif")

@client.command()
@commands.cooldown(1,10000,commands.BucketType.guild)
async def mult75(ctx,*,content:str):
  await ctx.message.delete()
  global last
  global text
  text = content  
  global date_time
  date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
  last = ctx.author
  
  await ctx.send("https://c.tenor.com/CWgfFh7ozHkAAAAC/rick-astly-rick-rolled.gif")


@client.command()
@commands.cooldown(1,3,commands.BucketType.guild)
async def mult100(ctx,*,content:str):
  await ctx.message.delete()  
  global last
  global text
  text = content
  global date_time
  date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
  last = ctx.author
  
  
  await ctx.send("https://c.tenor.com/CWgfFh7ozHkAAAAC/rick-astly-rick-rolled.gif")
    
@client.command()
async def who(ctx):
  embedVar=discord.Embed(title="who used _mult")
  embedVar.add_field(name=f"{last}",value=f"{text}")
  embedVar.add_field(name="time",value=f"{date_time}")
  await ctx.send(embed=embedVar)



@client.command(aliases=["kll"])
async def kill(ctx,member:discord.Member):
  no = random.randint(0,7)
  await ctx.send(f"{member} {killlist[no]}")


@client.command(aliases=["spnk","spk"])
async def spank(ctx,member:discord.Member=None):
  no = random.randint(0,13)
  
  if member == None:
    embedVar = discord.Embed(title=f"Oof {ctx.author} spanked em self ",description = '\200',color=0x206694)
    embedVar.set_image(url=spank[no])
    await ctx.send(embed=embedVar)

  else:
    embedVar = discord.Embed(title=f"Oof {ctx.author} spanked {member} ",description = '\200',color=0x206694)
    embedVar.set_image(url=spank[no])
    await ctx.send(embed=embedVar)

@client.command(aliases=["pps","pp"])
async def ppsize(ctx,member:discord.Member):
  
  no = random.randint(0,10)
  if no == 0:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = 'Too Small To Be Seen')
  if no == 1:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8=D')
  if no == 2:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8==D')
  if no == 3:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8===D')
  if no == 4:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8====D')
  if no == 5:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8=====D')
  if no == 6:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8======D')
  if no == 7:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8=======D')
  if no == 8:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8=======D')
  if no == 9:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = '8========D')
  if no == 10:
    embedVar=discord.Embed(title=f"{member}'s pp size",description = "Too Large To Send On Discord.")
  await ctx.send(embed=embedVar)
  
    
@client.command()
async def rule34(ctx, *,tag:str):
  url = f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}"
  response = requests.get(url)
  image = response.json()['file_url']
  
  
  if image.endswith('.mp4'):
    response = requests.get(url)
      

  await ctx.send(image)

@client.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def credit(ctx):
    ques = 1
    global question
    if ques == 1:
      embedVar = discord.Embed(title = "Credit Test",description="Question: Who Is The President Of China")
      embedVar.add_field(name="_a",value="Master Jinping")
      embedVar.add_field(name="_b",value="My Mom")
      await ctx.send(embed = embedVar)
      global question
      question = 1
      message = await ctx.wait_for('a' or 'b')
      if message == 'a':
          users = await get_bank_data()
          user = ctx.author
          earnings = 15
          embedVar=discord.Embed(title="Correct Answer",description="15 Credit Score Has Been Added To Your Bank Account")
          embedVar.set_image(url="https://i.kym-cdn.com/entries/icons/original/000/027/195/cover10.jpg")
          await ctx.send(embed=embedVar)
          question = 0

          users[str(user.id)]["credit_score"] += earnings

          with open("mainbank.json","w") as f:
            json.dump(users,f)
            

      if message == 'b':
            users = await get_bank_data()
            user = ctx.author
            earnings = 15
            embedVar=discord.Embed(title="Wrong Answer",description="-15 Credit Score Has Been Added To Your Bank Account")
            embedVar.set_image(url="https://i.ytimg.com/vi/fJ5T2tNcpG4/hqdefault.jpg")
            await ctx.send(embed=embedVar)
            question = 0

            users[str(user.id)]["credit_score"] = users[str(user.id)]["credit_score"] - earnings

            with open("mainbank.json","w") as f:
              json.dump(users,f)
            
      else:
            await ctx.send("Wait Who Asked? You?")
            return
    



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#





async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 250
        users[str(user.id)]["bank"] = 0
        users[str(user.id)]["credit_score"] = 0

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)
    return users

async def update_bank(user,change = 0 ,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change
    with open("mainbank.json","w") as f:
        json.dump(users,f)


    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"],users[str(user.id)]["credit_score"]]
    return bal

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

def rndnitro(string_length=16):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}, Go get a life!')
        users[f'{user.id}']['level'] = lvl_end



keep_alive()
startTimer()
client.run(os.environ['TOKEN'])
