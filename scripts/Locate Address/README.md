![image](https://user-images.githubusercontent.com/89864818/193449128-73fe21ca-f1d3-45e6-b8b1-d4d2e4983048.png)

- Sometimes you'll need to know the location of an IP address, whether it's your own or that of a site you're using.

    One use-case for this is when you want to send login information to users for your website.

    In this article, we're going to see how you can find the location of an IP address using Python.

- Get your tools ready

      To accomplish this goal, we'll be using two APIs mentioned below $ pip install requests

ipify: This API will help us know the IP address from where the request is coming.   

ipapi: This API will help us fetch location information for a particular IP address.

To interact with these APIs, we'll be using the requests library in Python. If you're new to APIs, make sure you check out this tutorial to learn about them.

- You can install this library using the 'pip' command like this:

      $ pip install requests

Once the library is installed, we're good to go!

- Get Location Information

   As we discussed, we'll first fetch our IP address from the first API. Then we'll make use of this IP address to fetch location information for this particular IP
   address. So, we'll have two functions:
   
   ![Screenshot (12)](https://user-images.githubusercontent.com/89864818/193449621-883f4649-8f2f-42f4-b383-28031a6ad0b0.png)
   
   In the above code, we have two functions – get_ip() and get_location().                                                                                        
     Let's discuss each of them separately.
     
- get_ip() function                                                                                                                              
As per the API documentation of ipify, we need to make a GET request on https://api.ipify.org?format=json to get a JSON response that looks like this:

      {

      "ip": "117.214.109.137"
  
     }
     
     
  We store this response in a response variable which is nothing but a sort of Python dictionary with one key-value pair. So we returned the value of the 
             
             key ip as response["ip"].

- get_location() function                                                                                                                 
As per the API documentation of ipapi, we need to make a GET request on https://ipapi.co/{ip}/{format}/ to get location information for a particular IP address. {ip} is replaced by the IP address and {format} can be replaced with any of these – json, jsonp, xml, csv, yaml.

This function internally calls the get_ip() function to get the IP address and then makes a GET request on the URL with the IP address. This API returns a JSON response that looks like this:

![](https://user-images.githubusercontent.com/89864818/193450445-c9e7669b-bd75-4d87-9142-06636163149a.png)

We get a whole lot of data in the response. You can use whatever works for
you. For this tutorial, we'll just be using  city, region and country. That's
why we created a dictionary called location_data and stored all the data
inside it and returned the same.

At last, we call the get_location() function and print the output. Our output will look like this:

       {
             "ip": "117.214.109.137", 
             "city": "Gaya", 
             "region": "Bihar", 
             "country": "India"
      }
      
- Conclusion                                                                                                                    
  Here we learned how we can interact with web services to get location information for a particular IP address.    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      













