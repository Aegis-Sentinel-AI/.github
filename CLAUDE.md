# CLAUDE.md — Aegis Sentinel Project Rules

> This file is read by Claude at the start of every session.
> Every time Claude makes a mistake, we add a rule so it NEVER happens again.

---

## Project Overview

**Aegis Sentinel** is an AI-powered cybersecurity protocol for Web3/DeFi.
- **Owner**: @Srodland (Sean Rødland)
- **Project account**: @AegisSentinelAi
- **Domain**: aegissentinel.online
- **Presale**: Q2 2026 (target June 1, 2026)
- **Token**: $AEGIS (1B fixed supply)

---

## Repository Map

```
Github public/
├── aegis-landing-next/     — Next.js 16 landing page & enterprise dashboard (Vercel)
├── aegis-ai-engine/        — Python AI threat detection engine (35+ threat types)
├── aegis-sentinel-contracts/ — Solidity 0.8.24 smart contracts (Foundry, Sepolia)
├── aegis-discord-bot/      — Discord bot (TypeScript, discord.js v14)
├── aegis-x-bot/            — @AegisSentinelAi X bot (TypeScript, twitter-api-v2)
├── aegis-x-personal/       — @Srodland X bot (TypeScript, twitter-api-v2)
├── aegis-docs/             — Technical documentation & lightpaper
├── aegis-docs-site/        — Docusaurus documentation site
├── aegis-portal/           — Enterprise integration portal
├── aegis-zkp-prover/       — Zero-Knowledge Proof circuits
└── .github/                — GitHub Actions CI/CD
```

---

## Tech Stack Rules

### Next.js (aegis-landing-next)
- **Version**: Next.js 16.1.5 with Turbopack
- **Styling**: Tailwind CSS — NEVER use inline styles or CSS modules
- **Data**: Prisma 7.4.0 + Neon PostgreSQL 17
- **API routes**: Use App Router (`app/api/`) — NEVER use Pages Router
- **Imports**: Use `@/` path alias for imports from `src/`
- **Components**: Place in `src/components/` — use PascalCase filenames
- **Server vs Client**: Default to server components. Only add `'use client'` when needed (hooks, interactivity)

### Python (aegis-ai-engine)
- **Version**: Python 3.11+
- **Framework**: Custom engine, no Django/Flask
- **Structure**: `src/sentinel_engine/` — use snake_case everywhere
- **Types**: Always use type hints on function signatures
- **Config**: Use pydantic for settings/config

### Solidity (aegis-sentinel-contracts)
- **Version**: Solidity 0.8.24
- **Framework**: Foundry/Forge — NEVER use Hardhat
- **Tests**: Use Forge test (`forge test`) — 120+ tests must pass
- **Deploy**: Forge scripts in `script/`
- **Network**: Sepolia testnet (will migrate to mainnet)
- **Dependencies**: OpenZeppelin Contracts via Foundry git submodules

### TypeScript Bots (discord, x-bot, x-personal)
- **Module**: ESM (`"type": "module"` in package.json)
- **Module system**: Node16 module resolution — use `.js` extension in imports
- **Runtime**: tsx for development, tsc for builds
- **Config**: dotenv for environment variables — NEVER commit .env files
- **Error handling**: Always catch with `err?.data || err?.message || err` pattern

---

## Coding Conventions

### General
- **No var** — always `const`, use `let` only when reassignment needed
- **Template literals** over string concatenation
- **Early returns** over deeply nested if/else
- **Descriptive names** — no single-letter variables except loop counters
- **Console logging** — use prefixed format: `[module] message` (e.g., `[sched]`, `[engage]`, `[x]`)

### TypeScript
- **Strict mode** always enabled
- **Export types** separately: `export type { MyType }`
- **Async/await** over .then() chains
- **Interfaces** over type aliases for object shapes (unless union types needed)

### API Patterns
- **3-tier fallback**: AI Engine → Prisma/PostgreSQL → Mock data
- **Base URL**: `https://aegissentinel.online` — configurable via env
- **Auth**: Middleware-based, JWT tokens
- **Error responses**: `{ error: string, status: number }`

---

## Critical Rules (Learned from Mistakes)

### Auth / Credentials
- X API uses **OAuth 1.0a** for posting (appKey, appSecret, accessToken, accessSecret)
- X API uses **Bearer token** for read-only (search, timelines)
- Regenerating Consumer Keys **invalidates** existing Access Tokens — must regenerate both
- X Free tier is gone — now pay-per-use ($25 minimum, ~$0.008 per tweet)
- Access Tokens are tied to the **developer portal owner's account**, not the app name
- NEVER log or display full API keys — show only first 8-10 chars

### X Bot Specifics
- twitter-api-v2 search results: iterate with `results.data.data` NOT `results.data`
- Tweet limit: 280 chars — always check length before posting
- Rate limits: Max 2-3 engagements per cycle, 15-60sec delays between actions
- Schedule offsets: Project bot and personal bot times MUST NOT overlap
- Project bot times: 08:00, 13:00, 18:00, 22:00 UTC
- Personal bot times: 09:30, 14:30, 19:30, 23:30 UTC

### Discord Bot
- Use `async` in ready handler for initialization: `client.once(Events.ClientReady, async (c) => { ... })`
- Signal system uses channel names with emoji prefixes (e.g., `#🚨-threat-alerts`)
- `startAlerts()` does NOT take a `client` parameter — uses signal router module directly
- Deploy commands with `npm run deploy-commands` after adding new slash commands

### Next.js / Vercel
- Environment variables on Vercel must be set in project settings, not just .env
- Prisma needs `prisma generate` after schema changes
- Database URL format: `postgresql://...@ep-xxx.us-east-2.aws.neon.tech/neondb?sslmode=require`
- NEVER expose database URLs or secrets in client-side code

### SEO (aegis-landing-next)
- `metadataBase` is set in root layout — all OG/image URLs resolve relative to it
- `'use client'` pages CANNOT export `metadata` — create a server-component `layout.tsx` wrapper for them
- Dashboard layout: server layout.tsx wraps DashboardShell.tsx (client component) — do NOT merge back into one file
- All presale/public pages get `index: true`; all `/dashboard/*` and `/login` get `index: false, follow: false`
- JSON-LD structured data is injected via `<script type="application/ld+json">` in root layout body
- Sitemap at `/sitemap.xml` (from `src/app/sitemap.ts`) — update when adding new public routes
- Robots at `/robots.txt` (from `src/app/robots.ts`) — disallows `/dashboard/`, `/login`, `/api/`
- Security headers (HSTS, X-Frame-Options, X-Content-Type-Options, etc.) are in `next.config.js` `headers()`
- `poweredByHeader: false` in next.config.js — never re-enable
- Web manifest at `/manifest.json` — linked in root layout metadata

### Mobile Responsiveness (aegis-landing-next)
- Body has `overflow-x-hidden` — NEVER remove (prevents horizontal scroll on mobile)
- Card padding must be responsive: `p-5 sm:p-6 md:p-8` — never use fixed `p-8`
- Section headings scale: `text-2xl sm:text-3xl lg:text-4xl` — always include `sm:` step
- Hero/page headings scale: `text-4xl sm:text-5xl md:text-6xl lg:text-7xl` — smooth stepping
- Dashboard sub-page headers: `flex flex-col sm:flex-row sm:items-center justify-between gap-4` — never use bare `flex items-center justify-between` (overflows on mobile)
- Tables MUST have `overflow-x-auto` wrapper div + `min-w-[480px]` on the inner grid
- Dashboard stat grids: `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4` — never start at 2-col
- Charts/maps need responsive heights: `h-[280px] sm:h-[350px] lg:h-[420px]`
- Side-by-side chart + legend: use `flex flex-col sm:flex-row` to stack on mobile
- Contract addresses / long strings: use `truncate` + `min-w-0` for proper text truncation
- HTML has `-webkit-text-size-adjust: 100%` for consistent iOS text rendering
- Navbar already has mobile hamburger menu (xl: breakpoint) — do not modify
- Architecture & Roadmap components have separate mobile/desktop layouts (lg:hidden / hidden lg:block) — do not merge

### Solidity / Foundry
- Run `forge test` before any deployment — all 120+ tests must pass
- Use `forge script` for deployments — never manual contract creation
- Contract addresses are on Sepolia — will change on mainnet migration

### File System
- Windows paths use backslashes — use quotes around paths with spaces
- PowerShell: use `;` to chain commands, NOT `&&`
- Node REPL can steal the terminal — use `.exit` or Ctrl+C to escape
- Background terminals may not show output — verify with foreground run first

---

## Project Status (Last Updated: Feb 23, 2026)

### Completed
- ✅ Auth middleware & backend API
- ✅ Neon PostgreSQL database (seeded)
- ✅ Presale page
- ✅ AI engine integration (3-tier fallback)
- ✅ Smart contracts (5 contracts, 120 tests, Sepolia deployed)
- ✅ Discord bot (9 commands, signal routing, 5 monitors)
- ✅ Domain redirect (aegissentinel.online)
- ✅ X bot — @AegisSentinelAi (content, engagement, threads, alerts)
- ✅ X bot — @Srodland (build-in-public, CT engagement, founder brand)
- ✅ CI/CD (GitHub Actions for all repos)
- ✅ SEO & meta tags (OG, Twitter cards, sitemap, robots, JSON-LD, security headers)
- ✅ Mobile responsiveness audit (15+ files, all 12 pages + 18 components audited)

### Remaining
- ⬜ Bot hosting (deploy to always-on server)
- ⬜ Discord `/signal setup` (run in server)
- ⬜ Bearer token for @Srodland app (engagement/search)

---

## CI/CD Workflows

| Repo | Workflow | Jobs | Status |
|------|----------|------|--------|
| aegis-sentinel-contracts | `.github/workflows/ci.yml` | Build, Test, Coverage, Lint, Slither | ✅ Existed |
| aegis-ai-engine | `.github/workflows/ci.yml` | Lint, Type Check, Test (3.10-3.12), Build, Docker | ✅ Existed |
| aegis-landing-next | `.github/workflows/ci.yml` | Lint, Type Check, Build, Prisma Validate | ✅ Created |
| aegis-portal | `.github/workflows/ci.yml` | Lint, Type Check, Build | ✅ Created |
| aegis-discord-bot | `.github/workflows/ci.yml` | Build, Type Check | ✅ Created |
| aegis-docs-site | `.github/workflows/ci.yml` | Build, Type Check | ✅ Created |
| aegis-x-bot | No own repo | N/A — no `.git` directory |
| aegis-x-personal | No own repo | N/A — no `.git` directory |

### CI Rules
- All workflows trigger on push to `main`/`develop` and PRs to `main`
- Node.js workflows use `npm ci` (not `npm install`) for reproducible builds
- Next.js builds that use Prisma need `prisma generate` before build step
- aegis-landing-next build needs `DATABASE_URL` secret set in GitHub repo settings
- Contracts CI uses pinned foundry-toolchain action hash for security

---

## How to Update This File

After every mistake or correction, add a new rule to the appropriate section:

```
### [Section Name]
- New rule learned from the mistake
```

This file makes Claude smarter on YOUR project with every session.
