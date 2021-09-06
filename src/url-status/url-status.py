import urllib.request

response = urllib.request.Request("https://medsims-338-react-authoring.k8s.feature.medsims.com/", headers={'User-Agent': 'Mozilla/5.0'})

res = urllib.request.urlopen(response).getcode()


print(res)