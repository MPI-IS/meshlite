MeshLite
========
This package was created as an accessory for visualizing, editing and saving meshes
by the Perceiving Systems Department at Max Planck Institute for Intelligent Systems. 
The meshlite packaage was created specifically for use with our body, hands and face models.

This package is being provided as an accessory for visualizing, editing and saving meshes for
our body, hands and face models, namely SMPL, MANO and FLAME. To learn more about these models,
please visit the model websites:

- http://smpl.is.tue.mpg
- http://mano.is.tue.mpg
- http://flame.is.tue.mpg

Please see the accompanying LICENSE.txt file for licensing and contact information. You must agree to the
license terms before using this package.


System Requirements
===================
Currently this package has only been tested for the following:

Python version:
- Python 2.7

Operating systems:
- OSX (10.12)
- Linux (Ubuntu 14.04.1 LTS)

Installation Guide
==================

## Install from compiled binaries
---------------------------------
You can install the package directly from the .whl binary files instead of compiling & installing through the
source. The wheels (.whl files) are located in the downloads folder of the repository:

```
pip install --find-links=downloads psbody-meshlite
```

## Install from source
-----------------------

### 1. Clone the repository
---------------------------
Get the repository as follows:

```
git clone git@github.com:naureenm/meshlite.git
```

This will download the repository into a directory named `meshlite` by default.


### 2. Install pip
-----------------

For LINUX:
```
sudo apt-get install python-pip
```


For OSX:
Get the script get-pip.py from it's official website (https://pip.pypa.io/en/stable/installing/),
then run the following commands on a terminal wnidow:

```
sudo python get-pip.py
pip install --upgrade pip
```


### 3. Install VirtualEnv
------------------------
It is a good practice to install the python packages in a Python virtualenv (https://virtualenv.pypa.io/en/stable/)

Your system can have its own versions of the packages, while meshlite can use additional or updated ones.
You do not need administrative privileges on your computer to install additional packages in a `virtualenv`, which
lowers the risks of having an unstable computer and does not require the intervention of a sys-admin.


For LINUX:
```
sudo apt-get install python-virtualenv
```

For OSX:
Get the script get-pip.py from it's official website (https://pip.pypa.io/en/stable/installing/),
then run the following commands on a terminal wnidow:

```
pip install virtualenv
```


### 4. Setup VirtualEnv
----------------------
It's convenient to have a single location for all of your project virtualenvs, so we'll create one.

```
#   Make a virtual env container directory, and create a venv named 'meshlite'
export WORKON_HOME="$HOME/.virtualenvs"
mkdir $WORKON_HOME
virtualenv --system-site-packages $WORKON_HOME/meshlite

#   Now activate the new virtualenv
source $WORKON_HOME/meshlite/bin/activate
```

*Note*: Remember to always activate your virtualenv before trying your frankengeist code



### 5. Install MeshLite
----------------------
Navigate to the meshlite directory, and run the following two commands

```
make
make install
```


### 6. Clean up
--------------
During the build or the use of the repository, some intermediate files are generated. It is possible to remove those intermediate
files by running the following:

```
make clean
```


Run Hello-World Script
======================
If all goes well, you are now ready to try the hello_world.py script. Simple run the following in a terminal window:

```
python sample/hello_world.py
```

- This should display a MeshViewer window with a teapot.
- You can click and drag on the window to rotate around the mesh.
- Press 'c' to continue. This will save the mesh as an obj file to your /tmp folder.
