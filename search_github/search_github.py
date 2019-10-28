import csv
import requests
import argparse
from datetime import datetime
import urllib.parse as parse


def ini_arguments():
    """
    Initialize and read arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("search_term", type=str, help="Search term")
    parser.add_argument("-t", "--token", type=str, nargs=1, default='', help='Github OAuth Access token')
    return parser.parse_args()


def trim_list(repos):
    return [{'name': repo['name'], 'description': repo['description'], 'url': repo['html_url'],
             'language': repo['language'], 'updated': repo['updated_at']} for repo in repos]


def search_github(search_term, auth_header):
    github_search_link = "https://api.github.com/search/repositories"
    parameters = {'q': parse.quote_plus(search_term), 'per_page': 100}
    response = requests.get(github_search_link, params=parameters, headers=auth_header)
    repos = response.json()['items']

    while 'next' in response.links.keys():
        response = requests.get(github_search_link, params=parameters, headers=auth_header)
        repos.extend(response.json()['items'])
        if len(repos) > 1000:
            return repos[0:1000]

    return repos


def create_csv(repos):
    with open(f'output-{datetime.now().strftime("%y-%m-%d-%H-%M")}.csv', "w+", newline='', encoding='utf8') as csv_file:
        writer = csv.DictWriter(csv_file, ["name", "description", "url", "language", "updated"], delimiter=',')
        writer.writeheader()
        writer.writerows(repos)


def main():
    parsed = ini_arguments()
    token = {'Authorization': f'token {parsed.token[0]}'}
    create_csv(trim_list(search_github(parsed.search_term, token)))


if __name__ == '__main__':
    main()
