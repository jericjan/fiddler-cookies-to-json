# fiddler-cookies-to-json

Converts Fiddler cookies from "Copy Header" to a JSON usable for [Cookie-Editor](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en)

Example:
```
What is your domain?
> .hoyoverse.com
```
Fiddler cookies:

```
Cookie: 
cookie1=value1;
cookie2=value2
````
Converted to JSON:
```
[
   {
      "domain":".hoyoverse.com",
      "name":"cookie1",
      "value":"value1"
   },
   {
      "domain":".hoyoverse.com",
      "name":"cookie2",
      "value":"value2"
   }
]
```
