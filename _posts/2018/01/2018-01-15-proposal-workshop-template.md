---
layout: post
authors: ["Raniere Silva"]
title: "Workshop Template Enhancement Proposal"
date: 2018-01-15
time: "10:00:00"
category: ["Workshops"]
---

Over the couples of years,
many emails and issues on GitHub
requested to move the setup instructions in the workshop page/template to a separate page
for valid reasons.
To provide some reference, see
[swcarpentry/DEPRECATED-bc#415](https://github.com/swcarpentry/DEPRECATED-bc/pull/415),
[swcarpentry/DEPRECATED-bc#729](https://github.com/swcarpentry/DEPRECATED-bc/issues/729),
[swcarpentry/workshop-template#194](https://github.com/swcarpentry/workshop-template/issues/194)
and
[swcarpentry/workshop-template#408](https://github.com/swcarpentry/workshop-template/issues/408).
What we discovered during those years and trials?
Find the balance to accommodate long time and advance instructors, novice or intermediate instructors and learners
is as hard as carry a watermelon with a tea spoon.
So why are we having this discussion again?

Last year,
we change the Workshop Template
by adding some if-clauses so that Software Carpentry, Data Carpentry and Library Carpentry
instructors could share the same template.
In part because minor differences in how Software Carpentry, Data Carpentry and Library Carpentry lessons and workshops are structured,
the if-clauses weren't enough for Data Carpentry and Library Carpentry to use the Workshop Template.
With the plans to create more lessons in the short future
under the umbrella called "The Carpentries",
the urge to move the setup instructions reapear
and we need to nail it.

I put a prototype in place,
see [swcarpentry/workshop-template#459](https://github.com/swcarpentry/workshop-template/pull/459),
that demonstrate how we can require from leader instructor
to only list at the YAML header the lessons that will be used during the workshop
and let some Javascript code to fetch the latest instalation instructions.

The proposal idea has as advantages:

- reduction in the numbers of lines that need to be edit in the workshop page; and
- reduction in the amount of time to propagate some important change, e.g. that learners can't use Firefox Quantum because the SQLite3 add-on isn't compatible.

Some drawbacks will happen:

- one time customizations will require more work, basically to clone a repository to customize the installation instructions;
- instability due client-side Javascript code, it might not work in one year in the future; and
- increase of page load/redering time, I'm talking about much less than 1s.

For this to work,
all lessons will need to improve the Setup page that they already have
by mainly copying and pasting part of the current content in the Workshop Template page,
for example see [this change to the Git lesson](https://github.com/rgaiacs/swc-git-novice/commit/a35b7fc151b5679dd9a2d608f875b4d8a61cef95)
and [this change to the Python lesson](https://github.com/rgaiacs/swc-python-novice-inflammation/).
In addition to it,
some things can be improved in the Javascript code to provide a better user experience.

This post is only the start of the conversation.
All comments are welcome in [swcarpentry/workshop-template#459](https://github.com/swcarpentry/workshop-template/pull/459).
Any change will be made without a technical and rolling plan consensus.
