import gitlab

gl = gitlab.Gitlab('http://10.0.0.1', private_token='g7dMmQo2bQecXdukBuux')

print(gl)

projects = gl.projects.list()

for project in projects:
    print(project)