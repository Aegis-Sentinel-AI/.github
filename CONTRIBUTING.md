# Contributing to AegisSentinel

First off, thank you for considering contributing to AegisSentinel! 🛡️

This document provides guidelines and steps for contributing. By participating in this project, you agree to abide by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Process](#development-process)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [security@aegissentinel.online](mailto:security@aegissentinel.online).

---

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title** describing the issue
- **Detailed steps** to reproduce the problem
- **Expected behavior** vs. actual behavior
- **Environment details** (OS, versions, etc.)
- **Screenshots/logs** if applicable

### 💡 Suggesting Features

Feature suggestions are welcome! Please:

1. Check if the feature has already been suggested
2. Open an issue with the `enhancement` label
3. Clearly describe the feature and its use case
4. Explain why this feature would benefit the project

### 📝 Documentation

Documentation improvements are always appreciated:

- Fix typos or clarify existing docs
- Add examples and tutorials
- Translate documentation
- Improve API reference

### 💻 Code Contributions

We welcome code contributions across all repositories:

| Repository | Languages | Focus Areas |
|------------|-----------|-------------|
| aegis-sentinel-contracts | Solidity | Smart contracts, testing |
| aegis-ai-engine | Python, Rust | AI models, integrations |
| aegis-zkp-prover | Circom, Rust | ZK circuits, optimization |
| aegis-docs | Markdown | Documentation, guides |

---

## Development Process

### 1. Fork & Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
git remote add upstream https://github.com/Aegis-Sentinel-AI/REPO_NAME.git
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Make Changes

- Write clean, documented code
- Add tests for new functionality
- Ensure all tests pass
- Update documentation as needed

### 4. Stay Updated

```bash
git fetch upstream
git rebase upstream/main
```

---

## Style Guidelines

### Solidity (aegis-sentinel-contracts)

- Follow [Solidity Style Guide](https://docs.soliditylang.org/en/latest/style-guide.html)
- Use NatSpec comments for all public functions
- Maximum line length: 120 characters
- Use `forge fmt` for formatting

### Python (aegis-ai-engine)

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints
- Maximum line length: 88 characters (Black formatter)
- Use `black` and `isort` for formatting

### Rust (aegis-ai-engine, aegis-zkp-prover)

- Follow [Rust Style Guide](https://doc.rust-lang.org/nightly/style-guide/)
- Use `cargo fmt` for formatting
- Use `cargo clippy` for linting

### Circom (aegis-zkp-prover)

- Clear signal naming conventions
- Document all templates
- Include constraint counts in comments

---

## Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```
feat(contracts): add staking functionality to SentinelToken

fix(ai-engine): resolve memory leak in threat detector

docs(api): update authentication endpoint documentation
```

---

## Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass locally
- [ ] New code has appropriate test coverage
- [ ] Documentation is updated
- [ ] Commit messages follow conventions
- [ ] Branch is up to date with `main`

### PR Template

When opening a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

### Review Process

1. At least one maintainer must approve
2. All CI checks must pass
3. No unresolved conversations
4. Squash and merge preferred

---

## Recognition

Contributors will be recognized in:

- Repository README
- Release notes
- Community announcements

---

## Questions?

- Open a [Discussion](https://github.com/Aegis-Sentinel-AI/aegis-docs/discussions)
- Join our [Discord](https://discord.gg/aG5XwyV7sV)
- Join our [Telegram](https://t.me/AegisSentinelAi)
- Email: [contributors@aegissentinel.online](mailto:contributors@aegissentinel.online)

---

Thank you for contributing to AegisSentinel! 🛡️
