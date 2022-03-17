import random
voted = {}
def vote(name):
    if voted.get(name):
        print("Kick out")
    else:
        voted[name] = True
        print("let them vote!")
        
vote("kyaw gyi")
vote("william")
vote('Thiha')
vote('kyaw gyi')
print(voted)


def get_data_from_url(url):
    return random.randint(0,1000)
    

urls = {}
def get_url(url):
    if urls.get(url):
        print("from hash")
        return urls[url]
    else:
        print("from server")
        data = get_data_from_url(url)
        urls[url] = data
        return data
    
get_url('facebook')
get_url('google')
get_url("quora")
get_url('facebook')
