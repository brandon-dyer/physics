##setup
from ubuntu:20.04 
run mkdir /physics/scripts -p

##base install
copy source/scripts/install /physics/scripts/install
run /physics/scripts/install

##user entrypoint + dev copy of source
copy source /physics
entrypoint /physics/scripts/entrypoint

