# NPM Publishing Guide

## Prerequisites

1. **NPM Account**: Create one at https://www.npmjs.com/signup if you don't have one
2. **Email Verification**: Make sure your NPM email is verified

## Step 1: Login to NPM

Run this command and follow the prompts:

```bash
npm login
```

You'll be asked for:
- Username
- Password
- Email
- One-Time Password (OTP) if you have 2FA enabled

## Step 2: Verify Login

Check you're logged in:

```bash
npm whoami
```

This should display your NPM username.

## Step 3: Test Package

Before publishing, test that the package is correctly configured:

```bash
cd /Users/anveshk/Desktop/Cursour\ Projects/skills
npm pack --dry-run
```

This shows what files will be included in the package.

## Step 4: Publish to NPM

Publish your package:

```bash
cd /Users/anveshk/Desktop/Cursour\ Projects/skills
npm publish
```

Since your package is scoped (`@affilino/...`), it will be published as a public package automatically.

## Step 5: Verify Publication

After publishing, verify it's live:

```bash
npm view @affilino/ecommerce-seo-audit-skill
```

Or visit: https://www.npmjs.com/package/@affilino/ecommerce-seo-audit-skill

## Installation for Users

Once published, anyone can install your skill:

```bash
npm install -g @affilino/ecommerce-seo-audit-skill
```

Or use it directly:

```bash
npx @affilino/ecommerce-seo-audit-skill
```

Or add to their Claude Code:

```bash
/plugin marketplace add affilino/ecommerce-seo-audit-skill
```

## Future Updates

When you release updates:

1. **Update version** in package.json:
   ```bash
   npm version patch   # 1.0.0 → 1.0.1 (bug fixes)
   npm version minor   # 1.0.0 → 1.1.0 (new features)
   npm version major   # 1.0.0 → 2.0.0 (breaking changes)
   ```

2. **Commit and push**:
   ```bash
   git push origin main --tags
   ```

3. **Publish to NPM**:
   ```bash
   npm publish
   ```

## Troubleshooting

### Error: 403 Forbidden

You might not have permission to publish under the `@affilino` scope.

**Solution 1**: Create the organization on NPM
- Go to https://www.npmjs.com/org/create
- Create organization named "affilino"
- Add your account as owner

**Solution 2**: Publish without scope
- Change package name in package.json to: `"name": "ecommerce-seo-audit-skill"`
- Commit and publish again

### Error: Package name already exists

If someone else already published a package with that name:
- Try a different name like: `affilino-ecommerce-seo-audit`
- Or use your username scope: `@yourusername/ecommerce-seo-audit-skill`

## Package Information

- **Package Name**: @affilino/ecommerce-seo-audit-skill
- **Current Version**: 1.0.0
- **Repository**: https://github.com/affilino/ecommerce-seo-audit-skill
- **License**: SEE LICENSE IN LICENSE

## After Publishing

Share your NPM package:

**Twitter/X:**
```
📦 Now on NPM!

npm install -g @affilino/ecommerce-seo-audit-skill

Professional ecommerce SEO audits with 7 specialized audit types.

🔗 https://www.npmjs.com/package/@affilino/ecommerce-seo-audit-skill

#NPM #SEO #Ecommerce #ClaudeCode
```

**LinkedIn:**
```
Excited to announce that our Ecommerce SEO Audit Skill is now available on NPM!

Install it globally:
npm install -g @affilino/ecommerce-seo-audit-skill

Or check it out on GitHub:
https://github.com/affilino/ecommerce-seo-audit-skill

Perfect for Shopify, WooCommerce, Magento stores and more.

#NPM #OpenSource #SEO #Ecommerce
```

---

**Ready to publish? Run these commands:**

```bash
# 1. Login to NPM
npm login

# 2. Navigate to project
cd /Users/anveshk/Desktop/Cursour\ Projects/skills

# 3. Publish
npm publish

# Done! 🎉
```
