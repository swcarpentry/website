---
layout: post
authors: ["Alexander Konovalov"]
title: "Programming with GAP"
date: 2016-11-18
time: "15:00:00"
category: ["Lessons"]
---

 Software Carpentry is more than just a set of workshops and lessons. It is
 also a way to develop lessons, one that we have used successfully to create
 a lesson on [Programming with GAP](http://alex-konovalov.github.io/gap-lesson/).

[GAP](http://www.gap-system.org/) is an open source system for discrete
computational algebra. It provides a programming language with the same name;
thousands of functions implementing various algebraic algorithms; and data
libraries containing extensive collections of algebraic objects. GAP
distribution includes its detailed documentation; even more materials on
learning GAP and on using it in teaching a variety of courses are available
on GAP homepage [here](http://www.gap-system.org/Doc/doc.html).

Throughout the history of GAP, its development has been supported by a
number of [grants](http://www.gap-system.org/Contacts/funding.html), one
of these being the EPSRC project EP/M022641 ["CoDiMa (CCP in the area of
Computational Discrete Mathematics"](http://www.codima.ac.uk/). This is
a community-building project centred on [GAP](http://www.gap-system.org/)
and another open source mathematical software system,
[SageMath](http://www.sagemath.org/). CoDiMa activities include [annual training
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
Since I have never been at any of the Software Carpentry workshops before and
had not yet completed instructor training at that point (it is currently in
progress), it was extremely beneficial for me to come as a helper to the first ever
[Software Carpentry workshop in St Andrews](https://lmwake.github.io/2015-06-18-StAndrews/)
in June 2015, and obtain an insight into the Software Carpentry teaching
methodology.

I took inspiration from the core Software Carpentry lessons,
in particular from those on UNIX shell, Python and R.
All of them have a central story which goes through almost every episode.
For the GAP lesson, I have imagined a common situation: a
research student with no prior experience of working with GAP (and perhaps
little or no experience with programming at all) is facing a task to find
a way in the huge library of GAP functions in order to study some research
problem. Along this way, they start to work with GAP command line to explore
algebraic objects interactively; then use the GAP language to write
some simple scripts; then create own functions. More advanced topics
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
[here](http://www.codima.ac.uk/2015/07/01/average-order-of-group-elements-a-demo-of-test-driven-development-in-gap/)),
and thus the choice has been made.

The resulting lesson leads the learner along the path from working in the GAP
command line and exploring algebraic objects interactively to saving the GAP
code into files, creating functions and regression tests, and further to
performing comprehensive search using one of the data libraries supplied with
GAP, and extending the system by adding new attributes. On this path, the
learner will became familiar with basic constructions of the GAP programming
language; ways to find necessary information in the GAP system; and
good design practices to organise GAP code into complex programs
(for a more detailed lesson overview, see my blog post
[here](http://blogs.cs.st-andrews.ac.uk/alexk/2016/11/22/publishing-software-carpentry-lesson-on-gap/)).

Of course, it is not possible to cover everything in a several hours long
course, but it fits really well into the week-long CoDiMa training school like
[this](http://www.codima.ac.uk/school2016/). It prepares the audience to hear
about more advanced topics during the rest of the week: debugging and profiling;
advanced GAP programming; GAP type system; distributed parallel calculations;
examples of some algorithms and their implementations, etc. Also, staying for
the whole week of the school, everyone has plenty of opportunities to ask
further questions to instructors.

What next?
The lesson on GAP can be seen [here](http://alex-konovalov.github.io/gap-lesson/),
and it has been published via Zenodo [here](http://doi.org/10.5281/zenodo.167362).
So far I am only aware that it has been taught twice (by myself) at two annual
[CoDiMa training schools in computational discrete mathematics](http://www.codima.ac.uk/schools/).
I can surely teach it myself, but is it written clearly enough
to be taught by others? Is it possible for the reader to follow it for
self-studying? Is there any introductory material missing, or is there an
interest in having more advanced lesson(s) on some other aspects of
the GAP system? If you would like to contribute to its further development,
issues and pull requests to its repository on
[GitHub](https://github.com/alex-konovalov/gap-lesson) are most welcome!
Also, we invite collaborators interested in developing a lesson on
[SageMath](http://www.sagemath.org/): please look at
[this repository](https://github.com/alex-konovalov/sage-lesson) and
add a comment to [this issue](https://github.com/alex-konovalov/sage-lesson/issues/1)
if you’re interested in contributing.
