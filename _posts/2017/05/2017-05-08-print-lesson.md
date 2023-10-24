---
layout: page
authors: ["Raniere Silva"]
title: "How to print our lessons?"
date: 2017-05-08
time: "18:00:00"
tags: ["Community","Tools","Lessons","Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

From the time that I joined Software Carpentry,
I remember two feature requests that often showed up on our list of issues.
The first one was links to help navigate the lessons
and the second one was a way to print the lessons.
Adding these two features was challenging
because the limited information that is available as metadata by Jekyll
(or Pandoc, which we used for a while).
In addition,
we want to have a "real" solution,
instead of a workaround that is going to stop work in a few months. 
Although as software developers we knew that at every release of Jekyll,
or any other library, that we are using
exist a chance that our pipeline will break.

At some point,
Greg Wilson managed to implement the navigation
using [Jekyll Collections](https://jekyllrb.com/docs/collections/),
introduced in [Jekyll 2.0.0](https://jekyllrb.com/docs/collections/),
after [the last review of our template](https://github.com/swcarpentry/DEPRECATED-lesson-template/pull/282#issuecomment-226742892).

But until this month,
instructors and learners had to print each episode of our lesson individualy.
We are happy to introduce our "All episodes in one page".

## How to Use

1. Access the [lesson](/lessons/) you want to print.
2. At the navigation bar, on the top, open the "Episodes" menu.
3. Click on the last option, "All in one page (Beta").

   ![Navigation bar](/files/2017/05/aio.png)

   **If the option isn't available yet it will be soon. We are still merging the pull request that include the new feature.**
4. In your web browser,
   select the "Print" option
   and proceed to print the lesson as any other document.

   If your web browser offers the option to save the document as PDF
   you can use it to read the lesson off-line.

**Bonus:** If you are using [Chrome 59 or higher](http://lists.software-carpentry.org/pipermail/maintainers/2016-September/000328.html)
you should be able to get the PDF of the lesson using

~~~
$ chrome --headless --disable-gpu --print-to-pdf http://swcarpentry.github.io/your-favorite-lesson/aio/
~~~

## Next Steps

Our CSS rules for the print version need some improvements.
If you want to contribute with it [contact us](/contact/).

## Technical Details

After we play around with
[Pandoc and XPATH](http://lists.software-carpentry.org/pipermail/maintainers/2016-September/000328.html)
and [other methods](http://lists.software-carpentry.org/pipermail/maintainers/2016-September/000328.html)
to have the lesson in PDF and EPUB
we decided to those approaches were incompatible with our pipeline
that depends on [GitHub Pages](https://pages.github.com/)
and because of it we should try to come up with a solution
that only use [Liquid](https://shopify.github.io/liquid/).
Since part of the lesson was stored on the YAML header
and need to be compiled by Jekyll we end up with a difficult challenge.
Fortunately, we can use Javascript not only to animate web pages
but also to query servers for data (or episodes in our case)
and inject the new data into the page.
For this reason,
the solution that we implemented is 100% powered by Javascript
and isn't available to web browsers without a Javascript engine.

The code running to generate the all episodes in one page is

~~~
  window.onload = function() {
    var lesson_episodes = [...];
    var xmlHttp = [];  /* Required since we are going to query every episode. */
    for (i=0; i < lesson_episodes.length; i++) {
      xmlHttp[i] = new XMLHttpRequest();
      xmlHttp[i].episode = lesson_episodes[i];  /* To enable use this later. */
      xmlHttp[i].onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var article_here = document.getElementById(this.episode);
        var parser = new DOMParser();
        var htmlDoc = parser.parseFromString(this.responseText,"text/html");
        var htmlDocArticle = htmlDoc.getElementsByTagName("article")[0];
        article_here.innerHTML = htmlDocArticle.innerHTML;
        }
      }
      episode_url = ".." + lesson_episodes[i];
      xmlHttp[i].open("GET", episode_url);
      xmlHttp[i].send(null);
    }
  }
~~~

Suggestions to improve the Javascript are welcomed.
