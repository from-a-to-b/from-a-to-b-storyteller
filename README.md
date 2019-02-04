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

$ python client.py

## 데이터 형식

스토리텔러로 넘어가기 직전 데이터의 예시입니다. 이전과 달라진 점은 1. path 데이터를 따로 뽑아오지 않고 POI와 POI를 패스에 프로젝션한 포인트만 가지고 이야기를 만들수 있게 했습니다. 즉 포인트 A에서 B 사이의 주변에 (15m) 있는 POI를 긁어온 후, 그 POI들을 A-B 패스 위에 얹히고 그것을 시간순서로 배열했습니다. 이렇게 만들면 따로 Path를 불러올 필요없이 POI의 배열순서가 패스의 순서와 같게 됩니다. 즉 POI를 따라가면 이야기가 되는 방식이 되도록 했습니다. 스토리텔러는 여기에서 좋은 POI를 순차적으로 참조해가면서 만들면 되겠지라는 생각으로..? 스토리텔러는 여기에서 일단 pois 배열에서 fiction 오브젝트를 추가한다는 방식으로 가면 좋지 않을까 싶고요.

```javascript
{
  total_time: 2978,
  pickup_time: 1449079362,
  dropoff_time: 1449082340,
  type: "taxi",
  pois: [{
      osm_id: 2610440263,
      code: 2004,
      fclass: "post_box",
      name: null,
      location: [
        -73.9832839,
        40.7612791
      ],
      index: 0,
      projected_point_on_path: [
        -73.983374,
        40.761148
      ],
      timestamp: 1449079365.1731405
    },
    {
      osm_id: 2610440252,
      code: 2301,
      fclass: "restaurant",
      name: "TGI Fridays",
      location: [
        -73.9829819,
        40.7611131
      ],
      index: 2,
      projected_point_on_path: [
        -73.980418,
        40.759911
      ],
      timestamp: 1449079455.6773279
    }
  ]
}
```

위의 request를 받아 스토리텔러가 POI에 픽션을 추가하면 각 poi 객체에 fiction이 들어가도록 요렇게 되면 좋겠습니다만 100% 확신은 없는..: 

```javascript
{
  total_time: 2978,
  pickup_time: 1449079362,
  dropoff_time: 1449082340,
  type: "taxi",
  pois: [{
      osm_id: 2610440263,
      code: 2004,
      fclass: "post_box",
      name: null,
      location: [
        -73.9832839,
        40.7612791
      ],
      index: 0,
      projected_point_on_path: [
        -73.983374,
        40.761148
      ],
      timestamp: 1449079365.1731405
      fiction: "A song can make or ruin a person’s day if they let it get to them."
    },
    {
      osm_id: 2610440252,
      code: 2301,
      fclass: "restaurant",
      name: "TGI Fridays",
      location: [
        -73.9829819,
        40.7611131
      ],
      index: 2,
      projected_point_on_path: [
        -73.980418,
        40.759911
      ],
      timestamp: 1449079455.6773279,
      fiction: "Everyone was busy, so I went to the movie alone."
    }
  ]
}
```