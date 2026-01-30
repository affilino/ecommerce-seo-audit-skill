# Skill Submission Guide

This document contains submission drafts for publishing the Ecommerce SEO Audit Skill to various community repositories and marketplaces.

---

## 1. Submission to anthropics/skills

### Pull Request Title
```
Add Ecommerce SEO Audit Skill by Affilino NZ
```

### Pull Request Description
```markdown
## Skill Name
Ecommerce SEO Audit

## Description
Professional ecommerce SEO audit skill for Claude Code, developed by Auckland Shopify SEO Agency - Affilino NZ. Provides comprehensive SEO audits for online stores with 7 specialized audit types.

## Features
- 7 specialized audit types (Technical, Product, Collection, Log Files, Competitors, Keywords, Full)
- Competitor analysis with top 5 ranking sites
- Log file analysis for crawl budget optimization
- Keyword research and mapping
- Real, actionable recommendations with before/after examples

## Use Cases
- Ecommerce store SEO optimization (Shopify, WooCommerce, Magento)
- Product page optimization
- Collection/category page SEO
- Technical SEO audits
- Competitor analysis for rankings
- Crawl budget optimization

## Author
Affilino NZ - Auckland Shopify SEO Agency
- Website: https://affilino.co.nz
- Email: hello@affilino.co.nz

## Repository
https://github.com/affilino/ecommerce-seo-audit-skill

## Installation
```bash
/plugin marketplace add affilino/ecommerce-seo-audit-skill
/plugin install ecommerce-seo-audit
```

## Testing
- Tested with Claude Code latest version
- All audit types functioning correctly
- WebSearch and WebFetch integration verified
```

### Files to Include in PR
- `/ecommerce-seo-audit/SKILL.md`
- `/ecommerce-seo-audit/.claude-plugin/marketplace.json`
- `/ecommerce-seo-audit/README.md`

---

## 2. Submission to awesome-claude-skills

### Pull Request Title
```
Add Ecommerce SEO Audit Skill
```

### Pull Request Description
```markdown
Adding a comprehensive ecommerce SEO audit skill for online stores.

**Category:** SEO / Marketing

**Description:** Professional ecommerce SEO audit skill with 7 specialized audit types including technical SEO, product pages, collections, log files, competitors, and keyword research.

**Author:** Affilino NZ (Auckland Shopify SEO Agency)

**Repository:** https://github.com/affilino/ecommerce-seo-audit-skill
```

### Markdown Entry for README
```markdown
### SEO / Marketing

- [Ecommerce SEO Audit](https://github.com/affilino/ecommerce-seo-audit-skill) - Comprehensive ecommerce SEO audits with 7 specialized audit types. Covers technical SEO, product pages, collections, log files, competitor analysis, and keyword research. By Affilino NZ.
```

---

## 3. Submission to SkillsMP (skillsmp.com)

### Skill Listing Information

**Skill Name:**
```
Ecommerce SEO Audit
```

**Short Description (160 chars):**
```
Professional ecommerce SEO audits for online stores. 7 audit types: technical, products, collections, logs, competitors, keywords. By Affilino NZ.
```

**Long Description:**
```
Professional ecommerce SEO audit skill for Claude Code, developed by Auckland Shopify SEO Agency - Affilino NZ.

This skill provides comprehensive SEO audits for online stores with 7 specialized audit types:

1. Quick Technical Audit - Crawlability, indexability, schema (10-15 min)
2. Product Page Audit - Deep product optimization analysis (20-30 min)
3. Collection Page Audit - Category/collection SEO review (20-30 min)
4. Log File Analysis - Crawl budget optimization (30-45 min)
5. Competitor Analysis - Top 5 ranking competitors (30-45 min)
6. Keyword Research - Find opportunities and map keywords (30-45 min)
7. Full Comprehensive Audit - Everything combined (60-90 min)

Features:
- Real, actionable recommendations
- Before/after examples
- Prioritized action plans
- Competitor benchmarking
- ROI projections

Perfect for Shopify, WooCommerce, Magento, and other ecommerce platforms.
```

**Category:**
```
SEO, Marketing, Ecommerce
```

**Tags:**
```
seo, ecommerce, shopify, audit, competitor-analysis, technical-seo, keyword-research, log-analysis
```

**Author:**
```
Affilino NZ
```

**Author Website:**
```
https://affilino.co.nz
```

**Repository URL:**
```
https://github.com/affilino/ecommerce-seo-audit-skill
```

**Installation Command:**
```
/plugin marketplace add affilino/ecommerce-seo-audit-skill && /plugin install ecommerce-seo-audit
```

**Version:**
```
1.0.0
```

**License:**
```
Proprietary - Copyright Affilino NZ
```

---

## 4. Submission to claudemarketplaces.com

### Listing Details

**Plugin Name:**
```
Ecommerce SEO Audit Skill
```

**Tagline:**
```
7 specialized SEO audit types for ecommerce stores
```

**Description:**
```
Professional ecommerce SEO audit skill by Auckland Shopify SEO Agency - Affilino NZ.

Audit Types:
• Quick Technical Audit (crawling, schema, indexing)
• Product Page Audit (optimization analysis)
• Collection Page Audit (category SEO)
• Log File Analysis (crawl budget)
• Competitor Analysis (top 5 rankings)
• Keyword Research (mapping & opportunities)
• Full Comprehensive Audit (all-in-one)

Provides actionable recommendations, competitor benchmarking, and ROI projections.
```

**Category:**
```
SEO Tools
```

**Pricing:**
```
Free
```

**Installation:**
```
/plugin marketplace add affilino/ecommerce-seo-audit-skill
/plugin install ecommerce-seo-audit
```

---

## 5. Submission to mcpmarket.com

### Tool Information

**Name:**
```
Ecommerce SEO Audit
```

**Type:**
```
Claude Code Skill
```

**Description:**
```
Professional ecommerce SEO audits with 7 specialized audit types. Covers technical SEO, product pages, collections, log file analysis, competitor research, and keyword mapping. Developed by Affilino NZ.
```

**Categories:**
```
SEO, Marketing, Analytics
```

**Use Cases:**
```
- Shopify store SEO optimization
- Product page SEO analysis
- Collection/category page optimization
- Technical SEO audits
- Competitor ranking analysis
- Crawl budget optimization
- Keyword research and mapping
```

**Installation:**
```bash
/plugin marketplace add affilino/ecommerce-seo-audit-skill
/plugin install ecommerce-seo-audit
```

**Documentation:**
```
https://github.com/affilino/ecommerce-seo-audit-skill/blob/main/README.md
```

**Repository:**
```
https://github.com/affilino/ecommerce-seo-audit-skill
```

---

## General Submission Checklist

Before submitting to any marketplace, ensure:

- [ ] Repository is public on GitHub
- [ ] v1.0.0 tag is created and pushed
- [ ] README.md is complete with installation instructions
- [ ] SKILL.md has proper YAML frontmatter
- [ ] marketplace.json is configured correctly
- [ ] All email addresses use hello@affilino.co.nz
- [ ] "Auckland Shopify SEO Agency" is mentioned in README
- [ ] License information is included
- [ ] Contact information is correct

## Next Steps

1. **Create GitHub Repository**
   ```bash
   # Create repository on GitHub first, then:
   git remote add origin https://github.com/affilino/ecommerce-seo-audit-skill.git
   ```

2. **Push Code with Tag**
   ```bash
   git add .
   git commit -m "Initial release v1.0.0"
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin main
   git push origin v1.0.0
   ```

3. **Submit to Communities**
   - Fork anthropics/skills and create PR
   - Fork awesome-claude-skills and create PR
   - Submit to SkillsMP via their submission form
   - Submit to claudemarketplaces.com
   - Submit to mcpmarket.com

4. **Announce**
   - Share on Twitter/X with #ClaudeCode
   - Share on LinkedIn
   - Share in relevant Discord/Slack communities
   - Email existing customers/contacts

---

**Ready to publish!** Follow the steps above to get your skill into multiple marketplaces.
