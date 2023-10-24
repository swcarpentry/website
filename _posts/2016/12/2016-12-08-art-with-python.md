---
layout: page
authors: ["Eleanor Lutz"]
title: "Making art with Python: Projects after Software Carpentry"
date: 2016-12-08
time: "00:10:00"
tags: ["Community", "Art", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

This March I signed up for a Software Carpentry class and learned Python for the first time. I had a great time at the workshop, and I wanted to share one of the first Python projects I completed thanks to Software Carpentry. 

I originally signed up for the workshop for my PhD research in mosquito behavior. I needed to automate some video analysis tasks, and several friends recommended learning Python. I ended up making the video analysis work (thanks Software Carpentry!), but this blog is actually about a Python art project that I worked on right after finishing the class.

![](/files/2016/12/art2.gif)

One of my Python [matplotlib](http://matplotlib.org/) animations, based on the public commons image [Arabesques: mosaïques murales XVe. & XVIe. siècles](http://digitalcollections.nypl.org/items/510d47d9-665a-a3d9-e040-e00a18064a99).

Coming into the class I had a little coding experience, but not much. I’d taken an introductory Java class four years ago (and barely used it since), and learned GitHub and HTML/CSS while [making maps](http://a.tiles.mapbox.com/v3/eleanor.ipncow29/page.html#16/48.8656/2.3170) as a designer at Mapbox.

[Dave Williams](http://www.charlesdavidwilliams.com/) and [Jes Ford](http://jesford.github.io/), the Python instructors for my class, did an amazing job of making the class accessible to beginners like me. I particularly appreciated how they took the time to set up their own computers to look exactly like what a beginner would see - no shell aliases or custom installs and appearance settings. 

In our class we worked on graphing the example "inflammation dataset" using matplotlib. I was impressed by the Seaborn graphics library shown in the class, and I wanted to see how far I could get using vanilla matplotlib for an art project. I needed a practice project to get better at Python, and as a former designer one of my favorite challenges is making art out of limited tools. 

For my project I wanted to make a browsable color palette website like [Adobe Kuler](https://color.adobe.com/explore/most-popular/?time=all), but with animated examples for every color palette. This was fairly straightforward once I figured out that [matplotlib.patches](http://matplotlib.org/api/patches_api.html) will plot any shape given a list of points. After that I just needed to define a set of shapes and pass their location and size to each frame of the GIF. (I also turned the project into an [open source Git repository](https://github.com/TabletopWhale/AnimatedPythonPatterns), for anyone who wants to take a closer look.)

![](/files/2016/12/art0.gif)

Another Python animation, based on the public commons image [Mosaik aus der Moschee des Galaon el Alfi auf der Citadelle zu Kairo (Friedrich Hessemer 1842)](http://digitalcollections.nypl.org/items/510d47d9-6923-a3d9-e040-e00a18064a99)

I learned a lot about Python while making this, so for me it was a really useful practice project. For example, by generating hundreds of figures and unintentionally causing a huge memory leak, I learned that matplotlib doesn't have automatic garbage collection. It was also useful to carefully decide which parts of the project to write in Python, and which to write in HTML/CSS/Javascript. In the end my final [color palette browser website](http://tabletopwhale.com/colorpalette.html) uses a mix of original HTML/CSS/Javascript, automatically generated Javascript written in Python, and GIF images generated in Python. 

![](/files/2016/12/art1.jpg)

This was a fairly basic coding project, but I wanted to share it with the Software Carpentry community to show that I actually learned something useful from the class. I ended up really enjoying Python, and the structure of the class helped me quickly get a handle on the basics. 

Finally, I want to acknowledge everyone at Software Carpentry who helped me during the March 2016 workshop: Dave Williams, Jes Ford, Ariel Rokem, Allison Smith, Rick Riehle, Emilia Gan, Bernease Herman, Bryna Hazelton, Chris Suberlak, and Jeremey McGibbon. Thanks for all of your work helping beginners in coding!
