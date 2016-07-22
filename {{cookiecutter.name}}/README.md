# Tests for {{cookiecutter.name}}
This repository contains tests for [{{cookiecutter.name}}]({{cookiecutter.url}}).

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}/blob/master/LICENSE)
[![travis](https://img.shields.io/travis/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}.svg?label=travis)](http://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}/)
[![requirements](https://img.shields.io/requires/github/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}.svg)](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}/requirements/?branch=master)

## How to run the tests locally

### Clone the repository
If you have cloned this project already then you can skip this, otherwise you'll
need to clone this repo using Git. If you do not know how to clone a GitHub
repository, check out this [help page][git-clone] from GitHub.

If you think you would like to contribute to the tests by writing or maintaining
them in the future, it would be a good idea to create a fork of this repository
first, and then clone that. GitHub also has great documentation for
[forking a repository][git-fork].

### Install dependencies
To run these tests you will need to have [Python][python] and [tox][tox] installed.

### Run the tests
Tests are run using the command line using the `tox` command. By default this
will run all of the environments configured, including checking your tests against
recommended style conventions using [flake8][flake8].

To run against a different base URL, pass in a value for `--base-url`:

```bash
$ tox -- --base-url={{cookiecutter.url}}
```

To run against a different browser, pass in a value for `--driver`:

```bash
$ tox -- --driver=Chrome
```

To run a specific test, pass in a value for `-k`:

```bash
$ tox -- -k=test_my_feature
```

The pytest plugin that we use for running tests has a number of advanced
command line options available. To see the options available, run
`py.test --help`. The full documentation for the plugin can be found
[here][pytest-selenium].

[git-clone]: https://help.github.com/articles/cloning-a-repository/
[git-fork]: https://help.github.com/articles/fork-a-repo/
[python]: https://www.python.org/downloads/
[tox]: http://tox.readthedocs.io/en/latest/install.html
[flake8]: http://flake8.readthedocs.io/
[pytest-selenium]: http://pytest-selenium.readthedocs.org/
