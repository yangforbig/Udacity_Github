# To experiment with this code freely you will have to run this code locally.
# Take a look at the main() function for an example of how to use the code.
# We have provided example json output in the other code editor tabs for you to
# look at, but you will not be able to run any queries through our UI.
import json
import requests
import pprint

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    # This is the main function for making queries to the musicbrainz API.
    # A json document should be returned by the query.
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    # This adds an artist name to the query parameters before making
    # an API call to the function above.
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    # After we get our output, we can format it to be more readable
    # by using this function.
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data

'''
def main():

    Modify the function calls and indexing below to answer the questions on
    the next quiz. HINT: Note how the output we get from the site is a
    multi-level JSON document, so try making print statements to step through
    the structure one level at a time or copy the output to a separate output
    file.


    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    #pretty_print(results)

    artist_id = results["artists"][1]["id"]
    #print "\nARTIST:"
    pretty_print(results["artists"])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    #print "\nONE RELEASE:"
    pretty_print(releases[0], indent=2)

    release_titles = [r["title"] for r in releases]



    #print "\nALL TITLES:"
    #for t in release_titles:
    #    print t
'''
# How many bands named "First AID KIT"
'''
first_result = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AID KIT")
pretty_print(first_result)
count = 0
for e in first_result['artists']:
    if e['name'].upper() == 'FIRST AID KIT':
        count += 1
print count
'''
# Begin area name for Queen?
'''
second_result = query_by_name(ARTIST_URL, query_type["simple"], "QUEEN")
pretty_print(second_result)
for e in second_result['artists']:
    print e.get('begin-area')

'''
# Spanish ALIAS for Beatles?
# Language code for Spainsh is es
'''
third_result = query_by_name(ARTIST_URL, query_type['simple'], "BEATLES")
#pretty_print(third_result)

for e in third_result['artists']:
    if e.get('aliases') is not None:
        aliases = e.get('aliases')
        for e in aliases:
            if e.get('locale') == 'es':
                print e

'''

# Nirvana Disambiguation

fourth_result = query_by_name(ARTIST_URL, query_type['simple'], "Nirvana")
pretty_print(fourth_result)

for e in fourth_result['artists']:
    if e['name'].upper() == 'NIRVANA':
        print e.get('disambiguation')


# When was one direction formed?
'''
fifth_result = query_by_name(ARTIST_URL, query_type['simple'], "ONE DIRECTION")
#pretty_print(fifth_result)

for e in fifth_result['artists']:
    if e['name'].upper() == "ONE DIRECTION":
        print e.get('life-span')
'''
