## Exploratory testing :: Shortly - SignUp

## Goal
* To identify major inconsistencies in the system without using scripted test cases

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
1..We are going to perform an exploratory testing with no prior knolwedge of the application and tech stack. Along with the feature requirements, our focus would also be on the UI components. The UI part includes the responsiveness of the site in multiple dimensions.\
2..The feature is to upload the CV, for which we also need to see the network tab (to see if the resources are correctly uploaded / downloaded) along with the performance tab (to see the time it takes to upload the CV) from the browser inspect window.\
3..Primarily, we are testing the feature using Chrome 100.XXX but we will also see if the UI components works in other platforms (Linux / Mac), browsers including FireFox, Edge, and Safari.  

## Test Scenarios
#### Pre-req:
* user is successfully signed-up and on Profile page.
* `Upload you CV` button is enabled on the profile page.
  
### Happy day

* scenario 1 - Registered user can upload the CV in multiple supported document formats (doc, docx, pdf, odt, rtf etc.
  * PASS  
  Scenario1.docx / scenario1_pdf sample files attached for reference.  
* scenario 2 - Registered user can upload the CV where `Profile prefill` is `off` AND data is NOT pre-filled.
  * PASS
* scenario 3 - Registered user can upload the CV where `Profile prefill` is `ON` AND data is pre-filled in `Experience and Skills` page.
  * PASS
  
### Rainy day
* scenario 1 - user upload the invalid file type e.g. .exe; .cmd etc.
  * Pass :: validation error. 
* scenario 2 - user upload the blank document.
  * Pass
* scenario 3 - user upload the document with duplicate experience and skill sections.
  * Pass
* scenario 4 - user upload the document with the size more than the supported/documented
  * Pass :: validation error (not more than 3 MB)
* scenario 5 - user upload the document with asci characters in the name of the file
  * Pass
* scenario 6 - documents with invalid experience dates e.g. future dates, past century dates etc
  * FAIL
* scenario 8 - user upload the document with malicious macros .docm.
  * Pass :: File type not supported.

##### GHERKIN Template for scripting:
** Given a CV in word document with experience & skills sections\
** When user upload the CV in a word document\
** Then the data correctly filled in to respective page on Shortlyster

## Bugs / Issues
* Happy day - scenario 1 -   There is a slight change in behaviour with PDF and docx. In case of PDF, Experience & Skills is prefilled with the projects under the job as well e.g. Innovation Group as part of my first job. The PDF prefilled the section with the link whereas in case of docx, the correct name of organization is prefilled.
* Rainy day - scenario 6 - The Experience & Skills page populated the future dated experiences e.g. 2023 ~ 2024 etc. sample file = Rain_scenario6.docx