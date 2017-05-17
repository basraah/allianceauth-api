# Alliance Auth API

An internal OpenAPI for [Alliance Auth](https://github.com/allianceauth/allianceauth).

## Quick Start

1. Install the package, `pip install git+https://github.com/basraah/allianceauth-api.git`
2. Add the following to the relevant parts of your AllianceAuth `settings.py` file:
```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_swagger',
    'allianceauth_api',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    )
}
```
3. Add the URL endpoint to your `ROOT_URLCONF` file:
```python
from django.conf.urls import include, url
import allianceauth_api.urls

urlpatterns = [
    url(r'^api/', include(allianceauth_api.urls)),
]
```
4. Restart AllianceAuth and you should be good to go. Browse to the base API URL you set to access the Swagger UI.

Make sure you read the security section below!

## Security and Authentication

By default, the API framework has no security and allows public access. There's a pretty good chance that's highly undesirable for your application. With the configuration given above, access should be limited only to logged in users flagged as Administrators. 

If you want to enable Token based authentication or some other type of authentication, please read the [Django REST framework Authentication docs](http://www.django-rest-framework.org/api-guide/authentication/).

### Permissions
This is intended as an internal API for consumption by internal apps. **When you grant access to someone or some application, you are granting access to the entire API.** It is not designed to have granular access granted to users (so they can access only their information), or as a public facing API backing a UI or similar. It could be modified to work in this way with some effort, but this is currently not how it is designed.

### IP Restrictions
If you wish to restrict the IP addresses that can access the API (probably a good idea as part of a layered security approach) I would suggest using your external web server (Apache, Nginx etc) to whitelist the IPs you access the API from.

For example:
- Apache 2.4
```
<Location /api>
        Order Deny,Allow
        Deny from all
        Allow from 127.0.0.1
</Location>
```

- NGINX
```
location /api/ {
    allow   127.0.0.1;
    deny    all;
}
```

## Q & A
### Why can't I POST/PUT/PATCH this endpoint?
There are a number of endpoints that need some work on the Alliance Auth side to make work consistently without duplicating code. Usually in these instances the logic exists in the views rather than in the models. As the code gets cleaned up on the Alliance Auth side, they'll get added here.

Other endpoints are wholly managed on the Alliance Auth side (e.g. characters and corps) and wont accept direct modifications.

### Can I access all EVE Characters/Corps/Alliances through the `eve` endpoint?
No, only the entities stored locally. The API makes no attempt to proxy information from the XML API or ESI if it's not stored locally. If you can't find the model via this API then you would need to query ESI for that information. ESI would also be more up-to-date, if that is important to you. 

### Why isn't there a Fleet-Up endpoint?
Alliance Auth just accesses and displays the Fleet-Up API, so you should access that API directly.

### I wrote a service integration, how do I add an API endpoint?
I haven't figured out how I'm going to handle services yet. It will probably be with a parameter in the services hook that returns the ViewSet to provide the endpoint.
