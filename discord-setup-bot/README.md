# Discord Server Setup Bot

Automatically configures your Aegis Sentinel Discord server with channels, roles, and welcome messages.

## What It Creates

### Roles
| Role | Color | Purpose |
|------|-------|---------|
| Team | Green | Admins |
| Moderator | Blue | Moderators |
| Developer | Purple | Developers |
| OG | Gold | Early supporters |
| Presale | Orange | Token holders |
| Verified | Gray | Basic members |

### Categories & Channels
- **📌 INFO**: #welcome, #rules, #announcements, #links (read-only)
- **💬 COMMUNITY**: #general, #introductions, #memes, #off-topic
- **💰 TOKEN**: #presale, #sentinel-chat, #token-faq
- **🛠️ SUPPORT**: #help, #bug-reports, #feature-requests
- **👨‍💻 DEVELOPERS**: #dev-chat, #api-discussion, #github-feed
- **🔒 MODERATION**: #mod-chat, #mod-logs, #audit-logs (hidden)

### Auto-Sends Messages
- Welcome message with links
- Server rules
- Presale info
- Token FAQ
- And more...

---

## Setup Instructions

### Step 1: Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application**
3. Name it `Aegis Setup Bot` → Create
4. Go to **Bot** tab (left sidebar)
5. Scroll down to **Privileged Gateway Intents**
6. Enable:
   - ✅ SERVER MEMBERS INTENT
   - ✅ MESSAGE CONTENT INTENT
7. Click **Save Changes**

### Step 2: Get Bot Token

1. On the **Bot** tab, find **Token** section
2. Click **Reset Token** → Yes
3. Click **Copy** — save this somewhere safe!

> ⚠️ Never share this token! Anyone with it controls your bot.

### Step 3: Invite Bot to Server

1. Go to **OAuth2** → **URL Generator** (left sidebar)
2. Under **Scopes**, check:
   - ✅ `bot`
   - ✅ `applications.commands`
3. Under **Bot Permissions**, check:
   - ✅ `Administrator`
4. Copy the **Generated URL** at the bottom
5. Open URL in browser
6. Select your server → Authorize

### Step 4: Get Server ID

1. Open Discord
2. Go to **User Settings** → **Advanced**
3. Enable **Developer Mode**
4. Right-click your server icon
5. Click **Copy Server ID**

### Step 5: Run the Script

```powershell
# Navigate to the folder
cd "Github public\discord-setup-bot"

# Install requirements
pip install -r requirements.txt

# Run setup
python setup_discord.py
```

When prompted:
1. Paste your **bot token**
2. Paste your **server ID**

The script will create everything automatically!

---

## After Setup

1. **Remove the setup bot** from your server (optional but recommended)
2. **Add Carl-bot** for moderation: https://carl.gg
3. **Assign roles** to your team members
4. **Review permissions** on each channel
5. **Customize messages** if needed

---

## Troubleshooting

### "Invalid token"
- Make sure you copied the full token
- Try resetting the token and copying again

### "Could not find guild"
- Make sure Developer Mode is enabled
- Right-click server → Copy Server ID (not channel ID)
- Make sure the bot is actually in the server

### "Missing permissions"
- Make sure bot has Administrator permission
- Try kicking the bot and re-inviting with [correct permissions](#step-3-invite-bot-to-server)

### "Rate limited"
- The script has built-in delays, but Discord may still rate limit
- Wait a few minutes and run again — it will skip existing items

---

## Customization

Edit `setup_discord.py` to customize:
- `ROLES` — Change role names/colors
- `CATEGORIES` — Add/remove channels
- `WELCOME_MESSAGE`, etc. — Edit message content

---

## Security Note

Your bot token stays on your local machine. This script:
- ✅ Runs locally
- ✅ Never sends data anywhere except Discord
- ✅ Can be deleted after use

Delete the bot from Developer Portal after setup if you want.
