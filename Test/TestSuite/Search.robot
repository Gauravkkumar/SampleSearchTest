#__author__ = gaukuma@adobe.com
#version = 0.1
#date= 7/23/2018

*** Settings ***
Documentation    This is Sanity Suite for Sample Search Test Automation
Library          Selenium2Library
Library          ../../Libraries/CommonFunctions.py
Resource         ../../Global/Keywords.robot
Test Setup        Generic TestCase Setup        ${BROWSER}      ${URL}
Test Teardown     Generic TestCase Teardown

*** Variables ***

${BROWSER}      Firefox
${URL}          http://www.google.com/
${text}         Selenium Webdriver framework architecture diagram
${searchtext}   Relayr


*** Test Cases ***

Verify Search Box is Present
     [Documentation]            This is sanity testcase for Verifying Search Box is Present.
     [Tags]                     Sanity
     ${result1} =   Is Search Box Present
     Run Keyword If     '${result1}' == 'False'       Fail    Search Box is not present on the Page

Verify Image Link is Present
     [Documentation]            This is sanity testcase for Verifying Image Link is Present on Home Screen.
     [Tags]                     Sanity
     ${result1} =   Is Image Link Present
     Run Keyword If     '${result1}' == 'False'       Fail    Image Link is not present on the Page

Search Images and validate Result count
     [Documentation]            This is sanity testcase for Search Image and validate Result Count.
     [Tags]                     Sanity
     ${result2}=  SEARCH IMAGES   ${text}
     Run Keyword If     '${result2}' == 'False'       Fail    Result Images count is not coming as 100


Search Text and validate Result text in Results
     [Documentation]            This is sanity testcase for Search text and validate search text in Result.
     [Tags]                     Sanity
     ${result2}=  SEARCH TEXT   ${searchtext}
     Run Keyword If     '${result2}' == 'False'       Fail    Result is not showing search text


