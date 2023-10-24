---
layout: page
authors: ["Greg Wilson"]
title: "Designing Lessons Collaboratively"
date: 2016-02-15
time: "00:30:00"
issues: "https://github.com/swcarpentry/python-novice-gapminder/issues"
tags: ["Community", "Lessons", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>
A few days ago,
I asked for feedback on a new Python lesson aimed at people who've never programmed before.
The [outline]({{site.github_url}}/python-novice-gapminder/blob/gh-pages/index.md)
had already received several rounds of feedback from a handful of people,
but there were still lots of comments:

*   As always,
    the choice of **tools** attracted a [lot of discussion]({{page.issues}}/15).
    Jeremy Metz opened by saying,
    "I worry that the use of a more abstract environment like the Jupyter Notebook
    might confuse and add an additional barrier to people wanting to 'really' use Python."
    I agree that the Notebook imposes an extra cognitive load,
    since it's so different from anything else novices are likely to have seen,
    but it has become the tool of choice for many scientists for good reasons:
    it's stable, cross-platform, encourages reproducible practices,
    and has a great, supportive community.
    We're also starved for alternatives:
    the audience for this class isn't required to have seen the shell,
    so running scripts from the command line is out,
    and all of the Python IDEs we've tried have significant shortcomings for our audience.

*   **Time estimates** are one of the places where community input matters most.
    In [this issue]({{page.issues}}/9),
    two experienced instructors discuss how far they think learners could get by lunch,
    while [here]({{page.issues}}/19),
    two others talk about whether lots of short exercises will be manageable in practice,
    and whether using the Notebook will help.
    The former was a useful reality check
    (which is my way of saying "I cut some material based on their feedback")
    while we will address the latter by having most exercises be multiple choice questions,
    Parsons Problems,
    and filling in the blanks or tweaking existing code
    rather than writing things from scratch.
    Rayna Harris has also [suggested]({{page.issues}}/25)
    that we use [Socrative](http://www.socrative.com/) quizzes for real-time assessment.
    While I'm a bit nervous about becoming any more dependent on closed-source commercial sites than we already are,
    it's a great tool,
    and we'll definitely explore it.

*   **Potential problems** are another place where having a community makes a big difference.
    [This discussion]({{page.issues}}/20) reminded me that loading data is hard
    if you don't know how to navigate the filesystem;
    we've addressed that by allocating 10 minutes for learners to read their first CSV data set,
    most of which we expect will be taken up with tech support.

*   **Testing** is important
    and coverage of these practical aspects of programming
    is part of what distinguishes SWC from "pure programming" classes,
    but (a) will it be accessible,
    (b) will it be [compelling]({{site.baseurl}}/blog/2014/10/why-we-dont-teach-testing.html),
    and (c) what should we take out to make room for it?
    We could show `assert` and focus on defensive programming rather than testing per se,
    and it's less effort (no separate functions).
    See [this thread]({{page.issues}}/6) for the discussion.

*   **Debugging** is also important.
    I'm a big fan of interactive symbolic debuggers,
    but all the Notebook provides right now is `pdb`,
    which we are *not* showing to novices.
    Instead,
    we have 15 minutes of lesson and discussion on how to make sense of error messages
    (which will draw on [this discussion]({{page.issues}}/22)
    as well as recycling [this material]({{site.github_io_url}}/python-novice-inflammation/07-errors.html))
    and 25 minutes on actual debugging.
    The latter episode is toward the end of the lesson,
    and I suspect that many workshops will drop it because they'll run short of time.

*   **NumPy** was the heart and soul of scientific Python for many years,
    but this lesson will only mention it in passing,
    devoting its attention to Pandas instead.
    It really deserves more air time---as [Bartosz Telenczuk observes]({{page.issues}}/17),
    "students leaving the course without basic familiarity of NumPy
    will not be able to understand ~60% (my rough guess) of scientific Python applications."
    The problem once again is what to cut to make room...

The biggest message for me in this wasn't the specific feedback, though.
It was the way that two dozen people who are familiar with our current content and teaching methods,
and have first-hand experience delivering this material in the classroom,
were willing and able to share what they knew.
That doesn't guarantee that the first draft of the lesson will be perfect,
but it does improve the odds of it being good.

The next step is to figure out how to go about writing the lesson.
Should one or two people assemble a first draft for others to critique?
Or should we start by crowd-sourcing the creation of the exercises
(which I think will parallelize better)?
And if we do the latter,
should we ask instructor trainees who already speak Python to propose exercises
as part of their training?
Comments would be greatly appreciated.
