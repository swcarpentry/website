---
layout: page
authors: ["Ian Hawke"]
title: "Context when teaching Numerical Methods"
date: 2016-02-11
time: "00:30:00"
tags: ["Teaching", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>
As a director of the [Centre for Doctoral Training in Next Generation Computational Modelling](http://ngcm.soton.ac.uk/) I spend plenty of time thinking about, working with, and particularly teaching Numerical Methods. The [general intro course](https://github.com/IanHawke/NumericalMethods) I give is Maths focussed, has around 100 participants, has about 50 contact hours over 12 weeks, and gets a range of interested students from Maths, Physics and Engineering.

The past two weeks I've been teaching Numerical Methods for the [Centre for Doctoral Training in New and Sustainable Photovoltaics](http://www.cdt-pv.org/). With around a dozen participants, many of whom had minimal theory or coding background, and only 10 hours available, some changes in the teaching were required. Most of these followed Software Carpentry approaches: live coding, Jupyter notebooks, sticky notes, and a set of "authentic" examples to train underpinning principles.

The [course we ended up with](https://github.com/IanHawke/Southampton-PV-NumericalMethods-2016) covered most of the key Numerical Methods topics, but all used a motivating example from Photovoltaics or Solar Cells. The feedback showed that, despite my almost complete lack of knowledge of PV modelling, these examples did provide crucial context that the students found useful and relevant. In combination with live coding we were able to build up some fairly detailed numerical methods, up to coupling PDEs and ODE boundary value problems, all whilst talking about the implications for Photovoltaic modelling.

This very much put me in mind of the Software Carpentry Instructor Training course [I attended in 2014](http://ngcm.soton.ac.uk/blog/2014-10-24/software-carpentry-instructor-training-workshop-tgac.html). Much of the *content* was nearly identical to that on generic lecturer training courses I've been on. But the context, and authentic examples given in the Software Carpentry training, made all the difference in engaging me. Tailoring the material to the interests of the learners (as in [Guzdial's *Learner Centered Design*](https://computinged.wordpress.com/2015/12/23/book-released-learner-centered-design-of-computing-education-research-on-computing-for-everyone/) approach) in my case made a big difference. But I also matched to my strengths as a trainer, to make the "authentic" examples ones I could motivate and be enthusiastic about.

Of course, not all aspects of the course went well - unsurprisingly for a first attempt at delivery. The most consistent piece of feedback was that I typed too fast for people to keep up. This wasn't a huge problem when live coding, which (almost) slowed me down enough. When I made mistakes, live *debugging* was a different problem. Minor typos were straightforward, with the students usually spotting them before me. More complex issues, especially where coding and numerical methods problems combined, I tended to find and fix automatically, sometimes without even fully vocalizing the logic behind the bug and its resolution. More practice at revelling in my own errors is clearly required.
