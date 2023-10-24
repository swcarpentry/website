---
layout: page
authors: ["Robin Wilson"]
title: "Showing Changes When Teaching"
date: 2016-07-25
time: "00:07:00"
tags: ["Teaching", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

A key - but challenging - part of learning to program is moving from
writing technically-correct code "that works" to writing high-quality
code that is sensibly decomposed into functions,
generically-applicable and generally "good". Indeed, you could say
that this is exactly what Software Carpentry is about - taking you
from someone bodging together a few bits of wood in the shed, to a
skilled carpenter. As well as being challenging to learn, this is also
challenging to teach: how should you show the progression from
"working" to "good" code in a teaching context?

I've been struggling with this recently as part of some small-group
programming teaching I've been doing. Simply showing the "before" and
"after" ends up bombarding the students with too many changes at once:
they can't see how you get from one to the other, so I want some way
to show the development of code over time as things are gradually done
to it (for example, moving this code into a separate function, adding
an extra argument to that function to make it more generic, renaming
these variables and so on). Obviously when teaching face-to-face I can
go through this interactively with the students - but some changes to
real-world code are too large to do live - and students often seem to
find these sorts of discussions a bit overwhelming, and want to refer
back to the changes and reasoning later (or they may want to look at
other examples I've given them). Therefore, I want some way to
annotate these changes to give the explanation (to show why we're
moving that bit of code into a separate function, but not some other
bit of code), but to still show them in context.

Exactly what code should be used for these examples is another
discussion: I've used real-world code from other projects, code I've
written specifically for demonstration, code I've written myself in
the past and sometimes code that the students themselves have written.

So far, I've tried the following approaches for showing these changes
with annotation:

1. Making all of the changes to the code and providing a separate
   document with an ordered list of what I've changed and why.
   (Simple and low-tech, but often difficult for the students to
   visualise each change)

2. The same as above but committing between each entry in the list.
   (Allows them to step through git commits if they want, and to get
   back to how the code was after each individual change - but many of
   the students struggle to do this effectively in git, and it adds a
   huge technological barrier...particularly with Git's 'interesting'
   user-interface)

3. The same as above, but using Github's line comments feature to put
   comments at specific locations in the code.  (Allows annotations at
   specific locations in the code, but rather clunky to step through
   the full diff view of commits in order using Github's UI)

I suspect any solution will involve some sort of version control
system used in some way (although I'm not sure that standard diffs are
quite the best way to represent changes for this particular use-case),
but possibly with a different interface on it.

Is this a problem anyone else has faced in their teaching? Can you
suggest any tools or approaches that might make this easier - for both
the teacher and students?
