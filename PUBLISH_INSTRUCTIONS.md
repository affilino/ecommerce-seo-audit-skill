# Publishing Instructions

Follow these steps to publish your Ecommerce SEO Audit Skill to GitHub and various marketplaces.

---

## Step 1: Set Up Remote Repository

The repository is already created at: https://github.com/affilino/ecommerce-seo-audit-skill

Add the remote:

```bash
cd /Users/anveshk/Desktop/Cursour\ Projects/skills
git remote add origin https://github.com/affilino/ecommerce-seo-audit-skill.git
```

---

## Step 2: Create Initial Commit

Stage all files and create the first commit:

```bash
git add .
git commit -m "$(cat <<'EOF'
Initial release: Ecommerce SEO Audit Skill v1.0.0

- 7 specialized audit types (Technical, Product, Collection, Log Files, Competitors, Keywords, Full)
- Competitor analysis with top 5 ranking sites
- Log file analysis for crawl budget optimization
- Comprehensive keyword research and mapping
- Real, actionable recommendations with before/after examples
- Developed by Affilino NZ - Auckland Shopify SEO Agency

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

---

## Step 3: Create and Push Git Tag

**CRITICAL:** Plugin marketplaces fetch tags, not the main branch. You MUST tag before users can install.

Create the v1.0.0 tag:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0 - Initial public release"
```

---

## Step 4: Push to GitHub

Push both the code and the tag:

```bash
# Push the main branch
git push -u origin main

# Push the tag
git push origin v1.0.0
```

If you're using a different default branch name (like 'master'):

```bash
git push -u origin master
git push origin v1.0.0
```

---

## Step 5: Verify on GitHub

1. Go to https://github.com/affilino/ecommerce-seo-audit-skill
2. Check that all files are present
3. Go to "Releases" tab and verify v1.0.0 tag is visible
4. Verify README displays correctly

---

## Step 6: Test Installation

Test that users can install your skill:

```bash
# In a new Claude Code session
/plugin marketplace add affilino/ecommerce-seo-audit-skill
/plugin install ecommerce-seo-audit

# Test the skill
/ecommerce-seo-audit
```

---

## Step 7: Submit to Community Repositories

### A. Submit to anthropics/skills

1. Fork https://github.com/anthropics/skills
2. Create a new branch: `git checkout -b add-ecommerce-seo-audit`
3. Add your skill to the appropriate category
4. Create PR using the template in SUBMISSION_GUIDE.md
5. Wait for review and approval

### B. Submit to awesome-claude-skills

1. Fork https://github.com/travisvn/awesome-claude-skills
2. Create a new branch: `git checkout -b add-ecommerce-seo-audit`
3. Add entry to README.md under "SEO / Marketing" section:
   ```markdown
   - [Ecommerce SEO Audit](https://github.com/affilino/ecommerce-seo-audit-skill) - Comprehensive ecommerce SEO audits with 7 specialized audit types. By Affilino NZ.
   ```
4. Create PR with description from SUBMISSION_GUIDE.md
5. Wait for merge

### C. Submit to SkillsMP (skillsmp.com)

1. Visit https://skillsmp.com/submit (or their submission page)
2. Fill in the form using details from SUBMISSION_GUIDE.md
3. Use repository URL: https://github.com/affilino/ecommerce-seo-audit-skill
4. Submit and wait for approval

### D. Submit to claudemarketplaces.com

1. Visit https://claudemarketplaces.com/submit
2. Fill in plugin details from SUBMISSION_GUIDE.md
3. Submit for review

### E. Submit to mcpmarket.com

1. Visit https://mcpmarket.com/submit
2. Select "Claude Code Skill" as type
3. Fill in details from SUBMISSION_GUIDE.md
4. Submit

---

## Step 8: Announce Your Skill

### Social Media

**Twitter/X:**
```
🚀 Just released: Ecommerce SEO Audit Skill for @ClaudeAI Code!

7 specialized audit types for online stores:
✅ Technical SEO
✅ Product pages
✅ Collections
✅ Log file analysis
✅ Competitor research
✅ Keyword mapping

Install: /plugin marketplace add affilino/ecommerce-seo-audit-skill

#ClaudeCode #SEO #Ecommerce
```

**LinkedIn:**
```
Excited to announce the release of our Ecommerce SEO Audit Skill for Claude Code!

As an Auckland Shopify SEO Agency, we've packaged our professional SEO audit methodology into a Claude Code skill that anyone can use.

Features:
• 7 specialized audit types
• Real-time competitor analysis
• Crawl budget optimization
• Actionable recommendations
• Before/after examples

Perfect for ecommerce stores on Shopify, WooCommerce, Magento, and more.

Install it now:
/plugin marketplace add affilino/ecommerce-seo-audit-skill

Check it out: https://github.com/affilino/ecommerce-seo-audit-skill

#SEO #Ecommerce #AI #ClaudeCode #Shopify
```

### Email Newsletter

If you have a customer email list, announce the skill:

**Subject:** New Free Tool: Ecommerce SEO Audit Skill for Claude Code

**Body:**
```
Hi [Name],

We've just released a powerful new tool for ecommerce store owners!

Our Ecommerce SEO Audit Skill for Claude Code brings professional-grade SEO audits to your fingertips.

What it does:
- 7 specialized audit types (technical, products, collections, competitors, etc.)
- Real, actionable recommendations
- Competitor benchmarking
- Crawl budget optimization
- Keyword research and mapping

It's completely free and open source.

Installation is simple:
1. Install Claude Code (if you haven't already)
2. Run: /plugin marketplace add affilino/ecommerce-seo-audit-skill
3. Run: /plugin install ecommerce-seo-audit

Get it here: https://github.com/affilino/ecommerce-seo-audit-skill

Questions? Reply to this email!

Cheers,
Affilino Team
Auckland Shopify SEO Agency
https://affilino.co.nz
```

---

## Future Updates

### When You Make Changes

1. Make your code changes
2. Update version in marketplace.json
3. Commit changes
4. Create new tag:
   ```bash
   git tag -a v1.1.0 -m "Release version 1.1.0 - Description of changes"
   git push origin main
   git push origin v1.1.0
   ```
5. Update release notes on GitHub
6. Notify users via social media

### Version Numbering

Follow semantic versioning (semver):
- **Major (1.x.x)**: Breaking changes
- **Minor (x.1.x)**: New features, backward compatible
- **Patch (x.x.1)**: Bug fixes, backward compatible

Examples:
- v1.0.0 → v1.0.1 (bug fix)
- v1.0.0 → v1.1.0 (new audit type added)
- v1.0.0 → v2.0.0 (major rewrite, breaking changes)

---

## Monitoring Success

Track these metrics:

1. **GitHub Stats**
   - Stars
   - Forks
   - Issues opened
   - Pull requests

2. **Installation Metrics**
   - Monitor social media mentions
   - Track website referrals
   - Email inquiries

3. **User Feedback**
   - GitHub issues
   - Social media comments
   - Direct emails

---

## Support

If users have issues:

1. **GitHub Issues**: https://github.com/affilino/ecommerce-seo-audit-skill/issues
2. **Email**: hello@affilino.co.nz
3. **Website**: https://affilino.co.nz

---

## Quick Reference Commands

```bash
# Add remote (if not already added)
git remote add origin https://github.com/affilino/ecommerce-seo-audit-skill.git

# Initial commit
git add .
git commit -m "Initial release: Ecommerce SEO Audit Skill v1.0.0"

# Create tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push everything
git push -u origin main
git push origin v1.0.0

# Test installation
/plugin marketplace add affilino/ecommerce-seo-audit-skill
/plugin install ecommerce-seo-audit
```

---

**You're all set!** Follow these steps and your skill will be live and available to the Claude Code community.
