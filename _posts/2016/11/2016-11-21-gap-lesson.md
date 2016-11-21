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
of these being the EPSRC project EP/M022641 ["CoDiMa (CCP in the area of
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

This naturally led to the idea of establishing a Software Carpentry lesson
on programming with GAP. I started to develop it in 2015 for our
[first training school in Manchester](http://www.codima.ac.uk/school2015/).
I took inspiration from the core Software Carpentry lessons, in particular
from those on UNIX shell, Python and R.

Since I have never been at any of the Software Carpentry workshops before and
had not yet completed instructor training at that point (it is currently in
progress), it was extremely beneficial for me to come as a helper to the first ever
[Software Carpentry workshop in St Andrews](https://lmwake.github.io/2015-06-18-StAndrews/)
in June 2015, and obtain an insight into the Software Carpentry teaching
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

I started from picking up a research-like problem which may nicely expose
all needed techniques and explain the mindset required to deal with it.
A good candidate was the problem of calculating an average order of an element
of the group, which once I've seen being used by Steve Linton to quickly
demonstrate some GAP features to a general scientific audience. I have tried to
expand this problem in my talk in Newcastle in May 2015 (see the blog post
[here](http://www.codima.ac.uk/2015/07/01/average-order-of-group-elements-a-demo-of-test-driven-development-in-gap/),
an thus the choice has been made.

Indeed, the problem of determining an average order of the element of the group
is simple enough to not to distract learners too much from the intended learning
outcomes of the lesson. An undergraduate algebra course is sufficient for its
understanding. Moreover, those not familiar with the group theory still should
be able to follow the lesson just by grasping the idea that there is a
mathematical structure called group, and we need to find an average value of a
certain numerical parameter associated with each of its elements. On the other
hand, those with sufficient theoretical background will hopefully enjoy seeing
how the initial naive implementation is being refined several times during the
lesson, and how theoretical insights are giving much more significant advances
than minor code optimisations or just getting more cores.

The lesson starts with formulating the problem of finding examples of groups
such that the average order of their element is an integer. It first explains
how to work with the GAP command prompt, demonstrates some basic language
constructions and explains how to find necessary information in the GAP help system.
At this point using the command line we establish a rough prototype of the code to
compute an average order of a group, and tried several examples, none of them
yielding an integer.

Next, it discusses that the command line usage is good only for rapid
prototyping, and explains how to create GAP functions, place them into
a file, and read that file into GAP. After that, the initial implementation is
used to create a regression test: GAP runs it by comparing the actual output
with the reference output, and will fail the test in case of any discrepancies.
Testing the code is a topic that usually escapes beginners' attention,
and I am really excited about managing to cover it as a part of the introductory
GAP lesson. I explain the "make it right, than make it fast" paradigm, and
show how to create and run regression tests in GAP after the first naive
implementation is available. To demonstrate test failures, I deliberately mixed
up function names to break the test, and it was a real pleasure when the
audience pointed that out before I even managed to re-run the test and demonstrate
that it failed.

Having the improved and tested implementation, we start systematic search for
finite groups with an integer average order of an element using the
[GAP Small Groups Library](http://www.gap-system.org/Packages/sgl.html) which
contains, among others, all 423 164 062 groups of order at most 2000 except 1024.
At the same time, the lesson introduces modular programming and shows how one
can design a system of functions to perform the search in a way that one could re-use
most of the code and only develop a new function to test a single group to deal
with another search problem. Then the first interesting example
(a group of order 105 such that the average order of its elements is 17) is
discovered! The next obstacle is to check all 56092 groups of order 256, however,
a short theoretical observation shows that we can exclude groups of prime power
order from the search, as they will never have an integer average order of an
element. After modifying the code to skip such orders, the search continues, and
then another example (a group of order 357) is found. Discovering another known
group with this property is left as one of the exercises.

The lesson finishes with explaining how the knowledge about the object can be
stored in it. For example, once the average order of an element of a group is
calculated and stored in the group, it can be next time retrieved at zero cost,
avoiding redundant calculations.

The lesson on GAP can be seen [here](http://alex-konovalov.github.io/gap-lesson/),
and it has been published via Zenodo [here](http://doi.org/10.5281/zenodo.167362).
So far I am only aware that it has been taught twice (by myself) at two annual
[CoDiMa training schools in computational discrete mathematics](http://www.codima.ac.uk/schools/).
What next? I can surely teach it lesson myself, but is it written clearly enough
to be taught by others? Is it possible for the reader to follow it for
self-study? Is there any introductory material missing, or is there an
interest in having more advanced lesson(s) on some other aspects of
the GAP system? If you would like to contribute to its further development,
issues and pull requests to its repository on
[GitHub](https://github.com/alex-konovalov/gap-lesson) are most welcome!
Also, we invite collaborators interested in developing a lesson on
[SageMath](http://www.sagemath.org/): please look at
[this repository](https://github.com/alex-konovalov/sage-lesson) and
add a comment to [this issue](https://github.com/alex-konovalov/sage-lesson/issues/1)
if you’re interested in contributing.
