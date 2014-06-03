import Activities.search, Activities.business
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

def get_yelp_data(name,lng,lat):
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
	entry = business_data[0]
	rating = entry['rating']
	if "img_url" in entry.keys():
		img_url = entry['image_url']
	else:
		img_url = -1
	if rating is None or img_url is None:
		return -1
	return rating,img_url


def search_location(lat,lng,keyword):
	host = 'api.yelp.com'
	path = '/v2/search'
	url_params = { 'term':keyword, 'll': str(lat)+','+str(lng)}

	data = Activities.search.request(host, path, url_params, consumer_key, consumer_secret, token_key, token_secret)

	
	location_data = data['region']['center']
	lat = location_data['latitude']
	lng = location_data['longitude']
	#print lat, lng
	business_list = []
	business = data['businesses']
	for i in range(0,5):
		business_obj = {}
		business_obj['name'] = business[i]['name']
		business_obj['id'] = business[i]['id']
		business_obj['location'] = business[i]['location']['display_address'][0]
		business_list.append(business_obj)

	return {
		'lat' : lat,
		'lng' : lng,
		'business_list':business_list
	}


def get_business_info(businessID, latitude, longitude):
	result = {}
	host = 'api.yelp.com'
	path = '/v2/business/' + businessID

	# url_params = { 'id': businessID }
	url_params = {}

	data = Activities.business.request(host, path, url_params, consumer_key, consumer_secret, token_key, token_secret)

	name = data['name']
	address = data['location']['address']
	city = data['location']['city']
	state = data['location']['state_code']
	zipcode = data['location']['postal_code']
	return {
		'business_name':name,
		'address':address,
		'city' : city,
		'state': state,
		'zipcode':zipcode
	}
	


