---
layout: page
authors: ["Peter Steinbach"]
title: "HPC in a day?"
date: 2017-06-20
time: "06:00:00"
tags: ["Community","Teaching", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

__Preface__

In today's scientific landscape, computational methods or efficient use thereof can be at the heart of the race for new insights, if not at the heart of the race with the academic competition. Learning how to automate tasks from data analysis to data preprocessing as taught by the carpentries provides the technical concepts to enter this race with an advantage. 

If you just graduated a software/data carpentry boot camp and want to go beyond your laptop's capabilities, the next step in academia is typically to approached the data center of your university or alike. There, a user account application has to be filed for the High Performance Computing (HPC) facilities. After some more formalities, storage and computing time is awarded and you can successfully log into the cluster. And then? Then either our carpenter is given a link to the wiki of the local cluster and how to use it. Sometimes there can be a short course on the mechanics of the HPC cluster and how to use tools that are installed on the cluster. That's it and good luck.

Clearly, the details of the last paragraph vary from site to site and may be a bit exagerated. Judging from YouTube, there are a lot of dedicated and highly enthusiastic HPC instructors out there. 
Even so, there is yet a large gap from filing an account on the HPC machine to running an analysis or simulation campaign autonomously and at scale. The reason for this is, that HPC clusters are very complicated installations. Moreover, the trainings in HPC jump very quickly to the nuts and bolts of HPC, i.e. the number of cores, size of CPU caches, batch system intrinsic, optimal communication patterns, what profiler to use etc. As many (if not the majority) of HPC users stem from domain sciences and hardly ever received a formal education in (parallel) programming or modern computer architecture, this situation leaves many users with despair and hopelessness. 

Many of the latter end up 'copy & paste'ing scripts from wikis or arbitrary places and using these snippets in a mechanical fashion. Simply put: the fun disappears very quickly. With fun lost, creativity will be the next victim which can be detrimental to the scientific race mentioned above. 

__[hpc-novice](https://github.com/swcarpentry/hpc-novice)__

So let's change this! Let's bring fun back to HPC (training) for all. For this purpose, [Christina Koch](http://christinalk.github.io/) from the University of Wisconsin-Madison, [Ashwin Srinath](https://github.com/shwina) from Clemson University and myself (Peter Steinbach from [Scionics Computer Innovation GmbH](https://www.scionics.de)) started to come about with a [hpc-novice](https://github.com/swcarpentry/hpc-novice) curriculum that is inspired by the software carpentry spirit and pedagogical methods. Although this set of material is still in it's infancy, the idea behind it can be paraphrased by "Help a carpentry learner to use a cluster of computers to speed up their day-to-day data lifting". Our efforts to brain storm a possible curriculum are currently fixed in [this document](https://docs.google.com/document/d/1WHPdU7_dlFRytuIJE9I3DJKCd_esiF82ZhTHIIyfRN0/edit?usp=sharing). Feel free to dial over and provide comments.

In an attempt to converge on a curriculum based on user feedback and due to the need for local training at our client, the [Max Planck Institute of Molecular Cell Biology and Genetics](https://www.mpi-cbg.de), I went ahead and came up with an one-day HPC course, which I called [hpc-in-a-day](https://psteinb.github.io/hpc-in-a-day/). [People invited me to](https://github.com/swcarpentry/hpc-novice/issues/24#issuecomment-299396469) to report my experiences made there, so I dedicated the remainder of this post to that.

[hpc-in-a-day](https://psteinb.github.io/hpc-in-a-day/) was conceived as a course for our scientists as our (client) institute is becoming more and more cross-disciplinary and hence we have mathematicians, physicists, biologists and engineers that all want to use our HPC infrastructure. As we were about to open our new cluster extension, hardware resources were a bit scarce at the time of the workshop. I started to ask around if I could get support from the AWS cloud team through my data carpentry contacts and some vendors that we work closely together with. But no luck. Surprisingly, our Lenovo re-seller [pro-com](http://www.pro-com.org/) helped us out and put up a temporary cluster of 8 machines just for our workshop. A big thank you them at this point! 

Before going in, I prepared pre-workshop assessments to infer the expertise level of the learners. I asked them mostly questions regarding how familiar they were with the terminal and how familiar they were with programming. To give you a feeling of the crowd, 90% of my participants expressed that they use the terminal at least once a day. 45% of all learners mentioned that they would required "google or a colleague of choice" to infer how much disk space they have left on the computer using the terminal. Along the same line of thought, 90% of the participants claimed that they program at least once a day. So I thought I was well prepared and went ahead composing the material. 

The contents were set up in the following way:

1. Two sessions about advanced shell methods ([ssh/scp](https://psteinb.github.io/hpc-in-a-day/01-01-taking-the-space-shuttle/) and [file system recap](https://psteinb.github.io/hpc-in-a-day/01-02-filesystems/))
2. Two sessions on how to submit jobs to the cluster ([scheduler basics](https://psteinb.github.io/hpc-in-a-day/02-01-batch-systems-101/), [submit scripts](https://psteinb.github.io/hpc-in-a-day/02-02-advanced-job-scheduling/))
3. One session on using the [shared file system](https://psteinb.github.io/hpc-in-a-day/02-03-shared-filesystem/)
4. Three sessions on the basics of parallel programming with python (from [serial implementation, to a shared memory parallel one](https://psteinb.github.io/hpc-in-a-day/03-01-parallel-estimate-of-pi/) and a [distributed one](https://psteinb.github.io/hpc-in-a-day/03-02-mpi-for-pi/))
5. One session on [using the scheduler for high-throughput computing](https://psteinb.github.io/hpc-in-a-day/03-03-mapreduce-for-pi/)

__What went wrong?__

First of all, I had to learn the hard way that lime survey also records incomplete surveys. It turns out that 2 of my learners didn't complete the survey and those were the ones with rarely any expertise in using the terminal. Me, as the instructor, I need to be more careful with this. Not only did this produce a bi-modal distribution of prior expertise in programming among the participants, but it made structuring the course much more difficult as the majority of learners were able to work with the terminal. 

Second of all, when you are an experienced HPC user and half-time admin, you simply stop seeing the obstacles - many things like file system mechanics are simply done by your fingers and not by your mind anymore. This made my time estimates very inaccurate and tempted me to ditch large parts of some lessons. Judging from this, a 1.5 or even 2 day workshop would be better. A quote from the feedback:

> Course was very intensive (or just too fast) for unexpirienst user. Very fast in the beggining with all the ssh connection, without explanation what is it and how to work with it.

Last but not least, it became apparent in the feedback round ([learner 1](https://github.com/psteinb/hpc-in-a-day/issues/9), [learner 2](https://github.com/psteinb/hpc-in-a-day/issues/10), [learner 3](https://github.com/psteinb/hpc-in-a-day/issues/11), [learner 4](https://github.com/psteinb/hpc-in-a-day/issues/12), [learner 5](https://github.com/psteinb/hpc-in-a-day/issues/13), [learner 6](https://github.com/psteinb/hpc-in-a-day/issues/14) and [learner 7](https://github.com/psteinb/hpc-in-a-day/issues/15)) that some of the terms which I used to relate the parallel execution of a program (think "threads on cores") where not mentioned at all in source code. Apparently, this mental mapping was missing and so one learner even said: 

> I’ve also missed examples of how to run programs that already have a --threads option in the cluster. 

even though I covered this type of parallelization in detail. That said I wondered, [if python is really the best language to teach parallel programming?](https://github.com/psteinb/hpc-in-a-day/issues/17)

__What went well?__

In the post-workshop assessment, participants were asked to indicate if they would recommend the course to others, where a score of 5 refers to very strong agreement and 0 no agreement. The feedback from my learners averaged to a score of 4.5 out of 5! A quote from the feedback:

> Otherwise, great course. Thanks for having me.

During the course, I saw that many people just immediately grasped the content that I was trying to convey. Many people immediately asked how to automate job submission, how to profile their Fortran or C++ application, how to automate the optimal parameter set for submitting their jobs and much more. You could tell that some of these questions grew out of their day job use of HPC clusters. 

Also, I was personally happy to see that people enjoyed parallel programming as much. I chose the Monte Carlo style estimation of Pi using 2 arrays of pseudo-random numbers as the underlying algorithmic problem to solve. I had the impression that people could grasp this rather easily - something I was not clear about beforehand.

__Summary__

To put up a carpentry inspired HPC course, some things became evident (again): my hpc-in-a-day curriculum should be split into 2 lessons (`hpc-novice` and `hpc-parallel`) to target people that just want to get their job done on the cluster (`hpc-novice`) and those that need to go further (`hpc-parallel`). 

A much more clear communication of the expected expertise of the learners is essential. Good teaching of parallel programming and processing can be done before any deep hardware details enter the stage, which is where I see the biggest selling point for this curriculum. Working in HPC for years and using these machines should not lead us to believe that we fit to teach it. We should therefor reduce the material to concepts first.

Further, some HPC centers and even one vendors already asked me if and how hpc-in-a-day will live on and if there will be other implementations of it. I personally would love to continue working with Christina and Ashwin as well as any other volunteers out there to do this and potentially bring HPC back home into the Carpentries. There already was one adaptation of hpc-in-a-day [by Andrea Zonca](https://github.com/swcarpentry/hpc-novice/issues/24#issuecomment-305582614).

