# DRONESHIELD TECHNICAL TEST

## PURPOSE

The purpose of the doc is to complete the technical test for Droneshield with satisfaction to all requested requirements. Submitted for your approval is a curated testing suite of scripts created to be an end-to-end solution for both the UI and API. Included are the installation and usage instructions. For any questions, comments, or concerns contact the author `Stephen Dodd` at `stephen@doddtek.com`.

## METHODOLOGY

For this testing suite we have chosen the `Pytest` and `Playwright` frameworks for both the UI and API tests. These were chosen for a number of reasons, most of which are expressed in the [EXERCISE-1.md](https://github.com/scdodd83/droneshieldDoddTest/blob/main/EXERCISE-1.md) and [EXERCISE-2.md](https://github.com/scdodd83/droneshieldDoddTest/blob/main/EXERCISE-2.md) files found in this repo.

## GETTING STARTED

This automation suite will require a few things:

* pip
* python3
* Pytest
* Playwright

`Python3` and `pip` are common, but in case you don't already have these installed you can find the installation instructions for `pip` [here](https://pip.pypa.io/en/stable/installation/).

1. Install `pip`

```
sudo apt install pip
```

This should install `pip`. You can confirm this by running the following command:

```
pip --version
```

Confirm that you have the latest version available.

2. Install `Python3`

```
sudo apt install python3
```

This should install the latest version of `Python3`. You can confirm this by running the following command:

```
python3 --version
```

Confirm that you have the latest version available.

### INSTALLATION

The `Pytest` installtion instructions can be found [here](https://docs.pytest.org/en/stable/getting-started.html) if you would like a reference to follow.

1. To install `pip` run the following command in the command line:

```
pip install -U pytest
```

2. Make sure you have installed it correctly, and it's up to date:

```
$ pytest --version
pytest 8.3.3
```

The `Playwright` installation instructions can be found [here](https://playwright.dev/python/docs/intro) if you would like a reference to follow.

1. To install `Playwright` run the following command in the command line:

```
pip install pytest-playwright
```

2. Install `Playwright` browsers:

```
playwright install
```

3. Make sure you have installed it correctly, and it's up to date:

```
playwright --version
```

Confirm you have installed it correctly and it's up to date.

### USAGE
