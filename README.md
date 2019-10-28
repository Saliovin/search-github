# search-github

## What is it?
This is a CLI tool used to search for repositories in Github. Outputs to a csv file.

## Requirements
- [Python 3](https://www.python.org/downloads/)

## How to install
```
pip install git+https://github.com/Saliovin/search-github.git
```

## How to use?
```
>>> search-github [-h] [-t TOKEN] search_term
```

## Arguments
```
positional arguments:
  search_term           Search term

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Github OAuth Access token
```

## Github OAth Access Token
A token is not needed to run the application, however, you are limited in the number of uses of the tool. You can create your own token and use it as a parameter to increase your number of uses per minute.

You can generate/use your own token [here](https://github.com/settings/tokens). No scopes are needed when generating the token. 


## Example
Search Github repositories for "tetris" with your own token:
```
search-github tetris -t <your-token>
```
