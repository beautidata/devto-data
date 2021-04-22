import requests
import json
from configparser import ConfigParser

config = ConfigParser()
config.read_file(open('settings.ini'))
api_key = config.get('devto', 'api_key')

baseurl = 'https://dev.to/api/'
username_endpoint = 'users/by_username'
username_url = baseurl + username_endpoint
headers = {'api_key': api_key}
username_payload = {'url': 'beautidata'}

article_endpoint = 'articles'
article_url = baseurl + article_endpoint
article_payload = {'per_page': 1000, 'tag': 'python', 'top': 60}

def collect_data():
    print('a program to get data from dev.to')
    u = requests.get(username_url, headers=headers, params = username_payload)
    print(u.status_code)
    print(u.json())

    a = requests.get(article_url, params = article_payload)
    print(a.status_code)
    #print(a.json())

    #articles = a.json()
    #print(articles)
    #for article in articles:
    #    print("%s: %s on %s" %(article['id'], article['title'], article['readable_publish_date']))

    post = requests.get('https://dev.to/bytesized/byte-sized-episode-2-the-creation-of-graph-theory-34g1')
    print(post.status_code)
    with open('post.html', 'w') as f:
        f.write(post.text)

def create_dict_from_jsonfile(filename):
    with open(filename) as f:
        json_dict = json.load(f)
    return json_dict

def save_post_html(post_dictionary):
    for post in post_dictionary:
        url = post_dictionary[post]['url']
        post_content = requests.get(url)
        post_filename = 'data' + str(post) + '.html'
        with open(post_filename, 'w') as f:
            f.write(post_content.text)

def main():
    print('a program for processing data from dev.to')
    filename_root = 'data/response-040921-latest-p'
    filename_end = '.json'
    all_posts = {}
    for x in range(1, 26):
        filename = filename_root + str(x) + filename_end
        #print(filename)
        page = create_dict_from_jsonfile(filename)
        for p in page:
            all_posts[p['id']] = p

    save_post_html(all_posts)




    

if __name__ == "__main__":
    main()