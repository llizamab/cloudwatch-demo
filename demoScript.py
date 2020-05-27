# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import http.client
import random
import time
#import mimetypes

url = ".execute-api.us-east-1.amazonaws.com"
apis = ['11111', '22222']
endp = ['/v1/pets', '/v1/pets/500', '/v1/pets/400']

cont200 = 0
cont400 = 0
cont500 = 0

''' get random number betwen 0 -- 10
'''
def getRandom():
    return (random.randint(0,1), random.randint(0,10))

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def call200(api_index):
    global apis
    global url
    global cont200
    global endp
    api = apis[api_index]

    conn = http.client.HTTPSConnection(api + url)
    conn.request("GET", endp[0], '', {})
    res = conn.getresponse()
    cont200 += 1
    print("Llamando a api: ", api, " end: ", endp[0], " code:", res.status)

def call500(api_index):
    global apis
    global url
    global cont500
    global endp
    api = apis[api_index]

    conn = http.client.HTTPSConnection(api + url)
    conn.request("GET", endp[1], '', {})
    res = conn.getresponse()
    cont500 += 1
    print("Llamando a api: ", api, " end: ", endp[1], " code:", res.status)

def call400(api_index):
    global apis
    global url
    global cont400
    global endp
    api = apis[api_index]

    conn = http.client.HTTPSConnection(api + url)
    conn.request("GET", endp[2], '', {})
    res = conn.getresponse()
    cont400 += 1
    print("Llamando a api: ", api, " end: ", endp[2], " code:", res.status)
    
''' Call apis random
'''
def llamadasRandom(api_index, endp_rand):

    api = apis[api_index]
    payload = ''
    headers = {}
    global cont200
    global cont400
    global cont500

    # si es par, llamar al 0
    if endp_rand % 2 == 0:
        conn = http.client.HTTPSConnection(api + url)
        conn.request("GET", endp[0], payload, headers)
        res = conn.getresponse()
        cont200 += 1
        print("Llamando a api: ", api, " end: ", endp[0], " code:", res.status)
    
    # si es primo, llamar al 500
    if is_prime(endp_rand):
        conn = http.client.HTTPSConnection(api + url)
        conn.request("GET", endp[1], payload, headers)
        res = conn.getresponse()
        cont500 += 1
        print("Llamando a api: ", api, " end: ", endp[1], " code:", res.status)
    
    # si es mult de 3 llamar al 400
    if endp_rand % 3 == 0:
        conn = http.client.HTTPSConnection(api + url)
        conn.request("GET", endp[2], payload, headers)
        res = conn.getresponse()
        cont400 += 1
        print("Llamando a api: ", api, " end: ", endp[2], " code:", res.status)

    #data = res.read()
    #print(data.decode("utf-8"))


# durante 10 minutos
for y in range(10):
    # ejecuta 20 peticiones random
    for x in range(20):
        tupla = getRandom()
        # si es par un numero random entre 0 y 10
        if tupla[1] % 2 == 0:
            call200(tupla[0])

        time.sleep(3)

    print("Cantidad de llamadas 200: ", cont200)

    # espero un minuto
    time.sleep(60)

    # en el minuto 3 llamo al 400
    if y == 2:
        call400(0)
    
    # en el minuto 6 llamo al 500
    if y == 5:
        call500(0)


    print("Cantidad de llamadas 400: ", cont400)
    print("Cantidad de llamadas 500: ", cont500)

