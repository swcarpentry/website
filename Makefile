PY=python3

all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## amy        : update workshop and other data from AMY.
amy :
	${PY} bin/amy.py https://amy.software-carpentry.org/api/v1/ _data/amy.yml

## dashboard  : update data about status of projects - requires ~/.git-token.
dashboard :
	${PY} bin/dashboard.py ${HOME}/.git-token _data/dashboard.yml

## week  : create skeleton for post with week update - requires ~/.git-token.
week :
	${PY} bin/week.py ${HOME}/.git-token

## includes   : update include file listing from disk.
includes :
	${PY} bin/includes.py _data/includes.yml

## serve      : run a local server.
serve : 
	bundle exec jekyll serve --config _config.yml,_config_dev.yml --verbose

## site       : build files but do not run a server.
site : 
	bundle exec jekyll build

## install    : install missing Ruby gems using bundle.
install :
	bundle install

#-------------------------------------------------------------------------------

## clean      : clean up junk files.
clean :
	rm -rf _site
	rm -rf .sass-cache
	find . -name '*~' -exec rm {} \;
	find . -name .DS_Store -exec rm {} \;
