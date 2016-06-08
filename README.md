# olacabs
Python client for APIs of Olacabs

API Doc (https://developers.olacabs.com/docs/overview)

### Installation

```
pip install olacabs
```

### Usage

```python
from olacabs import OlaCabsClient

client = OlaCabsClient(x_app_token=OLA_SERVER_TOKEN, debug=OLA_SANDBOX)

client.search_ride(pickup_lat, pickup_lng, category=None)

client.get_ride_estimate(pickup_lat, pickup_lng, drop_lat, drop_lng, category)

client.book_ride(pickup_lat, pickup_lng, category, oauthtoken, pickup_mode="NOW")

client.cancel_ride(crn, oauthtoken)

client.track_ride(oauthtoken)

```