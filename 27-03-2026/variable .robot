*** Settings ***
Documentation    Browser launch and variable usage demo
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.cricbuzz.com/

@{bikes}    ktm    kawasaki    honda    pulsar

&{cars}    nissan=gtr    honda=civic    bmw=m5

*** Test Cases ***
Launch Edge And Verify
    [Documentation]    Navigates to cricbuzz and logs variable values
    Open Browser    ${url}    edge
    Maximize Browser Window
    Log To Console    Reached cricbuzz successfully
    Log To Console    ${bikes}[1]
    Log To
