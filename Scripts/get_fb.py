#Archivo: get fb.py

#Importar Librería
import facebook
import json

#Definir token de acceso
token = 'EAACyysMFdnkBAOoT3vcYpDIzVQ1Igg7nRT5ZAiHaeud4D0GfWUgrGPfsfyXSTv2wuxZA2GlS7phSeUHelOCt4nky3YX8V3DBTAlvayZAMaxZCqeDrXvLeTOsKvUbXeNBXEUMIRZA3LCHlzBQuMSbrUBF3zlYX9mdVW8LuvtqGR0FGvDPMxhmGSO5Qoa9dh8R8kSc91PKxZBQZDZD'

#Definir id de página de donde adquirir posts
page = '1721398957963241'

#Conectarse a API de Facebook
graph = facebook.GraphAPI(token)

#Definir atributos deseados de los posts
all_fields = [
    'id',
    'message',
    'created_time',
    'likes.summary(true)',
    'comments.summary(true)',
    ]
all_fields = ','.join(all_fields)

#Obtener posts
posts = graph.get_connections(page, 'posts', fields = all_fields)

#Imprimir posts
for post in posts['data']:
    
    print (json.dumps(post, indent=4, sort_keys = True))



