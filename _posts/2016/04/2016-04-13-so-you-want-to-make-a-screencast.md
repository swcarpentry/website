---
layout: page
authors: ["Caleb Hattingh"]
title: "So You Want to Make a Screencast"
date: 2016-04-13
time: "05:30:00"
tags: ["Tooling", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>
I am the author of [Learning Cython](http://shop.oreilly.com/product/0636920046813.do),
a new series of videos teaching [Cython](http://cython.org/).
There are over 70 videos, making up around five and a half hours of content.
If you're involved in education,
you may have considered making a screencast like these
and I'd like to give a short overview of what that entails.

## Publisher

You may be happy to self-produce and self-host,
and I would be too except that I was approached by [a publisher](http://shop.oreilly.com/)
and made an offer to produce the videos for distribution on their site.
How this happened is interesting:
in 2015, on a whim, I decided to submit a Cython talk proposal for [PyCon AU](http://2016.pycon-au.org/).
My talk [got accepted](https://youtu.be/NfnMJMkhDoQ),
and a few weeks before the conference the publisher contacted me and made the offer.

You don't _need_ a publisher to make some videos, but I saw several advantages:

- Expertise: the publisher is likely to have experience with producing content, and is likely to be able to assist with quality control and direction when required. As it turns out, my publisher had a ready repository of "author training" material that I could refer to for a precise idea of what was expected in terms of layout, flow, production quality, and so on.
- Marketing: the publisher already has a distribution platform in place for making the content available. Without a platform, I'd have to do that work myself.
- Credibility: if the publisher is well-known and respected, and in particular has a reputation for producing quality content, then my own credibility would be enhanced by working with that publisher.
- Deadlines: having someone such as a publisher holding you to account for meeting deadlines is extremely valuable for making sure your content really does see the light of day.

Having accepted the offer, I was immediately asked to provide a table of contents (TOC) and a timeline.  In hindsight, the most important thing you can do in the entire process is give your TOC a great deal of thought and planning.  The titles for my first half of videos were meticulously planned in the TOC, and the second half to a lesser extent, and I found that I had to spend much more time making the second half. Your ability to plan lessons upfront, before you start with content generation, is probably the best predictor of your time-efficiency; at least this was the case for me.

The deadlines were arranged in three stages: 25%, 50% and 100%, as a proportion of the number of videos included in the TOC.  If you self-produce your own screencast videos without the aid of a publisher, it would be a great idea to impose deadlines on yourself.  My productivity during the week before each deadline was greater than any other period in the entire process.

## Equipment

To do the actual recording, you're going to need a few extra things.  My publisher provided the screencast software [Camtasia](https://www.techsmith.com/camtasia.html) to record the videos. For my first video, Camtasia was new to me but by the time I completed the last one, I was an editing pro.  The sooner you can get comfortable with your recording and editing software, the better. It is liberating to know that you can easily fix a small section of video, or change a small part of the audio very easily.  More on that later.

My publisher offered to send me a microphone, but I already had some audio equipment with professional-grade microphones set up so I used that. The publisher wanted to send me a headset microphone because with these, the distance between the mic and your mouth is always the same.  The concern with stand-mounted microphones, like mine, was that authors have a tendency to move their head around while speaking and recording, which changes the distance between the mic and your mouth, and therefore the volume. I only had to re-record one section of a single video because of this, and I got better at it over time.  Still, I'd recommend that you just use a headset microphone.  And make sure you get a noise-cancelling or noise-resistant mic! The best thing about my microphone is that it was a stage mic (Shure SM58), and therefore intended for use in noisy environments. This meant that I could record videos even in a noisy place like my home during school holidays!

My basic setup at home is with a Macbook Pro and a second, generic Samsung HD monitor. My publisher insisted on videos being 1280x720 (720p) resolution, insisting even that I had to record them that way. My dual-monitor setup made this easy, thankfully, and I set up my second Samsung LCD monitor at that resolution.

It is also worth mentioning that I created a separate user account on my Macbook, exclusively for these videos.  A separate account made it very easy to keep things isolated between my normal user account and the screencast account, and things like custom video resolution settings are included in that: I could log into my normal user account, and the second monitor goes to 1080p, but in my screencast user account the resolution changes back to 720p.  If you make the changes manually and forget to set it before a video, it would require a re-record so it's a fairly important setting to have automatically managed.  In addition, the desktop wallpaper was set to middle gray (in accordance with the publisher's recommendations), and all desktop icons were removed in the "screencast" user account.  The time display, as well as most of the dock and taskbar icons were also disabled, primarily to reduce opportunities for distraction for the viewer.

## What do you show on the screen?

The topic of my course is [Cython](http://cython.org/) and so what the viewer is going to be expecting to see is tons of Cython; however, what do we specifically want to show? My [text editor](http://blog.idyllic-software.com/wp-content/uploads/2012/04/my-vim-screenshot1.png)?  Slides?

This is where good planning makes a world of difference to your authoring experience.  When I started, I wasn't sure, but after a few videos I settled on a _presentation_ pattern that worked very well for the rest:

0. First show simple/clean/colorful slides
0. Then show how to use the info from the slides

Slides, as a _medium_, allow you to hide irrelevant details, and this allows the viewer, and you, to focus on crucial points. I used this a great deal to explain complex topics. Video also allows the viewer to pause and rewind, which I hope contributes further to the elevated focus.  Hopefully, when the viewer moves on from the slides to the _how to use_ section, the emphasized details also carry over.

Some videos did show me entering code into a text editor, and then running or compiling code in a terminal window, but the vast majority of teaching videos were made using the [Jupyter Notebook](http://jupyter.org/) which is not only an excellent, all-round development tool for Python and a [huge and growing](https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages) list of other languages, but it has very good support for Cython. For teaching Cython, the Notebook interface conceals the C/C++ compilation and command-line steps, as well as re-importing the changed binary object making it much, much easier to focus on the important information.

If you're going to be making screencasts for almost anything in the Python space, the Jupyter Notebook interface is hard to ignore. In addition to visual appeal, it also allows your viewers to run the code from your lessons in exactly the same way.

So in terms of presentation of _new_ information, those videos are made up of Slides. I used [Keynote](https://www.apple.com/au/mac/keynote/), a Powerpoint-like tool from Apple, the Jupyter Notebook, and some interaction with the Vim text editor and the Terminal (command-line) application. I heavily used clipboard copy/paste to move code from my text editor into the slides.  My blog gives a brief description of the [tricks](http://pythonomicon.com/?post=Keynode%20code%20snippets%20from%20vim) I used to convert copied code into a Rich Text Format to apply basic syntax highlighting in the slides. It is low-level, and possibly too esoteric but the steps fit in well with all the other parts of my workflow. Once I had set up a keyboard shortcut to both copy and convert code text into a rich text onto my system clipboard, syntax highlighting in slides was never an issue.

I found it very difficult to keep a shell-based interface clean in an _on-screen_ sense: output from previous commands still shows above your prompt which is likely to be distracting to the viewer.  It also makes it difficult to make surgical edits in the video afterwards, since there is no seamless cut point if you have to redo commands.  I artificially created these by running `clear` after explaining the output of each command.  This makes it easy to replace a section of video with something else, or remove it entirely.

## Lesson Preparation

My brief required videos of around five minutes in length, and no fewer than three nor more than ten.  If you've done any prepared speaking, for instance at a conference, you would be well aware that five minutes is an extremely short amount of time in which to convey a self-contained chunk of information. With complex information it can be even more restricting.

It required a great deal of preparation to make sure that each lesson could work inside such small time limits; c.f. Blaise Pascal, Provincial Letters: _I would have written a shorter letter but I did not have the time_. I was compelled to make short videos and therefore, I discovered, I would have to put in quite a lot of time!

My initial plan was to sketch out a few high-level bullet points for each video, and then discuss them with a light and easy, "conversational" and unrehearsed-sounding tone.  This plan was so laughably inadequate that I failed to complete even the first video recording this way. I eventually found that my most efficient method was to write out the entire script for a video, word-for-word, in the same way as one might expect a movie script to be written.  During recording, I would read from script, but with (hopefully!) liveliness and expression. If I practised the script a few times before the recording, it became that much easier to focus on the performance aspects, such as timing, pacing and emphasis. Indeed, merely practising the scripts helped to spot sections in need of correction or improvement.

In the second half of videos, I would even begin to script scroll-actions, typed (on the keyboard) sections, and where to put the mouse, and so on.  I found that every detail captured in the _script_ allowed me to think less about that, and focus on the pacing, sound of my voice and so on.  I don't know how other presenters do it, but my script preparation was the most important (and time-saving) aspect of my preparation. Whether I avoided sounding overly rehearsed, or worse, lifeless, is something that viewers will have to judge, but I could not have recorded the videos any other way.

As far as the technical aspects of preparation go, I am very comfortable with the material and even though I did have to research a few specific details that I had not yet had experience with, this was a minor headache. How _Cython_ works was never a problem: the real headaches were all about how to explain pitfalls on different operating systems, or dealing with differences between Python versions, or how to create packages; basically, the same things that all beginners in Python find difficult.

The most difficult balancing act was trying to decide what to mention, and what to leave out. I imagine this is the same for every lesson creator.  By planning each video in great detail, it was a lot easier to maintain more of a "big picture" view for each lesson.

## Habits

In my first few videos, my unthinking approach was similar to how one might approach giving a live talk. I would try very hard to speak correctly and clearly, and I would immediately be disappointed when I made a mistake, knowing that I would have to go back into the video afterwards and edit out or perhaps even re-record a section. This will sound very naive if you have experience in making screencasts, or recording in general, but I mention it for the benefit of other first-timers. For at least the first three videos I would sigh loudly every time I made a mistake!

Once you've edited a few videos though, you immediately realise that there is _zero_ cost to mistakes in recording, as long as you simply repeat without the error.  If I stumbled at the middle of a sentence, I realised that I could simply restart the sentence and cut the error out later.  Sometimes, in a particularly tricky sequence of words, I would get tongue-tied over and over again. You eventually learn to just stop speaking, compose yourself, take a few breaths, look out the window, check your notes, and then try again, _all the while the video is still recording_.  The dead time doesn't matter, and it takes less than a second to remove during video editing.  All that matters is getting the best "take" that you can, but you can try over and over in a single recording, and then afterwards choose the best one during editing.

Therefore, the first high-level habit is this: get used to making mistakes, and then keeping speaking through the  same section over and over until you get it right, because it is trivially easy to remove the errors and the multiple attempts during editing. During recording of my last few videos, I was so used to it that upon making a mistake, I'd automatically wait a second (to make the cut during editing easier) and immediately repeat the sentence. This becomes quite automatic. I used this even to rephrase sentences, or toy with moving the emphasis to different parts of the same sentence, just to see what the effect might be like during editing when you get to pick the version you want to keep.

### Mouse manners

In the author training videos supplied by my publisher, the management of the mouse cursor was strongly emphasized: it can be very distracting for viewers to see the mouse cursor jump from one position to another on the screen; a common occurrence if there are frequent edits and cut points.  The advice given was to place something on your computer screen like a small piece of sticky tape, or similar, to use as a visual marker of where to place your mouse cursor when not in use.  The idea is that if cuts or edits are required, the mouse cursor will always be in the same position on the screen, and so edits can be made seamless.

In _my_ situation I have two screens: one on my Macbook, and an external display. I found it much more convenient to simply move my cursor off the presentation screen entirely between actions or when not in use.

When using the Jupyter Notebook, scrolling becomes an important part of moving through the content because of the document-based design of the notebook interface. My guiding principle for how to scroll was based on whether my actions might be _distracting_ from the content; this principle was promoted heavily by the author training videos. All of my mouse movements or scroll actions were made in the best way to diminish distracting actions.  I would even frequently announce that I would be scrolling down to the next cell before doing so.  Sometimes, during editing, I would find that such announcements were unnecessary or were implied in the context of the surrounding speech. In these situations, I would edit them out. In others, however, it seemed to me a useful cue to the viewer that context was being changed in the video. I also learned to scroll slowly, knowing that I could easily speed up the scrolling later in editing if required.

### Time manipulation

While on the subject of speeding up and slowing down, many things become possible in editing. Initially, I was nervous about my typing speed, but again, it is so easy, trivial really, to speed up bits of typing that it becomes a non-issue.  Even typing mistakes are easily dealt with in editing.  It is slightly more annoying to cut a section of video than it is to apply a speedup, so once I became experienced, I would concentrate on making sure I typed accurately rather than fast, and then during editing I would apply a 200-400% speedup to typed sections. This sounds very rapid, but as a viewer, watching normal typing speed can be painfully slow.

In most situations I would use the video editing tools to speed things up; however, during editing I found some instances where a few extra seconds' lingering on the output of an especially complex command was likely to be useful to viewers. In these situations, I added some dead time in the video; basically, a stop-and-think moment that I had failed to provide during the original recording.

The point is that time management and pacing can easily be manipulated after recording.  It is up to you or your editing team to make decisions about what to speed up and what to slow down. And once you realise this, it is quite liberating: it allows you to relax about those issues while recording. Just focus on your content and the key points you want to drive home.  Take any pauses as you need, and feel free to repeat sections as often as you like: it all comes together during editing.

## Content

The topic of my course is Cython. This is a tool that allows you to write code that looks very similar to, but is not exactly Python, but then allows you to compile that code into a native binary module. The primary use case of the tool is for speeding up Python code, although what is really happening behind the scenes is that you're generating C code and compiling that with a C compiler.  The main attraction of Cython as a technology is that you can re-use your Python knowledge while optimizing for speed.

As you might imagine then, Cython is useful in a space where the person writing the code may not have had training with C/C++.  From the point of view of developers with a background in computer science, this is very hard to understand, because training or at least exposure to C/C++ is nearly mandatory in computer science schools in most countries. However, there is a class of people who sometimes need to write code that _do not_ have formal training in computer science: scientists and (non-electrical!) engineers.  And ironically, it is this group that _also_ frequently requires code to do number crunching at speed which is a feature that raw Python lacks. It is for this group that Cython is especially compelling: mostly the same, easy-to-understand Python syntax but with the speed of native numerical code.

This is interesting from the point of view of someone who wants to teach this topic. What do you focus on?  Is your time better spent on the code generation aspects of C/C++, i.e., explaining what your nearly-Python code gets converted into? Alternatively, is it better to focus on _using_ Cython and focusing on applications from the Python side of things? Do you prefer _How it works_, or instead, _How to use it_, or some mixture of the two?

For these questions, I relied on my experience working as a chemical engineer. Professionally, when using software tools I was generally focused on trying to achieve a domain objective; that means trying to solve some real-world problem at work. This is the approach I used in my videos. I decided to avoid discussing the internals about how C/C++ works, such as the linker and assembler and the rest of the compiler toolchain, and rather focus on the features that Cython provides from a _Python_ perspective.

I tried, perhaps too aggressively, to use examples and case studies that were _not_ scientific in nature. The problem with using scientific examples is that it is too easy to exclude people. Different scientists are not necessarily experts in each other's fields, so using a bioinformatics case study risks alienating the neuroscience folks, and vice versa, while using math examples alientates everyone! So I tried to find case studies that would have the most broad appeal. In one case study, I showed how to speed up a large-scale personal tax calculation. In another, I showed how to load and process data from a history file of Soccer World Cup matches. In yet another I showed basic image processing by changing the RGB color of red chillies to blue.  Whether this approach works for Cython remains to be seen, but my gamble is that by using examples that are likely to appeal to, or at least to be merely understandable by the largest number of people, will improve the odds that the lessons will be conveyed successfully.

I found Cython quite difficult to teach.  Python itself is fairly easy to teach, but Cython, even conceptually, begins to touch on many other disparate issues that are not specifically related to Python. It requires a C compiler, which is installed differently on different operating systems. The compiler doesn't even work the same on different OSs, making the OpenMP case study disconcertingly compiler-specific. Explaining the Cython type declarations threatens to pull in further discussion about whether a `long` means 32 or 64 bit; whether a `char` is a string; and whether that answer changes on Python 2 or Python 3.  These are just the most high-level issues.  Once you begin to sink your teeth into the meat of the subject, the complexity only increases further.  How do you package your Cython module? Do you explain how Python's `distutils` works? Oops, I meant `setuptools`?  Do you explain how wheels work?  The list goes on and on!

My goal eventually became to provide just enough information to allow the average developer to be able to get _something_ working on Cython with a significant speed-up, but not necessarily understanding all the low-level machinery. A complete treatment was unrealistic: the reality is that both my time, and the viewer's available time doesn't allow for it. I am proud of the set of videos I did manage to produce though: I think the content strikes a good balance between high-level topics, and just enough hinting at low-level topics to suggest further learning paths.

## General Advice

It is best to get feedback on your videos as often as possible, especially in the beginning. The feedback is not about whether your content is accurate.  The main thing is to get feedback about whether the visuals are clear and easy to understand, and whether your speaking pace is clear. My publisher pushed very hard for reviewing demos as well as my first few videos so in that sense I was fortunate. If you plan to self-publish I would strongly urge you to ask friends to critique your first few videos. Even before you spend any time on actual content, make a two-minute demo that you can get feedback on. It makes a world of difference to fix things early.

The second piece of advice: the only thing that really matters is whether your content is useful for viewers. It is of no use to rush to complete your videos, only to discover later that few people understood the material. The quality of instruction is more important than how quickly you finish your videos. If you _must_ obsess about something, let it be the success of knowledge transfer.  There were two videos in particular that I took _forever_ to complete. Each turned out to be, after editing, around 11 minutes, but my preparation time for _each_ was over 20 hours.  These were to do with wrapping C/C++ libraries with Cython, one for Mac and one for Windows.  The extensive preparation time was spent on finding a way to convey the most important concepts without getting bogged down in the noise. I kept trying different C libraries from github, and different ways of performing the command-line actions until I found a sequence that was both understandable and useful to a viewer who may perhaps lack significant Python experience. I am especially interested in feedback about these two videos: many years of experience went into their production!

The final piece of advice is: if you're preparing a screencast, aim to do a little every day.  I failed to do this, which resulted in large backlogs beset with looming deadlines. I succeeded in meeting my deadlines, but the process would have been much smoother if I had spread out the work more.

I hope to make more screencasts in the future, and I'd love to get feedback on [Learning Cython](http://shop.oreilly.com/product/0636920046813.do) to improve the next one!
