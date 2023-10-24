---
layout: page
authors: ["Juliane Schneider"]
title: "Teaching Library Carpentry to Librarians at UCSD"
date: 2016-08-17
time: "00:04:00"
tags: ["Library Carpentry", "Workshops", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

I sort of knew what I was getting into. I'd done the excellent instructor training in February at UC Davis, 
which is a good thing, because I didn't know the first thing about instruction. 
I didn't know the first thing about organizing workshops, either, but I figured what the hell; 
my colleague and partner-in-crime [Tim Dennis](https://twitter.com/jt14den) had reserved the big conference room in our library, 
which is really hard to get. If you're in academia you know the first rule, which is never waste 
a reserved prime conference room. With lots of prompts and help from my colleague Tim Dennis, 
we put together a Library Carpentry workshop at UC San Diego.

Since the instructors were all from the institution (UC San Diego), the host/instructor issue wasn't much of an issue. 

The workshop website was [https://ucsdlib.github.io/2016-07-18-UCSD/](https://ucsdlib.github.io/2016-07-18-UCSD/)

The workshop ran from July 18-22, and because some library staff would be unable to attend the entire workshop, 
I allowed people to register by the day. The schedule ran:

- Day one: Fundamentals/Regex
- Day two: Bash/shell/command line
- Day three: Git/Github
- Day four: Open Refine
- Day five: Office hours

There were 40-50 people on days one and four, and about 30-40 on days two and three. 
We had five or six people come to office hours for help with [Open Refine](http://openrefine.org/) after the workshop. 
I taught the Foundation/Regex and Open Refine, Tim Dennis and Reid Otsuji taught Bash/Shell, 
and Matt Critchlow taught Git/Github. We had at least two helpers per day who were indeed very helpful.

## What We Learned While Preparing

It takes a lot of time to think through what you need as far as room setup, materials, refreshments, and 
publicity. I wish I'd made a list for what we needed each day, 
as requirements differed throughout the week (the first day needed pens and paper, 
for example). You can rarely overestimate the amount of coffee needed when 
librarians and coding meet. Also, savory snacks are a hit, 
although I think someone lost a hand in the scramble for Babybel cheese.

## What We Learned While Instructing

Etherpad, etherpad etherpad! Mention the etherpad! There were a few obstacles to getting our 
attendees to collaboratively note-take. First of all, I think that the fact that our helpers
were taking notes gave them an 'official' air that we didn't mean to give. 
Secondly, especially during the Bash class, people were saying that with the Bash, 
Notepad, browser and etherpad open, it was too much. I think that 
next time, we'll make sure to have a second screen with the etherpad on it, 
so that people can see that others are taking notes and they can reference it 
without having it on their screen if inconvenient.

The helpers shouldn't huddle together in one spot in the room. 
Scatter them around the room so that they spend their time interacting with the students, 
not each other. 

## Audience Things

The audience was very engaged, helping each other and answering questions. 
From some of the comments, though, I think we may have erred on the side of caution in the 
Open Refine lesson by pausing too long to let everyone catch up. Next time, 
I'm going to try to strike a better balance in the speed of the lesson and 
more actively encourage students to help each other (and encourage the practice 
of staying off of peripheral devices and suspension of Pokemon play during the class).

## Particular Things

In the Open Refine session, I am going to try to create some exercises 
in order to break up the demo. I think that three hours of demo is hard for 
an audience to take in even if they're following along in the tool, 
so perhaps creating a second, 'test' dataset that can be used for exercises 
will drive home the concepts while allowing some hands-on expermentation 
and thought processes/co-learner discussion about the tool's context and use once outside the class.

The librarians who made up the workshop participants struggled to find context 
for the Bash/Shell and Git tools in their work. Matt made the excellent 
observation that while librarians are great at using tools, they don't really know how 
or have experience in how to use a computer. I think this lack of experience of 
using computers 'as computers', so to speak, makes it more difficult to understand 
how Bash and Shell can be used in their current tasks.

Git, on the other hand, has the interesting problem of being a tool for collaboration, 
which usually takes two people, or maybe one person and their doppleganger. 
Learning the steps in setting up a repository took so much time that the 
application of the space was not able to be effectively examined.

My thought was that if we taught it again, especially within the library, 
we could find people interested in the setup, and have Matt hold a pre-class 
to set up a repository for each department. Then, in the class proper, 
we could concentrate on the collaborative aspect of Git/Github and then 
let them all work with their department-specific repositories as departments 
in the class. This will emphasize the collaborative uses of the tool and 
perhaps uncover use cases for the various departments.  Of course, this 
would only work with a workshop that was institution-centered.

We'd rounded up a bunch of whiteboards for the classes to use, but we never really incorporated them. 
If, like us, you find yourself unable to get a second screen up for the etherpad, 
encourage the groups of students to use the whiteboards. They can be 
used to work out errors or roadblocks, write down commands, and record ideas 
which can then be transferred to the etherpad. Also, remind students that if they get an error 
message while working with a tool during an exercise or challenge, you can do a 
search for that error message and find solutions which they can then record 
on the etherpad or whiteboard. 

## Giving Back to the Community Things

After the workshop, all of us were inspired to improve current lessons, and create new ones. 
We sat down together the week after the workshop and Matt led us through the approved 
Software Carpentry method of adding materials to the [Library Carpentry repository](https://github.com/data-lessons) via Git. 
Some of the suggested new lessons are R for Librarians and an advanced Open Refine 
class concentrating on using Regex and GREL. We also want to work on the 
Git/Github lesson and the Open Refine lessons that currently exist.

## The Grand and Glorious Conclusion

We had a great time teaching the workshop! There were no brawls, 
nor were we pelted with muffins or laptops, so the students seemed to find it useful, 
which was reinforced by the comments and sticky-note feedback we received. 
We got several inquiries about when we were going to hold another one, 
so ongoing Library Carpentry instruction is something that is definitely a need for UC San Diego.

*Note:* The original Library Carpentry repository created by [Dr James Baker](https://twitter.com/j_w_baker) is [here](https://github.com/LibraryCarpentry). 
Reworked and updated lessons from the recent global sprint are [here](https://github.com/data-lessons). 
They are the lessons prefixed with 'library'.
