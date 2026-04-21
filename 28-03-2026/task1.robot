*** Settings ***
Documentation    Dropdown selection on practice site
Library    SeleniumLibrary

*** Variables ***
${url}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Colors Dropdown Test
    [Documentation]    Navigates to site and interacts with colors dropdown
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Scroll Element Into View    xpath=//label[text()="Sorted List:"]
    Page Should Contain List    id=colors
    ${all_options}=    Get List Items    id=colors
    Log To Console    ${all_options}
    Select From List By Label    id=colors    Blue    Yellow
    ${chosen}=    Get Selected List Label    id=colors
    Log To Console    ${chosen}
    Sleep    2s
    Close Browser
