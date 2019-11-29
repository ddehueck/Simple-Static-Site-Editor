# Simple-Static-Site-Editor

Flask application to update a static site's data via JS files. The editor writes to a JS file and the static site reads from the JS file. See my site as an example of a site that consumes this application.

**Why did you make this?** I wanted an interface to update my personal site so I could keep track of smaller scale things like papers I've been reading. I also did not want to add a full backend to my little static site for sake of simplicity (reading a JS file vs. consuming an API). 

**Why do you write to a JS file instead of a JSON file?** To avoid cross-origin resource sharing. If you could load a website and have it try to access any file on your system then that would be a serious security breech, so most browsers do not allow this functionality. Hence, reading a JSON file is much more difficult than reading a JS file as we do not run into this cross-origins problem.

## Editor File Structure

- app
  - data  `# data that will be ported to static site`
    - papers.js
  - papers  `# directory that handles papers.js`
    - routes.py
    - forms.py
  - static
    - css
      - style.css
      - papers.css
  - templates
    - layout.html
    - papers
      - index.html
      - edit.html
  - \_\_init\_\_.py
  - utils.py
