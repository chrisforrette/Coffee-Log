STATUS_OPTIONS = (
    (0, 'Deleted'),
    (1, 'Inactive'),
    (2, 'Active'),
)

GOOGLE_MAPS_API_KEY = "ABQIAAAAACr9e7mqlFH26wAD4fWpmRTpH3CbXHjuCVmaTc5MkkU4wO1RRhT98Ib4uYFiGc5rNYm4TzWwnl2yMQ"

def get_geo_point(address):
    
    """Attempt to resolve ``address`` using Google's geocoder. Returns a tuple with the canonical address and GEOS point"""
    
    import cjson
    from urllib import urlencode
    from urllib2 import urlopen
    from django.contrib.gis.geos import fromstr
 
    # encode the request
    data = urlencode({
        'q': address,
        'output': "json",
        'oe': "utf8",
        'sensor': "false",
        'key': GOOGLE_MAPS_API_KEY
    })
    
    url = "http://maps.google.com/maps/geo?%s" % data
 
    response = urlopen(url)
    geo_content = cjson.decode(response.read())
    
    placemark = geo_content['Placemark'][0]
    
    # convert to a geodjango point
    lng, lat = placemark['Point']['coordinates'][:2]
    point = fromstr("POINT(%s %s)" % (lng, lat))
    return (placemark['address'], point)
