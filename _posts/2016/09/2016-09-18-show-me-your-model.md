---
layout: page
authors: ["Greg Wilson"]
title: "Show Me Your Model"
date: 2016-09-18
time: "00:08:00"
tags: ["Opinion", "Research", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

As far as I can tell,
there are no published studies showing that version control is better than mailing files around
or sticking them in shared drives.
I believe it is–I wouldn't work on a project that didn't use version control–but
nobody's ever gathered data,
compared it to a model,
and published the result.

One reason,
I think,
is that we don't know how to measure the productivity of programmers.
"Lines of code per hour" clearly isn't right:
good programmers often write *less* code,
or spend their time on the parts of problems
that have the highest thinking-to-coding ratio.
Without some operationalization of "better" and "worse",
it's hard to rank or compare alternatives.

This problem came up again when [I tweeted](https://twitter.com/gvwilson/status/776733301419630592),
"If anyone has data showing Excel is *more* error-prone than MATLAB/Python/R once you normalize for hours spent learning it, plz post."
It's clear from the responses that most people on Twitter believe this,
but I'm not really sure what "this" is:

1.  *There are more errors in published results created with Excel than in results created with scripting languages like MATLAB, Python, and R.*
    OK,
    but given that many more people use Excel,
    that's like saying that people in China have more heart attacks than people in Luxembourg.

2.  *Results calculated with Excel are more likely to be wrong than results calculated with scripting languages.*
    This is what I had in mind when I tweeted,
    and I don't think the answer is obvious.
    Yes, there are lots of examples of people botching spreadsheets,
    but there's also a lot of buggy code out there.
    (Flon's Axiom states, "There is not now, nor has there ever been,
    nor will there ever be,
    any programming language in which it is the least bit difficult to write bad code.")

    And even if this claim is true, correlation isn't causation.
    I think that people who do stats programmatically
    have probably invested more time in mastering their tools
    than people who use spreadsheets.
    The (hypothesized) differences in error rates could easily be due to
    differences in time spent in reflective practice.

3.  *People who are equally proficient in Excel and scripting langauges are more likely to make mistakes in Excel.*
    This formulation corrects the flaw identified above,
    but is nonsensical,
    since the only meaningful definition of "equally proficient" is
    "use equally well".

4.  *Spreadsheets are intrinsically more error-prone than scripting languages because they don't show errors as clearly, they're harder to test, it's harder to figure out what calculations are actualy being done, or they themselves are buggier than scripting languages' math libraries.*
    These are all plausible,
    but may all be red herrings.
    Yes,
    it's hard to write unit tests for spreadsheets,
    but it's possible:
    Felienne Hermans found that 8% of spreadsheets included tests like
    `if(A1<>5, "ERROR", "OK")`.
    I'd be surprised if more than 8% of people who do statistics in Python or R
    regularly write unit tests for their scripts,
    so the fact that they *could* is irrelevant.

To be clear,
I'm not defending or recommending spreadsheets.
But if programming really is a better way to do science than using spreadsheets,
surely we ought to be able to use science to prove it
and to figure out *why*.

What I'm *really* hoping is that if we figure out how to answer an "obvious" question like this,
we will then have the tools we need to tackle harder ones.
Was the switch to Python3 worth making?
Will Julia be better *enough* than the languages we're using now
to justify the hundreds or thousands of programmer-years it will take
to build a comparable ecosystem?
What about requiring people to do code reviews when they review papers–is that
a better place for them to spend their time than having them pair-program
as they're developing their own code?
We make decisions like this all the time,
but victory seems to go to the loud and the lucky more often than to the righteous.

Leslie Lamport once said,
"Writing is nature's way of letting you know how sloppy your thinking is."
Experimental design has the same effect:
it forces you to clarify what questions you're asking and how you're answering them.
So instead of asking if anyone has *data* comparing Excel to programming languages,
I should have asked,
"What experiment would you run to decide whether spreadsheets are more or less error prone than programs?"
Answers to *that* would be very welcome.
