from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="ecommerce-seo-audit-skill",
    version="1.1.0",
    author="Affilino NZ",
    author_email="hello@affilino.co.nz",
    description="Professional ecommerce SEO audit skill for Claude Code with 7 specialized audit types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/affilino/ecommerce-seo-audit-skill",
    project_urls={
        "Bug Tracker": "https://github.com/affilino/ecommerce-seo-audit-skill/issues",
        "Documentation": "https://github.com/affilino/ecommerce-seo-audit-skill#readme",
        "Source Code": "https://github.com/affilino/ecommerce-seo-audit-skill",
        "NPM Package": "https://www.npmjs.com/package/@affilino/ecommerce-seo-audit-skill",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    package_data={
        "": ["SKILL.md", "README.md", "LICENSE", ".claude-plugin/marketplace.json"],
    },
    include_package_data=True,
    keywords=[
        "claude-code",
        "claude-skill",
        "agent-skill",
        "seo",
        "ecommerce",
        "shopify",
        "seo-audit",
        "technical-seo",
        "ecommerce-seo",
        "product-pages",
        "competitor-analysis",
        "keyword-research",
        "ai-agent",
        "anthropic",
        "claude",
        "affilino",
    ],
)
