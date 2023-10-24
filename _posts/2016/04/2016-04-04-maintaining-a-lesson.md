---
layout: page
authors: ["John Blischak"]
title: "Maintaining a Lesson"
date: 2016-04-04
time: "11:00:00"
tags: ["Lessons", "R", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

After two years as a Software Carpentry lesson maintainer of [r-novice-inflammation][],
I am stepping down so that I can spend more time on my research
(this thesis appears unwilling to write itself)
and with my family.
This therefore seems like a good time to summarize what's happened and what I've learned
for the benefit of anyone planning to become a maintainer.

## A Bit of Background

Software Carpentry really started growing the number of workshops and instructors in 2012.
At the time, there were two main sets of lessons in place:
the [version 4 SWC lessons][swcv4] written by Greg Wilson and others in 2010-11,
and a set developed by [The Hacker Within][thw],
a student group at the University of Wisconsin - Madison.
(These were referred to as the THW lessons,
and can be found in the old [boot-camps repository][boot-camps].)

Two problems arose as the number of workshops and instructors increased:

1.  Because no official lesson set was enforced,
    a workshop could be taught using the Version 4 lessons,
    the THW lessons,
    and/or lessons that an instructor put together the week before.
2.  Because the workshops were reaching a wider audience,
    many attendees had never programmed before,
    but the lessons were written for people who had at least some previous experience.

To address these problems,
the curriculum was [reorganized][reorg] to create an official set of lessons to be taught in all workshops.
As part of this,
we aimed to create one set of lessons for complete beginners with no previous programming experience ("novice")
and one for self-taught programmers ("intermediate").
Of these,
the novice versions received much more attention and development than the intermediate.
Both sets were stored in a single [bc][] repository
("bc" was short for "bootcamp", which is what we used to call workshops),
and the Python and SQL lessons were both written as Jupyter notebooks.

By late 2014,
storing all the lessons in one central repository had become unmanageable,
so we [split the bc repo][split] into separate repositories for each lesson.
At the same time,
we adoped a [lesson-template][template] to ensure that all the lessons would have the same structure.
This gave us the [lessons as they are today][lessons].

## Enter r-novice-inflammation

As SWC grew,
there was lots of interest in hosting R-based workshops.
While some instructors (myself included) experimented with custom R lessons,
there was no official set of R lessons:
the [reorganization][reorg] seemed like the perfect time to fix this.

It also seemed like a good time to experiment with collaboratively developing lesson material
(see for example these blog posts by [Greg Wilson in 2011][wilson2011] and [Justin Kitzes in 2014][kitzes2014] ---
this was also the time that the [r-discuss list][r-discuss] was created).
Inspired by these ideas,
we tried to make the lesson development process as similar to open source software development as possible.

Our [options][options] for creating a new R lesson were
to merge the already existing lesson sets,
to translate the novice Python lesson to R,
or to start from scratch.
In our initial [discussion][],
we decided it would be most straightforward to translate the novice Python lessons that used some fake "inflammation" data
(now [python-novice-inflammation][]).
Six months later, we [announced][announced] the completion of [r-novice-inflammation][],
which was subsequently migrated to the lesson template.

The strengths of [r-novice-inflammation][] are that
it focuses on language-agnostic programming principles
and parallels the standard Python lesson.
Its main weakness is that many of our R instructors are enthusiastic about their favorite language,
and preferred to have a lesson focus on how it,
in combination with packages like [dplyr][],
could be used for data analysis.
After much discussion,
we decided that the best way to resolve this was to support a second R lesson,
[r-novice-gapminder][],
that focuses more on R specifics for data analysis and visualization.

## Mechanics of the Lesson Template

The mechanics of our lessons have gone through almost as many changes as their content,
and are set to go through more in the coming months.
At present,
the core of the lesson template resides in the [lesson-template][] repo.
This repo is purposely very minimal
because it is repeatedly merged into the repos for specific lessons.
For example,
it does not contain a README file,
because if it did,
that file would create conflicts with the lesson's own README file at each merge.

An example of the lesson template is contained in [lesson-example][].
This repo contains the documentation for writing lessons using the template,
the most important of which is [LAYOUT.md][],
which describes all the files a lesson should contain
and how they should be structured.
As is often the case,
these instructions are an ideal,
and not necessarily how the repositories are maintained in practice:
for example,
[LAYOUT.md][] states that solutions to challenges are supposed to be contained in the file [instructors.md][],
but this is inconsistently implemented across the SWC lesson repos.

Here is how the template works in general.
Content is written in Markdown and converted to HTML using pandoc.
This process is automated using a [Makefile][],
so that running the command `make preview` builds the site.
All content, including generated HTML files and figures, are committed to the gh-pages branch of the repository.
When pushed to GitHub, the HTML files are automatically served online.

The template's maintainers usually merge changes to the lesson template into the downstream repositories,
but the lesson maintainers can also do this.
For example,
the commands below pull changes from [lesson-template][] into [r-novice-inflammation][]:

    git clone git@github.com:swcarpentry/r-novice-inflammation.git
    cd r-novice-inflammation/
    git remote add template git@github.com:swcarpentry/lesson-template.git
    git pull template gh-pages
    git push origin gh-pages

## They're All Special Cases

The R lessons are the only ones that still contain executable code---the Python and SQL lessons
switched from the Jupyter Notebook to plain Markdown
because the former's JSON format made merges complicated.
Support for R Markdown files is included in the [lesson-template][]:
the [Makefile][] converts files with the `Rmd` file extension to `md` using `knit` from the [knitr][] package.
(We do not need to use `render` from the [rmarkdown][] package because the pandoc formatting is already done by the template.)

Furthermore,
there is a file called [chunk-options.R][] in the subdirectory `tools/` that:

1.  Sends all output figures to the directory `fig/`.

2.  formats the code and output chunks so that they conform to the lesson template
    (check out one of the Markdown files in [r-novice-inflammation][] to see what this looks like). 

This is why all the Rmd files start with the chunk shown below to load this file.
Also note that this chunk overrides the default `fig.path`:
in addition to writing to `fig`,
we add the basename of the file
to make managing the figures much easier.
Some of these details are documented in a section called [Writing lessons with R Markdown][layout-rmd].

    # Code at the beginning of each lesson. We use chunk option `include = FALSE` to
    # hide this from the rendered file.
    source("tools/chunk-options.R")
    opts_chunk$set(fig.path = "fig/01-starting-with-data-")

## Current Challenges for the Lesson Template

If you become a maintainer,
you will be added to the mailing list [maintainers][],
which is where discussion and votes happen.
One of your responsibilities will be to help decide on changes to the template.
For example,
we recently voted on [a proposal for making it easier to find and use the setup instructions][setup-proposal],
and are currently voting on [a proposal to manage lesson versioning][versioning-proposal].

On the horizon, we need to decide where challenges and their solutions should go.
When there were only a few challenges per topic,
it made sense to embed them in the same file as the lesson content.
As more exercises have been contributed by trainee instructors,
this has grown unmanageable:
We have discussed having separate files for extra challenges and their solutions,
but have yet to make a decision (see this [thread][challenges-thread]).
We also need to revisit the question of using pandoc for turning Markdown into HTML,
or switching to Jekyll (the tool that GitHub uses):
see this [thread][jekyll-thread] and Issues [issue-279][] and [issue-280][].

A more big picture challenge is the target audience of the SWC lessons.
During the [reorganization][reorg], the goal was to create separate lessons for novice and intermediate learners.
However, only the novice versions of the lessons were developed and appear on the [lessons][] page.
Despite this, instructors wishing to teach intermediate learners have also developed and used these lessons in workshops.
Thus we are back at the original situation, where we have one sets of lessons and two different audiences.
In recognition of this,
we have started working on [a new novice Python lesson][python-novice-gapminder]
(which will hopefully also serve as an example for the instructor training course
of how to design a lesson systematically).

## A Final Thought

Perhaps the toughest part of being a maintainer is monitoring all the different places where important discussions take place.
I currently watch:

*  [r-novice-inflammation][]
*  [r-discuss][]
*  [maintainers][]
*  [discuss][] (it is high volume, so I just skim it)
*  [lesson-template][]
*  [r-novice-gapminder][]

Each one of these has a useful role,
but collectively they are simply too much.
Going forward,
I think the lesson maintainers' biggest task is to find ways to make the flood of information more manageable,
so that more people can play an effective part in curating and improving our content.

[LAYOUT.md]: https://github.com/swcarpentry/lesson-example/blob/gh-pages/LAYOUT.md
[Makefile]: https://github.com/swcarpentry/lesson-template/blob/gh-pages/Makefile
[announced]: http://software-carpentry.org/blog/2014/10/announcing-novice-r-lessons.html
[bc]: https://github.com/swcarpentry/bc
[boot-camps]: https://github.com/swcarpentry/boot-camps
[challenges-thread]: http://lists.software-carpentry.org/pipermail/maintainers/2016-January/000130.html
[chunk-options.R]: https://github.com/swcarpentry/lesson-template/blob/gh-pages/tools/chunk-options.R
[discuss]: http://lists.software-carpentry.org/listinfo/discuss
[discussion]: http://software-carpentry.org/blog/2014/04/novice-r-discussion-summary.html
[dplyr]: https://cran.r-project.org/web/packages/dplyr/index.html
[instructors.md]: https://github.com/swcarpentry/lesson-example/blob/gh-pages/instructors.md
[issue-279]: https://github.com/swcarpentry/lesson-template/issues/279
[issue-280]: https://github.com/swcarpentry/lesson-template/issues/280
[jekyll-thread]: http://lists.software-carpentry.org/pipermail/discuss/2015-June/003118.html
[kitzes2014]: http://software-carpentry.org/blog/2014/03/collaborative-lesson-development.html
[knitr]: http://yihui.name/knitr/
[layout-rmd]: https://github.com/swcarpentry/lesson-example/blob/gh-pages/LAYOUT.md#writing-lessons-with-r-markdown
[lesson-example]: https://github.com/swcarpentry/lesson-example
[lesson-template]: https://github.com/swcarpentry/lesson-template
[lessons]: http://software-carpentry.org/lessons/
[maintainers]: http://lists.software-carpentry.org/listinfo/maintainers
[options]: http://lists.software-carpentry.org/pipermail/r-discuss/2014-March/000001.html
[python-novice-gapminder]: https://github.com/swcarpentry/python-novice-gapminder
[python-novice-inflammation]: https://github.com/swcarpentry/python-novice-inflammation
[r-discuss]: http://lists.software-carpentry.org/listinfo/r-discuss
[r-novice-gapminder]: https://github.com/swcarpentry/r-novice-gapminder
[r-novice-inflammation]: https://github.com/swcarpentry/r-novice-inflammation
[reorg]: http://software-carpentry.org/blog/2013/11/reorganizing.html
[rmarkdown]: http://rmarkdown.rstudio.com/
[setup-proposal]: http://lists.software-carpentry.org/pipermail/maintainers/2016-March/000205.html
[split]: http://software-carpentry.org/blog/2014/09/splitting-the-repo.html
[swcv4]: http://software-carpentry.org/lessons/previous/
[template]: http://software-carpentry.org/blog/2014/10/a-new-template-for-lessons.html
[thw]: http://www.thehackerwithin.org/
[versioning-proposal]: http://lists.software-carpentry.org/pipermail/maintainers/2016-April/000222.html
[wilson2011]: http://software-carpentry.org/blog/2011/12/fork-merge-and-share.html
