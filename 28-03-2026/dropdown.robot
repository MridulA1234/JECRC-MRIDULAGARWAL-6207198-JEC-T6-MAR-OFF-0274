*** Settings ***
Documentation    Dropdown interaction on Herokuapp
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/

*** Test Cases ***
Dropdown Selection Test
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Click Element    xpath=//a[text()="Dropdown"]
    Page Should Contain List    id=dropdown
    ${available_options}=    Get List Items    id=dropdown
    Log To Console    ${available_options}
    Select From List By Label    id=dropdown    Option 1
    ${picked}=    Get Selected List Label    id=dropdown
    Log To Console
