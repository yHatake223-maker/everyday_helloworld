# Secrets / .env Policy

This repository is designed to be safe to share and use as a template.

## Never commit secrets

Do NOT commit any of the following:
- API keys / tokens
- passwords
- private keys
- `.env` files containing real values

## `.env` usage

- Use `.env.example` as the template
- Keep the real `.env` local only (ignored by git)

Recommended workflow:
1. Copy `.env.example` to `.env`
2. Fill in values locally
3. Never add `.env` to git

## GitHub Secrets

If CI/CD needs secrets:
- Store them in GitHub Actions Secrets
- Reference them from workflows (never hardcode)

## If a secret is leaked

1. Revoke/rotate the leaked secret immediately
2. Remove it from the git history if it was committed
3. Add/verify ignore rules to prevent reoccurrence
4. Document a 1-line lesson in README (optional)
