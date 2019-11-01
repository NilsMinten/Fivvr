# Route definitions
``` http://localhost:8000/ ``` - admin panel only for content management from builtin django admin

## User routes
``` http://localhost:8000/user/create  ``` - Used to create a user
``` 
username: string
passsword: string
email: string
```

``` http://localhost:8000/user/login ``` - used to login a user
```
email: string
password: string
```

``` http://localhost:8000/user/object_karma/<int:user_id> ``` - used to objectify to karma reduction

## Service urls
``` http://localhost:8000/service ``` - used to get all services

``` http://localhost:8000/service/create ``` - Create a new service
```
key: string - api key for identifying users
title: string
description: string
cost: int
```

``` http://localhost:8000/service/delete/<int:service_id> ``` - delete a service by owner or admin
```
api: string
```

``` http://localhost:8000/service/edit/<int:service_id> ``` - edit existing service
```
key: string
title: string
description: string
cost: int
```

``` http://localhost:8000/service/<int:service_id> ``` - load specific service
```
key: string
```

``` http://localhost:8000/service/upvote/<int:service_id> ``` - upvote service

``` http://localhost:8000/service/buy/<int:service_id> ``` - TODO: implement function

``` http://localhost:8000/service/cancel/<int:service_id> ``` - TODO: implement function


## ADMIN
### Karma management
``` http://localhost:8000/administrator/karma/<int:user_id> ``` - Load a users karma objections
```
api: string
```
``` http://localhost:8000/administrator/karma/<int:objection_id>/accept ``` - accept karma objection
```
api: string
```
``` http://localhost:8000/administrator/karma/<int:objection_id>/deny ``` - deny karma objection
```
api: string
```