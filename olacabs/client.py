import requests

PRODUCTION_URL = "https://devapi.olacabs.com/v1/"
STAGE_URL = "https://devapi.olacabs.com/v1/"


class OlaCabsClient(object):
    def __init__(self, x_app_token, debug=False):
        self.api_url = STAGE_URL if debug else PRODUCTION_URL
        self.x_app_token = x_app_token

    def search_ride(self, pickup_lat, pickup_lng, category=None):
        params = {
            "pickup_lat": pickup_lat,
            "pickup_lng": pickup_lng
        }
        if category:
            params['category'] = category

        headers = {
            "X-APP-TOKEN": self.x_app_token
        }
        return self._get("products", headers, params)

    def get_ride_estimate(self, pickup_lat, pickup_lng, drop_lat, drop_lng, category):
        params = {
            "pickup_lat": pickup_lat,
            "pickup_lng": pickup_lng,
            "drop_lat": drop_lat,
            "drop_lng": drop_lng,
            "category": category
        }

        headers = {
            "X-APP-TOKEN": self.x_app_token
        }
        return self._get("products", headers, params)

    def book_ride(self, pickup_lat, pickup_lng, category, oauthtoken, pickup_mode="NOW"):
        params = {
            "pickup_lat": pickup_lat,
            "pickup_lng": pickup_lng,
            "category": category,
            "pickup_mode": pickup_mode
        }

        headers = {
            "X-APP-TOKEN": self.x_app_token,
            "Authorization": oauthtoken
        }
        return self._get("bookings/create", headers, params)

    def cancel_ride(self, crn, oauthtoken):
        params = {
            "crn": crn
        }

        headers = {
            "X-APP-TOKEN": self.x_app_token,
            "Authorization": oauthtoken
        }
        return self._get("bookings/cancel", headers, params)

    def track_ride(self, oauthtoken):
        headers = {
            "X-APP-TOKEN": self.x_app_token,
            "Authorization": oauthtoken
        }
        return self._get("bookings/track_ride", headers)

    def _get(self, resource, headers, params=None):
        api_url = self.api_url + resource

        return requests.get(url=api_url,
                            headers=headers,
                            params=params
                            )
