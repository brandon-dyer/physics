##Dockerfile

from ubuntu:20.04 

run mkdir /physics

copy source/scripts/install /physics/install

run /physics/install

copy source /physics

run export PYTHONPATH=/physics/library && \
    python3 /physics/examples/example.py

