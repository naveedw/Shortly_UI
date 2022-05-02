## Shortlyster - SignUp

## Framework
* I have used
  * Language - python
  * framework - pytest
  * UI interaction - page objects (xpath / css selectors)
  * Browser loading - seleniun webdriver

 The reason of using is because I have started learning Python this year and I am still new with it. Every testcase will be a pytest function which will look for page objects. In side the page objects, I have used selenium function e.g. clicks, submit etc.... which interact with browser using webdriver. 
 
## Acceptance criteria
I wrote down in the Gerkin language (Given When Then)
As a user of shortlyster\
I want to upload the curriculum vitae in the profile page\
So that the document data is pre-fill on Experience & Skills page. 


## Details
* I couldn't get around the very first step of logging in to the website. I reckon the bot/automation is being blocked by the CDN or the network Shortlyster is currently using. I have tried so many ways to get through this but miserably failed. I have even tried Gecko driver (firefox) to change the header info but still couldn't make it.
  
* I partially went through the upload process and still needs to add assertions.
* I planned to set up the classes but since it's a single feature so though about creating a main file along with utilities. The other way is to create a single class to initiate the objects and then subsequently create the methods to expose their behaviour. 

## Structure
There are two python files for automation:
* main.py
* utilities.py

utilities have the respective functions which have been called within the main. The plan was the create the assertions after I successfully uploaded the CV. 



