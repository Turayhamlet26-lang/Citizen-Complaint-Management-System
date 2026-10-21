# Citizen Complaint Management System

## 1. Project Overview

The Citizen Complaint Management System is a Python program
developed to help citizens report problems in their communities.

These problems may include poor roads, water supply issues,
electricity problems, garbage, and drainage.

The system allows users to submit complaints, view complaints,
check complaint status, and update the status of complaints.

## 2. Problem Statement

People in my community face problems, but sometimes they do
not know where to report them or how to follow up.

This project provides a simple way to record complaints and
check their progress.

## 3. Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON file storage

## 4. Main Features

- Submit a complaint.
- View all complaints.
- Check complaint status.
- Update complaint status.
- Save complaints in a file.
- Load saved complaints when the program starts.

## 5. OOP Concepts Used

### Classes
The program contains two classes:
- Complaint
- ComplaintManagementSystem

### Objects
Each complaint submitted creates a Complaint object.

### Attributes
Complaint attributes include:
- Complaint ID
- Full name
- Location
- Complaint type
- Description
- Status

### Methods
Methods are used to submit, display, check, and update complaints.

### Data Structures
A list stores complaint objects, and dictionaries store complaint
details and available complaint statuses.

### Class Method
The Complaint class includes a class method named
get_office_name().

## 6. Digital Public Goods (DPG) Principles

### Open Source
The source code can be shared publicly through GitHub.

### Inclusive and Accessible Design
The program uses a simple text menu that is easy to understand.

### Privacy Respect
The program collects only the information needed to record a
complaint. Users should avoid entering sensitive personal information.

### Modular and Reusable
The program separates complaint details from complaint management
using two classes and different methods.

## 7. How to Run the Program

1. Install Python.
2. Open the project in PyCharm.
3. Run main.py.
4. Select an option from the menu.
5. Follow the instructions displayed by the program.

## 8. Example Usage

Example complaint:

Name: Mohamed Kamara
Location: Freetown
Complaint Type: Poor Roads
Description: The road has many potholes.

Example result:

Complaint ID: 1001
Status: Pending

The complaint is saved in complaints.json.

## 9. Conclusion

The Citizen Complaint Management System provides a simple way
to record community complaints and track their progress.
It demonstrates the use of classes, objects, methods, data
structures, and file handling in Python.