from Constants import classifiers, imports, encoding, requirements
#from coalib.bears.requirements.PythonRequirement import PythonRequirement
import subprocess
import shutil
import os
import glob
import re

if not os.path.exists('upload'):
    os.mkdir('upload')

#Reqrs = MockBear.REQUIREMENTS

# for req in Reqrs:
#    if type(req) == PythonRequirement:
#        if req.version:
#            reqs.write(req.package + '==' + req.version + '\n')
#        else:
#            reqs.write(req.package + '\n')

bears = glob.glob('**/*Bear.py')

for bear in bears:
    file = bear
    bear = re.match(r'.+/(.*)\.py', bear).group(1)
    if not os.path.exists('upload/' + bear):
        os.mkdir(os.path.join('upload', bear))
        if not os.path.exists(os.path.join('upload', bear, bear)):
            os.mkdir(os.path.join('upload', bear, bear))
    if not os.path.exists(os.path.join('upload', bear, bear, '__init__.py')):
        init = open(os.path.join('upload', bear, bear, '__init__.py'), 'w')
        init.write(' ')
        init.close()
    shutil.copyfile(file, os.path.join('upload', bear, bear, bear + '.py'))

    with open('upload/' + bear + '/requirements.txt', "w") as reqs:
        pass
    with open('upload/' + bear + '/setup.py', "w") as setup:

            # set env
        setup.write('#!/usr/bin/env python3\n\n')

        # write imports
        setup.write(imports + '\n\n')

        # encoding UTF-8
        setup.write(encoding + '\n\n')

        # requirements
        setup.write(requirements + '\n\n')

        # setuptools
        setup.write('if __name__== "__main__":\n')
        setup.write("\tsetup(name=" + "'" + bear + "',\n")
        setup.write('\t\t  version="0.1.30",\n')
        setup.write("\t\t  description='The " + bear + " bear for coala (Code")
        setup.write(" Analysis Application)',\n")
        setup.write('\t\t  classifiers=' + classifiers + ')')

        # upload everything

        os.chdir(os.path.join('upload', bear))
        #subprocess.call(['python', 'setup.py', 'register', '-r', 'pypitest'])
        #subprocess.call(['python', 'setup.py', 'sdist', 'upload', '-r',
        # 'pypitest'])
        os.chdir(os.path.join('..', '..'))
