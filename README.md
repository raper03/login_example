# login_example
The purpose of this repository is to **showcase the depth of my understanding of Git**. This Markdown is not only part of a homework assignment but also part practice into mastering the `README.md`.  
  
This project contains an example of a login page that also stores login information into a local file. The project is *of course* capable of using the login information to aid in logging in and catching exisiting usernames.

## Table of Contents
- [Installation](#installation)  
- [Usage](#usage)

## Installation
### Requirements
1. [Python](https://www.python.org/downloads/) 3.8.5 **+**
2. An IDE capable of running or interpreting Python  
3. pyinputplus

To install pyinputplus, enter the following into your terminal

    pip install --user pyinputplus

This project can be directly downloaded via [the main page](https://www.github.com/raper03/login_example) of this repository from the big green **Code** button.
Otherwise, you may clone this repository by grabbing the HTTPS also found in the big green **Code** button.

To check if the repo has installed correctly,  
Navigate to the directory in which you installed login_example with terminal.  

    cd C:\Users\user\...
    
In the directory run the main module

    C:\Users\user\...> python main.py


## Usage
### Sign in
A default account has already been created to use the 'sign in' feature right away without needing to create an account beforehand.  
Check `userdata.JSON` to view this account, or the ['Sign up'](#sign-up) section.

In the menu, select 'sign in' by typing 'sign in'

    Please select one of the following:
    *sign up 
    *sign in
    > sign in

When prompted, the user may then attempt to login with their information. If there is no record of this account, however, the login attempt fails. After many failed attempts at signing in, the user is kicked out of the prompt and must select sign in again. A successful login attempt will take you to Club Penguin.

### Sign up
In the menu, select 'sign up' by typing 'sign up'

    Please select one of the following:
    *sign up 
    *sign in
    > sign up

When prompted, the user may then attempt to create an account. Any username can be created (can have spaces!), but if this username is already in use, located in `userdata.JSON`, the user is notified and is able to create a different user.

    Create an account:
        Please enter a username: admin
    admin is already taken!
        Please enter a username: <username>

After creating a unique username the user is then required to create a password. The password must be strong because I borrowed a module from my python coding class that tests for password strength.  

If you would like to force create an account then simply modify `userdata.JSON` directly, make sure to follow proper JSON syntax, the account must be created as a separate object inside the 'data' list.

    {
        'data':[
            {
                'user': admin
                'password' : password
            },
            {
                'user' : <username>
                'password': <password>
            }
        ]
    }






