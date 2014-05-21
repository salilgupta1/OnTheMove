import Activities.search
import json,os
try:
	import config
	consumer_key = config.keys['YELP_CONSUMER']
	consumer_secret = config.keys['YELP_CONSUMER_SECRET']
	token_key = config.keys['YELP_TOKEN']
	token_secret = config.keys['YELP_TOKEN_SECRET']
except:
	consumer_key = os.environ['YELP_CONSUMER']
	consumer_secret = os.environ['YELP_CONSUMER_SECRET']
	token_key = os.environ['YELP_TOKEN']
	token_secret = os.environ['YELP_TOKEN_SECRET']

def get_rating(name,lng,lat):
	host = 'api.yelp.com'
	path = '/v2/search'	
	url_params = { 'term':name, 'll':str(lat)+','+str(lng)}

	data = Activities.search.request(host, path, url_params, consumer_key, consumer_secret, token_key, token_secret)

	#print data
	business_data = data['businesses']
	#print business_data
	#print business_data[0]['rating']
	if len(business_data) == 0:
		return -1
	rating = business_data[0]['rating']
	if rating is None:
		return -1
	return rating


def search_location():
	host = 'api.yelp.com'
	path = '/v2/search'
	#consumer_key = config.keys['YELP_CONSUMER']
	#consumer_secret = config.keys['YELP_CONSUMER_SECRET']
	#token_key = config.keys['YELP_TOKEN']
	#token_secret = config.keys['YELP_TOKEN_SECRET']
	
	url_params = { 'term':'bars', 'location':'San Francisco' }

	data = Activities.search.request(host, path, url_params, consumer_key, consumer_secret, token_key, token_secret)

	
	location_data = data['region']['center']
	lat = location_data['latitude']
	lng = location_data['longitude']
	print lat, lng

	for business in data['businesses']:
		print business['name']
		print business['id']
		print

def get_business_info(businessID, latitude, longitude):
	result = {}

	host = 'api.yelp.com'
	path = '/v2/search'
	#consumer_key = config.keys['YELP_CONSUMER']
	#consumer_secret = config.keys['YELP_CONSUMER_SECRET']
	#token_key = config.keys['YELP_TOKEN']
	#token_secret = config.keys['YELP_TOKEN_SECRET']

	url_params = { 'id': businessID }

	data = Activities.search.request(host, path, url_params, consumer_key, consumer_secret, token_key, token_secret)

	print data


