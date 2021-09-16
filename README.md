# Introduction

Project Peaches is a all-in-one grocery & retail inventory management system. It provides the solution for ship-to-customer grocery sales.

### Technology
- Backend: Flask Python
- Database: Postgres 12
- Front-end: React 18
- Containerization: Docker compose
- API & communication: RESTful APIs.

# Getting started
This guide assumes you have the following dependencies already set up:
- Docker
- Python 3.9.0

If you haven't got those ready, please refer to their documentations online.

## Backend
**Database**
First, start the docker & the database.
```
$ docker-compose up
```
This will install (if there's none) and run the Postgres v12 RMDBS. The database is avaialble in port `5432`.

The database admininistation software which allows direct access & SQL execution into the database is also available in via your browser at `localhost:8080`.

**Flask server**
To start the server, first activate the virtual python environment.
```sh
$ source backend/venv/bin/activate
```

Then start flask in the same terminal.
```sh
flask run
```
> You need to activate the virtual python environment for every new terminal you start.

**Test**
To run test, activate virtual environment (if not already), then run:
```sh
$ pytest
```

Pytest is a python testing framework. Any python file containing the word `test_` will be run. Refer to Pytest documentation to learn how to write tests.

## Front-end
_To be updated_

## Source control workflow
### Create a new branch
```sh
git checkout -b <branch_name>
```
Where `<branch_name>` is a string without space. It is recomended to name your branch with a descriptive name, like `feature_add_new_route`, for instance.

### Stage the changes
After you've done with your changes, it's time to stage them for subsequent committing.
```sh
$ git add <path_to_modified_files>
```
Where `<path_to_modified_files>` is the path to files of change. If the path refer to a directory instead of a file, all changed files within that directory will be staged.

To unstage, run `git reset <path_to_modified_files>`. Same rule applies.

### Commit the changes
After you've staged your desired change, create a commit.

```
$ git commit -m "<your message>".
```
Give it a descriptive message.

### Push to origin
When you are ready to have your code reviewed by other people, run:
```sh
git push <branch_to_be_pushed>
```

A pop up will appear from github server. Follow the link to create a pull request.
### Update main

After your changes has been approved and merged to main, your `main` will become outdated. It is therefore necessary to sync with Github (aka upstream).
```
$ git checkout main
$ git pull origin
```

And that's how you ace the git workflow ;).
