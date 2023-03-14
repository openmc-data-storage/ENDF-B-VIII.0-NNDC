
# this script uploads h5 files to the git repo
# large files over 100mb are added using git lfs
# not all files are added in this way to avoid the total lfs limits
# files above 100Mb can be found with a find terminal command
# find . -type f -size +100M

import os

# sets up git large file system as some h5 files are over 100mb
# https://git-lfs.com/
os.system('git lfs install')
os.system('git lfs track "h5_files/neutron/U238.h5"')
os.system('git lfs track "h5_files/neutron/U235.h5"')
os.system('git add .gitattributes')

# downloads the h5 files 
os.system('pip install openmc_data')
# os.system('download_nndc -d h5_files -r b8.0')


os.system('git pull')
os.system('git add h5_files/*.xml')
os.system('git commit -m "added xml"')
os.system('git push')
for char in [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u235', 'u238', 'u', 'v', 'w', 'x', 'y', 'z']:
    os.system(f'git add h5_files/photon/{char.title()}*.h5')
    os.system(f'git commit -m "added photon {char.title()}"')
    os.system('git push')
    os.system(f'git add h5_files/neutron/{char.title()}*.h5')
    os.system(f'git commit -m "added neutron {char.title()}"')
    os.system('git push')

# the files are often over 100mb in size
# os.system(f'git add h5_files/neutron/c_*.h5')
# os.system(f'git commit -m "added neutron {char.title()}"')
# os.system('git push')