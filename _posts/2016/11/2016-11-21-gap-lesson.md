---
layout: post
authors: ["Alexander Konovalov"]
title: "Programming with GAP"
date: 2016-11-18
time: "15:00:00"
category: ["Lessons"]
---

[GAP](http://www.gap-system.org/) is an open source system for discrete
computational algebra. It provides a programming language with the same name;
thousands of functions implementing various algebraic algorithms; and data
libraries containing extensive collections of algebraic objects. GAP
distribution included its detailed documentation, and more materials on
learning GAP and on using it in teaching a variety of courses are available
on GAP homepage [here](http://www.gap-system.org/Doc/doc.html).

Throughout the history of GAP, its development has been supported by a
number of [grants](http://www.gap-system.org/Contacts/funding.html), one
of these being the EPSRC project EP/M022641 []"CoDiMa (CCP in the area of
Computational Discrete Mathematics"](http://www.codima.ac.uk/). This is
a community-building project centred on [GAP](http://www.gap-system.org/)
and another open source mathematical software system,
[SageMath](http://www.sagemath.org/). Its activities include [annual training
schools in computational discrete mathematics](http://www.codima.ac.uk/schools/),
which are primarily intended for PhD students and researchers from UK
institutions. A typical school starts with the Software Carpentry workshop
covering basic concepts and tools, such as working with the command line,
version control and task automation, continued with introductions to GAP
and SageMath systems, and followed by the series of lectures and exercise
classes on a selection of topics in computational discrete mathematics.

This naturally leads to the idea of establishing a Software Carpentry lesson
on programming with GAP. I started to develop it in 2015 for our
[first training school in Manchester](http://www.codima.ac.uk/school2015/).
I took inspiration from the core Software Carpentry lessons, in particular
on UNIX shell, Python and R.

Since I have never been at any of the Software Carpentry workshops before and
had not yet completed instructor training, it was extremely beneficial for me
to come as a helper to the first ever
[Software Carpentry workshop in St Andrews](https://lmwake.github.io/2015-06-18-StAndrews/)
in June 2015 and obtain an insight into the Software Carpentry teaching
methodology.

A good Software Carpentry lesson should have a central story which goes
through almost every its episode. I have imagined a common situation: a
research student with no prior experience of working with GAP (and perhaps
little or no experience with programming at all) is facing a task to find
a way in the huge library of GAP functions in order to study some research
problem. Along this way, they start to work with GAP command line to explore
algebraic objects interactively; then start to use the GAP language to write
some simple scripts; then start to create own functions. More advanced topics
such as, for example, extending GAP with new methods for existing types of
objects, or even new objects, or organising your code in the form of a GAP
package, are not so obvious for the beginners, and I have made an attempt
to create a lesson which will show the direction in which their skills should
be developing, and also to cover the importance of testing their code.

I started from picking up a research-like problem which can be the central
one for the lesson and which may nicely expose all needed techniques and
mindsets. A good candidate was the problem of calculating an average order of
an element of the group, which once I've seen being used by Steve Linton to
quickly demonstrate some GAP features to a general scientific audience.
After I have used it for a talk in Newcastle in May 2015 (see the blog post
[here](http://www.codima.ac.uk/2015/07/01/average-order-of-group-elements-a-demo-of-test-driven-development-in-gap/),
the choice was made.

The problem of determining an average order of the element of the group
is enough simple problem to not to distract learners too much from the
intended learning outcomes of the lesson, and undergraduate course in
algebra is sufficient prerequisite to understanding the lesson. Those
learners who are not familiar with the group theory, should still be able
to follow the lesson just by assuming that there is a mathematical structure
called group, and we need to find an average value of a certain numerical
parameter associated with each of its elements. On the other hand, those
with sufficient theoretical background will hopefully enjoy seeing how the
initial naive implementation is being refined several times during the
lesson, and how theoretical insights are give much more advances than minor
code optimisations or just getting more cores.

One particular topic that usually escapes beginners' attention is testing,
and I am really excited about managing to cover it as a part of the introductory
GAP lesson. I explain the "make it right, than make it fast" paradigm, and
explain how to create and run regression tests in GAP after the first naive
implementation is available. To demonstrate test failures, I deliberately mix
up function names to break the test, and it's a real pleasure when someone
from the audience points it out before I even manage to re-run the test and
show how it fails.

TODO: Describe better how the structure of the lesson looks like
and how the problem of finding the group with an integer average order
of an element fits into every episode:

* First session with GAP - Working with the GAP command line
* Some more GAP objects	- Further examples of immediate and positional objects and operations with them
* Functions in GAP - Functions as a way of code re-use
* Using regression tests - Test-driven development
* Small groups search	- Modular programming: putting functions together. How to check some conjecture for all groups of a given order?
* Attributes and Methods - How to record information in GAP objects

GAP lesson taught twice so far and published on Zenodo
[here](http://doi.org/10.5281/zenodo.167362).
What next? I can teach my lesson myself, but is it written clearly enough
to be taught by others? Is it possible for the reader to follow it for
self-study? Is there any introductory material missing, or is there an
interest in having more advanced lesson(s) on some (which?) aspects of
the system? If you would like to contribute to its further development,
issues and pull requests to its repository on
[GitHub](https://github.com/alex-konovalov/gap-lesson) are most welcome!

We are now starting to develop a
[lesson on SageMath](https://github.com/alex-konovalov/sage-lesson).
We invite collaborators: please watch the repository if you’re
interested in following along, and add a comment to
[this issue](https://github.com/alex-konovalov/sage-lesson/issues/1)
if you’re interested in contributing.
