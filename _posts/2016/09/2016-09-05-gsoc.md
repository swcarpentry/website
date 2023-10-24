---
layout: page
authors: ["Raniere Silva"]
title: "Google Summer of Code 2016 ended"
date: 2016-09-05
time: "10:00:00"
tags: ["Community", "Google Summer of Code", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

As announced in April,
we had some Google Summer of Code Students working with us this year.

## Manage workflow for Software Carpentry and Data Carpentry instructor training

Chris Medrela, under the mentoring of Greg Wilson and Piotr Banaszkiewicz,
[worked](https://chrismedrela.github.io/end-of-gsoc)
on [AMY](https://github.com/swcarpentry/amy) implementing
instructor training workflow that is already in use
as we [reopened instructor trining](http://software-carpentry.org/blog/2016/07/reopening-instructor-training.html).

## Result-aggregation server for the installation-test scripts for Software Carpentry and Data Carpentry

Prerit Garg, under the mentoring of Piotr Banaszkiewicz and Raniere Silva,
[worked](http://prerit2010.github.io/GSoC-Project-Front-end-tests-and-updates)
on a [web server](https://github.com/swcarpentry/installation-testing-results-server)
that receive and store information provided by
[the installation script](https://github.com/swcarpentry/installation-testing-scripts).

## Other projects under NumFOCUS umbrella

This year our projects were under NumFOCUS umbrella.
We thanks NumFOCUS for their support
and we want to highlight their other Google Summer of Code projects.

### Dynamic Topic Models for Gensim

Bhargav Srinivasa, under the mentoring of Lev Konstantinovskiy, Radim Rehurek and Devasena Inupakutika,
[worked](https://topicmodel2016.wordpress.com/2016/08/21/gsoc-final-submission/)
on [Gensim](https://topicmodel2016.wordpress.com/2016/08/21/gsoc-final-submission/)
that now supports [Dynamic Topic Model](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/ldaseqmodel.ipynb).

### Upgrade to datapackage.json standard for EcoData Retriever

Akash Goel, under the mentoring of Henry Senyondo and Ethan White,
[worked](https://goelakash.wordpress.com/2016/08/21/gsoc-blog-wrap-up/)
on [EcoData Retriever](https://github.com/weecology/retriever)
that now is compatible with [Datapackage.JSON standard](http://specs.frictionlessdata.io/data-packages/)
when [saving the scripts](http://retriever.readthedocs.io/en/latest/scripts.html)
that retrieved the data requested by the user.
Also, now EcoData Retriever works with Python 3.

### Improving the state of Optim.jl for JuliaOpt

Patrick Kofod Mogensen, under the mentoring of Miles Lubin,
[worked](https://pkofod.github.io/2016/08/31/gsocfinal/)
on [JuliaOpt](http://juliaopt.org/)
that now has a faster implementation of Simulated Annealing solver.
Also, now JuliaOpt's documentation includes tons of examples.

## Presolve Routines for LP and SDP within Convex.jl for JuliaOpt

Ramchandran Muthukumar, under the mentoring of Madeleine Udell,
[worked](http://ramcha24.github.io/gsoc.html)
on [JuliaOpt](http://www.juliaopt.org/) [MathProgBase](https://github.com/JuliaOpt/MathProgBase.jl)
that provides high-level one-shot functions for linear and mixed-integer programming. Ramchandran's work focus on the presolving the linear and mixed-integer programming problems, a important step to improve benchmarks.

### Categorical Axis for matplotlib

Hannah Aizenman, under the mentoring of Michael Droettboom and Thomas Caswell,
[worked](http://story645.github.io/jekyll/update/2016/08/22/color.html)
on [matplotlib](http://matplotlib.org/)
to reduce the code that users need to write when working with [categorical data](http://pandas.pydata.org/pandas-docs/stable/categorical.html).
