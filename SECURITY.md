# Security Policy

## Reporting a Vulnerability

The AegisSentinel team takes security vulnerabilities seriously. We appreciate your efforts to responsibly disclose your findings and will make every effort to acknowledge your contributions.

### How to Report

**DO NOT** open a public GitHub issue for security vulnerabilities.

Instead, please report security vulnerabilities by emailing:

📧 **[security@aegissentinel.online](mailto:security@aegissentinel.online)**

Include the following information in your report:

- **Type of vulnerability** (e.g., smart contract bug, ZK circuit flaw, API vulnerability)
- **Full path(s)** of the affected source file(s)
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact assessment** of the vulnerability
- **Any suggested remediation** (if available)

### What to Expect

| Timeline | Action |
|----------|--------|
| 24 hours | Initial acknowledgment of your report |
| 72 hours | Preliminary assessment and severity classification |
| 7 days | Detailed response with remediation plan |
| 90 days | Public disclosure (coordinated with reporter) |

### Scope

The following are **in scope** for our security program:

| Repository | Components |
|------------|------------|
| aegis-sentinel-contracts | Smart contracts, deployment scripts |
| aegis-ai-engine | API endpoints, authentication, data handling |
| aegis-zkp-prover | ZK circuits, prover service, cryptographic implementations |
| aegis-docs | Sensitive information exposure |

The following are **out of scope**:

- Social engineering attacks
- Physical attacks
- Denial of service attacks
- Issues in third-party dependencies (report to upstream)
- Issues already reported or known

### Severity Classification

We use the following severity levels:

| Severity | Description | Examples |
|----------|-------------|----------|
| **Critical** | Immediate threat to funds or data | Smart contract fund drain, ZK proof bypass |
| **High** | Significant security impact | Authentication bypass, privilege escalation |
| **Medium** | Limited security impact | Information disclosure, input validation |
| **Low** | Minimal security impact | Minor information leaks, best practice violations |

### Bug Bounty Program

We plan to launch a formal bug bounty program in Q3 2026. Until then, valid security reports may be eligible for:

- Recognition in our security hall of fame
- $AEGIS token rewards (at our discretion)
- Swag and merchandise

### Safe Harbor

We consider security research conducted in accordance with this policy to be:

- Authorized under the Computer Fraud and Abuse Act (CFAA)
- Exempt from DMCA restrictions on security research
- Conducted in good faith

We will not pursue legal action against researchers who:

- Act in good faith
- Avoid privacy violations and data destruction
- Do not exploit vulnerabilities beyond proof of concept
- Report findings promptly and confidentially

---

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (main branch) | ✅ Yes |
| Previous releases | ⚠️ Critical fixes only |
| Deprecated versions | ❌ No |

---

## Security Best Practices for Users

### Smart Contract Interaction

- Always verify contract addresses before interacting
- Use hardware wallets for large transactions
- Review transaction details carefully before signing

### API Usage

- Never share API keys or access tokens
- Use secure, encrypted connections (HTTPS)
- Implement proper key rotation

### Node Operation

- Keep node software updated
- Use secure key management practices
- Monitor for unusual activity

---

## Contact

- Security Team: [security@aegissentinel.online](mailto:security@aegissentinel.online)
- General Inquiries: [contact@aegissentinel.online](mailto:contact@aegissentinel.online)
- Discord: [Join our community](https://discord.gg/Z5NcWtqB)

---

Thank you for helping keep AegisSentinel and our users safe! 🛡️
