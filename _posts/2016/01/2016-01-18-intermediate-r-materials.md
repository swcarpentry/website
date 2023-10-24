---
layout: page
authors: ["Scott Ritchie"]
title: "Presenting Materials for Intermediate UseRs"
date: 2016-01-18
time: "23:00:00"
tags: ["Lessons", "R", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

We've been teaching R workshops for over a year now at the University of
Melbourne, and one thing we've noticed is the disparity in skill level among
workshop attendees. Researchers generally fall into one of two catergories:

1. Absolute novices: those who have heard of R, but have never touched a
   programming language before.

2. Regular users: those who are using R in their research, possibly on a
   regular basis. They can modify scripts, and have a general understanding of
   the language basics, but want to extend their knowledge.

Those who fall into the first category fit the Software Carpentry attendee
archetype. The novice materials work well for them. The latter group typically
find the novice materials too basic, and end up quickly bored and tune out.
However, like the absolute novice they have never encountered programming
concepts, and have never written their own function, nor understand for loops.

Early last year we recieved a request to run a workshop for a group of
[quantitative ecologists](http://qaeco.com/) at the University of Melbourne.
The organiser, [Saras Windecker](https://twitter.com/smwindecker) had attended a novice workshop
previously, found the material too basic, but had appreciated the best
practices and programming concepts. Together we sat down, and came up with a
rough outline for some of the extension material she thought her group would
find useful, and taught a two day workshop themed "effectively working with
data".  A write up of the workshop can be found [here](http://melbourne.resbaz.edu.au/post/125756026789/unleashing-the-power-of-r)

Since then, we've typed up our notes from the workshop into the Software
Carpentry lesson format, and can now present you with [intermediate materials
for regular useRs](http://resbaz.github.io/r-intermediate-gapminder/)

Just like the novice materials, the lesson spends a lot of time covering the
staple programming concepts taught by Software Carpentry:

 - functions
 - control flow
 - looping
 - code organisation
 - best practices

At a faster pace, we also expose attendees to more advanced concepts and R
specific material that gets missed out in novice lessons:

 - The `apply` family of functions.
 - Effective data manipulation using `data.table` and `reshape2`.
 - How to solve "split-apply-combine" problems with `data.table` and `plyr`.
 - Solving embarrassingly parallel problems with parallel `foreach` loops.
 - Reproducible documents with `R markdown`.

We hope that the community finds these materials useful and look forward to
hearing about intermediate and advanced R workshops in the future!
