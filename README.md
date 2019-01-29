# Storyteller for From Point A to Point B

Takes in data including starting/ending points, POI, and timestamps; spits out generative fictional accounts of the trip


## Setup

1. Conda (optional if you know how to set up a virtual environment)

Follow instructions at: https://conda.io/projects/conda/en/latest/user-guide/install/macos.html

2. Python 3.6 and packages

Create a new Python 3.6 environment with `conda create --name fromatob python=3.6`

Activate the environment with `conda activate fromatob`

`pip install flask requests`

(should i have a make file?)

3. For development

```
$ export FLASK_APP=storyteller
$ export FLASK_ENV=development
$ flask run
```

4. Test

`example_trip.json` looks like this:

```
[{"timestamp": "1:00", "POI_name": "Empire State", "POI_type": "landmark"}, 
 {"timestamp": "1:04", "POI_name": "Bryant Park", "POI_type": "park"}]
```

Sending `example_trip.json` via a POST http request to the `/fictionalize` subdomain will return sth like:

```
[{"timestamp": "1:00", "POI_name": "Empire State", "POI_type": "landmark", "fiction": "At 1:00, they were passing by Empire State. The landmark felt overrated. It also made them think about road to Damascus."}, 
 {"timestamp": "1:04", "POI_name": "Bryant Park", "POI_type": "park", "fiction": "At 1:04, they were passing by Bryant Park. The park felt boring. It also made them think about animal."}]
```

## Ideal return data structure from wy..
```javascript
{
  success: true, 
  trip: {
    total_time: 145, // seconds
    pickup_time: 1448983253, // unix time
    dropoff_time: 1448983398, // unix time
    type: "taxi", // taxi, bike
    sequence: [
      { 
        location: [lng, lat],
        timestamp: unix timeframe
        poi: {
          osm_id: poi.osm_id,
          code: poi.code,
          fclass: poi.fclass,
          name: poi.name,
          location: [lng, lat]
        },
        fiction: ""
      },
      ...
    ]
  }
}
```