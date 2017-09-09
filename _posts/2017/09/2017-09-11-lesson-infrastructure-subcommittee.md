---
layout: post
authors: ["Raniere Silva"]
title: "Lesson Infrastructure Subcommittee 2017 September meeting"
date: 2017-09-12
time: "10:00:00"
category: ["Community", "Lesson Infrastructure Subcommittee"]
---

On 5 September 2017 at 14:00UTC+0,
the Lesson Infrastructure Subcommittee had their 2017 September meeting.
This post will cover the topics discussed and their resolutions.

## Software Carpentry and Data Carpentry merge

With the [upcoming merge](https://software-carpentry.org/blog/2017/09/merger.html),
this subcommittee needs to start thinking about streamline the thinking process and disconect from the organisations that maintain the lessons.
The responsibilities for this subcommittee will stay unchanged:

- maintain [lesson template](https://github.com/swcarpentry/styles)
- maintain [lesson documentation](https://github.com/swcarpentry/lesson-example)
- maintain [workshop template](https://github.com/swcarpentry/workshop-template)
- overview of what features the lessons will continue to have
- stay in contact with maintainers of lesson
- stay in contact with staffs

[Lesson template](https://github.com/swcarpentry/styles),
[lesson documentation](https://github.com/swcarpentry/lesson-example)
and
[workshop template](https://github.com/swcarpentry/workshop-template)
**will have a new home in 2018**.
If you have questions or want to help with this migration,
[Christina Koch](mailto:koch.christinal@gmail.com) is the person you should contact.

During the migration,
we will solve the divergences between
[Software Carpentry workshop template](https://github.com/swcarpentry/workshop-template)
and
[Data Carpentry workshop template](https://github.com/datacarpentry/workshop-template).
If you have questions or want to help with this migration,
[Maneesha Sane](mailto:maneesha@software-carpentry.org) is the person you should contact.

## Keyboard key visual look

To improve the reader experience of the lesson,
we will make a visual diference of keyboard keys that need to be pressed by the reader.
We expected to merge the new CSS and documentation in the next few weeks
and that release 2018.6 of all the lessons complain with the new visual.
More information about the new visual is available [at this pull request](https://github.com/swcarpentry/styles/pull/165).
Thanks to [Brandon Curtis](https://github.com/brandoncurtis) to propose the new visual.

## Jekyll/Liquid include for images/figures

To improve the reader experience of the lesson by providing a more uniform render of images,
we will pursuit the proposal on [GitHub issue styles#161](https://github.com/swcarpentry/styles/issues/161)
after we review [lessons unit test suite](https://github.com/swcarpentry/styles/blob/gh-pages/bin/lesson_check.py)
and its use by a continuous integration platform.

## Citing the templates

If you want are reusing the lesson template
and you to credit us,
please use [Software Carpentry: Example Lesson at Zenodo](https://zenodo.org/record/838778#.WbPw1HVifCl).

## Lesson release and hosting scheme

[For years](http://lists.software-carpentry.org/pipermail/maintainers/2016-April/000230.html),
we want to point readers to the last release of our lessons
but due technical limitations on GitHub Pages
and all the trouble that branches created for Git novice users
(for example,
the current branch isn't clear when visiting the lesson homepage in GitHub
and
maintainers not be able to change the target branch of a pull request)
we stayed with a single `gh-pages` branch in the Git repository.

[Jonah Duckles opened a issue](https://github.com/swcarpentry/lesson-example/issues/126)
to discuss possible solutions to this issue.
If you want to contribute with the discussion
left your comments on the [GitHub issue](https://github.com/swcarpentry/lesson-example/issues/126).

## Fully-offline-capable functionality in lesson navigation

[vuw-ecs-kevin GitHub user](https://github.com/vuw-ecs-kevin)
requested for us to improve the reader experience for those that get our lesson from [Zenodo](https://zenodo.org/),
i.e. [from one of our releases](https://software-carpentry.org/blog/2017/08/release-2017.08.html).
Changes on the line of [vuw-ecs-kevin's pull request](https://github.com/swcarpentry/styles/pull/166) or [Raniere's pull request](https://github.com/swcarpentry/lesson-example/pull/127)
will be included in the next release of our lessons.

## Managing workshop websites and install instructions

This is another old request [[1](https://github.com/swcarpentry/DEPRECATED-bc/pull/415), [2](https://github.com/swcarpentry/DEPRECATED-bc/pull/738), [3](https://github.com/swcarpentry/workshop-template/issues/194), [4](https://github.com/swcarpentry/amy/issues/1087)].
Edit only one line of [`index.html`](https://github.com/swcarpentry/workshop-template/blob/gh-pages/index.html)
and have the correct instructions for the workshop.
[Jonah Duckles opened a new issue](https://github.com/swcarpentry/workshop-template/issues/421)
to discuss ideas to archive our old request.

Kate Hertweck,
Christina Koch,
Raniere Silva
and
Tracy Teal
are going to work on strategic plan document to addres this request taking in consideration the [comments on the GitHub issue](https://github.com/swcarpentry/workshop-template/issues/421).

## Next steps

We will freeze
[lesson template](https://github.com/swcarpentry/styles)
and
[lesson documentation](https://github.com/swcarpentry/lesson-example)
in October
so maintainers have time to work on the next release.

The subcommittee will meet again in November to provide update on some of the topics covered by this post
and discuss new requests from the community.

## Acknowledgement

Thanks to 
Kate Hertweck,
Maneesha Sane,
Mark
Naupaka Zimmerman,
Person Paula Andrea Martinez,
SherAaron Nicole Hurt
and
Tracy Teal.
Special thanks to Christina Koch for the great [notes](http://pad.software-carpentry.org/infrastructure-subcommittee).