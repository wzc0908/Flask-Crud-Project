
# Brief introduction

## Part 1 Crud System with Python Flask

### 1.	Component(standalone table): the devices which contains by a product. For example you can define speaker, shell, screen for a phone device. The component include manufacturer(type text), contact(email, type text), failure rate(type float), component name(type text) and id(type integer primary key).

### 2.	Fail Mode(standalone table): the failure tested out by a tester(Audio Degradation, Hardware Degradation, Battery Degration etc.). the fail mode include fail mode name(type text), Fail code(type text, length=6), and id(type integer primary key) 

### 3.	Mapping: a describe for a failure relation between component and fail mode, column: id(type integer primary key), component_id(type integer), failmode_id(type integer).

### Summary: 

## •	Page 1
### o	View component

### o	Able to create/update/read/delete component

## •	Page 2

### o	View fail mode table

### o	Able to create/update/read/delete fail mode

## •	Page 3

### o	View mapping table
### o	Modified mapping
### o	Remove mapping
### o	Update mapping

## Part 2: Creating Dashword with quicksort algorithm/sql commands
### •	Show to the user 3 reports:
### o	Top 5 of the most bad quality components.
### o	Top 5 of the most used of test devices.
### o	Top 3 of the highest PFR(product failure rate) manufacturer.
### Summary: I used to methods to do this. In myService.app I wrote a dynamic quicksort functions and sorted the data with python dictionary. I also used SQL commands in dbQuery.app to do the same sorting process. And I generated graphs with highcharts.


