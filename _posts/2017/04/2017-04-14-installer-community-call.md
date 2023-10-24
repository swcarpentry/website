---
layout: page
authors: ["Kate Hertweck"]
title: "Software tools for unix shell: Survey and April community call"
date: 2017-04-14
time: "11:00:00"
tags: ["Community","Tools","Teaching", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

The Software Carpentry [Code of Conduct](https://software-carpentry.org/conduct/) includes 
a somewhat tongue-in-cheek reference to nondiscrimination based on "choice of text 
editor." While a choice of software may seem trivial, this particular discussion has led 
to more than one heated exchange among programmers. In fact, the [Discuss list in March](http://lists.software-carpentry.org/pipermail/discuss/2017-March/thread.html) 
was very active concerning issues with the Windows installer, which provides access to the 
nano text editor through Git for Windows (used in both the Software Carpentry Shell and Git 
lessons). That discussion eventually transitioned to consideration of alternative software 
tools we might consider using and moved over to [GitHub](https://github.com/carpentries/conversations/issues/11), 
where you can read more about the opinions and options voiced by participants.

To help us understand what our community thinks about the software we use for teaching the 
shell lesson, we've developed a [short survey](https://goo.gl/forms/wR160moyJmhrxmfr1) to 
gather information. Please share your thoughts! You may find it useful to peruse the summary 
and links below before taking the survey.

The [Community Call for April](http://pad.software-carpentry.org/community-call-2017-04-20) 
will be dedicated to a discussion of software tools used while teaching workshops, 
with a specific focus on the shell lesson. 
Please join us on Thursday, April 20 in either of two sessions to hear about the 
results of the survey and share your thoughts on what tools we should introduce to learners.

The rest of this post includes a quick summary of the discussion regarding the installer. 
We've had increasing reports lately of problems with the installer failing to function as 
expected, especially in relation to nano. Tracy Teal administered a 
[quick survey](https://github.com/carpentries/conversations/issues/11#issuecomment-285793923) 
and found that, despite these issues, folks tend to like the installer. Given that a few 
years have passed since this tool was built by our community to teach workshops, it's 
worth revisiting how we could improve the tools used for the benefit of both instructors 
and learners. The following suggestions have been offered as ways to resolve the 
logistical problems we've been facing lately while teaching shell at workshops. 
While we're specifically discussing software used to teach the shell lesson, we also 
acknowledge that some of these tools could also be used for installation of other software as well.

* [Windows installer](https://github.com/swcarpentry/windows-installer): Modify or update to 
reduce installation problems in workshops. On top of the standard suite of tools provided by 
Git for Windows, the installer ensures learners have access to nano, SQlite, and make, 
with all easily accessible in path (it's worth noting that the latter two tools are only 
used in workshops specifically about them, which have not often been taught in recent past). 
* Create a new custom package that includes nano using:
	* [Git for Windows SDK](https://github.com/git-for-windows/git/wiki/Technical-overview)
	* [MSYS2](http://www.msys2.org): discussion [here](https://github.com/swcarpentry/workshop-template/issues/394)
	* [conda](https://conda.io/docs/): discussion for how it would work in workshops [here](https://github.com/swcarpentry/workshop-template/issues/395)
	* [Cygwin](https://www.cygwin.com): [installation instructions](https://github.com/swcarpentry/workshop-template/pull/391) for workshops, 
with extra discussion [here](https://github.com/swcarpentry/windows-installer/issues/2)
* [Atom](https://atom.io): a stand-alone text editor which would abandon use of nano altogether, 
although this is problematic for workshops focusing on the use of HPC resources

The challenge associated with utilizing particular software tools during our workshops is 
that we must balance multiple (sometimes conflicting) needs on the part of both instructors 
and learners. Some of these considerations that are especially releavant for the shell lesson include:

* Ease of use for learners: Novice programmers should be able to use it without too much 
effort, and it should be able to handle a breadth of activities throughout the workshop.
* Ease of installation: Learners should be able to install the software without much (if any!) 
trouble, and it should work as expected for the duration of the workshop.
* Minimal installation: Some options above allow installation of multiple tools at once, 
which makes getting the workshop set up easier.
* Propensity of learners to continue use: If learners will continue developing their coding 
skills, the tools we show them should be something that will be useful even months after the 
workshop.
* Similarity across platforms: installation of nano is a non-issue for Mac/Linux computers, 
and a basic workaround for a lack of nano on Windows is using notepad (which easily opens 
from the command line in Git for Windows). This means that learners will be using two 
different commands while editing files, which can be confusing for learners and instructors.
* Favored by instructors: Instructors need to be comfortable with the tools they are using 
to teach. If it's not their top choice of software, they should at least be comfortable enough 
to help learners troubleshoot.

If you have other thoughts on this conversation, please take the [survey](https://goo.gl/forms/wR160moyJmhrxmfr1) 
or feel free to comment on the relevant GitHub discussions linked above.
