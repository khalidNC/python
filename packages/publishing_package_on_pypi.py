''' This section we will narrate the steps of publishing a package on Pypi site and will do a small
project in a separate directory. The steps to publish package on pypi.org are as below :

1. Visit pypi.org sute and signup and verify your email account also set 2 factor authentication.

2. Go back to the terminal and install 3 tools globally:
    a. Setuptools
    b. Wheel
    c. Twine

    The terminal command is: pip3 install setuptools wheel twine
    This will download and install all the tools.

3. Now need to create a new directory for the new project. let's say the new package is on working with pdf.
   So create a new directory named khalidpdf in terminal the related commands as below:
   - to create a directory: mkdir khalidpdf
   - to open the directory: cd khalidpdf
   - to open the directory in vscode: code .
      Note: if 'code' does not install on vscode then code . command will not work. So in this case you need
      to install 'code' on vscode. The step to install 'code' are bellow:
      - Open vscode
      - Menu bar on top, go to View then go to Command Palette
      - or via shortkey: shift+command+P and type 'shell command' to find the Shell Command:
      - Then install 'code' command in PATH


4. This command will open the project directory in vscode. Now as a best practice it should create the high
   level directory with the same nome of our package so;
   a. Create a directory named: khalidpdf
   b. We need another directory for unit test named: tests
   c. We might have another directory for some sort of data named: data
   d. Note: all our source code will be in the directory khalidpdf. So add init file to khalidpdf so that
      Python recognizes this directpry as package. [Note: make sure you have select the global python
      interpretor in vscdoe] Then add a couple modules. So we add a couple of files let's say,
      pdf2text.py[here we will write simple fuction that converts pdf]

      def convert():
        print("pdf2text")
      
      and another module pdf2image.py
      here we also write funtion that converts pdf to image. 
      This is a basic struture of a package.

      So the khalidpdf directory structure looks like:
      khalidpdf
        __init__py
        pdf2text.py
        pdf2image.py

5. Now in order to publish into pypi site we need to add another 3 files in the root directory. The most 
   important one is setup.py, README.md file, and LICENSE
   a. setup.py file: First import setuptools(That we installed at the begining). That module has 
      a method called .setup(). We will call this method and will pass few keyword=arguments there.
      Here the essential ones:

      name="khalidpdf" [set this to a unique name of the package so that it does not conflict with other name.]
      version=1.0
      long_description="" [Need to write a description that will display on pypi site as package decription.
                            We will create a README file and will link up here]
      packages=setuptools.find_packages(exclude=["tests", "data"])

      [We need to setup like, telling what package and module we are going to publish. To do so
      we use a method .find_packages() this method will look at our project and automatically discover the 
      packages that we have difine. However we need to tell to exclude tests and data files because this are 
      not the object in the source code by suppling keyword=arguments in a list into the method.]
      This is our setup file looks like as below:

          import setuptools

          setuptools.setup(
          name="khalidpdf"
          version=1.0
          long_description=""
          packages=setuptools.find_packages(exclude=["tests", "data"])
          )

   b. README.md file: In the readme file we need to write in markdown syntax. For the time being we write a text
      like "This is the homepage of our project"

   c. LICENSE file: We also need to create a LICENSE file in the root directory. If you vist to this site:
      https://choosealicense.com you will find a basic template for the license file. Let's say we select
      and go to this page: https://choosealicense.com/licenses/gpl-3.0/# and copy the text for the license
      and paste into the LICENSE file.

   d. Now go back to the setup.py file and should setup the long_description content to our README.md file
      to do so, on the top import Path from pathlib
      then create a Path() object and set this to Path("README.md")
      and then call Path("README.md").read_text()

      So the setup.py file finally looks like;
       
        import setuptools
        from pathlib import Path

          setuptools.setup(
          name="khalidpdf"
          version=1.0
          long_description=Path("README.md").read_text()
          packages=setuptools.find_packages(exclude=["tests", "data"])
          )
      
   e. So far we created a project then added few directories and modules in it and write some functions.
      At this point, the structure looks like as below;

      KHALIDPDF
        - khalidpdf
          - __init__.py
          - pdf2text.py
          - pdf2image.py
        - tests
        - data
        - setup.py
        - README.md
        - LICENSE

6. Now we need to generate a distribution package and that is very easy. Just need to open up the terminal
   and run a command python3 setup.py and pass 2 arguments: sdist [Short form of Source distribution] and 
   bdist_wheel [Short form of build distribution] with this command we can generate 2 distribution packages
   in the root directory with name: dist and build.
          
          The terminal command: python3 setup.py sdist bdist_wheel

   Now in the dist file we see 2 files. One of them is wheel(.whl) file which is build distribution. 
   Another one is source distribution. Both are zip files so you can unzip and can see what inside there. 
   Now the project structure look like;

      KHALIDPDF
      - khalidpdf
        - __init__.py
        - pdf2text.py
        - pdf2image.py
      - tests
      - data
      - setup.py
      - README.md
      - LICENSE
      - build
      - dist
        - khalidpdf-1.0-py3.whl
        - khalidpdf-1.0.tar.gz

7. Now we have the distribution packages and we are ready to upload the package into the pypi site. 
   To do so, back to the terminal and use twine to upload as terminal command. The command will be:

   twine upload dist/*

   Which means we are telling twine to upload all the files in dist directory. 

   After running this command it asks my username: then password: and input the informantion and my 
   package is uploaded to the pypi.org site.

   Note: It is recommanded that, for testing purpose it is preffered to register on testpypi site: and complete
         the registration part with 2FA.
         Doc for more detail: https://packaging.python.org/en/latest/guides/using-testpypi/
         Then upload package on the testpypi site by the below terminal command:

         twine upload --repository testpypi dist/*

         After run this command it ask for input username and password. Then upload completed.
         Terminal output:
            View at:
            https://test.pypi.org/project/khalidpdf/1.0/

         Then visit to the site site and look at the package you just uploaded.
         There is a link to install the package: pip3 install -i https://test.pypi.org/simple/ khalidpdf==1.0
         Use the link to install in your project and import the module of the package and use.
         Ypu can also use the pipenv command to install the package.

8. Now visit to pypi.org and search for khalidpdf you find find this on the site. Now you can install
   this package just like other packages on pypi.org for example:

   a. Open a different project on vscode
   b. install khalidpdf: pipenv install khalidpdf
   c. create a py file and on the top import khaldpdf
   d. now you can see moshpdf. has 2 modules(pdf2text, pdf2image)
   e. so let's import pdf2text: from khalidpdf import pdf2text
   f. then call pdf2text.convert()
   g. and run the program 
   h. and in the output: pdf2text '''


''' For real world example, a separate project name khalidpdf has been created for publishing package on pypi. '''

''' Finally, the instalation part:
1. In 2 ways you can install the package '''

from khalidpdf import pdf2text

pdf2text.conver()

