# API'a sorgu göndermek için requests paketini kullanıyoruz.
import requests
# JSON formatındaki verileri almak ve yazdırmak için json paketine ihtiyacımız var.
import json
import config
from pprint import pprint


def search_place(query):
    # Arama yapmak istediğimiz için aşağıdaki URL'yi kullanıyoruz. Arama dışındaki örneklerde URL değişecek.
    url = 'https://api.foursquare.com/v2/venues/search'

    # Sorgu parametrelerini tanımlayalım.
    """
    client_id ve client_secret kendimizi Foursquare'e tanımlamak için kullandığımız anahtarlar.
    v değeri API'ın hangi versiyonunu kullandığımızı gösteriyor ve zorunlu bir alan.
    query değeri de yapmak istediğimiz sorgunun arama kelimesi
    """
    params = dict(
    client_id=config.FOURSQUARE_Client_ID,
    client_secret=config.FOURSQUARE_Client_Secret,
    v='20170801',
    near="Istanbul, Turkey",
    intent="browse",
    query=query,
    limit = 1
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    # pprint(data)
    return data['response']['venues'][0]['id']



def get_url(query):
    venue_id = search_place(query)
    url = 'https://api.foursquare.com/v2/venues/{}'.format(venue_id)
    params = dict(client_id=config.FOURSQUARE_Client_ID, client_secret=config.FOURSQUARE_Client_Secret,v='20170801')
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    pprint(data)
