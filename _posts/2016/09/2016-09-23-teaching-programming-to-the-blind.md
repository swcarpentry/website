---
layout: page
authors: ["Greg Wilson"]
title: "Teaching Programming to the Blind"
date: 2016-09-23
time: "07:00:00"
tags: ["Community", "Teaching", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

[Andreas Stefik](https://ramblesblog.files.wordpress.com/2016/05/inpraiseoftweaking.pdf)
(who discusses what we know about the usability of programming languages
in [this entertaining podcast](https://www.functionalgeekery.com/episode-55-andreas-stefik/))
has worked extensively on computing education and programming tools for the visually impaired.
When asked earlier this week how to teach programming to the blind,
he sent the response below.
We're grateful for his comments,
and for [Evan Williamson](https://vivo.nkn.uidaho.edu/vivo/display/n43629)'s
[recent pull request](https://github.com/swcarpentry/styles/pull/103)
to improve the accessibility of our lessons.

---

1. If you are making any presentations, be sure to provide the
   powerpoints to the blind individual in advance if you
   can. Powerpoint is the "most" accessible, but if you have any
   images, you need to manually specify "alts" inside the
   presentation. It's not hard, but most people don't realize
   powerpoint has this feature.

2. When actually presenting material, for any kind of diagrams, I find
   it helpful (if my audience is blind) to practice oral description
   of the images ahead of time. This is sometimes tricky in code,
   especially for things like linked structures or trees. So, if you
   are explaining those kinds of concepts, just be aware that it might
   take some practice. I've practiced this for years in my own
   presentations, but still find it challenging sometimes for highly
   visual content (e.g., we taught 3D gaming to blind people this
   summer, which was a real challenge).

   Same goes with code. If the person doesn't read code coming in,
   screen readers don't even output all of the special characters
   without special modes turned on (e.g., verbosity mode in JAWS). For
   example, if I have:

   ~~~
   a = a - b
   ~~~

   it might say "a equals a b" (notice the missing minus).  Point
   being, depending on the experience level of the person coming in,
   and how comfortable they are with their screen reader, they might
   need some help getting used to the quirks. When presenting, you
   sometimes have to actually say the special characters or they won't
   know they need to be typed.

3. If you are using tools for programming, a great many out there
   don't work for the blind. The best you can do here is make sure you
   get them to the person in advance if you know they work. If you
   don't, you can either ask or at least have a fallback. A basic text
   editor and the console usually works on most systems, although that
   doesn't mean that kind of setup is easy to use. We have some stuff
   that might help, but it depends on what you are teaching and your
   specific needs.

4. Different languages can cause major issues for blind individuals. I
   could go into detail, but imagine things like white space in
   Python. Or, imagine hearing statements like, "for left paren int i
   equals semicolon i less than ten semicolon i plus plus right paren
   left brace" in C. Both can cause headaches for various reasons.

5. Find out about their specific needs beforehand if you can and if
   they are willing to tell you. If they just need magnification and
   large print materials, this stuff is a lot easier. If they are a
   total, then braille can be helpful. **But**, crucially, you need to
   know whether they know Braille, and if so, which kind. Braille
   standards have changed in recent years and it matters for computer
   code because of the special characters. I'm not a Braille expert,
   but if this is an issue on your end, I can get you info from some
   experts.

Finally, one thing I almost always recommend to do before hand, just
to make sure you have a little bit of context, is to download a screen
reader and give it a shot. On Windows, grab NVDA, or on Mac, just
press APPLE F5. Even spending an hour going over a tutorial can help
give you a little of context. Spending an hour programming blind on
your own won't make you an expert, but it's such a different way of
programming that it might help give a glimpse into that world.
