---
layout: page
authors: ["Raniere Silva"]
title: "Plans for Windows Installer"
date: 2017-05-04
time: "16:00:00"
tags: ["Community","Tools","Teaching","Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

In March,
we had two email threads on our [discuss mailing list](http://lists.software-carpentry.org/listinfo/discuss)
related to nano on Windows machines
The [first thread](http://lists.software-carpentry.org/pipermail/discuss/2017-March/005085.html)
was about "nano not found",
a bug on our installer that we never managed to trace.
The [second thread](http://lists.software-carpentry.org/pipermail/discuss/2017-March/005140.html)
was about some "misbehaviour" of nano on Windows,
and the suggestion to use [Atom](https://atom.io/) as the default text editor.
The suggestion to use Atom
started a long discussion where instructors described their reasons to use nano
and why Atom is inadequate which lead us to start investigating ways to install nano properly on Windows.
On May 3rd,
Kate Hertweck, Maneesha Sane, Naupaka Zimmerman, Rémi Emonet and I met online
to draft a plan---taking into consideration all of the feedback that was provided in the past month---to solve the problem with nano on Windows.

## Plan

We will work to use [Git for Windows SDK](https://github.com/git-for-windows/git/wiki/Technical-overview)
to compile our own installer that will include
bash, Git, nano, SQLite and make.
In the future we can work to include man pages and Jekyll.

## Acknowledgement

Thanks very much to everyone that contributed with the discussion
on the mailing list, GitHub issues and other places.
We had a great resource for anyone that wanted to investigate
other options for different projects.

## FAQ

1. What Software Carpentry is looking for?

   A novice-friendly **command-line** text editor
   for use (primarily) during the shell and Git episodes of Software Carpentry workshops
   that works across Windows, macOS and Linux distributions.
   The installation of this command-line text editor **must** be
   easy or transparent to install along with the other tools we ask learners to have before showing up.

2. Where can I review the background materials that were considered in the developemnt of this plan?

   - [discuss mailing list](http://lists.software-carpentry.org/listinfo/discuss)
   - [Survey](https://docs.google.com/forms/d/e/1FAIpQLSfKxs0fVJsHF33BojYK3xYsEd2KGe2NA-0j0XczM3ah7CTtGA/viewform)
   - [Best strategies for Windows installation](https://github.com/carpentries/conversations/issues/11)
   - [Add installation instructions for Atom](https://github.com/swcarpentry/workshop-template/issues/390)
   - [Replace Git Bash with Cygwin](https://github.com/swcarpentry/workshop-template/pull/391)
   - [Replace Git Bash with conda](https://github.com/swcarpentry/workshop-template/issues/395)
   - [Replace Git Bash with MSYS2](https://github.com/swcarpentry/workshop-template/issues/394)
   - [Community Call](http://pad.software-carpentry.org/community-call-2017-04-20)

3. Which versions of Windows will the installer support?

   The installer will support Windows 7, Windows 8 and Windows 10.
   The [end of extended support to Windows 7 by Microsoft is January 14, 2020](https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet)
   We don't have data about how many learners are using Windows 7, so
   we believe it would be unfair to not include Windows 7
   at the first release of our installer.

4. Do we have a date where the new installer will be available?

   Not yet. Software Carpentry staff and Steering Committee
   are looking at efficient and sustainable ways to implement the recommendations.

5. No change necessary if you already use your own custom installer or teaching environment?

   If you are already using an installer you've created for your own systems or environment,
   you do not need to make any changes.
