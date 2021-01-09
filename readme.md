
### About this Project:
This is a 'Portfolio Exercise' Portfolio Exercise based on the instructions from Udacity Data Scientist Nanodegree/Software Engineer/Lesson 5. I use object-oriented programming and create a package and upload the package to make a calculus package that implements algorithms Newton's method.

### Environment:
This project is run in a virtual workspace set by Udacity. The workspace is the same Ubuntu Linux environment.
Workspace URL: https://classroom.udacity.com/nanodegrees/nd025/parts/0469f04b-1440-4b2c-9f69-8882d6ec436b/modules/237f5e87-7a8e-49d1-aab9-241006ce715e/lessons/af569005-7bce-4f72-a95c-0c2aaf71634d/concepts/c68f8fc0-8864-4ede-8255-6ee195873895

### CodeDescription:
Inside the folder called `NewtonMethod_QM`, you'll find 4 .py files. Here is a description of each
- GeneralDiff.py  which contains the code for the Diff (doing differentiation) package including FstDiff.py, SecDiff.py, and NewtonMethod.py code.
- FstDiff.py  which contains the code for the Jacobian package(doing first-order derivation) including NewtonMethod.py.
- SecDiff.py  which contains the code for the Hessian package(doing second-order derivation) including NewtonMethod.py.
- NewtonMethod.py  which contains the code for the Newmeth package


### UnitTest:
- UnitTest test
pip install your NewtonMethod_QM package and then run the unit tests. In the terminal, in the 'package' directory, type `pip install .` into the command line. Then run the unit tests by typing `python -m UnitTest test`.


### Init Setting
Out of all module files(4 .py files list in 'CodeDescription' session), I config following:
- __init__.py inside the NewtonMethod_QM folder. I imported all the packages: NewMeth, Jacobian, Hessian, Diff. Also Symbol operation for 2 vectors are pre-config in the file.


### Into Python package
Convert the modularized code into a Python package.Inside the 'package' folder, need to create a few folders and files:
-  setup.py  which is required in order to use pip install
-  folder called 'NewtonMethod_QM', which is the name of the Python package
*  inside the 'NewtonMethod_QM' folder, there are 4 .py files and an __init__.py file.

Once everything is set up, open a new terminal and type:
(cd package)
pip install .


### Upload to pypi
Before uploading, I created a setup.cfg file, README.md file, and license.txt file. Also I need to create accounts for the pypi test repository and pypi repository. The username and password are needed to type in the command line.

* Note that you need to make the name of the package unique, else it will be reject when upload into pypi. Remember to update the package folder name (NewtonMethod_QM) and configs in setup.py.
https://test.pypi.org/

Then, I used the following commands on the command line:

cd package
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/project/NewtonMethod-QM/

# command to upload to the pypi repository
twine upload dist/*
pip install --
