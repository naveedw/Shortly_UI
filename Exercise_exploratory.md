## Exploratory testing :: Shortly - SignUp

## Goal
* Demonstrate your skill at coding automation frameworks for use
by other engineers.
* Demonstrate your ability to advise others on writing valuable
automated tests.

## Task
A team has finished developing a new feature in Shortlyster wherein a candidate can `upload` their `curriculum vitae (CV)` in the `Profile page`. The data captured in the document will `pre-fill` some fields on the `Experience and Skills page`.

#### Please note that Work area and Skills are not included in the process.


[Sign up as a Shortlyster candidate using the test
environment](https://candidate--qa-exercise.reviews.compono.dev/signup)

## Recording your results
* A short description (1-2 sentences) of the approach you took to your testing.
* A list of test scenarios you executed to conduct testing the feature.
* A short description of bugs you may have encountered.
If you can think of other areas for your testing before deploying the feature, what would they be?


# RESULTS
## Testing approach
Since we are doing manual testing, and the application is web-based so our focus would be the UI components along with the functionality of the feature being developed. The UI part includes the responsiveness of the site in multiple dimensions.\
The feature is to upload the CV, for which we also need to see the network tab (to see if the resources are correctly uploaded / downloaded) along with the performance tab (to see the time it takes to upload the CV) from the browser inspect window. 
## Test Scenarios
#### Pre-req:
* user is successfully signed-up and on Profile page.
* `Upload you CV` button is enabled on the profile page.
  
### Happy day

* scenario 1 - Registered user can upload the CV in multiple supported document formats (doc, docx, pdf, odt, rtf etc.
* scenario 2 - Once uploaded, the data is pre-filled in `Experience and Skills` page.
* 
### Rainy day
* scenario 1 - user upload the invalid file type e.g. .exe; .cmd etc.
* scenario 2 - user upload the blank document.
* scenario 3 - user upload the document with multiple experience and skill sections.
* scenario 4 - user upload the document with the size more than the supported/documented
* scenario 5 - user upload the document with asci characters in the name of the file
* scenario 6 - user upload the document with malicious macros 

Given a CV in word document with experience & skills sections\
When user upload the CV in a word document\
Then the data correctly filled in to respective page on Shortlyster

* Scenario 2 - 
## Bugs