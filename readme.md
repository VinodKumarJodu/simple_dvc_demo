env
```bash
    conda create -n WineQ python=3.7 -y
```
```bash
    conda activate WineQ
```
create rquirements.txt
installed requirements
```bash   
    pip install -r requiremetns.txt
```
Download WineQuality Dataset
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

Add Data to data_given folder
```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given\winequality.csv
```
```bash
git add . && git commit -m "first commit"
```
```bash
git branch -M main
```
```bash
git remote add origin https://github.com/VinodKumarJodu/simple_dvc_demo.git
```
```bash
git push -u origin main
```
```bash
git add . && git commit -m "Oneliner update for readme.md"
```
```bash
git push -u origin main
```