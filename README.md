**Pitch Splash** <br/>
****
![Alt text](./app/static/projectScreenshots/signUp.png?raw=true "Optional Title")
**Description:**
****
*Pitch Splash is a web application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.*

 *The pitches are organized by category. You can have different categories like pickup lines, interview pitch, product pitch, promotion pitch.*
                                                                        **Just Pitch it!**
<br />

<!-- **Live link:**  *https://pitchSplash.herokuapp.com/* <br /> -->


**Setup/Installation Requirements** 
****
*From your terminal:* <br />
```py
git clone git@github.com:AtienoObwanda/pitchSplash.git
```
<br />

*Once the program has been cloned, run this on your terminal* <br />

```
cd pitchSplash
```

<br />

*Depending on your code editor,run this on your terminal:* <br />

<br />

*Vs Code* <br />

```
code .
```
<br />

*Atom* <br />
```
atom .
```
<br />

*In order to run this project your can git clone it and then download all the requirements started on the requiremen.txt, open the app in the editor of your choice,open your terminal and run the  app*
<br />

**Known Bugs**
****
*There are no known bugs...*

**Project Features**
****
*You have one minute to pitch...* <br />

**Login:** <br />
![Alt text](./app/static/projectScreenshots/login.png?raw=true "Optional Title")

<br />

**Splash Pitch:**
![Alt text](./app/static/projectScreenshots/pitch.png?raw=true "Optional Title")

<br/>

**Account:** 
![Alt text](./app/static/projectScreenshots/account.png?raw=true "Optional Title")

<br/>


**View Your Pitch from your account:**
![Alt text](./app/static/projectScreenshots/profilePitch.png?raw=true "Optional Title")

<br />

**React to pitch-Also added delete function to comments, exclusively to pitch authors and comment author:**
![Alt text](./app/static/projectScreenshots/react.png?raw=true "Optional Title")

<br/>

**User Story** <br/>
****

* Comment on the different pitches posted py other uses. <br/>
* See the pitches posted by other uses. <br/>
* Vote on s pitch they have viwed by giving it a upvote or a downvote. <br/>
* Register to be allowed to log in to the application <br/>
* View pitches from the different categories. <br/>
* Submit a pitch to a specific category of their choice. <br/>

**BDD** <br/>
****
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, User can either signup or login|
| Upon Selecting SignUp| **Email**,**Username**,**Password** | Then you get redirected to the login|
| For returning users, you can Login | **email** and **password** | Then you are redirected to the home page with pitches. Also, you can comment on all posts... If you're post author, you can delete any comment on your pitch! If you are pitch author, you can also delete it...|
| Select comment icon | **Comment Icon** | Redirects you to a page where you can input your comment, as much as you want|

<br/>

**Technologies Used** <br/>
****

*Python3.9.10*<br />
*Flask2.11*<br />
*Bootstrap*<br />


**Contact:**
****

*Incase of any question or contributions, you can contact me through:*
 [Atieno Obwanda](https://github.com/AtienoObwanda) ||*atienoobwanda@gmail.com* </br>


**License**
****
MIT License <br/>
**Copyright** *(c)2022* **Pitch Splash.** *All rights reserved.*

