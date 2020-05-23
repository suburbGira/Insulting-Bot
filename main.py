import discord
from discord.ext import commands
import time
import asyncio
from platform import python_version
import random
import os
import shutil
import logging
import traceback
#//////////////////////////////////////////////////////
if str(os.path.basename(__file__)) == "main.py":
  f = open("token.txt")
  t = f.read()
  f.close()
else:
  f = open("tokendev.txt")
  t = f.read()
  f.close()

BOT_PREFIX = "?"
#//////////////////////////////////////////////////////
bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.load_extension("cogs.gnome")
bot.remove_command("help")
logging.basicConfig()
#//////////////////////////////////////////////////////

possible_responses = [
  "Nobody likes you",
  "Ur ugly",
  "It is quite possible that you are dumb",
  "That's what she said",
  "I know you are but what am I?",
  "You live like simple cattle or irrational pigs and, despite the fact that the gospel has returned, have mastered the fine art of misusing all your freedom",
  "Don't feel bad, there are many people who have no talent!",
  "I'd like to kick you in the teeth, but why should I improve your looks?",
  "At least there's one thing good about your body, it's not as ugly as your face",
  "Brains aren't everything. In fact, in your case they're nothing",
  "Did your parents ever ask you to run away from home?",
  "If I had a face like yours I'd sue my parents",
  "Any similarity between you and a human is purely coincidental",
  "Keep talking - someday you'll say something intelligent",
  "Don't you love nature, despite what it did to you?",
  "You're a man of the world. And you know what sad shape the world is in",
  "How much refund do you expect on your head now it's empty?",
  "You're like the end pieces of a loaf of bread. Everyone touches you, but nobody wants you",
  "You're not pretty enough to be that stupid",
  "I would love to insult you but I'm afraid I won't do it as well as nature did",
  "Somewhere out there, there's a tree whose single purpose on earth is to replace the oxygen you waste. Go find it and apologize",
  "I have neither the time nor the crayons to explain anything to you",
  "Are you naturally this dumb or do you have to put in effort",
  "You consistently set low expectations and fail to achieve them",
  "Just quit being yourself",
  "If I wanted to kill myself, I'd climb up your ego, and jump to your IQ",
  "I refuse to enter a battle of wits with an unarmed opponent",
  "Life is full of disappointments, just ask your parents",
  "When your mom dropped you off at school, she got a fine for littering",
  "You shouldn't act hard-to-get when you're hard-to-want",
  "Shall I compare thee to a summers day because thou art so temperate that your heat is triple that of the epicenter of the Tsar Bomb Explosion.",
  "Your face killed more people than Communism",
  "You have more chins than a Chinese phone directory",
  "HONK HONK, IT IS THE CLOWN CAR, YOU CLOWN, GET THE F*CK IN",
  "I am going to defenestrate you",
  "You are just like iron sulfide, a dull grey lifeless lump",
  "There are approximately 1,010,300 words in the English language, but I could never string enough words to express how much everyone wants to hit you with a chair",
  "You are proof that God has a sense of humor"
]
possible_nice_responses = [
  "Your face makes other people ugly",
  "You have really good taste in discord servers! (I.E. This one)",
  "Luckily, I'm not a drug, because you would be a nasty addict seeing how much you use me, seeing this is a message that appears less that 1/100 times",
]
on_message_responses = ["no u", "uno reverse", "reverse of reverse", "owo", "uwu", "stfu", "finger_guns", "@insulting bot"]
itdoeswhatyousay = ["kill me", "<:kms:686241691363311631>", "<:kms_weeb:686238052972232759>"]
death = ["kill yourself", "kill your self", "kys"]

class Listeners(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.index = 0
    self._last_member = None 
#//////////////////////////////////////////////////////
  @commands.Cog.listener()
  async def on_ready(self):
    global cooldown
    cooldown = dict()
    
    for user in bot.users:
      cooldown[str(user.id)] = int(time.time()) - 5

    with open("activity.txt") as f0, open("activitytype.txt") as f1, open("status.txt") as f2:
        activity = f0.read()
        activitytype = f1.read()
        status = f2.read()        
    
    activitytype1 = getattr(discord.ActivityType, activitytype)
    status1 = getattr(discord.Status, status)
    await bot.change_presence(status=status1, activity=discord.Activity(name=activity, type=activitytype1))
    
    print("Logged in as " + bot.user.name + "\nDiscord.py version", discord.__version__ + " (should be 1.3.3)\n" + "and Python Version " + python_version())
    print("\n" + str(bot.user.name), "is on:")
    for guild in bot.guilds:
      print(guild.name + " | ID = " + str(guild.id))
      if guild.id == 693901918342217758:
        #Support Server
        pass
    print ("")
#//////////////////////////////////////////////////////
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    os.mkdir("servers/" + str(guild.id))
    try:
      targetguild = bot.get_guild(693901918342217758)
      role = targetguild.get_role(703307566654160969)
      if guild.owner in targetguild.members:
        await targetguild.get_member(guild.owner.id).add_roles(role)
        
      for user in guild.members:
        cooldown[str(user.id)] = int(time.time()) - 5
      
      with open("servers/" + str(guild.id) + "/nummessages.txt", "x") as f0, open("servers/" + str(guild.id) + "/banned_words.txt", "x") as f1, open("servers/" + str(guild.id) + "/" + str(guild.name), "x") as f2:
        f0.write("0") 
      
      await guild.create_role(name="LUCKY PERSON!", colour=discord.Colour(0xfe00ff), hoist=True, reason="Setting up Lucky Person role, is given to someone who triggers @Insulting Bot and gets a 1/100 chance.")
            
      await bot.get_guild(693901918342217758).get_channel(695575453095821313).send("Just joined " + str(guild.name) + "! I am now in " + str(len(bot.guilds)) + " different servers!")
      await guild.owner.send("Insulting Bot has just joined your server! \nYou need to move the 'Lucky Person' Role above whoever you want to have a chance to get it, and the Insulting Bot role above that so it can actually give the role! \nDo ?helpme to find out more and check out the support server if you have any trouble! https://discord.gg/zWPWwQC")
    except:
      await guild.owner.send("Insulting Bot tried to join your server, but either didn't get the permissions it needs or errored.\n" + "To get Insulting bot to start working, simply make a role called ```LUCKY PERSON!```, and it will run." "\nIf you want to talk to the owner of the bot about this join the support server at https://discord.gg/zWPWwQC")
      await bot.get_guild(693901918342217758).get_channel(695575453095821313).send("Just tried to join " + str(guild.name) + " but didn't get perms?")
  
  @commands.Cog.listener()   
  async def on_guild_update(self, before, after):
    if before.name != after.name:
      os.rename("servers/" + str(before.id) + "/" + before.name, "servers/" + str(after.id) + "/" + after.name)
  
  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    mypath = "servers/" + str(guild.id)
    shutil.rmtree(mypath)
    await bot.get_guild(693901918342217758).get_channel(695575453095821313).send("Just left/got kicked from " + str(guild.name) + ". I am now in " + str(len(bot.guilds)) + " servers")
    for user in bot.users:
      cooldown[str(user.id)] = int(time.time()) - 5
#//////////////////////////////////////////////////////
  @commands.Cog.listener()
  async def on_member_join(self, member):
    global cooldown
    cooldown[str(member.id)] = int(time.time()) - 5
    targetguild = bot.get_guild(693901918342217758)
    role = targetguild.get_role(703307566654160969)
    for guild in bot.guilds:
      if guild.owner.id == member.id and guild.owner in targetguild.members:
        await targetguild.get_member(member.id).add_roles(role)
#//////////////////////////////////////////////////////
  @commands.Cog.listener()
  async def on_error(self, ctx, event, args):
    error = traceback.format_exc()
    await bot.get_channel(696062725725618176).send(ctx.author.name + " caused an error with the message: " + ctx.clean_content + " in " + ctx.guild.name + "\n```" + str(error) + "```\n")
#//////////////////////////////////////////////////////
class Main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.index = 0
    self._last_member = None 
    
  def cooldown_test(ctx):
    currenttime = time.time()
    if cooldown[str(ctx.author.id)] is None:
      cooldown[str(user.id)] = int(time.time()) - 5
    mintime = int(cooldown[str(ctx.author.id)]) + 5
    if mintime >= currenttime:
      return False
    else:
      return True
      cooldown[str(ctx.author.id)] = time.time()
#//////////////////////////////////////////////////////
  @commands.Cog.listener()
  async def on_message(self, message):
    
    if any(x in message.clean_content.lower() for x in on_message_responses):
      #if "send_messages" not in str(message.guild.me.permissions_in(message.channel)):
       # await message.author.send("Sorry I could not respond as I don't have permissions to send messages.")
       # return
      if discord.utils.get(message.guild.roles, name="LUCKY PERSON!") is None:
        await message.channel.send("Please make a role called ```LUCKY PERSON!``` and try again!")
        return  
  
    path = "servers/" + str(message.guild.id) + "/"
    nummessagespath = "servers/" + str(message.guild.id) + "/nummessages.txt"
    banned_words_path = "servers/" + str(message.guild.id) + "/banned_words.txt"

    with open(banned_words_path) as f0, open(nummessagespath) as f1:
      banned_words = f0.read().splitlines()
      numberofmessages = f1.read()
    
    if any(x in message.clean_content.lower() for x in banned_words) and message.author.guild_permissions.administrator is False and message.author.bot == False:
      await message.delete()
      sendmessage = "Shut up, " + message.author.mention
      await message.channel.send(sendmessage)
    
    if os.path.exists(path + "retry") is False and message.author.bot is False:
      randomchance = random.randint(0, 100)
      if str(bot.user.id) in message.content:
        currenttime = int(time.time())
        if cooldown[str(message.author.id)] is None:
          cooldown[str(message.author.id)] = int(time.time()) - 5
        mintime = int(cooldown[str(message.author.id)]) + 5
        if mintime <= currenttime:
          cooldown[str(message.author.id)] = time.time()
          if randomchance == 69 or message.author.id == 560824246356410378: #lol
            if "spam" not in message.channel.name and message.author.id != 613999658339008523:
              await message.author.add_roles(discord.utils.get(message.guild.roles, name="LUCKY PERSON!"))
            await message.channel.send(random.choice(possible_nice_responses) + ", " + message.author.mention)
          else:
            await message.channel.send(random.choice(possible_responses) + ", " + message.author.mention)
        else:
          cooldown[str(message.author.id)] = time.time()
          await message.channel.send("Calm down, " + message.author.mention)
      elif numberofmessages == "50":
        if randomchance == 69:
          if "spam" not in message.channel.name:
            await message.author.add_roles(discord.utils.get(message.guild.roles, name="LUCKY PERSON!"))
          await message.channel.send(f"{random.choice(possible_nice_responses)}, {message.author.mention}")
        else:
          await message.channel.send(random.choice(possible_responses))
        with open(nummessagespath, "w") as f:
          f.write("0")
      else:
        with open(nummessagespath, "w") as f:
          f.write(str(int(numberofmessages) + 1))
      
      currenttime = int(time.time())
      if cooldown[str(message.author.id)] is None:
        cooldown[str(message.author.id)] = int(time.time()) - 5
        
      mintime = int(cooldown[str(message.author.id)]) + 5
      if mintime <= currenttime:
        if "no u" in message.clean_content.lower():
          cooldown[str(message.author.id)] = time.time()
          await message.channel.send("<:reverse_card:686247784898494492>")
        if "uno reverse" in message.clean_content.lower() or "<:reverse_card:686247784898494492>" in message.clean_content.lower():
          cooldown[str(message.author.id)] = time.time()
          await message.channel.send("<:reverse_of_reverse:686259425954234429>")
        if "reverse of reverse" in message.clean_content.lower() or "<:reverse_of_reverse:686259425954234429>" in message.clean_content.lower():
          cooldown[str(message.author.id)] = time.time()
          await message.channel.send("<:counter_counter:686260454670205009>")
        if "owo" in message.clean_content.lower():
          cooldown[str(message.author.id)] = time.time()
          await message.channel.send("<:uwu:686246706198872074>")
        if "uwu" in message.clean_content.lower():
          cooldown[str(message.author.id)] = time.time()
          await message.channel.send("owo")
        if "stfu" in message.clean_content.lower():
          cooldown[str(message.author.id)] = time.time()
          await message.channel.send("no u :)")
        if "finger_guns" in message.clean_content.lower():
          cooldown[str(message.author.id)] = time.time()
          await message.channel.send("<:finger_guns:686261755684716584>")
      # below code breaks everything, don't uncommment
      #if any(x in message.clean_content.lower() for x in on_message_responses) and mintime >= currenttime:
        #await message.channel.send("Calm down, " + message.author.mention)
#//////////////////////////////////////////////////////
  
  @commands.bot_has_permissions(send_messages=True, embed_links=True)
  @commands.command()
  async def helpme(self, ctx):
    await ctx.channel.trigger_typing()
    try:
      embed=discord.Embed(title="Insulting Bot Help!", url="https://www.discord.gg/zWPWwQC", color=0xff5300)
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/698567401721167872/698575832054104145/0e291f67c9274a1abdddeb3fd919cbaa.png")
      embed.add_field(name="@Insulting Bot", value="Randomly insults you! (or does it?)", inline=True)
      embed.add_field(name="?insult @person", value="Randomly insults the person you ping!", inline=True)
      embed.add_field(name="?laughing/?laugh, ?cringe, and ?breakdown", value="Express your feelings", inline=True)
      embed.add_field(name="Moderation", value="Important Commands!", inline=False)
      embed.add_field(name="?add_phrase", value="Adds a word or phrase to the 'shut up' list!", inline=True)
      embed.add_field(name="?delete_phrase", value="Deletes a word or phrase from the 'shut up' list!", inline=True)
      embed.add_field(name="?list_phrase", value="Lists all the words and phrases from the 'shut up' list.", inline=True)
      embed.add_field(name="Others", value="Universal Commands", inline=False)
      embed.add_field(name="?help", value="Shows this message", inline=True)
      embed.add_field(name="?suggest *suggestion*", value=f"Sends a suggestion to the owner of {bot.user.name}!", inline=True)
      embed.add_field(name="?invite", value=f"Sends the instructions to invite {bot.user.name}!", inline=True)
      embed.set_footer(text=f"Do you want to get support for {bot.user.name} or invite it to your own server? https://discord.gg/zWPWwQC")
      await ctx.send(embed=embed)
    except:
      await ctx.send("```I don't have embed messages perms, falling back to old (outdated) help message```")
      await ctx.send(f"***Insulting Bot Help List***\n{bot.user.mention}: Shows a Random Insult, 1/100 chance to be nice and give you the Lucky Person role (this is triggered every 50 messages aswell)\n\n?insult @*person*:  Randomly chooses a insult with no chance to be nice and mentions the person you ping!\n?laughing/?laugh, ?cringe and ?breakdown: Express your feelings\n\n<:finger_guns:686261755684716584> Will be mimiced back\nowo: Says <:uwu:686246706198872074>\nstfu: Don't be mean\n<:kms:686241691363311631> <:kms_weeb:686238052972232759> and kill me: will complete the action\n\n**Important Commands**\n?add_phrase/?delete_phrase: Adds or deletes a word or phrase from the 'shut up' list.\n?suggest: Tells Gnome!#6669 to add something to Insulting Bot. This could be new insults, commands or tweaks to existing commands!\n?lag: Are you lagging or am I?\n\nYou want a invite link to invite Insulting Bot to your own server, join the support server!\nhttps://discord.gg/zWPWwQC")
#//////////////////////////////////////////////////////
  @commands.bot_has_permissions(send_messages=True)
  @commands.check(cooldown_test)
  @commands.command()
  async def insult(self, ctx, insulte : discord.Member):
    cooldown[str(ctx.author.id)] = time.time() #Sets cooldown
    if insulte.id == bot.user.id:
      await ctx.send("Why would I do that?")
    else:
      await ctx.send(f"{random.choice(possible_responses)}, {insulte.mention}")
#//////////////////////////////////////////////////////
  @commands.command()
  @commands.bot_has_permissions(send_messages=True, attach_files=True, embed_links=True)
  @commands.check(cooldown_test)
  async def cringe(self, ctx):
    await ctx.send(file=discord.File('images/cringe.jpg'))
  
  @commands.command(aliases=['laughing'])
  @commands.bot_has_permissions(send_messages=True, attach_files=True, embed_links=True)
  @commands.check(cooldown_test)
  async def laugh(self, ctx):
    randomc = random.randint(1,2)
    if randomc == 1:
      await ctx.send(file=discord.File('images/laughing.jpg'))
    if randomc == 2:
      await ctx.send(file=discord.File('images/laughing2.jpg'))
  
  @commands.command()
  @commands.bot_has_permissions(send_messages=True, attach_files=True, embed_links=True)
  @commands.check(cooldown_test)
  async def breakdown(self, ctx):
      await ctx.send(file=discord.File('images/breakdown.jpg'))
  
  @commands.command()
  @commands.bot_has_permissions(send_messages=True, attach_files=True, embed_links=True)
  @commands.check(cooldown_test)
  async def mood(self, ctx):
      await ctx.send(file=discord.File('images/mood.jpg'))

#//////////////////////////////////////////////////////
  @commands.command(aliases=['add_word'])
  @commands.bot_has_permissions(send_messages=True, manage_messages=True)
  @commands.has_permissions(administrator=True)
  async def add_phrase(self, ctx, *, phrase : str):
    banned_words_path = f"servers/{str(ctx.guild.id)}/banned_words.txt"
    with open(banned_words_path) as f0:
      banned_words = f0.read().splitlines()
    with open(banned_words_path, "a") as f:
      f.write(phrase.lower() + "\n")
    
    await ctx.send("Added phrase: " + phrase)
    banned_words.append(phrase)
  
  @commands.command(aliases=['delete_word', 'del_word', 'del_phrase'])    
  @commands.bot_has_permissions(send_messages=True, manage_messages=True)
  @commands.has_permissions(administrator=True)
  async def delete_phrase(self, ctx, *, phrase : str):
    banned_words_path = f"servers/{str(ctx.guild.id)}/banned_words.txt"
    with open(banned_words_path) as f0:
      banned_words = f0.read().splitlines()
    if phrase in banned_words:
      while phrase in banned_words: banned_words.remove(phrase)
      os.remove(banned_words_path)
      with open(banned_words_path, "a") as outfile:
        for word1 in banned_words:
          outfile.write(word1.lower() + "\n")
      await ctx.send(f"Deleted phrase from banned phrases: {phrase}")
    else:
      await ctx.send(f"Error, I don't think that is in the banned phrases list: {phrase}")
      await ctx.send(f"The banned phrases on this server are: {str(banned_words)}")
  
  @commands.command(aliases=['delete_all_words', 'delete_all_word', 'delete_all_phrase'])
  @commands.bot_has_permissions(send_messages=True, manage_messages=True)
  @commands.has_permissions(administrator=True)
  async def delete_all_phrases(self, ctx):
    banned_words_path = f"servers/{str(ctx.guild.id)}/banned_words.txt"
    os.remove(banned_words_path)
    with open(banned_words_path, "x") as f:
      pass
    await ctx.send("Done")

  @commands.command(aliases=['list_words', 'list_word', 'list_phrases'])  
  @commands.bot_has_permissions(send_messages=True, manage_messages=True)
  async def list_phrase(self, ctx):
    with open(f"servers/{str(ctx.guild.id)}/banned_words.txt") as f0:
      banned_words = f0.read().splitlines()
    
    if len(banned_words) >= 1:
      await ctx.send(f"The banned phrases on this server are: {str(banned_words)}")
    else:
      await ctx.send(f"I don't think there are any banned phrases on this server, {ctx.author.mention}")
  
  #//////////////////////////////////////////////////////
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if hasattr(ctx.command, 'on_error'):
      return
    error = getattr(error, 'original', error)
    if isinstance(error, commands.DisabledCommand):
      return await ctx.send(f'{ctx.command} has been disabled.')
    elif isinstance(error, commands.NotOwner):
      return
    elif isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
      return await ctx.send(f"Did you type the command right, {ctx.author.mention}?\nTry doing ?helpme!")
    elif isinstance(error, commands.MissingPermissions):
      return await ctx.send("You are missing the permmission to run this command.")
    elif isinstance(error, commands.BotMissingPermissions):
       if "send_messages" in str(error.missing_perms):
         await ctx.author.send("Sorry I could not complete this command as I don't have send messages permissions.")
       else:
         await ctx.send(f'I am missing the permissions: {str(error.missing_perms).replace("[", "").replace("]", "")}')
    elif isinstance(error, commands.CheckFailure):
      deletablemessage = await ctx.send("Please don't spam (5 second cooldown on this command)")
      return 
    elif isinstance(error, commands.CommandNotFound):
      return await bot.get_channel(705011123778486302).send(f"{ctx.author.name} just typed the wrong command {ctx.message.content} in {ctx.guild.name}")
    
    with open("temp.txt", "w") as f:
      print(ctx.author.name + " caused an error with the message: " + ctx.message.clean_content + " in " + ctx.guild.name + "\n```", file=f)
      traceback.print_exception(type(error), error, error.__traceback__, file=f)
    with open("temp.txt") as f:
      temp = f.read()
    await bot.get_channel(696062725725618176).send(temp + "```\n")
#//////////////////////////////////////////////////////

bot.add_cog(Listeners(bot))
bot.add_cog(Main(bot))
bot.run(t)
