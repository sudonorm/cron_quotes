# :clubs: cron_quotes
A repo containing code which can be used to pull quotes from an API on a daily basis using a Jenkins and a set-up CRON job

:floppy_disk: Operating system: Windows

:hammer:  Requirements: Jenkins, Python 3

:wrench:  Usage: 
- We need to pass in the username of the Windows environment to our Python script using argparse because we want to save the pulled quote to an Excel file in our Windows environment
- To achieve this, we will need to create a username credential in Jenkins and pass this in as an argument
- After this is done, the repo can be forked, and the script can be run from the Jenkins environment
