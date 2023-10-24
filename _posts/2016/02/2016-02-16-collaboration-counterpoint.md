---
layout: page
authors: ["Greg Wilson"]
title: "A Counterpoint to Collaborative Lesson Design"
date: 2016-02-16
time: "00:30:00"
repo: "https://github.com/swcarpentry/modern-scientific-authoring"
site: "https://swcarpentry.github.io/modern-scientific-authoring"
tags: ["Community", "Lessons", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>
Discussion of our proposed lesson on
[on modern scientific authoring]({{site.github_url}}/modern-scientific-authoring)
is an instructive counterpoint to our previous post
extolling the virtues of [collaborative lesson development]({{site.baseurl}}/blog/2016/02/designing-lessons-collaboratively.html).
The aim of the lesson is to show researchers how to write and publish in the early 21st Century---or more honestly,
to persuade them to stop mailing each other copies of Microsoft Word files
and start using something else.
After a long-winded opening (which I'll cut substantially),
the [current introduction]({{page.site}}/01-mess.html) summarizes the strengths and weaknesses of six options:

1.  WYSIWYG on the desktop (Microsoft Word).
2.  WYSIWYG on the web (Google Docs).
3.  Desktop typesetting (LaTeX).
4.  Web-based typesetting hybrids (Authorea, Overleaf).
5.  HTML.
6.  Markdown.

It concludes that for the foreseeable future,
many researchers will continue to prefer WYSIWYG tools
rather than typesetting tools requiring compilation
(such as LaTeX and Markdown).
However,
since most researchers are already familiar with WYSIWYG tools,
and since typesetting tools are easier to integrate into reproducible workflows,
the lesson will focus on LaTeX for mansucripts
and Markdown for the web.

The feedback to date has been interesting:

*   Word's built-in compare/merge tool can be launched from version control systems.
*   New tools (like Authorea and Overleaf) are necessarily immature,
    and there's no guarantee they'll still be around in a couple of years.
*   Many journals won't accept either LaTeX or Markdown,
    so we should teach a Markdown-plus-Pandoc workflow.
*   Setting up a build environment for a randomly-selected LaTeX document
    is exactly as challenging as setting one up for a randomly chosen piece of software.
*   What about [LyX](http://lyx.org)?
*   What about [CommonMark](http://commonmark.org)?
*   What about [reStructuredText](http://docutils.sourceforge.net/rst.html)?
*   What about [RMarkdown](http://rmarkdown.rstudio.com/)?
*   What about [Microsoft OneDrive](https://onedrive.live.com/)?
*   What about [org-mode](http://orgmode.org/)?
*   What about the [Jupyter Notebook](http://jupyter.org/)?

There *were* a few comments about lesson content
(mostly about workflows for reviewing changes),
but compared to the feedback on the new introduction to Python,
there was much more about technical issues like tools and formats
and much less about pedagogy and big ideas.
I suspect there are two reasons for that:

1.  We've been teaching Python for years,
    so instructors are more familiar with the pedagogical issues.

2.  There's genuinely less agreement about tools for modern research writing.

The next step is going to be to draw up an outline
like [this one]({{site.github_url}}/python-novice-gapminder/blob/gh-pages/index.md)
laying out topics, exercises, and timings.
We've found with the new Python lesson that this focuses the discussion,
and we're hoping that it will allow parallelization,
i.e.,
that many people will be able to fill in different parts of the outline simultaneously
once the overall structure has been agreed.

One of the biggest challenges in doing this will be
to make the lesson *not* depend on command-line skills,
so that it's accessible to people who are attending Data Carpentry workshops.
That's going to be hard,
as both LaTeX and Pandoc are command-line tools.
Whatever results,
building lessons this way is a big step for us,
and I'm eager to see how well it actually works.
