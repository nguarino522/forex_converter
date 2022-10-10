### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
> There are definitely multiple important differences to note here.
1. Python immutable and data types, JavaScript no concept of them.
2. Python has indentation, JavaScript uses curly brackets.
3. JavaScript doesn't really have a lot modules, while Python has a very extensive collection.
4. Javascript only floating point numbers, Python many different types.
5. Python uses class-based inheritence model, JavaScript uses prototype based inheritence model.
6. Missing func vars Python raises an exception while JavaScript simply sets as undefined.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
> Potentially 'try and catch' method and perhaps set a default value if one isn't found.

- What is a unit test?
> A unit test, is a term used in computer programming testing of applications. Essentially it is testing one small piece of code (could be a function for example) in the application.

- What is an integration test?
> An integration test is for all intents and purposes is made up of multiple unit tests which are combined and tested as a potential group. It can be for example to confirm interaction between them is working correctly.

- What is the role of web application framework, like Flask?
> The main role is to provide a uniform and easier way to to build and deploy an application and reduce overhead, as it provides many tools and libraries that make it much easier building an applicaiton from scratch.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
> This would highly be situational depending on how you are grabbing or generating data from and where you storing as well where you might be sending it to.

- How do you collect data from a URL placeholder parameter using Flask?
> You can specify in the route definition `'/foods/<food>` for example and then `def food_route(food):` pass it in for it to be become available.
 
- How do you collect data from the query string using Flask?
> You can use the `request.args.get()` method in the route function to pull the URL placeholder or parameter passed in.

- How do you collect data from the body of the request using Flask?
> You can use the `request.files` method.

- What is a cookie and what kinds of things are they commonly used for?
> A cookie, as it pertains to web application, is essentially text files with small pieces of data stored in a web browser that can be retrieved at a later time.
  A use case could be storing username and password information.

- What is the session object in Flask?
> The session object in Flask is essentially a dictionary like file that is stored in a signed cookie and uses key value pairs. The 'session' it tracks can be defined as the time from which a user may login and out of the web app/server.

- What does Flask's `jsonify()` do?
> In Flask, the `jsonify()` method/tool (helper) will serialize data to JSON format and returns a Response object.