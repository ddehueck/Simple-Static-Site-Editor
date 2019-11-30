# Simple-Static-Site-Editor

Flask application to update a static site's data via JS files. The editor writes to a JS file and the static site reads from the JS file. See my site as an example of a site that consumes this application. It's a good tnterface for editing a github pages site!

**Why did you make this?** I wanted an interface to update my personal site so I could keep track of smaller scale things like papers I've been reading. I also did not want to add a full backend to my little static site for sake of simplicity (reading a JS file vs. consuming an API). 

**Why do you write to a JS file instead of a JSON file?** To avoid cross-origin resource sharing. If you could load a website and have it try to access any file on your system then that would be a serious security breech, so most browsers do not allow this functionality. Hence, reading a JSON file is much more difficult than reading a JS file as we do not run into this cross-origins problem.

### How to get running!

`$ python -m flask run`

Feel free to create an issue if you want to adapt any functionality or learn more!

## Features

- Save data to JSON (in a JS file) to be easily read into html documents with vanilla JS
- Push file changes to github (will require your own user token)
- Add/Edit/Delete JSON objects
- Extend to your own data needs - defined new schemas

## Editor File Structure

- app
  - data  `# holds data that will be ported to static site`
  - managers  `# directory that handles managers that update data files`
  - static
  - templates
  - \_\_init\_\_.py
  - utils.py


## Screenshots

<img src="https://i.imgur.com/cPFp5Cv.png" alt="Main page with create new form and past entries" width="500px"/>

<img src="https://i.imgur.com/SwWz9Jc.png" alt="Edit form" width="500px"/>
