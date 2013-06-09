GET or POST requests directed at "/" with a values parameter that's a list of integers will return a json object with the sum and product of the integers.

GET requests to "/history" will see the full history of requests made
GET requests to "/history" with a "since" parameter formatted `YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]` will return a history of requests made after the date/time specified.
an example history request can look like this:
/history?since=2013-06-09 00:12

