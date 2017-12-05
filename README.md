Item-Catalog-Project
====================
Project files for the Item Catalog Project in the Udacity Full Stack Nanodegree.

This project contains a database of comic book universe characters.

## Set Up Instructions
Follow these instructions to set up the Vagrant Linux Environment and the Item Catalog Project

### Prerequisite Resources
You will need the following Python resources for it to run:
<ul>
  <li>Python 2.7 or above (https://www.python.org/downloads/).
  <li>Git (https://git-scm.com/downloads).
  <li>Vagrant (https://www.vagrantup.com/).
  <li>VirtualBox (https://www.virtualbox.org/wiki/Downloads).
  <li>Sqlalchemy (https://www.sqlalchemy.org/download.html).
</ul>

You will need the following other resources for it to run:
<ul>
  <li>Flask (http://flask.pocoo.org/).
  <li>Httplib2 (https://pypi.python.org/pypi/httplib2/0.10.3).
  <li>Oauth2client (https://pypi.python.org/pypi/oauth2client/).
  <li>Web browser i.e. Chrome (https://www.google.com/chrome/)
</ul>

### Installation

<ul>
  <li>Install Git (https://git-scm.com/downloads) on the local machine
  <li>Install Python 2.7 or above (https://www.python.org/downloads/) on the local machine
  <li>Install VirtualBox (https://www.virtualbox.org/wiki/Downloads) on the local machine
  <li>Install Vagrant (https://www.vagrantup.com/) on the local machine
</ul>

### Preparing the Virtual Machine
<ol>
  <li>Use git clone https://github.com/petergns/item-catalog-project.git to clone this repository.
  <li>Navigate to the cloned repository using Git i.e. cd desktop/local-machine/vagrant
  <li>Run the command 'vagrant up' to download and install the linux operating system.
  <li>Run the command 'vagrant ssh' to log in to the virtual machine.
  <li>Install Flask (http://flask.pocoo.org/) with pip install Flask, if it is not installed already.
  <li>Install Sqlalchemy, Httplib2 and Oauth2client with sudo apt-get install, if they are not installed already.
 </ol>

### Setup the Database
After the initial setup you can load the project files while connected to vagrant.

Navigate to cd item-catalog-project:
<ol>
  <li>Run python requirements.txt
  <li>Run python database_setup.py
  <li>Run your web browser.
</ol>

### Contents of the Project
It uses python to establish a simple item-catalog database with an ability to add and edit new items.

The Item Catalog allows:
<ul>
  <li>Facebook or Google online login to edit add or delete content.
  <li>Comic book characters to be added from comic book universes.
  <li>New comic book universes to be added for characters.
</ul>

### Preparing the Project
In order to run the project you must have:
1. Run requirements.txt with the python requirements.txt command.
2. Run database_setup.py with the python database_setup.py command.
3. Checked universe_characters.py in a editor (some of which are featured below), if you would like to add more characters locally.
4. Run python universe_characters.py with the python universe_characters.py command.
5. Prepared your web browser to navigate to http://localhost:5000

### Run the Project
1. Run the command python project.py in order to start the item-catalog.
2. Navigate to http://localhost:5000 on your web browser for access.

### Useful Editors:
<ul>
  <li>Atom (https://atom.io/)
  <li>Notepad++ (https://notepad-plus-plus.org/)
  <li>Sublime Text (https://www.sublimetext.com/)
</ul>

### Catalog When Logged In
![Image of Output](https://github.com/petergns/item-catalog-project/blob/master/comic-universe-catalog.PNG)

### Adding a Comic Book Character Page
![Image of Output](https://github.com/petergns/item-catalog-project/blob/master/add-new-character.PNG)

## Author
[petergns](https://github.com/petergns)

### Free Image Resource
1. https://pixabay.com/en/x-men-hero-marvel-comic-book-2640250/

## Acknowledgments
Acknowledgments to [Udacity](https://www.udacity.com/) for the resources that helped me develop this.
