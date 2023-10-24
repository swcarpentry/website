---
layout: page
authors: ["Greg Wilson"]
title: "Close Cousins"
date: 2016-10-30
time: "07:00:00"
tags: ["Community", "Programming Historian", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

Our process for developing and maintaining lessons has grown and changed over time.
Simultaneously but separately,
an organization called [the Programming Historian](http://programminghistorian.org)
has crafted a diverse set of open, reusable lessons
on computing skills for people working in the digital humanities (DH),
and [their process](http://programminghistorian.org/contribute)
is different from ours in some interesting ways.

The main elements of our approach are:

1.  A first version is created by:
    *   someone writing something on their own (or translating something they've written before),
    *   a group of people getting together at a hackathon to create a roadmap, or
    *   someone driving an open design process of the kind used for
        [our new Python lesson](http://swcarpentry.github.io/python-novice-gapminder/)
	or
	[Zack Brym's new visualization lesson](http://swcarpentry.github.io/visualization-novice/).
2.  The lesson is put in a GitHub repository.
    Everyone is invited to submit enhancements and changes by filing issues and/or submitting pull requests,
    and to comment on other people's submissions.
    This is a doubly-open process:
    both the submissions and the reviews are tied to the GitHub usernames of their creators,
    which in turn are usually tied to their actual identities.
3.  One or two people act as the lesson's maintainers
    (a term we borrowed from open source software projects).
    Their role is primarily editorial:
    they either review PRs themselves or make sure that other people review them,
    and have final say over whether changes are merged or not.
4.  We publish our lessons twice a year by tidying them up
    and then archiving them at [Zenodo](http://zenodo.org),
    which gives each of them a DOI.
    Everyone whose work has been merged into the lesson is listed as a contributor,
    and the maintainers are listed as editors
    (because that's a role everyone in academia understands).

The strengths of this approach are that the community maintains the lessons
(we've had about 400 distinct contributors in the past three years),
while the editor-vs-contributor distinction allows us
to recognize people who are doing extra work.
Its weaknesses are that big changes are more difficult to make
than they would be if there was a single author,
and there's no incentive for people to do reviews:
someone's name doesn't show up in the bibliographic record for a lesson
if "all" they did was craft hundreds of lines of thoughtful feedback.

In contrast, the Programming Historian's model is:

1.  A would-be author submits a proposal for a lesson,
    which is reviewed by two assigned reviewers
    as well as the general public.
2.  If the lesson receives a green light,
    the author writes it (using PH's template)
    and submits it for peer review.
3.  The lesson is then reviewed as if it were a research publication.
    The review is doubly open,
    but only the original author (or less commonly, authors) make fixes in response.
4.  Once the lesson is done,
    it is published on the PH website.
    It is also published in the more traditional academic sense:
    the Programming Historian has status as an online journal,
    so their lessons are indexed in the usual scholarly way.

The strengths of this approach are the review process
and the fact that authors get credit in a way that academia finds digestible.
Its main weakness is maintenance:
while people may submit errata or make other comments,
lessons continue to be maintained by their original creators,
which can be problematic as other demands on their time grow,
or as platforms and APIs change beneath the lesson's feet.

Could we hybridize these approaches to create something with the strengths of both?
Could the Programming Historian start accepting updates via pull requests
and adding people whose changes have been accepted
to the lesson's byline?
And could we start using a more formal review process,
either as lessons are being designed
or when major changes are proposed?
And in parallel,
what should we both do about giving people credit for their work?
Someone who writes thoughtful, detailed reviews of a lesson deserves to be recognized,
but how should we count and weight that?
Lots of groups are exploring exactly this question with regard to academic publications, software, and data;
which of their answers could and should we borrow?

If you're interested in discussing this,
please add your thoughts to [this GitHub issue](https://github.com/programminghistorian/jekyll/issues/304)
some time in the coming weeks.
