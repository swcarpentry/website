---
layout: page
authors: ["Ryan Avery", "Kunal Marwaha", "Katie Moore", "Kelly Meehan"]
title: "Two Workshops at NASA DEVELOP (or, Python De-Fanged)"		
date: 2017-07-11
time: "06:00:00"
tags: [ "Debriefs", "Workshops", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

 On 8-9 June, 2017, Katie Moore, Deputy Data Management Team Lead for the [NASA CERES](https://ceres.larc.nasa.gov/) Science Team, and
 Ryan Avery, Geoinformatics Fellow with the [NASA DEVELOP National Program](https://develop.larc.nasa.gov/),
 ran a Self-Organised workshop in Hampton, VA.

 On 12-13 June, 2017, Kunal Marwaha, a software engineer with Palantir, Kelly Meehan, Geoinformatics Fellow with NASA DEVELOP, and Ryan ran another
 Self-Organised workshop in Norton, VA.

 Both workshops focused on building skills in NASA DEVELOP participants, who work on 10-week feasibility projects
 that demonstrate how to apply NASA Earth observations to environmental concerns to enhance
 project partner decision-making. In the process, both partners and participants gain a better understanding
 of NASA's Earth-observing (EO) capabilities and improve their professional and technical capacity to use EO data.
 For Katie, Kelly, and I, these were the first workshops in which we taught entire lessons
 and we found it to be an extremely rewarding experience.

 ## NASA DEVELOP at Langley Workshop

 - Attendees Day 1: 19
 - Attendees Day 2: 15

 At the Hampton workshop, learners came from a variety of academic backgrounds and with a spectrum of skillsets.
 The majority of learners fell within environmental or planetary sciences, but we also had
 undergraduate and graduate students attending who were studying mathematics, chemical engineering,
 economics, physics, and social sciences. Because of the types of programs written for DEVELOP
 research projects, we opted to focus on covering programming fundamentals, leaving out most of
 the UNIX shell lesson after the working with directories section.

 For Python, we incorporated the Gapminder Variables and Assignment and Libraries lessons into the Inflammation lessons, which was a success. We also
 covered the Gapminder Plotting lesson, which ended up being a little redundant. The Git lesson excited and
 motivated most participants but also left some participants wondering when or if they would ever use Git. In our
 next workshop in Norton, VA, we changed our delivery of these lessons to include more hands-on examples. For most
 learners, the pace of the workshop was spot on, with a handful of respondents saying the pace was either too slow or too fast.

 There were some technical issues with being able to open the Python interpreter from Git Bash.
 We solved this problem pretty quickly by creating a `.bashrc` file to point the Python command to the `python.exe`
 executable file. Instructions to do this have been documented on the [Configuration Problems](https://github.com/swcarpentry/workshop-template/wiki/Configuration-Problems-and-Solutions)
 page.

 Another big lesson from this workshop was not to hold intensive two-day workshops during the orientation
 week of our program, when participants are tired out from getting accustomed to a new job.
 There was some drop off in attendance on the second day, however, overall feedback and survey
 responses were positive and most learners reported feeling more motivated and less intimidated by the UNIX Shell, Python, and Git.

## Some of the feedback we got:

 **Good**

 -	The sticky notes help system worked well and was a good idea
 -	The pace, the instructors, and the content that was [provided] were fantastic. Thank you again.
 -	Thank you Ryan and Katie! That was very helpful and very informative.

 **Improve**

 - I would have loved a couple extra days to learn R, more bash, and sql!
 - None that I can think of right now

## NASA DEVELOP at Wise Workshop

- Attendees Day 1: 9
- Attendees Day 2: 9

The audience was very engaged and committed to staying the full length of the workshop. It included a high school teacher and student from John I. Burton High School (where we hosted the workshop) and the 7 participants of the NASA DEVELOP program at Wise. The NASA participants had already met a week prior, so there was existing camaraderie that made the workshop less formal and more welcoming. Furthermore, this workshop began after a weekend, with participants fresh and ready to tackle new challenges.

The audience was new to programming but were proficient at typing and navigating their computer via a GUI, which made this workshop a lot easier to teach. Three instructors for nine learners also made a huge difference, for example, one participant was slightly behind for most of the first Python lesson, but was able to catch up each time with one-on-one help from an instructor.

Some changes we made between this workshop after learning from the one at Hampton - we decided to not teach plotting from the Gapminder tutorial since we had already covered this in Inflammation. We also decided to provide more challenge exercises to give more hands-on experience and less "lecture" time. Folks were really excited by a few hands-on tutorials; there were several moments where the room was full of "oohs" and cheering.

A couple of highlights included:

After teaching Git, we pointed people to the Github repository for [pianobar](https://github.com/PromyLOPh/pianobar), a program to run Pandora from your command line. [Find the binaries here](https://github.com/thedmd/pianobar-windows-binaries). Learners cloned the appropriate repository (or `brew installed` it), and were able to connect their Pandora accounts and use the command line to create stations and play music. This was a good tie-in with versioning and collaboration and got the learners excited about the world of open source programming.

In the final hour, we ran a couple of exercises at the end:

1.	Write a function that takes in a number (1-12) and runs the plots for the associated `inflammation-xx.csv` file. This tied together relevant concepts including `if` statements, chained functions, and data types. It also showed learners that there are often multiple ways to accomplish a task when programming.

2.	Use `vi` to write a simple questionnaire using python's `input()` function, so that it would interactively ask for your name and how you're doing and then provide a response which uses your answer. Learners came up with other questions and wrote humorous questionnaires. We wrapped up with learners trying each other's programs and had lots of fun!

Feedback was overwhelming positive, with 8/8 respondents to the post-workshop survey identifying as promoters.

## Some of the feedback we got:

**Good**

- Learned Python!!!
- Learned how to use the terminal. I've used it before but never understood what I was doing and probably couldn't have done anything useful with it before the workshop.
- Liked Rodeo & I think it'll be useful in my DEVELOP project & my other research project.
- Instructors were really good & easy to follow. I was scared of coding before but not anymore so THANKS!
- I liked learning about the various applications & uses of Python.
- Awesome how it was step-by-step.
- I knew nothing about coding, but it was explained very well.
- Apply[ing] the coding... to actual problems was cool to see.
- The information was easy to understand.
- I liked the challenges after the lessons. I also liked hearing how the things we learned apply to real world applications.
- Ya'll made coding fun for someone who has had no previous experience.
- Willing to help when we are stuck.
- EVERYTHING! Very useful & learnt A LOT especially Python.
- Learning the basics, plotting, functions, etc is very helpful in school & at work.
- I feel like I removed the fangs of the Python in this workshop and now it can't bite me anymore. Before I was scared of it. OK maybe a bad pun.
- Intense course in 2 days but learning was steep.

**Improve**

- With more time it would be nice to go over indexing and how computers read rasters.
- More explanation on Python basics.
- Possibly slow down the Python coding section.
- This workshop was not long enough for the information given.
- Possibly tailor to specific projects.
- Include more exercises.
- I want more than 2 days of Software Carpentry. I want to learn more.
- Maybe just slow down explaining some parts.
- Maybe break down exactly how these programs could work with our specific projects.
