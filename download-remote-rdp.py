import argparse
from getpass import getpass
import requests
import urllib.parse


def main(username, password, app_name, output_filename, only_link):
    data = 'username={}&password={}&vhost=standard'.format(
        urllib.parse.quote(username),
        urllib.parse.quote(password)
    )
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 '
                             'Safari/537.36'
               }

    with requests.Session() as s:
        print('Downloading...')
        # get necessary cookies from redirection
        s.get('https://sso.nmbu.no', headers=headers)

        # login
        s.post('https://sso.nmbu.no/my.policy', headers=headers, data=data)

        # get necessary cookies from redirection
        s.get('https://sso.nmbu.no/saml/idp/res?'
              'id=/Common/SR-sso.nmbu.no-portal.nmbu.no', headers=headers)

        # get list of apps
        response = s.post('https://portal.nmbu.no/f5vdi/'
                          'rdp/resource/Common/HomeOffice', headers=headers)
        apps = response.json()['items']

        # filter for given name
        iterator = (app['launchUri'] for app in apps
                    if app['caption'].upper() == app_name.upper())
        launch_uri = next(iterator, None)
        assert launch_uri is not None, \
            'Cannot find application {}'.format(app_name)

        # get rdp link
        launch = s.get('https://portal.nmbu.no' + launch_uri, headers=headers,
                       allow_redirects=False)
        link = urllib.parse.unquote(launch.headers['Location'])
        print('link: {}'.format(link))

        if not only_link:  # save file also
            # convert link to text to save as .rdp
            # remove scheme from the start rdp://a?
            content = link[8:].replace('&', '\n').replace('=', ':')

            with open(output_filename, 'w') as f:
                f.write(content)

        print('Done!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Auto-downloader of remote desktop files for NMBU from '
                    'portal.nmbu.no')
    parser.add_argument('-app', '--app-name', default='RealTek',
                        help='name of application (default=RealTek)')
    parser.add_argument('-f', '--filename',
                        help='path to save .rdp file')
    parser.add_argument('-l', '--only-link', action='store_true', default=False)
    args = parser.parse_args()
    if args.filename is None:
        args.filename = args.app_name + '.rdp'

    username = input('Username: ')
    password = getpass()
    main(username, password, args.app_name, args.filename, args.only_link)
