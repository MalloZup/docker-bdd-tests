Feature: docker daemon basic

 Scenario Outline: pull some images
     Given docker daemon running
     When we pull image <images>
     Then we got <images> dockerized 

     Examples: docker-images
	| images	| 
	| opensuse      | 
	| mongo		|
	| busybox	| 
	| httpd	        | 

 Scenario Outline: run commands on container
     Given docker daemon running
     When  run <cmd> in <images> 
     Then  command executed on container

     Examples: images command
	| images	|  cmd 		 |
	| opensuse      |  uptime    	 |
	| busybox	|  ls   	 |
	| httpd	        |  uptime        |

