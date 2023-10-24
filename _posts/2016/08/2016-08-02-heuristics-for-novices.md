---
layout: page
authors: ["Greg Wilson"]
title: "Heuristic Evaluation for Novice Programming Systems"
date: 2016-08-02
time: "00:01:00"
tags: ["Lessons", "Research", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

I have recently been reading and enjoying
a new paper by Michael Kölling and Fraser McKay titled
"[Heuristic Evaluation for Novice Programming Systems](https://kar.kent.ac.uk/55885/1/kolling-heuristics-submitted.pdf)".
In it,
the authors say:

> With the proliferation of competing systems [for novices], the problem [of evaluation ] has become more complicated.
> Not only should we ask the question whether such kinds of tools are helpful at all
> (which many instructors strongly believe them to be, even in the absence of hard evidence),
> but we need to decide which of a significant number of competing systems is "better" for a given task in a given context.
> Educators have to make choices, not only between using an educational IDE or not, but between a number of direct competitors.
>
> Studies evaluating the actual learning benefit of the use of a specific system are rare.
> This is not for lack of interest or realisation of the usefulness of such studies,
> but because they are difficult to conduct with a high degree of scientific reliability...
> Running two groups (experiment group and control group)
> in parallel is usually difficult to resource:
> the teacher almost doubles the workload and has to avoid bias.
> It also introduces an ethical problem:
> If we expect one variant to be superior, and the setting is an actual examined part of a student's education,
> then we would knowingly disadvantage a group of students.
> However, if we run the two trials sequentially,
> it becomes very difficult to compensate for possible other factors influencing the outcome,
> such as difference in teachers or populations.

They then propose 13 heuristic criteria by which programming systems presented to novices can be evaluated:

1. **Engagement**:
   The system should engage and motivate the intended audience of learners.
   It should stimulate learners' interest or sense of fun.
1. **Non-threatening**:
   The system should not appear threatening in its appearance or behaviour.
   Users should feel safe in the knowledge that they can experiment without breaking the system, or losing data.
1. **Minimal language redundancy**:
   The programming language should minimise redundancy in its language constructs and libraries.
1. **Learner-appropriate abstractions**:
   The system should use abstractions that are at the appropriate level for the learner and task.
   Abstractions should be driven by pedagogy, not by the underlying machine.
1. **Consistency**:
   The model, language and interface presentation should be consistent – internally, and with each other.
   Concepts used in the programming model should be represented in the system interface consistently.
1. **Visibility**:
   The user should always be aware of system status and progress.
   It should be simple to navigate to parts of the system displaying other relevant data, such as other parts of a program under development.
1. **Secondary notations**:
   The system should automatically provide secondary notations where this is helpful,
   and users should be allowed to add their own secondary notations where practical.
1. **Clarity**:
   The presentation should maintain simplicity and clarity, avoiding visual distractions.
   This applies to the programming language and to other interface elements of the environment.
1. **Human-centric syntax**:
   The program notation should use human-centric syntax.
   Syntactic elements should be easily readable, avoiding terminology obscure to the target audience.
1. **Edit-order freedom**:
   The interface should allow the user freedom in the order they choose to work.
   Users should be able to leave tasks partially finished, and come back to them later.
1. **Minimal viscosity**:
   The system should minimise viscosity in program entry and manipulation.
   Making common changes to program text should be as easy as possible.
1. **Error-avoidance**:
   Preference should be given to preventing errors over reporting them.
   If the system can prevent, or work around an error, it should.
1. **Feedback**:
   The system should provide timely and constructive feedback.
   The feedback should indicate the source of a problem and offer solutions.

The full explanation of each criterion runs to half a page or more,
and includes references to the research literature to clarify and justify it.
As I read through these,
a few things struck me:

1. Most of the tools we teach in Software Carpentry score very poorly
   on these criteria.
   The Unix shell and Git, for example,
   are not engaging,
   are definitely threatening
   (in the sense that users quite reasonably fear the consequences of making a mistake),
   do not present level-appropriate abstractions or make system status clearly visible,
   (definitely) do not have human-centric syntax,
   and so on.
   (They do well, however, on edit-order freedom:
   both tools encourage tinkering
   and allow users to leave tasks partially finished
   and return to them later.

2. On the other hand,
   Excel and OpenRefine score quite well:
   they're engaging,
   there's little redundancy,
   they present tabular data as tables
   (which programming languages could have started doing thirty years ago---but
   that's a rant I'll save for some other time),
   they make system status very visible,
   support edit-order freedom,
   and so on.

3. Together,
   #1 and #2 make me think that there should be another couple of heuristics:
   authenticity (i.e., do practitioners use it in their daily work)
   and upper bound (i.e., how far can you go with the tool before you have to switch to something else).
   Git and the Unix shell score highly on both,
   as does OpenRefine,
   but Excel does less well.
   Tools like [Scratch](https://scratch.mit.edu/) come up short on both counts:
   while it's a wonderful way to teach programming to newcomers of all ages,
   most people quickly outgrow it.

4. Having invented two more heuristics, though,
   I can't help but wonder whether doing so is actually rationalization.
   I've said many times that if you can't win, you should change the rules:
   it's entirely possible that if (for example) Git had scored highly on Kölling and McKay's heuristics,
   I wouldn't have thought to suggest others.

5. It's interesting to compare [RStudio](https://www.rstudio.com/home/)
   and the [Jupyter Notebook](http://jupyter.org/) using these heuristics.
   In both cases,
   I think that when they do poorly it's because they are containers for
   a purely-textual programming language:
   for example,
   neither does particularly well on the "human-centric syntax" heuristic,
   but that's not their fault.
   I think RStudio does better than the Notebook overall,
   primarily because of its interactive debugger and continuous redisplay of the state of the workspace.

One final thought:
it would be really interesting to have a similar set of heuristics for evaluating lessons.
Some criteria would transfer directly (e.g., engagement, being non-threatening),
but others are thought-provoking:
what's are the equivalents of error avoidance and edit-order freedom for teaching materials?
If anyone knows of a rubric like this,
I'd be grateful for a pointer.

See also [this post from Mark Guzdial](https://computinged.wordpress.com/2016/06/20/how-to-choose-programming-languages-for-learners/)
that identifies five principles for selecting a programming language for learners:

1. Connect to what learners know
1. Keep cognitive load low
1. Be honest
1. Be generative and productive
1. Test, don’t trust

---   

Michael Kölling and Fraser McKay: "[Heuristic Evaluation for Novice Programming Systems](https://kar.kent.ac.uk/55885/1/kolling-heuristics-submitted.pdf)". *ACM Transactions on Computing Education*, 16(3), June 2016, 10.1145/2872521.
