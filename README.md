
# Sample Search Test

This is a Basic Repo with Testing Search functionality of an App.

#### Prerequisites for the creating are:
1) python2.7.x https://www.python.org/downloads/ (32 bit)
2) git https://git-scm.com/downloads 
3) pycharm community edition https://www.jetbrains.com/pycharm/download/ 
4) Chromedriver http://chromedriver.chromium.org/downloads

#### Steps for installation and running:
1) Run `pip install -r requirements.txt'

#### Prerequisites for running scripts after configuration:
1) Chrome browser is installed on machine
2) Chromedriver.exe is placed inside python installation directory on test machine

#### Command for running scripts after configuration:
For windows:
1) Open command prompt and goto the path of code\Test\Testsuite
2) run command: robot -d C:\Test_Results --variable text:"Selenium Webdriver framework architecture diagram" --variable searchtext:Relayr  --include sanity *.robot if you want to pass text as arguments
otherwise robot -d C:\Test_Results --include sanity *.robot

For Mac:
Open Settings > Security and Privacy > Accessibility > unlock > click on + > Applications > Utilities > (Terminal and system events and Script editor)
1) Open terminal prompt and goto the path of code\Test\Testsuite
2) run command: sudo  robot -d /Users/user/Desktop/Test_Results --variable text:"Selenium Webdriver framework architecture diagram" --variable searchtext:Relayr  --include sanity *.robot



#### Basic Testcases for Search Functionality
Test Cases of Google Search
#### Front End - UI Test Cases of Google Search
1. Verify that Google Logo is present and centre aligned
2. Verify that the search textbox is centre aligned and editable
3. Verify that search request should get hit by clicking on search button or hitting enter after writing the search term
4. Verify that in the search result- webpage's title, URL and description are present
5. Verify that clicking the search result will lead to the corresponding web page
6. Verify that pagination is present in case number of results are greater than the maximum results allowed in a page
7. Verify that user can navigate to a page number directly or move to previous or next page using the links present
8. Verify that different languages links are present and gets applied on clicking the same
9. Verify that the total number of results for the keyword is displayed
10. Verify that the time taken to fetch the result is displayed

#### Functionality- Test Cases of Google Search
1. Verify that user can make search corresponding to different categories - web, images, videos, news, books etc and response should correspond to the keyword in that category only
2. Verify that the response are sorted by relevancy in descending order i.e. most relevant result for the keyword are displayed on top
3. Verify that the link title, URL and description have the keyword highlighted in the response
4. Verify if the search is case-insensitive or not
5. Verify auto-suggestion in Google. 
6. Verify that the suggestion provided by Google are sorted by most popular/relevant suggestions
7. Verify that misspelled keyword should get corrected and response corresponding to the correct keyword should get displayed
8. Verify that the search response should be localized that is response should be more relevant to the country/area from which the search request is initiated
9. Verify Google calculator service- make any arithmetic request, calculator should get displayed with correct result
10. Verify Google converter service- make request like- 1 EURO in INR and check if the result is correct
11. Verify that user can make search using different languages
12. Verify the functionality of "I'm feeling Lucky" search- the top most search result should get directly returned (but as of now google doodle page link is displayed)
13. Verify the pagination should be enabled when there are more results than the default result count per page


