---
layout: page
authors: ["Greg Wilson"]
title: "We Still Can't Have Nice Things Together"
date: 2016-09-05
time: "00:01:00"
tags: ["Opinion", "Software Carpentry"]
---

<p><b>This post originally appeared on the <a href="https://software-carpentry.org/">Software Carpentry website.</a></b></p>

Last year I used YAML and Norway to explain why [why we can't have nice things][nice-things].
We've just stumbled over a problem that has forced us to re-do some of the work we did
to publish our lessons a couple of months ago,
and which illustrates how openness can still be frustrating to actually do.
Are you sitting comfortably?
Then let's begin.

## GitHub can publish repositories as website.

If the user's ID is `gloom`, and the project's name is `despair`,
then the GitHub repository's URL is `http://github.com/gloom/despair`.
If that repository has a branch called `gh-pages`,
GitHub automatically creates a website at `http://gloom.github.io/despair`.

## You will never find a more wretched hive of scum and villainy than the web.

As a result,
sites and browsers need to take precautions,
some of which affect us.

1. Many sites (including GitHub) encourage people to use HTTPS (which is secure)
   rather than HTTP (which is not).
   In particular,
   newly-created repositories on GitHub will *only* serve GitHub Pages websites over HTTPS,
   and older sites are being pushed to switch over as well.
   This is often done using *redirection*:
   if you go to http://whatever (insecure HTTP),
   the website automatically redirects you to https://whatever (secure HTTPS).

2. If a browser loads a page using HTTPS (secure),
   and that page then tries to load CSS stylesheets or Javascript files using plain old HTTP (insecure),
   the browser won't do it.

## GitHub uses Jekyll to convert Markdown and HTML to published pages.

If Markdown or HTML files in the `gh-pages` branch have the right kind of header,
GitHub doesn't publish them as-is.
Instead,
it uses a tool called Jekyll to translate them.

Jekyll reads variables from a file in the project's root directory called `_config.yml`
and makes it available to pages as they're being translated.
For example,
if the configuration file defines a variable called `title`,
pages can refer to `site.title`.
This lets people avoid repeatedly repeating information repeatedly.

## Our web pages need to know where to find their CSS and Javascript.

Our lesson pages and workshop website pages have to refer to the CSS and Javascript we use to style them.
The simplest way to do this is to use *absolute references from the root* like this:

    <link rel="stylesheet" type="text/css" href="/css/pretty.css" />

The only part of this that matters for present purposes is the `href` URL.
It looks like an absolute path (i.e., it starts with a slash),
so web browsers will automatically put the name of the website's domain in front of it.
For example,
if the website is `http://woe.com`,
and the page is `http://woe.com/misery.html`,
then the browser will convert `/css/pretty.css`
to `http://woe.com/css/pretty.css`.

But wait:
if the GitHub repository's URL is `http://github.com/gloom/despair`.
its website is published at `http://gloom.github.io/despair`.
The last part of that URL --- `despair` --- *isn't* part of the domain name,
so the browser cuts it out when following absolute references.

For example,
imagine that the GitHub Pages website contains a page called `index.html`,
and that page has the CSS link above to `pretty.css`.
The browser will convert the URL to `http://gloom.github.io/css/pretty.css`,
*which is wrong*,
because the `despair` part of the path has been chopped out.

Oops.

## OK, let's just add the domain name.

One way to solve this is to use full URLs for resources instead of absolute paths.
For example,
instead of loading `/css/pretty.css`,
our web page could explicitly refer to `http://gloom.github.io/despair/css/pretty.css`.
That's easy...

...except we want to share page templates between many different websites,
each of which has a different base URL.
More specifically,
we want to have a single HTML file (let's call it `_layouts/page.html`)
that specifies our pages' fonts and color scheme,
places the logo in the right place,
and so on.
We don't want to have to edit that page for each website,
because then we'd have to re-do all our edits each time we wanted to make a style change
that affected all our sites.

## Variables to the rescue.

We're not the first people to run into this problem,
so GitHub provides some help.
When GitHub runs Jekyll to convert our pages,
it gives Jekyll all the variables we define in our repository's `_config.yml` file,
*and* another bunch of variables that GitHub automatically defines for us.
One of these is called `site.github.url`,
and its value is exactly the URL we want:
the sub-domain *with* the base URL of our website.

In our running example,
the value of `site.github.url` is `http://gloom.github.io/despair`.
Our layout can then use:

    <link rel="stylesheet" type="text/css" href="{% raw %}{{site.github.url}}{% endraw %}/css/pretty.css" />

to refer to things.
The double curly braces tell Jekyll to insert the variable's value,
so the link here becomes what we want.

## Or not.

Unfortunately,
GitHub always sets `site.github.url` to be the HTTP version of the site's URL,
rather than the HTTPS version.
Boom:
if the page is loaded via HTTPS (secure),
the URL for the CSS is just HTTP (insecure),
so the browser refuses to load it,
and the page appears without any styling.

## It gets worse.

There's another problem here.
We don't want our pages to have URLs that start with `gloom.github.io` ---
we want them to start with `optimism.org`,
because that's the name of *our* website.
GitHub lets us do this using something called a CNAME.
In brief,
we can tell GitHub that we want `gloom.github.io` to pretend to be `optimism.org`,
so that:

1. If someone goes to `http://gloom.github.io`,
   they are automatically redirected to `http://optimism.org`.

2. If someone goes to `http://optimism.org`,
   the pages are served from `http://gloom.github.io`,
   but the URL still appears to be `http://optimism.org`.

Oops:
if Jekyll used the variable `site.github.url` when creating the web pages,
all the URLs for CSS and Javascript in those pages
will have `http://gloom.github.io/despair` as their URL.
If the browser thinks it's going to `https://optimism.org` (with secure HTTPS),
then it has *two* reasons to refuse to load the CSS:
those files are coming from insecure URLs (HTTP instead of HTTPS),
and they're coming from a completely different domain.

## Let's load the styles from a fixed domain.

But hang on:
there's nothing wrong per se with loading files from another domain.
Why don't we do something like this for our CSS:

    <link rel="stylesheet" type="text/css" href="https://content.org/css/pretty.css" />

The difference here is that the URL always refers to a *fixed site*
(in this case, `content.org`)
and *always uses HTTPS*.
As long as that site has a valid certificate for HTTPS,
the browser will quite happily load this file.
And since the URL is independent of which website is hosting the page,
the configuration file can define a variable like `site.content_url` to be a fixed value,
and everything can refer to that
and it will all just work and we can go home.

But suppose we want to do some more work on the subway ride home.
We make a change to a page,
run Jekyll to convert the page to HTML,
open it in the browser---and the CSS doesn't load,
because *we're offline*.

This isn't a big problem for people who are creating workshop websites
(which is by far the most common use of our templates).
It *is* a problem for people who want to contribute to lessons, though,
since they will often want to preview their changes locally,
and may well be doing that work on a plane or while otherwise disconnected.

## Let's define our own variable.

All right,
let's try another approach.
Suppose each of our websites defines a variable called `site.baseurl` in its configuration file
to be the name of the project with a leading `/`.
All of our web pages can then refer to things using:

    <link rel="stylesheet" type="text/css" href="{% raw %}{{site.baseurl}}{% endraw %}/css/pretty.css" />

which Jekyll expands to something like:

    <link rel="stylesheet" type="text/css" href="/despair/css/pretty.css" />

If we access the page using HTTPS (secure),
everything is fine,
because this now looks like an absolute path below the name of the domain.
If we access the page using HTTP (insecure) and are redirected to HTTPS,
this is still fine (same reasons).
And if we are using a CNAME,
and have mapped `http://gloom.github.io` to `http://optimism.org`,
then:

1. `http://optimism.org/despair/index.html` is mapped to `http://gloom.github.io/despair/index.html`.

2. The browser translates the reference inside that page from `/despair/css/pretty.css`
   to `http://optimism.org/despair/css/pretty.css`.

3. The web then finds that file at `https://gloom.github.io/despair/css/pretty.css`,
   which is exactly what we want.

Yay!
We're done!
We can---

Wait.
What about offline work?
When we run Jekyll locally to preview pages,
it starts up a little web server at `http://localhost:4000`,
and tells you "please go to this URL to preview your pages".
That URL is *wrong* if we are using this `site.baseurl` trick:
we actually need to go to `http://localhost:4000/despair` to get everything.

## Interlude: What's standard may not be right for everyone.

Defining `site.baseurl` is [the standard workaround][baseurl] for the problem we're trying to solve,
but it's not a good solution for us.
First,
many of our users are newcomers to HTML templating,
web servers,
and pretty much everything else we've been discussing.
If we rely on `site.baseurl`,
people will (quite reasonably) follow Jekyll's instructions to go to `http://localhost:4000`,
get a "page not found" error,
and wonder what they've done wrong.
(This is not speculation.)

Second,
if we rely on `site.baseurl`,
then everyone who creates a new workshop website
will have to edit that site's `_config.yml` file
as well as its `index.html` file.
Given what we've seen in instructor training workshops,
that will significantly increase people's frustration quotient.

## Overriding variables.

Here's another approach.
When Jekyll runs on GitHub,
it reads its configuration from `_config.yml`,
and *only* from `_config.yml`.
When we run it on our desktops,
though,
we can tell Jekyll to read several configuration files,
each of which can re-set variables set in previous files.
We can therefore create a second configuration file called `_config_local.yml` (or any other name we choose)
and have it define `site.baseurl` to be the empty string.
When we want to preview locally,
we pass Jekyll extra parameters to tell it to read this configuration file,
and all the URLs are then correct for a local build.

This works ---
until someone just runs `jekyll serve` on the command line
as they would normally do
(and as all the online documentation tells them to).
Boom:
the CSS isn't loaded.
Again,
this isn't speculation
(though it probably affects fewer people).

## Let's use relative URLs.

What if we don't use absolute URLs at all?
What if we use *relative URLs* everywhere?
If a page is in the root directory of our website,
it can refer to the CSS files using:

    <link rel="stylesheet" type="text/css" href="./css/pretty.css" />

If a page is in a sub-directory,
it can use:

    <link rel="stylesheet" type="text/css" href="../css/pretty.css" />

i.e., use `..` instead of `.` as the first part of the path to the CSS file.
That will always work;
the trick is to get the path to the root directory of the website into each page.

A sensible system would automatically give us a variable
with the path to the project's root directory.
Jekyll doesn't,
but we can define a variable for ourselves in each page's header.
If the page is in the root directory, `page.root` is `.`;
if it's a level down, `page.root` is `..`,
and so on.
The layout pages can then link to the CSS using:

    <link rel="stylesheet" type="text/css" href="{% raw %}{{page.root}}{% endraw %}/css/pretty.css" />

Requiring every single page to define a particular variable
when almost all of those pages will give it the same value
feels like sloppy programming practice.
Luckily for us,
Jekyll provides a way to set a default.
If we add this:

    defaults:
      - values:
          root: ..

to `_config.yml`,
then every page gets a variable called `root` with the value `..`.
This *almost* does what we want:
when we compile the Markdown file `melancholy.md`,
we are creating a page `melancholy/index.html` in the output directory,
so that its URL is `http://gloom.github.io/despair/melancholy/`.
(By convention,
a URL that ends with a slash `/` is assumed to refer to a directory,
and the file we actually want is the `index.html` file in that directory.)
Thus,
all of our pages are one level below the root directory in the output directory,
so they all want `page.root` to be `..`

But there's one exception:
the home page of the lesson itself.
This page is `./index.html`,
i.e.,
it's the `index.html` file in the root directory of the whole lesson,
so its `page.root` needs to be `.` rather than `..`
We can handle that by explicitly defining `page.root` in `index.md`,
which overrides the default set in `_config.yml`.
Once we've done that,
our pages, layouts, and included HTML fragments can all use `{% raw %}{{page.root}}{% endraw %}/this/that`
to refer to whatever they want.
It's not ideal --- we'll have to explain it to people who've used Jekyll before,
and if we ever create deeper directory hierarchies,
it will quickly become as complicated as the alternatives we've discarded ---
but it's good enough for now.

## How this got into production.

The new template that we deployed in June 2016 uses `site.github.url`.
We recognized the problem with HTTP vs. HTTPS early on,
so the standard layouts shared by all the lessons do this:

    <link rel="stylesheet" type="text/css" href="{% raw %}{{ site.github.url | replace_first: 'http:', 'https:' }}{% endraw %}/css/pretty.css" />

i.e., they convert the `http` prefix given in `site.github.url` into `https`.
That solved the problem for pages served from `github.io` domains,
but not for domains using CNAME:
GitHub even says that [they don't support HTTPS and CNAME domains][github-cname] (paragraph 3).
I didn't spot this because I didn't think to test pages on CNAME'd domains:
once it worked for HTTPS on GitHub,
I assumed it would work everywhere.

I should have known better.
Hacks like turning `http` into `https` *always* break,
and if one of my GSoC students had tried to put something like this into production,
I would have told them to think again.

The real lesson from this episode is that we still can't have nice things ---
or rather,
we can't have them all at once.
GitHub Pages are a great way for people to build simple little web sites.
Templating tools like Jekyll are great too,
and HTTPS is essential,
but when you try to combine them,
you wind up with [this][science-experiment].
If we really want people to do open research,
we have to make openness a lot less frustrating.

[baseurl]: https://byparker.com/blog/2014/clearing-up-confusion-around-baseurl/
[github-cname]: https://help.github.com/articles/securing-your-github-pages-site-with-https/
[nice-things]: {{site.url}}/blog/2015/06/why-we-cant-have-nice-things.html
[science-experiment]: http://imgur.com/pkg1qIE?r
