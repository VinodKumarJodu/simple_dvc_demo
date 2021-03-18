env
    conda create -n WineQ python=3.7 -y
    conda activate WineQ
create rquirements.txt
installed requirements
    pip install -r requiremetns.txt
Download WineQuality Dataset
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

Add Data to data_given folder

git init

dvc init

dvc add data_given\winequality.csv

git add . && git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/VinodKumarJodu/simple_dvc_demo.git

git push -u origin main