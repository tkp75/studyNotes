# Coursera lab tests

To run a simple http server (serving files from current directory):
python3 -m http.server

To create a ssh key(pair):
ssh-keygen -C tkp75@github.com -f ~/.ssh/github.id_rsa -N "" -t rsa -b 3072

NOTE: remember to set permissions (to 600) for ssh keys and config

To create a tunnel (only) via ssh:
ssh -N -L 8000:127.0.0.1:8000 <user>@<host>
