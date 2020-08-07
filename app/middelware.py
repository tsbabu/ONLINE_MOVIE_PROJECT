import json
import http.client

class Moviesmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
        headers = {
                    'x-rapidapi-host': "imdb8.p.rapidapi.com",
                    'x-rapidapi-key': "4422ecdd22msh0284eaac7d64721p1d830ejsn5fc033392fd1"
                  }
        conn.request("GET", "/title/auto-complete?q=game%20of%20thr", headers=headers)
        res = conn.getresponse()
        data = res.read()
        x=data.decode("utf-8")
        dict_data = json.loads(x)
        a=open('app/raw/movies.json','w')
        json.dump(dict_data,a)

    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        return response