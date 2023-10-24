---
layout: page
authors: ["Belinda Weaver"]
title: "Teaching Library Carpentry"
date: 2016-06-22
time: "00:00:01"
tags: ["Workshops", "Library Carpentry", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>
## Teaching Library Carpentry 

I ran a two-day 'Library Carpentry' [workshop](http://weaverbel.github.io/2016-06-13-LibCarp/index.html) for librarians at [The University of Queensland](http://www.uq/edu.au/) on 13-14 June. The class covered

- jargon-busting and data structures
- writing and using regular expressions
- command line tools to find data in files
- version control
- [OpenRefine](http://openrefine.org/) for data cleanup

Eighteen people from six organisations attended, out of a pool of 26 who intially expressed interest. (In the small lab I was using, I only had room for 18.)

Because of my wish to spread these skills far and wide, people were only welcome to attend if they agreed to teach the material to others within 12 months -- to teach some of it at least. Despite some degree of trepidation among attendees, pretty much everyone signed up for that.

Though I am a certified Software Carpentry instructor, this was my first time teaching the full [Library  Carpentry](https://github.com/LibraryCarpentry) curriculum, so I was learning it myself as I went along. The material was developed by Dr James Baker, Owen Stephens and Daniel van Strien. This material was updated by a team during the recent Mozilla Global Sprint - see [blog post](http://software-carpentry.org/blog/2016/06/LibrarCarpentrysprint.html), so there are updated lesson repositories sitting on GitHub under [data-lessons](https://github.com/data-lessons) as well (which made preparing for the workshop tricky).

Teaching someone else's material is always a challenge, and I made many blunders, but this helped people relax about their own mistakes. In the end, my lack of familiarity did not prevent my teaching at least some of the material efectively, which is worth noting. A little knowledge can be useful! 

I did warn attendees that the material would be challenging. If you have never used the command line before, it can seem an unforgiving place. I likened it to learning to drive, where nothing is familiar or intuitive, and you have to remember to do complicated things in the right sequence. Some people loved that section and could see uses for both `grep` and `sed`, which I covered in detail. People also enjoyed the jargon busting and regular expressions challenges from the first session. 

The most popular session was definitely **OpenRefine**. This tool was the one most attendees said they would use after the workshop. Some of the suggested uses included: 

- Tidying up EndNote libraries by identifying where data is missing
- Wrangling data for bibliometric benchmarking exercises
- Cleaning up and standardising free text fields from surveys
- Anonymising sensitive data
- Turning messy, unstructured data into categorised data
- Using regular expressions to locate specific words or concepts within messy data
- Combining course feedback from different courses

The Git session was run only through the Web interface. People created a blog using [JekyllNow](https://github.com/barryclark/jekyll-now), and also created files to for a repository we set up at the workshop. This gave them the opportunity to fork and branch repositories and do pull requests in a visual-friendly environment.

I was very fortunate to have the assistance of [Marco Fahmi](https://twitter.com/dataronin) at the workshop. He knew regex backwards and came up with lots of good ideas to encourage greater involvement and input by attendees, and to use the tools later. He also helped people who got stuck at different points, not least me! He dug me out of the many holes I got into because of my inexperience with the material.

Would I do it differently next time? 

I would.

I learned it is vitally important, up front, to establish *how* people will use the different tools post-workshop. While we did brainstorm ideas for this in the workshop, it would help to have more ready-made examples at the start. Certainly the ideas for OpenRefine will be incorporated into the updated lessons, as will other examples from the workshop.

But my key message really is : **Just do it!** 

Even if you are not an expert, you can teach this material, or learn it with others as a group. The full curriculum is available, including notes, handouts, challenges, scripts, quizzes and slides. Skills like these will only become widespread if people take responibility for sharing them. Have a go. 

If you want to be part of developing and refining the material, or if you just want to be in touch with others in this area, join our [chatroom](https://gitter.im/weaverbel/LibraryCarpentry). I hope I'll see you in there.
