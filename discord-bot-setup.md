# Discord Auto-Moderation Setup Guide

Step-by-step setup using **free** tools: Carl-bot + Discord's built-in AutoMod.

> ⚠️ **Note:** MEE6 is NOT recommended — most features require paid subscription ($12/month).

---

## Option A: Carl-bot (Recommended - Free)

### 1. Add Carl-bot
1. Go to https://carl.gg
2. Click **Invite**
3. Select your server
4. Authorize

### 2. Welcome Messages

**Dashboard → Welcome & Goodbye**

**Welcome message:**
```
embed
title: Welcome to Aegis Sentinel! 🛡️
description: Hey {mention}, thanks for joining!
color: #00FF88
field: Quick Start::• Read #rules
• Introduce yourself in #introductions
• Chat in #general
field: Official Links::• [Website](https://aegissentinel.online)
• [Portal](https://portal.aegissentinel.online)
• [Docs](https://docs.aegissentinel.online)
footer: Team will NEVER DM you first!
```

**DM on join:**
```
Welcome to Aegis Sentinel, {user}! 🛡️

We're building AI-powered security for Web3. Glad to have you!

Get started:
→ #welcome - Official links
→ #rules - Community guidelines
→ #presale - Token info

⚠️ SCAM ALERT: Admins will NEVER DM you asking for funds or seed phrases!
```

### 3. Auto-Roles (Reaction Roles)

**Dashboard → Reaction Roles**

Create in #welcome:

```
React to get notified about:

🔔 @Announcements - Major updates
💰 @Presale - Token news  
🛠️ @Dev Updates - Technical updates
🌐 @Community - Events & AMAs
```

Mode: **Unique** (one role per user)

### 4. Auto-Moderation

**Dashboard → Automod**

**Banned Words:**
```
Add these filters:

- scam|phishing|hack
- validate wallet
- connect wallet to claim
- DM for support
- moderator/admin will DM
- free crypto|airdrop claim
- nitro free
```
Action: Delete + Warn

**Anti-Spam:**
- Max messages: 5 in 5 seconds → Mute 10 min
- Max mentions: 4 → Delete + Mute
- Max lines: 20 → Delete
- Max attachments: 3 per message → Delete

**Link Filter:**
- Block all links EXCEPT whitelist
- Whitelist:
```
aegissentinel.online
docs.aegissentinel.online
portal.aegissentinel.online
github.com
x.com
twitter.com
t.me
discord.gg (only official)
arbitrum.io
uniswap.org
etherscan.io
arbiscan.io
```

**Anti-Raid:**
- Enable raid protection
- Threshold: 10 joins in 10 seconds → Lock server + alert mods

### 5. Logging

**Dashboard → Logging**

Create channels:
- #mod-logs (visible to mods)
- #audit-logs (admins only)

Log these:
- Message edits/deletes
- Member joins/leaves
- Role changes
- Channel changes
- Bans/kicks
- Voice activity

### 6. Useful Commands

**Set up these commands:**

| Command | Response |
|---------|----------|
| `!website` | https://aegissentinel.online |
| `!portal` | https://portal.aegissentinel.online |
| `!docs` | https://docs.aegissentinel.online |
| `!presale` | Check #presale for token info! |
| `!tokenomics` | https://docs.aegissentinel.online/platform/investors |
| `!contract` | Contract address will be announced in #announcements after launch |
| `!scam` | ⚠️ Team will NEVER DM you first. Never share your seed phrase! |

---

## Discord's Built-in AutoMod

Discord now has native AutoMod (free, no bot needed):

**Server Settings → Safety Setup → AutoMod**

### Enable These Rules:

**1. Block Harmful Links**
- Toggle ON
- Action: Block message + Alert mods

**2. Block Spam Content**
- Toggle ON
- Action: Block + Timeout 60s

**3. Block Mention Spam**
- Max mentions: 4
- Action: Block + Timeout 5min

**4. Custom Keywords (Create Rule)**

Name: `Scam Filter`
Keywords:
```
validate*wallet*
connect*wallet*claim*
DM*support*
admin*will*message*
free*crypto*
claim*airdrop*
metamask*verify*
```
Action: Block + Alert in #mod-logs + Timeout 1hr

---

## Recommended Slowmode Settings

| Channel | Slowmode |
|---------|----------|
| #general | 5 seconds |
| #sentinel-chat | 10 seconds |
| #help | 15 seconds |
| #introductions | 30 seconds |
| #memes | 30 seconds |

Set with: Right-click channel → Edit → Slowmode

---

## Mod Commands Cheat Sheet

### Carl-bot
```
!warn @user reason
!mute @user 1h reason
!unmute @user
!kick @user reason
!ban @user reason
!purge 10
!lockdown (lock channel)
!slowmode 30s
```

---

## Quick Setup Checklist

- [ ] Add Carl-bot (free) or Dyno
- [ ] Configure welcome message (channel + DM)
- [ ] Set up auto-role for new members
- [ ] Enable anti-spam filters
- [ ] Whitelist official links
- [ ] Block scam keywords
- [ ] Create #mod-logs channel
- [ ] Enable message logging
- [ ] Set slowmode on busy channels
- [ ] Test with alt account

---

## Alternative: Dyno (Also Free)

If Carl-bot doesn't suit you:

1. Go to https://dyno.gg
2. Add to server
3. Free features include:
   - Welcome messages
   - Auto-roles
   - Basic moderation
   - Logging
   - Custom commands

---

Need help? Bot dashboard tutorials:
- Carl-bot: https://carl.gg/dashboard
- Dyno: https://dyno.gg/manage
