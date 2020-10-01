[![Build Status](https://travis-ci.org/swcarpentry/website.svg?branch=gh-pages)](https://travis-ci.org/swcarpentry/website)

# Software Carpentry Website

This is the repository for the new [Software Carpentry website](http://software-carpentry.org).
Please submit additions and fixes as pull requests to [our GitHub repository](https://github.com/swcarpentry/website).

*   [Setup](#setup)
*   [Previewing](#previewing)
*   [Development](#development)
    *   [Write a Blog Post](#blog)
    *   [Create a New Page](#page)
    *   [Add a Workshop](#workshop)
*   [The Details](#details)

Lessons are not stored in this repository:
please see [the lessons page](http://software-carpentry.org/lessons/)
for links to their repositories.

> Software Carpentry is an open project,
> and we welcome contributions of all kinds.
> By contributing,
> you are agreeing that Software Carpentry may redistribute your work
> under [these licenses](http://software-carpentry.org/license/),
> and to abide by [our code of conduct](http://software-carpentry.org/conduct/).

## Setup <a name="setup"></a>

The website uses [Jekyll](http://jekyllrb.com/), a static website generator written in Ruby.
You need to have Version 2.1.0 or higher of Ruby and the package manager Bundler (The package manager is used to make sure you use exactly the same versions of software as GitHub Pages).
Bundler can be installed with `$ gem install bundler`.
If you are on Linux, you will need to install the Ruby header files (e.g., `$ sudo apt-get install ruby-dev` on Debian/Ubuntu).
After checking out the repository, please run:

**Alternative Method**: If you have Docker installed on your system, you may be able to use the `make dockerbuild` and `make dockerserve` targets. These `Makefile` targets will install all Jekyll dependencies into the folder `vendor/` and build/serve the website respectively.

```
$ bundle install
```

to install Jekyll and the software it depends on.
You may consult [Using Jekyll with Pages](https://help.github.com/articles/using-jekyll-with-pages/) for further instructions.

You will also need [Python 3](http://python.org/) with
[PyYAML](https://pypi.python.org/pypi/PyYAML/) available in order to
re-generate the [data files](#details) the site depends on.

## Previewing <a name="previewing"></a>

Please do **not** use `jekyll build` or `jekyll serve` directly to build or view the website.
Instead, you should use the following commands:

*   `make` or `make commands`: list available commands.
*   `make serve`: build files locally and run a server at [http://0.0.0.0:4000/](http://0.0.0.0:4000/) for viewing.
    This is the best way to preview the site.
*   `make site`: build files locally, but do not serve them dynamically.
*   `make clean` removes the `_site` directory and any Emacs editor backup files littering the source directories.

The [details](#details) describes a few more advanced commands as well.
Please note that rebuilding this site can take 3-4 minutes on a moderately powerful laptop,
and occasionally times out on GitHub.
We're working on it...

## Development <a name="development"></a>

<a name="blog"></a>
To **write a blog post**,
create a file called `_posts/YYYY/MM/YYYY-MM-DD-some-title.html` or  `_posts/YYYY/MM/YYYY-MM-DD-some-title.md`
(for HTML and Markdown respectively).
YYYY is the 4-digit year of the post, MM the 2-digit month, and DD the 2-digit day;
`some-title` can be any hyphenated string of words that do not include special characters such as quotes.
Please do *not* use underscores or periods in the names.
When published,
your blog post will appear as `http://software-carpentry.org/blog/YYYY/MM/some-title.html`.

The YAML header of a blog post must look like this:

~~~
---
layout: post
authors: ["Your Name"]
title: "A Title-Cased Title for the Post"
date: YYYY-MM-DD
time: "hh:mm:ss"
tags: ["Some Category", "Some Other Category"]
---
~~~

where `YYYY-MM-DD` is replaced by the post's date and `hh:mm:ss` by the post's time.
Note that the time *must* be quoted so that the colons it contains do not confuse Jekyll's YAML parser.
Note also that `authors` is a list---if the post has more than one author,
please format the list like this:

~~~
...
authors: ["First Author", "Second Author", "Third Author"]
...
~~~

rather than running all the authors' names together in one long string.

<a name="page"></a>
To **create a new page**,
add a file to the `pages` directory.
This can be written in either Markdown or HTML,
and must have the following YAML header:

~~~
layout: page-fullwidth
permalink: /some/path/
title: Title in Title Case
~~~

You must then also add the page to `_data/navigation.yml`,
which is used to generate the site's pull-down navigation menu.

<a name="workshop"></a>
To **add a workshop**,
fill in the [workshop request form](https://amy.carpentries.org/workshops/swc/request/) online.
You should fill in this form even for self-organized workshops in order to get your workshop into our database.

Do *not* edit the YAML in `_data/amy.yml`:
this is overwritten every time the website is rebuilt on the server.

## The Details <a name="details"></a>

### Data Files

This website depends on three data files,
each of which is rebuilt by `make`:

*   `make amy` regenerates `_data/amy.yml`,
    which contains information about upcoming workshops, instructors' locations, and so on
    that is fetched from [our online workshop management tool](https://github.com/swcarpentry/amy/).
    You must be logged in to [AMY](http://amy.carpentries.org) in order to run this.

*   `make dashboard` generates `_data/dashboard.yml`,
    which contains information about the state of our GitHub repositories.
    In order to run this,
    you must get a [GitHub API token](https://github.com/blog/1509-personal-api-tokens)
    and store it in `$HOME/.git-token`.

*   `make includes` to rebuild the data file `_data/includes.yml`.
    This does not require special permissions,
    but is only necessary if you have added more people to `_includes/people` or more projects to `_includes/projects`.
    (We plan to move the content of these two directories to `_data` so that `make includes` will no longer be needed.)

We cache the output of these commands in the `_data` directory
so that people can rebuild the site without needing special permissions.

### Styles

The files in the `_sass` and `assets` directories control the appearance of this site.
Their contents are pulled in manually from a stand-alone [https://github.com/swcarpentry/styles](styles) repository,
which also controls the appearance of
the [workshop template](https://github.com/swcarpentry/workshop-template)
and [lesson template](https://github.com/swcarpentry/lesson-template).
Please [contact us](mailto:admin@software-carpentry.org) before modifying any of these files
so that we can figure out the best way to incorporate your improvements.

### Rebuilding the Main Web Site

A copy of the shell script `bin/rebuild-site.sh` is installed in the website's home directory on our server
and re-run hourly by cron.
If you are able to ssh to the server,
it can be re-run manually as:

~~~
$ ssh software-carpentry.org ./rebuild-site.sh
~~~

### Previewing the live site

Once changes to the site are merged, they can take several hours to go live.  In the meantime, changes can be [previewed here](http://software-carpentry.org.s3-website-us-east-1.amazonaws.com/). 

### Instructions

If there is something wrong with the content on that web site,
feel free to
[file an issue with this repository](https://github.com/swcarpentry/website/issues),
or formulate a pull request.
Note that most pages will come with an edit link in the bottom right corner.


