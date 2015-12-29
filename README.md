# Software Carpentry Website

This is the repository for the new [Software Carpentry website](http://software-carpentry.org).
Please submit additions and fixes as pull requests to [our GitHub repository](https://github.com/swcarpentry/website).

*   [Setup](#setup)
*   [Previewing](#previewing)
*   [Development](#development)
    *   [Write a Blog Post](#blog)
    *   [Create a New Page](#page)
    *   [Add a Workshop](#workshop)

## Setup <a name="setup"></a>

The website uses Jekyll, a static website generator written in Ruby.
You need to have Version 2.0.0 or higher of Ruby and the package manager Bundler.
(The package manager is used to make sure you use exactly the same versions of software as GitHub Pages.)
After checking out the repository, please run:

```
$ bundle install
```

to install Jekyll and the software it depends on.
You may consult [Using Jekyll with Pages](https://help.github.com/articles/using-jekyll-with-pages/) for further instructions.

You will also need Python 3.0 or higher in order to re-generate the [data files](#datafiles) the site depends on.

## Previewing <a name="previewing"></a>

Please do **not** use `jekyll build` or `jekyll serve` directly to build or view the website.
Instead, you should use the following commands:

*   `make` or `make commands`: list available commands.
*   `make serve`: build files locally and run a server at [http://0.0.0.0:4000/](http://0.0.0.0:4000/) for viewing.
    This is the best way to preview the site.
*   `make site`: build files locally, but do not serve them dynamically.
*   `make amy` and `make dashboard` to rebuild the data files `_data/amy.yml` and `_data/dashboard.yml`,
    which contain information about upcoming workshops and the state of our GitHub repositories respectively.
    You need special permission to run these:
    we cache the output of these commands in the `_data` directory so that you can rebuild the site without running either.
*   `make includes` to rebuild the data file `_data/includes.yml`.
    This does not require special permissions,
    but is only necessary if you have added more people to `_includes/people` or more projects to `_includes/projects`.
    (We plan to move the content of these two directories to `_data` so that `make includes` will no longer be needed.)
*   `make install` installs or updates Ruby gems (packages) to match those used by GitHub Pages.
*   `make clean` removes the `_site` directory and any Emacs editor backup files littering the source directories.

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
layout: post
author: "Your Name"
title: "A Title-Cased Title for the Post"
date: YYYY-MM-DD
time: "hh:mm:ss"
category: ["Some Category", "Some Other Category"]
~~~

where `YYYY-MM-DD` is replaced by the post's date and `hh:mm:ss` by the post's time.
Note that the time *must* be quoted so that the colons it contains do not confuse Jekyll's YAML parser.

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
fill in the [workshop request form](https://amy.software-carpentry.org/workshops/swc/request/) online.
You should fill in this form even for self-organized workshops in order to get your workshop into our database.

Do *not* edit the YAML in `_data/amy.yml`:
this is overwritten every time the website is rebuilt on the server.
