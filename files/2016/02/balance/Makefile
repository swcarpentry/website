# Rebuild data on gendered contributions to Software Carpentry projects.
# USAGE:
#   make USERNAME=aturing PASSWORD=bletchley repo_data.csv <<- re-generate repository data
#   make all <<- re-generate repo_results.csv and instructor_results.csv

REPOS = \
swcarpentry/shell-novice \
swcarpentry/git-novice \
swcarpentry/hg-novice \
swcarpentry/sql-novice-survey \
swcarpentry/python-novice-inflammation \
swcarpentry/r-novice-inflammation \
swcarpentry/r-novice-gapminder \
swcarpentry/matlab-novice-inflammation \
swcarpentry/make-novice

all : cooked/repo-results.csv cooked/instructor-results.csv

cooked/repo-results.csv : raw/repo-data.csv raw/names-genders.csv bin/analyze-repo-data.py
	python bin/analyze-repo-data.py raw/names-genders.csv < raw/repo-data.csv > cooked/repo-results.csv

cooked/instructor-results.csv : raw/instructor-data.csv
	python bin/analyze-instructor-data.py < raw/instructor-data.csv > cooked/instructor-results.csv

raw/repo-data.csv :
	python bin/get-repo.py ${USERNAME} ${PASSWORD} 2016-01-01 2016-01-31 ${REPOS} > raw/repo-data.csv

clean :
	find . -name '*~' -exec rm {} \;
	find . -name .DS_Store -exec rm {} \;

