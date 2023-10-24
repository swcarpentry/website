---
layout: page
authors: ["Greg Wilson"]
title: "Complexity vs. Subtlety"
date: 2016-03-05
time: "08:00:00"
tags: ["Opinion", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>
I gave a lightning talk on Software Carpentry for the [OICR](http://oicr.on.ca/) yesterday,
and in discussion afterward,
[Jonathan Dursi](http://www.dursi.ca/) made an observation that I've been thinking about since.
He wondered whether the key difference between commercial software and scientific software
is *complexity* versus *subtlety*.
For example,
the software that manages workplace insurance payouts for the province of Ontario is complex because
it has to handle every regulatory change since the mid-1920s.
None of the its rules and exceptions are intellectually taxing,
but by the time you turn them into a service,
provide a dozen different interfaces for different business roles,
and make the whole thing fault tolerant,
the software is incredibly tangled.

A lot of scientific software is relatively straightforward by comparison,
so long all you look at is the control flow.
It's the specific calculations that are hard:
what differencing scheme or statistical test to use,
what convergence criteria or significance measure to apply,
and so on.
And yes,
there are a lot of fiendishly tricky algorithms in science,
but they're often hidden in libraries built and maintained by specialists
who work and think like software engineers.

All of this brings me back to the issue of [testing]({{site.baseurl}}/blog/2014/10/why-we-dont-teach-testing.html).
(I'll pause a moment to let long-time readers groan, "Oh no, not this again.")
A lot of tools and techniques for testing mainstream software
are really about managing its complexity:
some of the [most](http://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052/)
[useful](http://www.amazon.com/Why-Programs-Fail-Second-Systematic/dp/0123745152/)
books I know about making software *right*
are good precisely because they makes this explicit.
Offhand,
I can't think of any good books about managing subtlety&mdash;about
picking the right calculation to perform
rather than handling badly-formatted input data
and corner cases in control flow.
I suspect this is because subtlety is inherently domain-specific,
which means many fewer people know enough to write about any particular bit.

In response to an early draft of this post,
Jonathan added,
"This distinction is especially important in the early experimental stage of developing a tool:
if something is successful enough and widely applicable enough that it becomes 'hardened' or 'productized' or the like,
then the complexity naturally grows to be robust and to handle a wider range of cases."
This is why I enjoy Software Carpentry so much:
someone always has new insights.
As always,
we'd be grateful for yours.
