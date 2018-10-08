#__author__ = gaurav kumar
#version = 0.1
#date= 10/08/2018

*** Settings ***
Documentation    Suite description
Library          Selenium2Library
Library          ../Libraries/CommonFunctions.py

*** Keywords ***
Generic TestCase Setup
    [arguments]          ${BROWSER}     ${URL}
    Driver Instance	     ${BROWSER}
    Open App             ${URL}

Generic TestCase Teardown
    Close App

