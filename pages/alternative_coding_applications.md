---
layout: page-fullwidth
permalink: /alternative_uses_for_code
title: Alternative ways to apply coding skills
excerpt: applying coding skills to real-life challenges
---

When many researchers learn how to code, they're immediately thinking of
research challenges that they encounter and how some carefully crafted code
can help them with the challenge. We thought it would be fun to ask the
community to share applications of their coding skills to other applications.
From planning weddings to controling a house full of IoT equipment, there are
many ways to apply one's coding skills. Using what you know about programming
and open source tools can have many interesting implications for your hobbies and
other pastimes. Have a read through the fun applications shared by our community.

Add your own entry as a Pull Request to this file: [https://github.com/swcarpentry/website/blob/gh-pages/_data/alternative_uses_for_coding.yml](https://github.com/swcarpentry/website/blob/gh-pages/_data/alternative_uses_for_coding.yml)

{% for item in site.data.alternative_uses_for_coding %}
## {{ item.Name }}

{{ item.Text }}

{% endfor %}
