Feature: docker daemon basic

 Scenario: pull opensuse
     Given docker daemon running
     when pull image opensuse
     then we got opensuse dockerized

 Scenario: run commands on container
    Given docker daemon running
    when  run command with docker
    then  command executed on container

 Scenario: download file from web-server container
    Given container with web-server
    when download a text file
    then file should be there
