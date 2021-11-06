*** Settings ***
Test Teardown    Take Screenshot
Library    Browser
Library    ../library/library.py 

*** Variable ***
${URL}          http://parodifood.qaninja.academy/
${NAVEGATOR}    chromium

*** Test Case ***
Start Session
    New Browser    ${NAVEGATOR}    False
    Start Session
    Reports
    For Stress

*** Keywords ***
Start Session
    New Page       ${URL}
Reports
    ${CPU_percent}=    CPU_percent
    Log To Console    ${CPU_percent}
    ${Virtual_Memory}=    Virtual_Memory
    Log To Console    ${Virtual_Memory}
    ${perc_ram}=    perc_ram
    Log To Console    perc_ram
    ${cpu_status}=    cpu_status
    Log To Console    ${cpu_status}
    ${avaible_memory}=    avaible_memory
    Log To Console    ${avaible_memory}
For Stress
    FOR    ${COUNT}    IN RANGE    1    10
    Start Session
    END