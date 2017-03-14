# GroupMeAnalyticsProject
The purpose of this project is to retrieve information using the GroupMe API to calculate certain statistics.
## How To Run
#### Install Python 2.7
That can be found here: https://www.python.org/downloads/
#### Make sure pip is installed
It should be installed with 2.7.9 already but if not follow the steps here: https://pip.pypa.io/en/stable/installing/
#### Install Requests library
This is required if you want to work with APIs in Python. Run the following command from your project directory:
    pip install requests
#### Run the program
    python main.py
## Development Workflow
* The `master` branch at any time represents a stable (and tested) version of the code base.
* All development work should be performed in feature branches. In most cases, feature branches will be branched off of the `master` branch. Naming of the feature branches is up to the developer. Using your initials is helpful so we know who is working where, but not crucial. (Ex: `dd-feature_name`)
* Rebase off of `master` often, and especially before submitting a pull request to make sure your feature branch has the latest hotness.
* When commits are made, 1) describe what was done, 2) indicate the amount of time in hours it took to complete it, 3) reference issue numbers and close issues with commits. E.g. "Added Koala gem - 0.1 hours - referencing #590"
* When a feature branch is ready for master, send a Pull Request detailing the changes made, any dependency updates, screenshots of updates if needed, and any other information to help with the merge.
* The repo admin will be responsible for merging all pull requests, enforcing coding standards and generally keeping `master` stable and clean. In most cases the repo admin will be responsible for upgrading dependencies as well.
