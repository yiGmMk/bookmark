from process_changes import get_text_content
import re

print(get_text_content("https://ssoready.com/docs/saml/saml-technical-primer"))


content="""
Title: SAML: A technical primer — SSOReady Docs

URL Source: https://ssoready.com/docs/saml/saml-technical-primer

Markdown Content:
If you just want to start integrating SAML right away, check out the [SAML quickstart](https://ssoready.com/docs/saml/saml-quickstart). You can get a SAML integration working end-to-end within a few hours.

This article is for folks who want to understand SAML at a deeper technical level, or how they could implement SAML without using an open-source library like SSOReady.

[SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) (“Security Assertion Markup Language”) is a source of a lot of confusion for developers. This article is a technical primer on some of the most common questions engineers and other technical folks have about SAML:

1.  [Why do businesses want their software vendors to support SAML](https://ssoready.com/docs/saml/saml-technical-primer#what-is-the-point-of-saml)? In other words, how does SAML fit into my customer’s business? Why do end users and C-level executives at my customer care about SAML?
2.  [How should I fit SAML into my existing software](https://ssoready.com/docs/saml/saml-technical-primer#fitting-saml-into-your-existing-software)? What parts of my software stack need to be “SAML-aware”? How lightweight can I make my integration? (The answer: quite lightweight. Only a small part of your codebase needs to know about SAML at all.)
3.  [At a technical level, how does SAML even work](https://ssoready.com/docs/saml/saml-technical-primer#saml-at-a-technical-level)? What does the SAML protocol even do? What kinds of security guarantees does it give me, or what assumptions can I make about it?

What is the point of SAML?
--------------------------
"""

# 使用正则表达式提取 title 和 URL Source
title_pattern = r'Title:\s*(.*)'


title_match = re.search(title_pattern, content)

if title_match:
    title = title_match.group(1)
else:
    title = None

# 输出结果
print(f"Title: {title}")


with open("a.md", 'w', encoding='utf-8') as f:
            f.write(f"""---
layout: post
---
{title}
""")