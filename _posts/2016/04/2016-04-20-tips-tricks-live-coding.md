---
layout: page
authors: ["Lex Nederbragt"]
title: "10 tips and tricks for instructing and teaching by means of live coding"
date: 2016-04-20
time: "00:00:00"
tags: ["Education", "Instructor Training", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

One of the key teaching practices used at Software and Data Carpentry workshops is 'live coding': instructors don't use slides, but work through the lesson material, typing in the code or instructions, with the workshop participants following along. Learning how to teach using live-coding is best done in practice, with feedback from peers (this is why it is included in [instructor training]({{site.github_io_url}}/instructor-training/08-practices.html)). Nonetheless, this post lists ten tips and tricks to help you get started.

This text (re)uses, and expands on, elements from the Software and Data Carpentry [instructor training]({{site.github_io_url}}/instructor-training/08-practices.html) materials.


### 1. Be seen and heard

If you are physically able to stand up for a couple of hours, do it while you are teaching. When you sit down, you are hiding yourself behind others for those sitting in the back rows. Make sure to notify the workshop organisers of your wish to stand up and, ask them to arrange a high table/standing desk or [lectern](https://en.wikipedia.org/wiki/Lectern#Academic_context).

Regardless of whether you are standing or sitting, make sure to move around as much as reasonable. You can for example go to the screen to point something out, or draw something on the white/blackboard (see below). Moving around makes the teaching more lively, less monotonous. It draws the learners' attention away from their screens, to you, which helps getting the point you are making across.

Even though you may have a good voice and know how to use it well, it may be an idea to use a microphone, especially if the workshop room is equipped with one. Your voice will be less tired, and you increase the chance of people with hearing difficulties being able to follow the workshop.

### 2. Take it slow

For every command you type, every word of code you write, every menu item or website button you click, say out loud what you are doing while you do it. Then point to the command and its output on the screen and go through it a second time. This not only slows you down, it allows learners who are following along to copy what you do, or to catch up, even when they are looking at their screen while doing it. If the output of your command or code makes what you just typed disappear from view, scroll back up so learners can see it again - this is especially needed for the Unix shell lesson.

Other possibilities are to execute the same command a second time, or copy and paste the last command(s) into the workshop Etherpad.

### 3. Mirror your learner's environment as much as possible

You may have set up your environment to your liking, with a very simple or rather fancy Unix prompt, colour schemes for your development environment, keyboard shortcuts etc. Your learners usually won't have all of this. Try to create an environment that mirrors what your learners have, and avoid using keyboard shortcuts. Some instructors create a separate 'bare-bone' user (login) account on their laptop, or a separate 'teaching-only' account on the service being taught (e.g. Github).

### 4. Use the screen - or screens - wisely

Use a big font, and maximise the window. A black font on a  white background works better than a light font on a dark background. When the bottom of the projector screen is at the same height, or below, the heads of the learners, people in the back won't be able to see the lower parts. Draw up the bottom of your window(s) to compensate. 

If you can get a second screen, use it! It will usually require its own PC or laptop, so you may need to ask a helper to control it. You could use the second screen to show the Etherpad content, or the lesson material, or illustrations.

Pay attention to the lighting (not too dark, no lights directly on/above the presenter's screen) and if needed, reposition the tables so all learners can see the screen, and helpers can easily reach all learners.

### 5. Use illustrations, or even better, draw them

Most lesson material comes with illustrations, and these may help learners to understand the stages of the lesson and to organise the material. What can work really well is when you as instructor generate the illustrations on the white/blackboard as you progress through the material. This allows you to build up diagrams, making them increasingly complex in parallel with the material you are teaching. It helps learners understand the material, makes for a more lively workshop (you'll have to move between your laptop and the blackboard) and gathers the learners' attention to you as well.

### 6. Avoid being disturbed

Turn off any notifications you may use on your laptop, such as those from social media, email, etc. Seeing notifications flash by on the screen distracts you as well as the learners -  and may even result in awkward situations when a message pops up you'd rather not have others see.
 
### 7. Stick to the lesson material

The core Software and Data Carpentry lessons are developed collaboratively by many instructors and tried and tested at many workshops. This means they are very streamlined - which is great when you start teaching them for the first time. It may be tempting to deviate from the material because you would like to show a neat trick, or demonstrate some alternative way of doing something. Don't do this, since there is a fair chance you'll run into something unexpected that you then have to explain. If you really want to use something outside of the material, try it out thoroughly before the workshop: run through the lesson as you would during the actual teaching and test the effect of your modification.

Some instructors use printouts of the lesson material during teaching. Others use a second device (tablet or laptop) when teaching, on which they can view their notes and the Etherpad session. This seems to be more reliable than displaying one virtual desktop while flipping back and forth to another.

### 8. Leave no learner behind

Give each learner two sticky notes of different colours, e.g., red and green. These can be held up for voting, but their real use is as status flags. If someone has completed an exercise and wants it checked, they put the green sticky note on their laptop; if they run into a problem and need help, the put up the red one. This is better than having people raise their hands because:

* it's more discreet (which means they're more likely to actually do it),
* they can keep working while their flag is raised, and
* the instructor can quickly see from the front of the room what state the class is in.

Sometimes a red sticky involves a technical problem that takes a bit more time to solve. To prevent this issue to slow down the whole class too much, you could use the occasion to take the small break you had planned to take a bit later, giving the helper(s) time to fix the problem.

### 9. Embrace mistakes

No matter how well prepared you are, you will be making mistakes. Typo's are hard to avoid, you may overlook something from the lesson instructions, etc. This is OK! It allows learners to see instructors' mistakes and how to diagnose and correct them. Some mistakes are actually an opportunity to point something out, or reflect back on something covered earlier. Novices are going to spend most of their time making the same and other mistakes, but how to deal with the is left out of most textbooks.

> The typos are the pedagogy - [Dana Brunson](https://twitter.com/danabrunson/status/684764295196876800)

### 10. Have fun

Teaching is performance art and can be rather serious business. On the one hand, don't let this scare you - it is much easier than performing Hamlet. You have an excellent script at your disposal, after all! On the other hand, it is OK to add an element of 'play', i.e. use humor and improvisation to liven up the workshop. How much you are able and willing to do this is really a matter of personality and taste - as well as experience. It becomes easier when you are more familiar with the material, allowing you to relax more. Choose your words and actions wisely, though. Remember that we want the learners to have a welcoming experience and a positive learning environment - a misplaced joke can ruin this in an instance. Start small, even just saying 'that was fun' after something worked well is a good start. Ask your co-instructors and helpers for feedback when you are unsure of the effect you behaviour has on the workshop.

>Teaching is theater not cinema - Neal Davis

(Thanks to Neil Davis, Rayna Harris and Greg Wilson for feedback on an earlier version of this post)
