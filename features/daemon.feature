Feature: docker daemon basic

 Scenario Outline: pull opensuse
     Given docker daemon running
     When we pull image <images>
     Then we got <images> dockerized 
      
     Examples: Pull-image
	| images	| 
	
	| opensuse      | 
	| mongo		|
	| busybox	| 
	| httpd	        | 

 Scenario: run commands on container
     Given docker daemon running
     when  run command with docker
     then  command executed on container
