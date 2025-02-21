import os, platform
#os.system('xdg-open https://facebook.com/groups/3017>
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import Sarfraz
elif bit == '32bit':
    import Dump32
