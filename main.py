import os
import discord
import random
from discord.ext import commands
import asyncio
import logging
import sys
import time


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents) 
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix="/", intents=intents)

local_files = [
    r"C:\Users\Acer\Downloads\snaptik_7351445890642545963_v2.mp4"
    ]

    # Badass skeleton meme URLs
meme_urls = [
        "https://i.redd.it/2b8s0g6jja2f1.jpeg",
            "https://i.pinimg.com/1200x/3c/08/de/3c08de2bfa09821b9c4e704022d8f2fa.jpg",
                "https://i.imgflip.com/7inqj0.jpg",
                    "https://i.imgflip.com/7xmn8n.jpg", 
                        "https://i.pinimg.com/736x/f0/1b/0e/f01b0e86d551a75ccf8c84b0826d0a11.jpg",
                            "https://i.pinimg.com/1200x/cd/f8/7a/cdf87a5186c87047c25080d3410ed946.jpg",
                                "https://i.pinimg.com/1200x/cd/f8/7a/cdf87a5186c87047c25080d3410ed946.jpg",
                                    "https://i.pinimg.com/1200x/2b/85/50/2b8550fb9b4e06d042eb5f5c05b618f1.jpg",
                                        "https://i.imgflip.com/6nd72z.jpg",
                                            "https://pbs.twimg.com/media/FeqDHE0WYAA0YTK.jpg",
                                                "https://i.imgflip.com/7sptju.jpg",
                                                    "https://i.imgflip.com/7gayq4.jpg",
                                                        "https://i.imgflip.com/7dpv0u.jpg",
                                                            "https://i.pinimg.com/736x/53/dc/d4/53dcd49e6827b4a079eaae02ee6b380b.jpg",
                                                                "https://i.imgflip.com/84g2g2.jpg",
                                                                    "https://i.imgflip.com/7a52cz.jpg",
                                                                        "https://media.tenor.com/pbqrX4yyf88AAAAe/skeleton-meme-alcoholic.png",
                                                                            "https://i.imgflip.com/8q95sa.jpg",
                                                                                "https://i.redd.it/gmgr96scrjv91.jpg",
                                                                                    "https://i.imgflip.com/7x7dwu.jpg",
                                                                                        "https://i.imgflip.com/7vrpwm.jpg",
                                                                                            "https://i.imgflip.com/65h8op.jpg",
                                                                                                "https://i.pinimg.com/736x/72/f1/ab/72f1abc9a21628ea56709ace202ee521.jpg",
                                                                                                    "https://i.imgflip.com/7vrr6j.jpg",
                                                                                                        r"C:\Users\Acer\Downloads\snaptik_7351445890642545963_v2.mp4"
                                                                                                        ]

# --- CONFIG -
REACTION_MESSAGE_1_ID = 1412931122320375919

REACTION_MESSAGE_2_ID = 1412933422896250970

REACTION_MESSAGE_3_ID = 1412935194457149493

# Reaction emoji: role ID
EMOJI_ROLE_MAP_1 = {
"🔴": 1412130611946061934,  # Red role
"🟠": 1412134932662325278,  # Orange role
"🟡": 1412136869474336838,  # Yellow role
"🟢": 1412137881656361071,  # Green role
"🔵": 1412135296283447417,  # Blue role
"🟣": 1412138469421224036,  # Purple role
"🟤": 1412138953745633383,  # Brown role
"⚫": 1412137284416966718,  # Black role
"⚪": 1412136850889375876,  # White role
"🔘": 1412139322957627513,  # Gray role
}

EMOJI_ROLE_MAP_2 = {
"1️⃣": 1412532937739599912,  # He/Him role
"2️⃣": 1412171501444006059,  # She/Her role
"3️⃣": 1412535964969996429,  # They/Them role
"4️⃣": 1412538448786493553,  # Postgender role
"5️⃣": 1412539040925749269,  # Neogender role
"6️⃣": 1412171457706070036,  # Any role
"7️⃣": 1412537631509578004  # None role
}

EMOJI_ROLE_MAP_3 = {
"🧒": 1412853158387912745,  # Pegi 7 role
"👦": 1412853444212953119,  # Pegi 12 role
"🧑": 1412853494536208655,  # Pegi 16 role
"👨": 1412853541776920696  # Pegi 18 role
}
                                                                                                                                                                                            
@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user}")


    @bot.event
    async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
        if payload.message_id == REACTION_MESSAGE_1_ID:
                guild = bot.get_guild(payload.guild_id)
role_id = EMOJI_ROLE_MAP_1.get(str(payload.emoji))
if role_id:
                                            role = guild.get_role(role_id)
member = guild.get_member(payload.user_id)
if member and role:
for emoji, r_id in EMOJI_ROLE_MAP_1.items():
old_role = guild.get_role(r_id)
if old_role in member.roles:
await member.remove_roles(old_role)
await member.add_roles(role)
print(f"🎨 Changed {member.display_name}'s color to {role.color}")


if payload.message_id == REACTION_MESSAGE_2_ID:
guild = bot.get_guild(payload.guild_id)
role_id = EMOJI_ROLE_MAP_2.get(str(payload.emoji))
if role_id:
                                                                                                                                                                                                                            role = guild.get_role(role_id)
member = guild.get_member(payload.user_id)
if member and role:
                                                                                                                                                                                                                                                                    await member.add_roles(role)
print(f"✅ Gave {member.display_name} role {role.name}")


if payload.message_id == REACTION_MESSAGE_3_ID:
                                                                                                                                                                                                                                                                                                guild = bot.get_guild(payload.guild_id)
role_id = EMOJI_ROLE_MAP_3.get(str(payload.emoji))
if role_id:
                                                                                                                                                                                                                                                                                                                            role = guild.get_role(role_id)
member = guild.get_member(payload.user_id)
if member and role:
                                                                                                                                                                                                                                                                                                                                                                    await member.add_roles(role)
print(f"✅ Gave {member.display_name} role {role.name}")

@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
                                                                                                                                                                                                                                                                                                                                                                                        guild = bot.get_guild(payload.guild_id)
if guild is None:
                                                                                                                                                                                                                                                                                                                                                                                                    return


if payload.message_id == REACTION_MESSAGE_1_ID:
                                                                                                                                                                                                                                                                                                                                                                                                                role_id = EMOJI_ROLE_MAP_1.get(str(payload.emoji))
if role_id:
                                                                                                                                                                                                                                                                                                                                                                                                                                    role = guild.get_role(role_id)
member = guild.get_member(payload.user_id)
if member and role and role in member.roles:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            await member.remove_roles(role)
print(f"❌ Removed color {role.color} from {member.display_name}")


if payload.message_id == REACTION_MESSAGE_2_ID:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        role_id = EMOJI_ROLE_MAP_2.get(str(payload.emoji))
if role_id:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            role = guild.get_role(role_id)
member = guild.get_member(payload.user_id)
if member and role and role in member.roles:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    await member.remove_roles(role)
print(f"❌ Removed role {role.name} from {member.display_name}")


if payload.message_id == REACTION_MESSAGE_3_ID:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                role_id = EMOJI_ROLE_MAP_3.get(str(payload.emoji))
if role_id:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    role = guild.get_role(role_id)
member = guild.get_member(payload.user_id)
if member and role and role in member.roles:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            await member.remove_roles(role)
print(f"❌ Removed role {role.name} from {member.display_name}")


@bot.command()
@commands.has_permissions(administrator=True)
async def colors(ctx):
    msg = await ctx.send(
            "***NO WEŹ WYBIERAJ TEN KOLOR NAZWY***:\n"
                    ">>> **1. Czerwony\n"
                            "2. Pomarańczowy\n"
                                    "3. Żółty\n"
                                            "4. Zielony\n"
                                                    "5. Niebieski\n"
                                                            "6. Fioletowy\n"
                                                                    "7. Brązowy\n"
                                                                            "8. Czarny\n"
                                                                                    "9. Biały\n"
                                                                                            "10. Szary**"

                                                                                                )
await msg.add_reaction("🔴")
await msg.add_reaction("🟠")
await msg.add_reaction("🟡")
await msg.add_reaction("🟢")
await msg.add_reaction("🔵")
await msg.add_reaction("🟣")
await msg.add_reaction("🟤")
await msg.add_reaction("⚫")
await msg.add_reaction("⚪")
await msg.add_reaction("🔘")
print(f"📌 Save this message ID: {msg.id}")


@bot.command()
async def genders(ctx):
msg = await ctx.send(
"***ZAIMKI TEŻ***:\n"
">>> **1. Męskie\n"
"2. Żeńskie\n"
"3. Niebinarne\n"
"4. Postpłciowe\n"
"5. Neo\n"
"6. Każde\n"
"7. Żadne**"
)

await msg.add_reaction("1️⃣")
await msg.add_reaction("2️⃣")
await msg.add_reaction("3️⃣")
await msg.add_reaction("4️⃣")
await msg.add_reaction("5️⃣")
await msg.add_reaction("6️⃣")
await msg.add_reaction("7️⃣")
print(f"📌 Save this message ID: {msg.id}")


@bot.command()
async def agess(ctx):
                                                                                                                                                                                                                                                        msg = await ctx.send(
                                                                                                                                                                                                                                                                "***WIEK? NO OCZYWIŚCIE ŻE TAK***:\n"
                                                                                                                                                                                                                                                                        ">>> **1. 7-12\n"
                                                                                                                                                                                                                                                                                "2. 12-16\n"
                                                                                                                                                                                                                                                                                        "3. 16-18\n"
                                                                                                                                                                                                                                                                                                "4. 18+**"

                                                                                                                                                                                                                                                                                                    )
await msg.add_reaction("🧒")
await msg.add_reaction("👦")
await msg.add_reaction("🧑")
await msg.add_reaction("👨")
print(f"📌 Save this message ID: {msg.id}")


@bot.event
async def on_member_join(member):
                                                                                                                                                                                                                                                                                                                            channel_1 = discord.utils.get(member.guild.text_channels, name="witamy")
channel_2 = discord.utils.get(member.guild.text_channels, name="ogólny")

if channel_1:
                                                                                                                                                                                                                                                                                                                                            await channel_1.send(f">>> 🔥 **WITAJ {member.mention} W NASZE ZAJEBIŚCIE ZAJEBISTE PROGI!** 🔥 ***(jak postanowisz griefować naszą ściane to wezwę moją mame...)***")
if channel_2:
                                                                                                                                                                                                                                                                                                                                                        await channel_2.send(f"WITAM, WITAM, **GORĄCO** WITAM {member.mention} 🔥🔥")


                                                                                                                                                                                                                                                                                                                                                        @bot.event
                                                                                                                                                                                                                                                                                                                                                        async def on_member_remove(member):
                                                                                                                                                                                                                                                                                                                                                            channel = discord.utils.get(member.guild.text_channels, name="żegnamy")
if channel:
                                                                                                                                                                                                                                                                                                                                                                        await channel.send(f">>> *{member.mention} odszet z serwera 😕 (morze wruci, chociasz wontpie w to...)*")



                                                                                                                                                                                                                                                                                                                                                                        @bot.command()
                                                                                                                                                                                                                                                                                                                                                                        async def badass_skeleton(ctx):
                                                                                                                                                                                                                                                                                                                                                                            url = random.choice(meme_urls)



                                                                                                                                                                                                                                                                                                                                                                            # Send local file
if os.path.exists(url):
                                                                                                                                                                                                                                                                                                                                                                                        await ctx.send(file=discord.File(url))
else:
                                                                                                                                                                                                                                                                                                                                                                                                    await ctx.send(url)


                                                                                                                                                                                                                                                                                                                                                                                                    @bot.command()
                                                                                                                                                                                                                                                                                                                                                                                                    async def zas(ctx):
                                                                                                                                                                                                                                                                                                                                                                                                        await ctx.send("**NO CHYBA WIESZ JAK... JAK SIĘ GRZECZNIE ZACHOWYWAĆ**")
                                                                                                                                                                                                                                                                                                                                                                                                       
   
bot.run(os.environ["TOKEN"])

def start_bot():
       while True:
               try:
                           keep_alive()  # Start web server
token = os.environ.get("TOKEN")
if not token:
                                                                   raise ValueError("TOKEN environment variable not set.")
bot.run(token)
except Exception as e:
print(f"Bot crashed with error: {e}")
print("Restarting bot in 5 seconds...")
time.sleep(5) 

if __name__ == "__main__":
                                                                                                                               start_bot()

                                                                                                                               async def run_bot():
                                                                                                                                   """Tries to start the bot with retries."""
retries = 0
max_retries = 5

while True:
try:
                                                                                                                                                                   logging.info("Starting Discord bot...")
await client.start(os.environ["Token"])

except (discord.ConnectionClosed, discord.HTTPException) as e:
retries += 1
wait_time = min(2 ** retries, 60)  # exponential backoff, max 1 min
logging.warning(f"Bot disconnected ({e}). Retrying in {wait_time}s...")
await asyncio.sleep(wait_time)

if retries >= max_retries:
                                                                                                                                                                                                                                                                   logging.error("Max retries reached. Restarting fresh loop...")
retries = 0  # reset retry counter

except Exception as e:
logging.exception(f"Unexpected error: {e}")
await asyncio.sleep(10)  # 

@client.event
async def on_ready():
                                                                                                                                                                                                                                                                                                                       logging.info(f"Logged in as {client.user} (ID: {client.user.id})")
logging.info("Bot is ready!")


@client.event
async def on_message(message: discord.Message):
try:
                                                                                                                                                                                                                                                                                                                                       if message.author == client.user:
                                                                                                                                                                                                                                                                                                                                                   return

if message.content.lower() == "ping":
                                                                                                                                                                                                                                                                                                                                                                       await message.channel.send("pong 🏓")

                                                                                                                                                                                                                                                                                                                                                                           except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                                   logging.exception(f"Error handling message: {e}")

                                                                                                                                                                                                                                                                                                                                                                                   if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                       try:
                                                                                                                                                                                                                                                                                                                                                                                               asyncio.run(run_bot())
                                                                                                                                                                                                                                                                                                                                                                                                   except KeyboardInterrupt:
                                                                                                                                                                                                                                                                                                                                                                                                           logging.info("Bot shut down manually.")


                                                                                                                                                                                                                                                                                                                                                                                                           async def run_bot():
                                                                                                                                                                                                                                                                                                                                                                                                               """Main loop that keeps bot alive and reconnects after errors or restarts."""
                                                                                                                                                                                                                                                                                                                                                                                                                   retries = 0
                                                                                                                                                                                                                                                                                                                                                                                                                       max_retries = 10  # adjust as needed

                                                                                                                                                                                                                                                                                                                                                                                                                           while True:
                                                                                                                                                                                                                                                                                                                                                                                                                                   try:
                                                                                                                                                                                                                                                                                                                                                                                                                                               logging.info("Starting Discord bot...")
                                                                                                                                                                                                                                                                                                                                                                                                                                                           await client.start(os.environ["TOKEN"])

                                                                                                                                                                                                                                                                                                                                                                                                                                                                               except (discord.ConnectionClosed, discord.HTTPException, OSError) as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           # Handle disconnects, network errors, or Replit restarts
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       retries += 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   wait_time = min(2 ** retries, 60)  # exponential backoff
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               logging.warning(f"Bot disconnected ({type(e).__name__}: {e}). Retrying in {wait_time}s...")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           await asyncio.sleep(wait_time)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       if retries >= max_retries:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       logging.error("Max retries reached. Restarting fresh process...")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       os.execv(sys.executable, ['python'] + sys.argv)  # full restart of script

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               except asyncio.CancelledError:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           logging.warning("Bot task cancelled. Restarting...")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       await asyncio.sleep(5)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           # Catch-all to prevent crashes
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       logging.exception(f"Unexpected error: {e}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   await asyncio.sleep(15)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       # Reset retry counter if bot shuts down cleanly
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   retries = 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                      
Initial commit: add Szkieletor

