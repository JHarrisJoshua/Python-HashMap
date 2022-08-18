# Python-HashMap

## Table of Contents
* [Overview](#Overview)
* [Chaining](#Chaining)
* [Open Addressing with Quadratic Probing](#Open-Addressing-with-Quadratic-Probing)
* [Continuous Integration Workflow and Testing](#Continuous-Integration-Workflow-and-Testing)

## Overview
Data Structures Portfolio Project - Implementation of a HashMap two ways - i) Chaining and ii) Open Addressing with Quadratic Probing

## Chaining
### Description
The first implementation of the HashMap uses chaining for collision resolution. The underlying data structure uses a dynamic array to store the hash table, with singly linked lists to facilitate   
### Methods 



## Open Addressing with Quadratic Probing 
### Description
The second implementation of the HashMap uses open addressing for collision resolution. The underlying data structure uses a dynamic array to store the hash table, with singly linked lists to facilitate   
### Methods 

## Continuous Integration Workflow and Testing
### Overview
A Continuous Integration Workflow was implemented using GitHub actions. While the original project was tested using basic testing, tests were converted into a testing suite to be used for the workflow. As part of the CI workflow, branch protections were implemented for the main branch to prevent new commits from being pushed to main without triggering the workflow and passing the testing suite(includes linting). Once the testing suite is passed, a branch can be pulled into main via a pull request, which would require a code review if there were multiple people working on the project.   

### Sample Workflow
While the original project did not follow a continuous integration workflow, if I were to start the project again, I would implement a continuous integration workflow as follows:
* Create a separate branch to add a feature or update existing code.  
* Update code on new branch using a testing suite and test driven development.
* When the code has been updated to pass the testing suite, issue a pull request to be submitted for code review (if working with a team).
* Merge branch into main codebase. 

## Sources Cited
Oregon State University (August 2022) Adapted from course materials for Data Structures & Software Engineering II http://www.oregonstate.edu
