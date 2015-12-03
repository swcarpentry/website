# Software Carpentry Website

This is the repository for the new [Software Carpentry website](http://software-carpentry.org).
Please submit additions and fixes as pull requests through [our GitHub repository](https://github.com/swcarpentry/site).

The website template and theme is based on [Feeling Responsive](https://github.com/Phlow/feeling-responsive),
a flexible theme for Jekyll built on the Foundation framework by [Moritz Sauer](https://github.com/Phlow)
which is also used by the [Data Carpentry](http://datacarpentry.org) website.

## Development

Please do **not** use `jekyll build` or `jekyll serve` directly to build or view the website.
Instead,
you should use the following commands:

*   `make` or `make commands`: list available commands.
*   `make build`: build files locally, but do not serve them dynamically.
*   `make serve`: build files locally and run a server at [http://0.0.0.0:4000/](http://0.0.0.0:4000/) for viewing.
    (This is the preferred way of previewing the site.)
*   `make amy` and `make dashboard` to rebuild the data files `_data/amy.yml` and `_data/dashboard.yml`,
    which contain information about upcoming workshops and the state of our GitHub repositories respectively.
    Note that you need special permission to run either;
    we cache the output of these commands in the `_data` directory
    so that you can rebuild the site without running either.
*   `make includes` to rebuild the data file `_data/includes.yml`.
    This does not require special permissions,
    but is only necessary if you have added more people to `_includes/people`
    or more projects to `_includes/projects`.
    (We plan to move the content of these two directories to `_data`
    so that `make includes` will no longer be needed:
    see issue #41 for more information.)
*   `make clean` removes the `_site` directory and any Emacs editor backup files littering the source directories.

Please note that rebuilding this site can take 3-4 minutes on a moderately powerful laptop,
and occasionally times out on GitHub.
We're working on it...
