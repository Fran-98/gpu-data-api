# GPU Benchmark score API
This API has a database with average benchmark scores for every GPU on the market, it has some endpoints to compare different GPUs and to get the info from the database. 

*It was made as an educational project and as an example of an API made using python.*

## Run the API
The API was made using **python 3.11**.
1. Clone the repo anywhere you want
2. Create a Virtual Enviroment into your project folder and activate it
```
python -m venv env
cd env/Scripts
activate
```
4. Install the requirements with pip
```
pip requirements -r 'requirements.txt
```
5. Create a .env file with your environment variables. The required ones are as follows:
```
DB_USER
DB_PASSWORD
```
6. Work in progress

## TO DO
- [x] Designate endpoints
- [x] Create and populate DB
- [ ] Clean data on DB
- [x] Models
- [ ] Create endpoints
- [ ] Template home
- [ ] Testing
- [ ] Host API

## Endpoints
- GET `/gpu_info_all` 
    Returns a json with all the GPUs that are inside the database.

- GET `/gpu_info/{gpu_name}` *gpu_name:str* 
    Returns a json with all the data of the GPU.
    
- GET `/gpu_compare/{gpu1}&{gpu2}` *gpu1:str*, *gpu2:str* 
    Returns a json with the comparison of the GPUs.

- GET `/gpu_in_rank/{rank}` *rank:int*
    Returns a json with the GPU in the rank inserted.

- GET `/gpu_info/manufacturer`
    Return a json with the gpus made by the manufacturer and the series if especified.

