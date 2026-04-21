*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://inc.in

*** Test Cases ***
JS Scroll Test
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Sleep    3s
    Execute Javascript    window.scrollTo(0,document.body.scrollHeight)
    Sleep    3s
    Close Browser
