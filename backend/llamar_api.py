import requests


def buscar_noticias(query):
    
    url = "https://newsapi.org/v2/everything"

    params = {
        "q":query,
        "language":"es",
        "apiKey":"a70ac0c4572441c0a4b7a0d080adc90d"
    }

    response = requests.get(url, params=params)
    data = response.json()

    print(data)

    return  data.get("articles" , [])
    















buscar_noticias("chile")










