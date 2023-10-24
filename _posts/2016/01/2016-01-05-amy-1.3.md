---
layout: page
authors: ["Piotr Banaszkiewicz"]
title: "AMY Version 1.3"
date: 2016-01-05
time: "02:00:00"
tags: ["AMY", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>
In the past month we've seen two releases of AMY: v1.2.1 and v1.3.
This blog post
(originally published on [my personal blog](http://piotr.banaszkiewicz.org/blog/2016/01/01/amy-release-13/))
contains a joined release notes for both of them.

## Bug fixes

* wrong URL used in event validation or import/update features is
  now indicated (and we won't receive wrong notifications about it)
* properly throw 404 on some pages (previously: 500)
* spaces are striped from `Person` and `ProfileUpdateRequest` 
  fields (names, emails)
* disable location inputs on event details page if online country
  was preselected

## New features

* use custom-built jQuery-UI (so that we no longer have conflicts 
  with Bootstrap's tooltip module)
* Greg updated the script used to send instructors "Hey, update 
  your info" mails (it's getting removed later on)
* it's possible to add memberships per host
* new badge: DC instructor
* new logic for dealing with two instructor badges
* timeline of TO-DO items
* basic models (e.g. lessons, tags, academic levels, etc.) are now
  manageable from Django's admin interface
* all persons view: add filtering by workshop type person taught at
* remove blurred production database in favor of generated fake 
  database
* mailing script turned into better Django management command
* bulk upload now shows generated username and suggested people with
  matching names
* show preview of event on SWC website
* API: filter events by tags

## No longer with us

* Greg removed some unused scripts (`test-command-line-upload.sh`)
  and commands (`parse-instructor-info.py`)
* notifications about invalid HTTP header `Host`
* other removed scripts and commands

January and February don't seem busy for me, so I hope to have more 
done on AMY in the coming months.  I also want to thank
[Prof. Ethan White](http://whitelab.weecology.org/) for
his support of my work through December,
and for extending his support for the next two months.

Interested in helping develop AMY?
See [what's scheduled for v1.4](https://github.com/swcarpentry/amy/milestones/v1.4).
