#  Test Framework Python, Unittest

The Test Framework has been verified with:
- Python 3.7
- pip 19.1.1
- browser Chrome Version 75.0.3770.100 (Official Build) (64-bit)
- browser Firefox Version 67.0.4 (64-bit)
- Mac OS 10.13.6

## Prerequisites

The Test Framework requires Python 3 and pip installed. To verify if you have both packages installed run the following commands:

`python3 --version`
`pip --version`

If pip and Python 3 are installed you should see version of each package. Otherwise you'll see an error message.

If you do not have Python 3 and pip installed, use your operating system package manager to install both tools.
On Mac OS you could use brew:

`brew install python`


## Install Requirements

`pip install -r requirements.txt` from project folder

If there is a permissions error add a `--user` flag to the end of the command.

If there is an SSL error, for example:

"Could not fetch URL https://pypi.python.org/simple/unittest/: There was a problem confirming the ssl certificate:
[SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:590) - skipping"

Try to upgrade pip using one of the following commands:

`pip install -U pip`
`curl https://bootstrap.pypa.io/get-pip.py | python3`
`pip2 install --upgrade pip`

Add this directory to your python path (replace with your own local path)

`export PYTHONPATH=${PYTHONPATH}:$(pwd)`

