# importamos geoip2
import geoip2.database

# carganmos la base de datos
reader = geoip2.database.Reader('/path/to/GeoLite2-City.mmdb')

# obtenemos la ubicacion geografica con la IP
response = reader.city('IP')

# recuperamos toda la informacion
print(response.country.iso_code)
print(response.country.name)
print(response.postal.code)
print(response.subdivisions.most_specific.name)
print(response.city.name)
print(response.location.latitude)
print(response.location.longitude)