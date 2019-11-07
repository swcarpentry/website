PY=python3

current_dir = $(shell pwd)

all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## dashboard  : update data about status of projects - requires ~/.git-token.
dashboard :
	${PY} bin/get-dashboard.py ${HOME}/.git-token _data/dashboard.yml

## serve      : run a local server.
serve : 
	bundle exec jekyll serve --config _config.yml,_config_dev.yml --future

dockerserve:
	docker run --rm --volume="${current_dir}:/srv/jekyll" --volume="${current_dir}/vendor/bundle:/usr/local/bundle" -p 127.0.0.1:4000:4000/tcp -it jekyll/jekyll:3.8 jekyll serve --config _config.yml,_config_dev.yml --future

## site       : build files but do not run a server.
site : 
	bundle exec jekyll build --incremental

## dockersite : using Docker jekyll for dependencies
dockersite:
	docker run --rm --volume="${current_dir}:/srv/jekyll" --volume="${current_dir}/vendor/bundle:/usr/local/bundle" -i jekyll/jekyll:3.8  jekyll build

## install    : install missing Ruby gems using bundle.
install :
	bundle install

## everything : rebuild all data files and then serve the site
everything:
	@make amy
	@make dashboard
	@make serve

#-------------------------------------------------------------------------------

## clean      : clean up junk files.
clean :
	rm -rf _site
	rm -rf .sass-cache
	find . -name '*~' -exec rm {} \;
	find . -name .DS_Store -exec rm {} \;
