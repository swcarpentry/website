---
layout: page
authors: ["Greg Wilson"]
title: "Lessons as Lab Protocols"
date: 2016-01-03
time: "03:00:00"
tags: ["Noticed", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

A [roundabout chain of references](http://www.felienne.com/archives/4327)
led me to Abbott et al's "[Programs for People: What We Can Learn from Lab Protocols](http://web.engr.oregonstate.edu/~walkiner/papers/vlhcc15-programs-for-people.pdf)"
(presented at [VL/HCC 2015](https://sites.google.com/site/vlhcc2015/))
which looks at how lab protocols are similar to and different from programs.
On the one hand,
a lab protocol describes the steps to be followed to (for example) prepare a particular kind of sample for analysis.
On the other hand,
"human plans are more like descriptions or predictions
than prescriptions of what actions a person will take given the most likely sequence of future actions;
they are resources for anticipating likely future events.
In programming language terms,
perhaps,
they are more declarative than imperative
in that people draw on knowledge of the whole plan rather than blindly following each step."

Later,
they say that,
"...actors following a protocol have their own 'trajectories',
that is,
their own goals and priorities;
they stray from the protocol to various extents, in various ways, for a variety of reasons."
And later still,
they make a comparison to a particular piece of software many readers will be familiar with:

> Some existing software tools play a similar role to protocols as tailorable process descriptions.
> For example the Bioconductor project uses literate R programs,
> called 'workflows' and 'vignettes',
> to describe how various packages can be marshalled to perform tasks.
> In these programs the data file and task are merely illustrative examples;
> the program does not differ semantically from any other R program,
> but it is meant pragmatically to be used primarily as
> a resource for copy/paste creation of a new program to do a similar task.

The authors' main contribution is to "...analyze peer-reviewed protocols published in *Cold Spring Harbor Protocols*.
Unlike personal or internal protocols,
these represent programs written for people unknown to the author(s) of the program."
Each step is classified according to *kind* (physical, cognitive, measuring, etc.),
*precision* (instruction, goal-directed, taks-directed, etc.),
and *features* (advice, wiggle room, reference, etc.).
One of their findings is that:

> A protocol describes an idealized course of action,
> but the person executing it will frequently deviate from this course by modifying, reordering, adding, or even skipping steps.
> By way of analogy, consider a program or protocol as describing a path.
> In a computer program, the path specified is very narrow, like a tightrope, which the computer follows precisely.
> In a human protocol, the path is much wider,
> and the person following it may wander freely from side to side, stop to smell the flowers, and so on.

This was the point where the light came on for me.
Everything they are saying about lab protocols can be said equally well for [lessons]({{site.baseurl}}/lessons/).
A lesson is one idealized path through particular material;
everyone who actually delivers it will,
as Abbot et al say,
wander from side to side and stop to smell the flowers.
Well-written lab protocols provide for this by explicitly including
advice, constraints, expected outcomes, optionality, wiggle room, and contingencies
to help users broaden the protocol,
narrow it,
or find their way back to the main path if they have wandered away:
in short,
they provide the kind of advice that we have been trying to accumulate in our instructors' guides.

I'd be very interested in hearing what other people think of this analogy,
and whether there are ways we could use it to make our lessons more useful.
As always,
comments on this post are very welcome.
