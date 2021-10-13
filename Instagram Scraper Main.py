import json
import time
import pandas as pd
import urllib.request
from collections import Counter
from Instagram_Scraper import login_and_get_post_links, get_post_details, bio

username_search_list = [
    'joshradnor',
    'nph',
    'courteneycoxofficial',
    'lisakudrow',
    'mattyperry4',
    'mleblanc',
    '_schwim_',
    'reesewitherspoon',
    'alysonhannigan',
    'cobiesmulders',
    'cristinmilioti',
    'emilia_clarke',
    'sophiet',
    'maisie_williams',
    'kitharingtonig',
    'iampeterdinklage',
    'iamlenaheadey',
    'roseleslie_got',
    'maddenrichard']

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

for username in username_search_list:
    #Extract data from bio
    Bios = bio(username)
    results1 = {
        'Username': username,
        'Post Numbers' : str(Bios['Post Numbers']),
        'Followers Number': str(Bios['Followers Number']),
        'Following Numbers': str(Bios['Following Numbers']),
        'Bio': str(Bios['Bio'])
    }

    #Extract links of posts of an username
    links = login_and_get_post_links(username, post_count=24)

    #Make a list from details of all posts of an username 
    counter_links = len(links)
    result_list = []
    while counter_links != 0:
        for link in links:
            results2 = get_post_details(link)
            result = Merge(results1,results2)
            result_list.append(result)
            counter_links = counter_links - 1

    #Make a JSON file for every username
    json_object = json.dumps(result_list,default=lambda o: '<not serializable>', indent = 4)
    with open(str(username) +'.json', "w") as outfile:
        outfile.write(json_object)
    

    

