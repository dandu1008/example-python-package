from __future__ import print_function
import requests

def main():
    print('Hello, World!')
    return True

def get_example():
    url = 'http://www.example.com/'
    print('GET {0}'.format(url))
    response = requests.get('http://www.example.com/')
    print('Response status: {0}'.format(response.status_code))

if __name__ == '__main__':
    main()
