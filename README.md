# Ecommerce SEO Audit Skill for Claude Code

Professional ecommerce SEO audit skill for Claude Code, developed by **Auckland Shopify SEO Agency** - Affilino NZ. This skill provides comprehensive SEO audits for online stores, covering product pages, collection pages, technical SEO, log file analysis, and competitor research.

## Features

- **7 Specialized Audit Types** - Technical, Product, Collection, Log Files, Competitors, Keywords, and Full Comprehensive audits
- **Competitor Analysis** - Analyze top 5 ranking sites for any keyword
- **Log File Analysis** - Crawl budget optimization and Googlebot behavior insights
- **Keyword Research & Mapping** - Find opportunities and map keywords to pages
- **Real, Actionable Recommendations** - Prioritized action plans with before/after examples
- **Three-Bucket Framework** - Systematic approach covering Technical, On-Page, and Off-Page SEO

## Installation

### Using Claude Code Plugin Manager

1. Add the marketplace to your Claude Code:
```bash
/plugin marketplace add affilino/ecommerce-seo-audit-skill
```

2. Install the skill:
```bash
/plugin install ecommerce-seo-audit
```

3. The skill will be available immediately in your Claude Code session.

### Manual Installation

1. Clone this repository:
```bash
git clone https://github.com/affilino/ecommerce-seo-audit-skill.git
```

2. Copy to your skills directory:
```bash
# For personal skills
cp -r ecommerce-seo-audit-skill ~/.claude/skills/

# OR for project-specific skills
cp -r ecommerce-seo-audit-skill .claude/skills/
```

3. Restart Claude Code or reload your skills.

## Usage

Invoke the skill in Claude Code:

```bash
/ecommerce-seo-audit
```

Or provide arguments directly:

```bash
/ecommerce-seo-audit technical https://yourstore.com
/ecommerce-seo-audit product https://yourstore.com/products/example
/ecommerce-seo-audit competitor https://yourstore.com "running shoes"
```

### Available Audit Types

1. **Quick Technical Audit** - Crawlability, indexability, and schema check (10-15 min)
2. **Product Page Audit** - Deep analysis of product page optimization (20-30 min)
3. **Collection Page Audit** - Category/collection page SEO review (20-30 min)
4. **Log File Analysis** - Crawl budget and Googlebot behavior analysis (30-45 min)
5. **Competitor Analysis** - Analyze top 5 ranking competitors (30-45 min)
6. **Keyword Research & Mapping** - Find opportunities and map keywords (30-45 min)
7. **Full Comprehensive Audit** - Complete audit covering all areas (60-90 min)

## Examples

### Quick Technical Audit
```bash
/ecommerce-seo-audit technical https://mystore.com
```

Get a health score with top 3 critical issues and quick wins.

### Product Page Audit
```bash
/ecommerce-seo-audit product https://mystore.com
```

Analyze 5-10 products with detailed optimization recommendations.

### Competitor Analysis
```bash
/ecommerce-seo-audit competitor https://mystore.com "men's running shoes"
```

Analyze top 5 ranking competitors with actionable roadmap to outrank them.

## Output Format

All audits provide:

- **Executive Summary** - SEO health score, critical issues, and quick wins
- **Detailed Findings** - Comprehensive analysis with data and examples
- **Prioritized Action Plan** - CRITICAL, HIGH, MEDIUM, and LOW priority items
- **Expected Impact** - Quantified traffic and revenue projections
- **Benchmarking** - How you compare to competitors

## Requirements

- Claude Code CLI
- Internet connection for WebSearch and WebFetch tools
- For log file analysis: Access to server logs (Apache, Nginx, or IIS format)

## Who Should Use This

- Ecommerce store owners (Shopify, WooCommerce, Magento, etc.)
- SEO professionals managing ecommerce clients
- Marketing teams optimizing online stores
- Agencies offering SEO services

## Developed By

**Affilino NZ - Auckland Shopify SEO Agency**

This skill was developed by the team at Affilino, a leading Auckland-based Shopify SEO agency specializing in ecommerce SEO audits and optimization for online stores.

### Need Professional Help?

For assistance, customization, or professional SEO services:

- **Website:** [affilino.co.nz](https://affilino.co.nz)
- **Email:** hello@affilino.co.nz
- **Specialization:** Shopify SEO, Ecommerce SEO Audits, Technical SEO

## Contributing

We welcome contributions! If you'd like to improve this skill:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add new audit feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## Version History

- **v1.0.0** (2026-01-30) - Initial release
  - 7 audit types
  - Competitor analysis
  - Log file analysis
  - Keyword research & mapping

## License

Copyright (c) 2026 Affilino NZ. All rights reserved.

## Support

If you encounter any issues or have questions:

1. Check the [GitHub Issues](https://github.com/affilino/ecommerce-seo-audit-skill/issues)
2. Contact us at hello@affilino.co.nz
3. Visit [affilino.co.nz](https://affilino.co.nz) for professional support

---

**Made with focus by Auckland Shopify SEO Agency - Affilino NZ**
