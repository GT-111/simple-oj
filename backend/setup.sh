conda create -n webenv python=3.10
conda activate webenv
conda install -c conda-forge flask=2.2.3
conda install -c conda-forge pydantic=1.10.5
pip3 install -r "requirements.txt"