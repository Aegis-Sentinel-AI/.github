"""
Aegis Sentinel Discord Server Setup Script
==========================================
This script automatically configures your Discord server with:
- Categories and channels
- Roles with permissions
- Welcome messages

INSTRUCTIONS:
1. Go to https://discord.com/developers/applications
2. Click "New Application" → Name it "Aegis Setup Bot"
3. Go to "Bot" tab → Enable these Privileged Gateway Intents:
   - SERVER MEMBERS INTENT
   - MESSAGE CONTENT INTENT
4. Click "Reset Token" → Copy the token
5. Go to OAuth2 → URL Generator:
   - Scopes: bot, applications.commands
   - Bot Permissions: Administrator
6. Copy the URL, open in browser, add bot to your server
7. Run this script and paste your token when prompted

The bot will configure everything, then you can remove it from your server.
"""

import asyncio
import discord
from discord import PermissionOverwrite

# Server configuration
ROLES = [
    {"name": "Team", "color": 0x00FF88, "hoist": True, "position": 6},
    {"name": "Moderator", "color": 0x5865F2, "hoist": True, "position": 5},
    {"name": "Developer", "color": 0x9B59B6, "hoist": True, "position": 4},
    {"name": "OG", "color": 0xF1C40F, "hoist": True, "position": 3},
    {"name": "Presale", "color": 0xE67E22, "hoist": False, "position": 2},
    {"name": "Verified", "color": 0x95A5A6, "hoist": False, "position": 1},
]

CATEGORIES = [
    {
        "name": "📌 INFO",
        "channels": [
            {"name": "welcome", "type": "text", "readonly": True},
            {"name": "rules", "type": "text", "readonly": True},
            {"name": "announcements", "type": "text", "readonly": True},
            {"name": "links", "type": "text", "readonly": True},
        ]
    },
    {
        "name": "💬 COMMUNITY",
        "channels": [
            {"name": "general", "type": "text", "slowmode": 5},
            {"name": "introductions", "type": "text", "slowmode": 30},
            {"name": "memes", "type": "text", "slowmode": 30},
            {"name": "off-topic", "type": "text", "slowmode": 10},
        ]
    },
    {
        "name": "💰 TOKEN",
        "channels": [
            {"name": "presale", "type": "text", "readonly": True},
            {"name": "aegis-chat", "type": "text", "slowmode": 10},
            {"name": "token-faq", "type": "text", "slowmode": 15},
        ]
    },
    {
        "name": "🛠️ SUPPORT",
        "channels": [
            {"name": "help", "type": "text", "slowmode": 15},
            {"name": "bug-reports", "type": "text", "slowmode": 60},
            {"name": "feature-requests", "type": "text", "slowmode": 60},
        ]
    },
    {
        "name": "👨‍💻 DEVELOPERS",
        "channels": [
            {"name": "dev-chat", "type": "text", "dev_only": True},
            {"name": "api-discussion", "type": "text", "dev_only": True},
            {"name": "github-feed", "type": "text", "readonly": True},
        ]
    },
    {
        "name": "🔒 MODERATION",
        "channels": [
            {"name": "mod-chat", "type": "text", "mod_only": True},
            {"name": "mod-logs", "type": "text", "mod_only": True},
            {"name": "audit-logs", "type": "text", "admin_only": True},
        ]
    },
]

# Welcome message content
WELCOME_MESSAGE = """═══════════════════════════════════════════════════
🛡️ WELCOME TO AEGIS SENTINEL
═══════════════════════════════════════════════════

AI-Powered Cybersecurity for the Decentralized Era

We're building the trust layer for Web3 — autonomous AI agents that detect threats in real-time, generate Zero-Knowledge proofs, and anchor verifiable security verdicts on blockchain.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 **OFFICIAL LINKS**

🌐 Website: https://aegissentinel.online
🖥️ Portal: https://portal.aegissentinel.online
📚 Docs: https://docs.aegissentinel.online
🐦 Twitter/X: https://x.com/AegisSentinelAi
� GitHub: https://github.com/Aegis-Sentinel-AI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 **QUICK START**

1️⃣ Verify in #✅-verify to unlock channels
2️⃣ Read the rules in #rules
3️⃣ Introduce yourself in #introductions
4️⃣ Join the conversation in #general
5️⃣ Got questions? Head to #help

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 **$AEGIS TOKEN**

• Early Bird Presale: LIVE NOW
• Early Bird Price: $0.015 (62.5% off listing)
• Network: Arbitrum (L2)

🚀 See #🚀-early-bird-presale after verifying

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ **SCAM WARNING**

• Team will NEVER DM you first
• We will NEVER ask for your seed phrase
• Only trust links posted in this channel
• Report suspicious DMs to moderators

Stay safe! 🛡️"""

RULES_MESSAGE = """═══════════════════════════════════════════════════
📜 COMMUNITY RULES
═══════════════════════════════════════════════════

Please follow these rules to keep our community safe and welcoming.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**1️⃣ BE RESPECTFUL**
• Treat everyone with respect
• No harassment, hate speech, or discrimination
• No personal attacks or toxic behavior

**2️⃣ NO SPAM OR SELF-PROMOTION**
• No unsolicited advertising
• No repetitive messages
• No shilling other projects

**3️⃣ NO SCAMS OR PHISHING**
• Never share wallet seeds or private keys
• Report suspicious links immediately
• Team will NEVER DM you first

**4️⃣ KEEP IT ORGANIZED**
• Use the correct channel for your topic
• Price discussion → #aegis-chat
• Support questions → #help
• Bug reports → #bug-reports

**5️⃣ ENGLISH IN MAIN CHANNELS**
• Main channels are English only
• Use international channels for other languages

**6️⃣ NO FOMO/FUD**
• No baseless price predictions
• No spreading misinformation
• Constructive criticism is welcome

**7️⃣ RESPECT PRIVACY**
• Don't share others' personal info
• Don't screenshot private conversations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚖️ **ENFORCEMENT**

• 1st offense: Warning
• 2nd offense: 24-hour mute
• 3rd offense: Permanent ban
• Severe violations: Immediate ban

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Questions? Ask a @Moderator

By participating, you agree to follow these rules. 🤝"""

ANNOUNCEMENT_MESSAGE = """═══════════════════════════════════════════════════
🛡️ AEGIS SENTINEL IS LIVE!
═══════════════════════════════════════════════════

Welcome to the official Aegis Sentinel Discord community!

**What is Aegis Sentinel?**

We're building AI-powered cybersecurity for Web3:
• 🤖 Autonomous AI threat detection (97.3% accuracy)
• 🔐 Zero-Knowledge proofs for privacy
• ⛓️ On-chain verification on Arbitrum L2
• ⚡ 15-second scans (vs 2-month audits)

**What's Next?**

� NOW: $AEGIS Early Bird Presale LIVE ($0.015)
📍 Q3 2026: Public presale & Uniswap listing
📍 Q3 2026: Enterprise partnerships
📍 Q4 2026: CEX listings

**Get Started**

🌐 Try the Portal: https://portal.aegissentinel.online
📚 Read the Docs: https://docs.aegissentinel.online
🚀 Early Bird: https://aegissentinel.online/early-bird.html

Turn on notifications 🔔 to stay updated!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

LINKS_MESSAGE = """═══════════════════════════════════════════════════
🔗 OFFICIAL LINKS
═══════════════════════════════════════════════════

**Main**
🌐 Website: https://aegissentinel.online
🖥️ Enterprise Portal: https://portal.aegissentinel.online
📚 Documentation: https://docs.aegissentinel.online

**Social**
🐦 Twitter/X: https://x.com/AegisSentinelAi
� Discord: You're here!

**Development**
💻 GitHub: https://github.com/Aegis-Sentinel-AI
📖 API Docs: https://docs.aegissentinel.online/api-reference

**Token (✅ Early Bird LIVE)**
🚀 Early Bird: https://aegissentinel.online/early-bird.html
💱 DEX: Uniswap on Arbitrum (after listing)

**Contact**
📧 General: contact@aegissentinel.online
🏢 Enterprise: enterprise@aegissentinel.online
💼 Partnerships: partnerships@aegissentinel.online

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ Only trust links from this channel!
Report fake links to @Moderator"""

PRESALE_MESSAGE = """═══════════════════════════════════════════════════
🎫 $AEGIS PRESALE INFO
═══════════════════════════════════════════════════

**Token Details**
• Name: Aegis Token
• Symbol: $AEGIS
• Network: Arbitrum (L2)
• Total Supply: 1,000,000,000 (1B)

**Presale Details**
• Platform: Direct contract on Arbitrum One
• Early Bird Price: $0.015 per token (62.5% off)
• Presale Price: $0.022 per token (45% off)
• Final Round Price: $0.032 per token (20% off)
• Listing Price: $0.04 (Uniswap on Arbitrum)
• Total Presale Tokens: 150M (15% of supply)

**Timing**
• Early Bird: LIVE NOW
• Public Sale: July 2026

**Vesting**
• 100% cliff — unlocks January 1, 2027

**How to Participate**
1. Add Arbitrum One network to wallet
2. Fund with ETH on Arbitrum
3. Send ETH to: 0x8F60e81Ca34510193D568A9a4CB4CbeF95e3F6a1
4. Tokens allocated automatically, vest Jan 1 2027

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📢 Turn on notifications for #announcements
We'll announce the exact date there first!

Questions? Ask in #token-faq"""

TOKEN_FAQ_MESSAGE = """═══════════════════════════════════════════════════
❓ TOKEN FAQ
═══════════════════════════════════════════════════

**Q: When is the presale?**
A: Early Bird is LIVE NOW at $0.015/token. Public presale at $0.022 starts July 2026.

**Q: What's the presale price?**
A: Three rounds — Early Bird $0.015 (62.5% off), Presale $0.022 (45% off), Final Round $0.032 (20% off). Listing price: $0.04.

**Q: What chain is $AEGIS on?**
A: Arbitrum (Ethereum L2) — low fees, fast transactions.

**Q: How do I participate in presale?**
A: Send ETH on Arbitrum to the presale contract: 0x8F60e81Ca34510193D568A9a4CB4CbeF95e3F6a1. See #🚀-early-bird-presale for the full guide.

**Q: Is there a vesting period?**
A: Yes. 100% cliff vesting — tokens unlock January 1, 2027.

**Q: What can I do with $AEGIS?**
A: 
• Pay for security scans (20% discount vs USD)
• Stake to earn rewards (8-12% APY)
• Vote on governance proposals
• Access premium features

**Q: Is the token deflationary?**
A: Yes! 5 burn mechanisms reduce supply over time.

**Q: Where will it be listed?**
A: Uniswap (Arbitrum) at launch. CEX listings planned for Q4 2026.

**Q: Is this a memecoin?**
A: No. $AEGIS has real utility — it powers the security platform.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

More questions? Ask below! ⬇️"""

INTROS_MESSAGE = """═══════════════════════════════════════════════════
👋 INTRODUCE YOURSELF!
═══════════════════════════════════════════════════

New here? Tell us about yourself!

**Template (optional):**

🏷️ Name/Alias:
🌍 Location:
🔧 Background: (dev, trader, security, etc.)
🤔 How did you find Aegis Sentinel?
💬 What interests you most about the project?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Welcome to the community! 🛡️"""


class SetupBot(discord.Client):
    def __init__(self, guild_id: int):
        intents = discord.Intents.default()
        intents.guilds = True
        intents.members = True
        super().__init__(intents=intents)
        self.target_guild_id = guild_id
        self.created_roles = {}
        self.created_channels = {}

    async def on_ready(self):
        print(f"\n✅ Logged in as {self.user}")
        
        guild = self.get_guild(self.target_guild_id)
        if not guild:
            print(f"❌ Could not find guild with ID {self.target_guild_id}")
            print("Available guilds:")
            for g in self.guilds:
                print(f"  - {g.name} (ID: {g.id})")
            await self.close()
            return

        print(f"📍 Configuring server: {guild.name}")
        
        try:
            await self.setup_roles(guild)
            await self.setup_channels(guild)
            await self.send_messages(guild)
            
            print("\n" + "="*50)
            print("✅ SETUP COMPLETE!")
            print("="*50)
            print("\nNext steps:")
            print("1. Remove this bot from your server (optional)")
            print("2. Add Carl-bot for auto-moderation: https://carl.gg")
            print("3. Review channel permissions")
            print("4. Invite your team and assign roles")
            
        except Exception as e:
            print(f"\n❌ Error during setup: {e}")
            import traceback
            traceback.print_exc()
        
        await self.close()

    async def setup_roles(self, guild: discord.Guild):
        print("\n📋 Creating roles...")
        
        for role_config in ROLES:
            existing = discord.utils.get(guild.roles, name=role_config["name"])
            if existing:
                print(f"  ⏭️  Role '{role_config['name']}' already exists")
                self.created_roles[role_config["name"]] = existing
            else:
                role = await guild.create_role(
                    name=role_config["name"],
                    color=discord.Color(role_config["color"]),
                    hoist=role_config["hoist"],
                    mentionable=True
                )
                self.created_roles[role_config["name"]] = role
                print(f"  ✅ Created role: {role_config['name']}")
                await asyncio.sleep(0.5)  # Rate limit prevention

    async def setup_channels(self, guild: discord.Guild):
        print("\n📁 Creating categories and channels...")
        
        # Get roles for permissions
        everyone = guild.default_role
        team_role = self.created_roles.get("Team")
        mod_role = self.created_roles.get("Moderator")
        dev_role = self.created_roles.get("Developer")
        
        for cat_config in CATEGORIES:
            # Check if category exists
            existing_cat = discord.utils.get(guild.categories, name=cat_config["name"])
            if existing_cat:
                category = existing_cat
                print(f"  ⏭️  Category '{cat_config['name']}' already exists")
            else:
                category = await guild.create_category(cat_config["name"])
                print(f"  ✅ Created category: {cat_config['name']}")
                await asyncio.sleep(0.3)
            
            for ch_config in cat_config["channels"]:
                channel_name = ch_config["name"]
                existing_ch = discord.utils.get(guild.text_channels, name=channel_name)
                
                if existing_ch:
                    print(f"    ⏭️  Channel #{channel_name} already exists")
                    self.created_channels[channel_name] = existing_ch
                    continue
                
                # Set up permission overwrites
                overwrites = {}
                
                if ch_config.get("readonly"):
                    overwrites[everyone] = PermissionOverwrite(
                        send_messages=False,
                        add_reactions=True
                    )
                    if team_role:
                        overwrites[team_role] = PermissionOverwrite(
                            send_messages=True,
                            manage_messages=True
                        )
                    if mod_role:
                        overwrites[mod_role] = PermissionOverwrite(
                            send_messages=True,
                            manage_messages=True
                        )
                
                if ch_config.get("mod_only"):
                    overwrites[everyone] = PermissionOverwrite(
                        view_channel=False
                    )
                    if team_role:
                        overwrites[team_role] = PermissionOverwrite(
                            view_channel=True,
                            send_messages=True,
                            manage_messages=True
                        )
                    if mod_role:
                        overwrites[mod_role] = PermissionOverwrite(
                            view_channel=True,
                            send_messages=True,
                            manage_messages=True
                        )
                
                if ch_config.get("admin_only"):
                    overwrites[everyone] = PermissionOverwrite(
                        view_channel=False
                    )
                    if team_role:
                        overwrites[team_role] = PermissionOverwrite(
                            view_channel=True,
                            send_messages=True,
                            manage_messages=True
                        )
                
                if ch_config.get("dev_only"):
                    overwrites[everyone] = PermissionOverwrite(
                        view_channel=False
                    )
                    if team_role:
                        overwrites[team_role] = PermissionOverwrite(
                            view_channel=True,
                            send_messages=True
                        )
                    if dev_role:
                        overwrites[dev_role] = PermissionOverwrite(
                            view_channel=True,
                            send_messages=True
                        )
                
                channel = await guild.create_text_channel(
                    name=channel_name,
                    category=category,
                    overwrites=overwrites or {},
                    slowmode_delay=ch_config.get("slowmode", 0)
                )
                self.created_channels[channel_name] = channel
                print(f"    ✅ Created channel: #{channel_name}")
                await asyncio.sleep(0.3)

    async def send_messages(self, guild: discord.Guild):
        print("\n📝 Sending welcome messages...")
        
        messages_to_send = [
            ("welcome", WELCOME_MESSAGE),
            ("rules", RULES_MESSAGE),
            ("announcements", ANNOUNCEMENT_MESSAGE),
            ("links", LINKS_MESSAGE),
            ("presale", PRESALE_MESSAGE),
            ("token-faq", TOKEN_FAQ_MESSAGE),
            ("introductions", INTROS_MESSAGE),
        ]
        
        for channel_name, message_content in messages_to_send:
            channel = self.created_channels.get(channel_name)
            if not channel:
                channel = discord.utils.get(guild.text_channels, name=channel_name)
            
            if channel:
                try:
                    # Check if channel already has messages
                    async for msg in channel.history(limit=1):
                        print(f"  ⏭️  #{channel_name} already has messages, skipping")
                        break
                    else:
                        await channel.send(message_content)
                        print(f"  ✅ Sent message to #{channel_name}")
                except discord.Forbidden:
                    print(f"  ❌ No permission to send to #{channel_name}")
                except Exception as e:
                    print(f"  ❌ Error sending to #{channel_name}: {e}")
                await asyncio.sleep(0.5)
            else:
                print(f"  ⚠️  Channel #{channel_name} not found")


def main():
    print("="*50)
    print("🛡️ AEGIS SENTINEL DISCORD SETUP")
    print("="*50)
    
    print("\nBefore running this script, make sure you have:")
    print("1. Created a bot at https://discord.com/developers/applications")
    print("2. Enabled SERVER MEMBERS INTENT and MESSAGE CONTENT INTENT")
    print("3. Added the bot to your server with Administrator permission")
    print()
    
    token = input("🔑 Paste your bot token: ").strip()
    if not token:
        print("❌ No token provided. Exiting.")
        return
    
    guild_id_str = input("🏠 Paste your server ID (right-click server → Copy Server ID): ").strip()
    try:
        guild_id = int(guild_id_str)
    except ValueError:
        print("❌ Invalid server ID. Must be a number.")
        return
    
    print("\n🚀 Starting setup...")
    
    bot = SetupBot(guild_id)
    try:
        bot.run(token)
    except discord.LoginFailure:
        print("❌ Invalid token. Please check and try again.")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
