# Software Carpentry Website

This is the repository for the [Software Carpentry website](http://software-carpentry.org).
Please submit additions and fixes as pull requests through [our GitHub repository](https://github.com/swcarpentry/site).

The website template and theme is from [Feeling Responsive](https://github.com/Phlow/feeling-responsive),
a flexible theme for Jekyll built on the Foundation framework by [Moritz Sauer](https://github.com/Phlow)
which is used by the [Data Carpentry](http://datacarpentry.org) website.

Run `make` in the root directory for a list of commands.
Please note that `make amy` and `make dashboard` may require special permissions
(since they talk to the Carpentry instructor database and GitHub respectively).
Their output is cached in this repository,
so `make build` and `make serve` will work without them being run.

Please also note that rebuilding this site can take 3-4 minutes on a moderately powerful laptop,
and occasionally times out on GitHub.
We're working on it...
