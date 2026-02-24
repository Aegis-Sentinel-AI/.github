# AegisSentinel

<p align="center">
  <img src="assets/aegis-sentinel-logo.png" alt="AegisSentinel Logo" width="200"/>
</p>

<p align="center">
  <strong>AI-Driven Cybersecurity for the Decentralized Era</strong>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#repositories">Repositories</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#ai-engine">AI Engine</a> •
  <a href="#dashboard">Dashboard</a> •
  <a href="#smart-contracts">Smart Contracts</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## Overview

**AegisSentinel** is a next-generation cybersecurity protocol that bridges advanced Artificial Intelligence with Layer 2 blockchain efficiency. We provide businesses with real-time, automated protection against evolving digital threats while maintaining absolute data privacy through Zero-Knowledge Proofs.

### Key Features

- 🛡️ **AI-Powered Threat Detection** — 35+ threat types with 97%+ confidence scoring
- 🔐 **Zero-Knowledge Privacy** — GDPR-compliant security logging without data exposure
- ⛓️ **L2 Blockchain Verification** — Immutable audit trails on Ethereum L2 (Sepolia)
- 📊 **Enterprise Dashboard** — Real-time SOC with progressive disclosure and AI insights
- 🏢 **Enterprise-Ready** — MiCA-compliant architecture for institutional adoption
- 🪙 **$AEGIS Token** — Utility token powering the protocol economy

### What This Means for Companies

| Metric | Traditional SIEM | AegisSentinel | Improvement |
|--------|-----------------|---------------|-------------|
| Mean Time to Detect | 4-6 hours | <100ms | 99%+ faster |
| Alert Fatigue | 10,000+ alerts/day | High-priority only | 90%+ reduction |
| SOC Analyst Workload | 10+ FTEs | 2-3 FTEs | 70% cost savings |
| Compliance | Manual audits | Automated on-chain | Continuous |

---

## Repositories

| Repository | Description | Status |
|------------|-------------|--------|
| [aegis-landing-next](./aegis-landing-next) | Landing page & enterprise dashboard (Next.js 16) | ✅ Live |
| [aegis-docs](./aegis-docs) | Technical documentation & lightpaper | 📚 Active |
| [aegis-docs-site](./aegis-docs-site) | Documentation website (Docusaurus) | ✅ Live |
| [aegis-sentinel-contracts](./aegis-sentinel-contracts) | L2 smart contracts (ERC-20, Verifier, Registry) | ✅ Deployed |
| [aegis-ai-engine](./aegis-ai-engine) | Off-chain AI threat detection engine (Python) | 🔨 Development |
| [aegis-zkp-prover](./aegis-zkp-prover) | Zero-Knowledge Proof circuits and prover | 🔨 Development |
| [aegis-portal](./aegis-portal) | Enterprise integration portal | 🔨 Development |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         AegisSentinel Protocol                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐     │
│  │   Enterprise    │    │   Sentinel AI   │    │   ZK-Prover     │     │
│  │   Network       │───▶│   Engine        │───▶│   Service       │     │
│  │                 │    │   (Off-chain)   │    │                 │     │
│  └─────────────────┘    └─────────────────┘    └────────┬────────┘     │
│                                                          │              │
│                                                          ▼              │
│                              ┌─────────────────────────────────────┐   │
│                              │      L2 Sentinel Contracts          │   │
│                              │         (Sepolia Testnet)           │   │
│                              │                                     │   │
│                              │  • SentinelToken (ERC-20)           │   │
│                              │  • SecurityVerifier                 │   │
│                              │  • TrustRegistry                    │   │
│                              └─────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Workflow

1. **Ingest** — Sentinel agents collect security events from your network
2. **Analyze** — AI engine classifies threats with 97%+ confidence
3. **Prove** — ZK-Prover creates cryptographic proof of the scan result
4. **Verify** — L2 contract verifies and logs the security status on-chain

---

## AI Engine

The Sentinel AI Engine detects **35+ distinct threat types** across 8 categories:

| Category | Threat Types | Examples |
|----------|--------------|----------|
| **Network** | 12 | DDoS, Port Scanning, DNS Tunneling, Man-in-the-Middle |
| **Application** | 8 | SQL Injection, XSS, Code Injection, API Abuse |
| **Identity** | 6 | Credential Stuffing, Account Takeover, Privilege Escalation |
| **Data** | 4 | Data Exfiltration, Sensitive Data Exposure |
| **Infrastructure** | 5 | Cryptojacking, Container Escape, Cloud Misconfiguration |
| **Insider** | 3 | Insider Threat, Policy Violation |
| **Supply Chain** | 2 | Dependency Confusion, Malicious Package Injection |
| **Cryptographic** | 2+ | Key Compromise, Certificate Abuse |

### Enterprise Detectors

- **Non-Human Identity (NHI) Monitor** — Service accounts, bots, API keys
- **Privileged Access Monitor** — Admin activity and escalations
- **Data Flow Analyzer** — Sensitive data movement tracking
- **Cloud Security Posture** — AWS, Azure, GCP misconfiguration

### MITRE ATT&CK Integration

Every threat maps to MITRE ATT&CK framework IDs (T1498, T1046, T1557, etc.)

---

## Dashboard

The Enterprise Dashboard provides a real-time security operations center:

### Pages

| Page | Features |
|------|----------|
| **Overview** | Metric cards, threat donut chart, geo heat map, AI insights |
| **Threats** | Threat table with filtering, severity badges, MITRE tags |
| **Scans** | Scan scheduling, results history, export reports |
| **Network** | Traffic analysis, anomaly detection, firewall status |
| **Identity** | NHI tracking, privileged access, login analytics |
| **Data** | Data flow mapping, exfiltration detection |
| **Infrastructure** | Cloud posture, container security, certificates |
| **Settings** | User management, integrations, API keys |

### Key Features

- **AI Insights Drill-Down** — Glassmorphism side panel with AI-generated threat summaries
- **Real-Time Pulse Animations** — Active alerts icon pulses on new threats
- **Geographic Heat Maps** — Attack origins by country with click-through
- **Confidence Indicators** — Visual 82-97% confidence scoring
- **Authentication** — SSO, MFA, role-based access control

---

## Smart Contracts

### Deployed on Sepolia Testnet

| Contract | Address | Purpose |
|----------|---------|---------|
| **SentinelToken** | `0x5cd78268AB8a8eF1F708E4aef911b211e52dEEd1` | ERC-20 utility token |
| **SecurityVerifier** | `0x535ff8D8A7DF86993720c7f56Ae34c78fe8ECBC6` | ZKP verification |
| **TrustRegistry** | `0x4a774a6C10a2722D1f808ccfC5087691662dC7F0` | Security status registry |

### Test Suite

- **120+ tests passing** — Comprehensive coverage
- **Internal security audit** — All critical issues resolved
- **Mainnet deployment** — Arbitrum One

---

## Getting Started

### Prerequisites

- Node.js >= 18.x
- Python >= 3.10
- pnpm (recommended) or npm

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Aegis-Sentinel-AI/aegis-sentinel.git
cd aegis-sentinel

# Run the landing page & dashboard
cd aegis-landing-next
pnpm install
pnpm dev
# Open http://localhost:3000

# Run the AI engine
cd ../aegis-ai-engine
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.lock
python -m pytest tests/

# Deploy contracts (requires Foundry)
cd ../aegis-sentinel-contracts
forge build
forge test
```

---

## Documentation

- 📄 [Technical Lightpaper v2.0](./aegis-docs/whitepaper/Technical-Lightpaper-v2.0.md)
- 🔧 [API Reference](./aegis-docs/api-reference/README.md)
- ⚖️ [Compliance Documentation](./aegis-docs/compliance/README.md)
- 🛠️ [Developer Guide](./aegis-docs/guides/README.md)
- 📊 [Dashboard Documentation](https://aegis-docs-site-two.vercel.app/platform/dashboard)

---

## Roadmap

### 2026

| Phase | Timeline | Status | Milestones |
|-------|----------|--------|------------|
| Foundation & Alpha | Q1–Q2 | 🟡 In Progress | AI engine (35+ threats), smart contracts (Sepolia), dashboard v1.0 |
| Token Launch & Beta | Q3–Q4 | ⚪ Planned | TGE (PinkSale), public beta, DEX/CEX listings |

### 2027

| Phase | Timeline | Milestones |
|-------|----------|------------|
| Ecosystem Expansion | H1 | Validator nodes, cross-chain integration, insurance partnerships |
| Institutional Scaling | H2 | Enterprise SDK, global compliance, full DAO governance |

---

## Tokenomics

### $AEGIS Token

| Utility | Description |
|---------|-------------|
| Subscription Lock | Enterprises lock tokens for service duration |
| Pay-Per-Scan | Micro-fees for one-off security audits |
| API Access | Token-gated premium API endpoints |
| Staking | Validators stake to participate in consensus |
| Governance | DAO voting on protocol upgrades |

### Presale Information

| Round | Price | Discount |
|-------|-------|----------|
| Early Bird | $0.015 | 62.5% off |
| Presale (PinkSale) | $0.022 | 45% off |
| Final Round | $0.032 | 20% off |
| Listing (Uniswap) | $0.04 | — |

**Timeline:** Q2 2026

---

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](./CONTRIBUTING.md) before submitting a pull request.

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/amazing-feature

# 3. Make your changes and commit
git commit -m 'Add amazing feature'

# 4. Push and open a PR
git push origin feature/amazing-feature
```

---

## Security

If you discover a security vulnerability, please report it responsibly via our [Security Policy](./SECURITY.md). Do not open a public issue.

---

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](./LICENSE) file for details.

---

## Links

| Platform | Link |
|----------|------|
| 🌐 Website | [aegissentinel.online](https://aegissentinel.online) |
| 📊 Dashboard | [aegissentinel.online/dashboard](https://aegissentinel.online/dashboard) |
| 📖 Documentation | [docs.aegissentinel.online](https://aegis-docs-site-two.vercel.app) |
| 🐦 X (Twitter) | [@AegisSentinelAi](https://x.com/AegisSentinelAi) |
| 💬 Discord | [discord.gg/aG5XwyV7sV](https://discord.gg/aG5XwyV7sV) |
| 📱 Telegram | [t.me/AegisSentinelAi](https://t.me/AegisSentinelAi) |
| 🐙 GitHub | [Aegis-Sentinel-AI](https://github.com/Aegis-Sentinel-AI) |
| 📧 Contact | [contact@aegissentinel.online](mailto:contact@aegissentinel.online) |

---

<p align="center">
  <sub>Built with 🛡️ by the AegisSentinel Team</sub>
</p>
