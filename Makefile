PY=python3

all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## amy        : update workshop and other data from AMY.
amy :
	${PY} bin/get-amy.py -u https://amy.software-carpentry.org/api/v1/ -o _data/amy.yml --tags-any=SWC

## dashboard  : update data about status of projects - requires ~/.git-token.
dashboard :
	${PY} bin/get-dashboard.py ${HOME}/.git-token _data/dashboard.yml

## includes   : update include file listing from disk.
includes :
	${PY} bin/get-includes.py _data/includes.yml

## serve      : run a local server.
serve : 
	bundle exec jekyll serve --config _config.yml,_config_dev.yml --future

## site       : build files but do not run a server.
site : 
	bundle exec jekyll build --incremental

## install    : install missing Ruby gems using bundle.
install :
	bundle install

## everything : rebuild all data files and then serve the site
everything:
	@make amy
	@make dashboard
	@make includes
	@make serve

#-------------------------------------------------------------------------------

## clean      : clean up junk files.
clean :
	rm -rf _site
	rm -rf .sass-cache
	find . -name '*~' -exec rm {} \;
	find . -name .DS_Store -exec rm {} \;
