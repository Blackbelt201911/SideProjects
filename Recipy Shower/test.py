import urllib.request, sys 

name = 'recipe'
but = '3'


urllib.request.urlretrieve('https://raw.githubusercontent.com/Blackbelt201911/Server/main/test2.txt', name + but + '.txt')