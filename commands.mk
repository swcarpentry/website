## ------------------------------------------------------------------------------

PY=python3

## amy        : update workshop and other data from AMY.
amy :
	${PY} bin/get-amy.py https://amy.software-carpentry.org/api/v1/ _data/amy.yml

## dashboard  : update data about status of projects.
dashboard :
	${PY} bin/get-dashboard.py ~/git-token.txt _data/dashboard.yml

## includes   : update include file listing from disk.
includes :
	${PY} bin/get-includes.py _data/includes.yml
