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

EMAIL_FILENAMES = $(wildcard raw/discuss-*.html)

all : cooked/repo-results.csv cooked/instructor-results.csv cooked/email-results.csv

cooked/repo-results.csv : raw/repo-data.csv raw/repo-names-genders.csv bin/analyze-repo-data.py
	python bin/analyze-repo-data.py raw/repo-names-genders.csv < raw/repo-data.csv > cooked/repo-results.csv

cooked/instructor-results.csv : raw/instructor-data.csv bin/analyze-instructor-data.py
	python bin/analyze-instructor-data.py < raw/instructor-data.csv > cooked/instructor-results.csv

cooked/email-results.csv : ${EMAIL_FILENAMES} raw/email-names-genders.csv bin/analyze-email-names.py
	python bin/analyze-email-names.py raw/email-names-genders.csv raw/discuss-*.html > cooked/email-results.csv

raw/repo-data.csv :
	python bin/get-repo.py ${USERNAME} ${PASSWORD} 2016-01-01 2016-01-31 ${REPOS} > raw/repo-data.csv

clean :
	find . -name '*~' -exec rm {} \;
	find . -name .DS_Store -exec rm {} \;

