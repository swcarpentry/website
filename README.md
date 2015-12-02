# Software Carpentry Website

This is the repository for the [Software Carpentry website](http://software-carpentry.org).
Please submit additions and fixes as pull requests through [our GitHub repository](https://github.com/swcarpentry/site).

The website is build with Jekyll which is a static website generator written
in Ruby. You need to have a working Ruby (version 2.0.0 or higher) and you
need to have the package manager Bundler installed. The package manager is
used to make sure you are use locally exactly the same software GitHub Pages
will use on the cloud.

After checking out the repository, please run

```
$ bundle install
```

to install Jekyll and the other required software. Please consult [Using
Jekyll with Pages](https://help.github.com/articles/using-jekyll-with-pages/)
for further instructions.

The website template and theme is from [Feeling Responsive](https://github.com/Phlow/feeling-responsive),
a flexible theme built on the Foundation framework by [Moritz Sauer](https://github.com/Phlow)
which is used by the [Data Carpentry](http://datacarpentry.org) website.

Run `make` in the root directory for a list of commands.
Please note that `make amy` and `make dashboard` may require special permissions
(since they talk to the Carpentry instructor database and GitHub respectively).
Their output is cached in this repository,
so `make build` and `make serve` will work without them being run.

Please also note that rebuilding this site can take 3-4 minutes on a moderately powerful laptop,
and occasionally times out on GitHub.
We're working on it...
