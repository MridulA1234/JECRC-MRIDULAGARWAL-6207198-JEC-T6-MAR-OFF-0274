*** Settings ***
Documentation    Checkbox interactions on Herokuapp
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/

*** Test Cases ***
Verify Checkbox Behavior
    Handle Checkboxes On Page

*** Keywords ***
Handle Checkboxes On Page
    [Documentation]    Verifies select and unselect actions on herokuapp checkboxes
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=//a[text()="Checkboxes"]
    Page Should Contain Checkbox    id=checkboxes
    Sleep    3s
    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    3s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    3s
    Close Browser
