# DRONESHIELD TECHNICAL TEST

## PURPOSE

The purpose of the doc is to complete the technical test for Droneshield with satisfaction to all requested requirements. Submitted for your approval is a curated testing suite of scripts created to be an end-to-end solution for both the UI and API. Included are the installation and usage instructions. For any questions, comments, or concerns feel free to contact me directly.

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
$ pip --version
pip 22.0.2
```

Confirm that you have the latest version available.

2. Install `Python3`

```
sudo apt install python3
```

This should install the latest version of `Python3`. You can confirm this by running the following command:

```
$ python3 --version
Python 3.10.12
```

Confirm that you have the latest version available.

### INSTALLATION

The `Pytest` installation instructions can be found [here](https://docs.pytest.org/en/stable/getting-started.html) if you would like a reference to follow.

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
$ playwright --version
Version 1.48.0
```

Confirm you have installed it correctly and it's up to date.

### CLONE THE REPO

Now that everything is installed correctly it's time to clone the repo:

1. Open a terminal.

2. Navigate to wherever you'd like to clone. 

```
cd wherever/you/want/to/go
```

3. Clone the repo.

```
git clone https://github.com/scdodd83/droneshieldDoddTest.git
```

### USAGE

A note on running the scripts: I did not want to hard code the credentials into the scripts. I know they were for testing purposes and largely irrelevant, but for the purposes of guaging flow and structure choice I opted to create a separate credentials file. Normally this file would be given to you separately, but to make things easier I'm going to give you the file name, placement, and payload.

#### CREDENTIALS:

1. Open the terminal and navigate to `tests`.

```
cd wherever/you/went/.../tests
```

2. Create the credentials file.
```
touch creds.py
```

3. Open the `creds.py` file in the editor of your choice.

4. Add the following lines:

```
# Stored credential file

username = "standard_user"
lockedout = "locked_out_user"
password = "secret_sauce"

api_user = "tester42"
api_pass = "terriblemethod"
```

5. Save.

This should create a `creds.py` file in the `droneshieldDoddTest/tests` directory. This will be necessary to run the scripts successfully.

#### HEADLESS

Headless mode just runs without the browser opening. Everything should be installed and ready. To run the test scripts:

1. Open a terminal.

2. Navigate to where you cloned the repo

```
cd navigate/to/where/you/went
```

3. To run the entire suite in headless mode:

```
pytest
```

4.  Observe the magic.

#### HEADED

 Headed mode opens a browser and shows you what's going on. To run the script in headed mode, run this in the terminal:

1. Run this command in the command line: 

```
pytest --headed
```

2. More magic, but this time with movement!

You can now observe it doing everything in a browser, but it's likely too quick to garner any real feel for what it's doing. It's just an option if you like to see things happening.

