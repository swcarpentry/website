---
layout: page
authors: ["Kathy Chung"]
title: "What Digital Humanists Do"
date: 2016-05-25
time: "00:05:00"
tags: ["Digital Humanities", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>
I have started gathering user stories from humanists
to give us a better sense of what they do
and how (or whether) our kind of skills training might help.
Two of these are summarized below;
there's a lot to think about,
but the most important observation is that
DH really is different in important ways
from what Software and Data Carpentry have been doing so far.

## Alpha

Alpha is studying the meeting of cultures
in a text which mixes vernacular (Judaeo-Provençal) and Hebrew.
The text's author was a physician,
and says in the introduction that
the vernacular was for women and children,
while the Hebrew was for men.
The text exists in only one hand-written manuscript from 1401,
which is based on the book of Esther used in the Purim holiday.

The original is at the Bodlein Library in Oxford,
but is available on microfilm,
and weighs in at about 22 folio pages.
(Alpha heard that there was another copy in Italy,
and obtained digitized copy,
but the original was in such bad shape
that they can't even tell if it's the same manuscript.)
There are also two 18th Century handwritten copies,
and a much later 19th Century copy from the Balkans,
all of which have variations from the original.

The first task was to transcribe the document,
which meant learning the quirks of the scribe's handwriting.
(The good news is,
those quirks can help to date the manuscript.)
Once it was transcribed,
the next step was to track down and record the sources of its Biblical quotations.
Luckily,
there's already a database of Biblical and other religious texts from different periods,
so this can be done with keyword searches.

Determining the significance of the choices of quotations is a harder task,
but necessary for writing a scholarly edition of the work.
This obviously relies on the Medievalist's expertise,
but good bibliography management tools are essential.

Step three was to translate the whole document for personal use,
then do a better translation of the bits actually used in
the Medievalist's dissertation.
The end product was based on the 1401 version,
but included variants in an appendix;
those variants were also used to fill in gaps in the original.
(The author of the original documen wrote a colophon as an acrostic,
which probably doesn't matter from a software skills point of view,
but is still pretty cool.)

Alpha's data management challenges
mostly revolve around tracking different formats:
microfilm, digitized images, PDF versions of a microfilm,
and so on.
Each page is a different image,
so this has to be done page by page.
The other major component is the critical analysis,
which requires linking discussion of
the literary, cultural, religious, and medical context of the work
back to the original.

## Beta

Beta has already used some computer tools in their MA research
(described below),
and tried to take a Software Carpentry workshop
but was unable to schedule it.
A friend introduced them to Markdown and Pandoc
and they use it to write all their work now.
They also uses Zotero.

Their MA research revolved around everyday use of vernacular medical manuscripts
in late Medieval England.
These contain a lot of text about everyday small-time medieval practices,
but not much about everyday life.
Their starting point was a single manuscript made up of several booklets
which are full of marginalia.
The first task was to transcribe all the marginalia with important metadata
(the folio, the marginalia's location, the color of the ink,
the date, the hand it was written in,
the beginning of the associated medical recipe,
etc.).

The result was 700 lines of marginalia data,
which they ended up analyzing using a pivot table in Excel.
The analysis revolved around classifying and grouping comments;
700 records is a manageable number,
but obviously doing this with a computer is a lot faster.
(It turns out, by the way,
that the most common subject was headaches,
but this was probably influenced by the content of the main text.)

Beta is now working with several other people
on a content management system for DH projects.
This relies on the
[International Image Interoperability Format](http://iiif.io/),
which they explained as "like DOIs but for images".
It links metadata to images so that you can open any image with an IIIF-compliant viewer,
then add more metadata,
and the original image holder can decide if they want
to incorporate the new data or not.

Their main goal is to help people produce
authoritative scholarly editions of manuscripts.
Lots of people will be involved in editing and annotating,
and these will be used in many ways that the original creators cannot anticipate.
One interesting challenge is how to handle variants:
if there are 25 slightly different versions of a text,
what do you print and how?
And how much of the original appearance do you try to preserve?
As noted in Alpha's story,
the handwriting can be as important as the actual text,
and in Beta's MA research,
the physical location or ink color of comments mattered too.
