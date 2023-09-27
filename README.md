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

## Base URL
The base URL for all API requests is:

`https://example.com`

## Endpoints
```GET /gpu_info_all```
    Returns a json with all the GPUs that are inside the database.

```GET /gpu_info``` 
*gpu_name:str* 
    Returns all the data of the GPU.
### Parameters
- `name`: Name of the GPU, it can admit multiple names at once.

### Response
Return a JSON object with the following properties:
- `gpus`: A list with GPU objects, each with the following properties:
    - `name`:
    - `manufacturer`:
    - `release`:
    - `memory_size`:
    - `memory_bus_width`:
    - `gpu_clock`:
    - `memory_clock`
    - `unified_shader`:
    - `tmu`:
    - `rop`:
    - `pixel_shader`:
    - `vertex_shader`:
    - `igp`:
    - `bus`:
    - `memory_type`:
    - `gpu_chip`:

### Example
#### Request
```
GET /gpu_info?name=GTX%201060&name=RX%207700
```
#### Response
```
{
    "gpus":[
        {   
            "name":
            "manufacturer":
            "release":
            "memory_size":
            "memory_bus_width":
            "gpu_clock":
            "memory_clock"
            "unified_shader":
            "tmu":
            "rop":
            "pixel_shader":
            "vertex_shader":
            "igp":
            "bus":
            "memory_type":
            "gpu_chip":
        },
        {   
            "name": "Radeon RX 7700 XT"
            "manufacturer": "AMD"
            "release": 2022
            "memory_size": 8
            "memory_bus_width": 128
            "gpu_clock": 1800
            "memory_clock": 2250
            "unified_shader": 4096
            "tmu": 256
            "rop": 128
            "pixel_shader": None
            "vertex_shader": None
            "igp": "No"
            "bus": "PCIe 5.0 x16"
            "memory_type": "GDDR6"
            "gpu_chip": "Navi 33"
        },
    ]
}
```



- GET `/gpu_compare/{gpu1}&{gpu2}` *gpu1:str*, *gpu2:str* 
    Returns a json with the comparison of the GPUs.

- GET `/gpu_in_rank/{rank}` *rank:int*
    Returns a json with the GPU in the rank inserted.

- GET `/gpu_info/manufacturer`
    Return a json with the gpus made by the manufacturer and the series if especified.

#### Errors
This API uses the following error codes:
- `400 Bad Request`: The request was malformed or missing required parameters.
<!-- - `401 Unauthorized`: The API key provided was invalid or missing. -->
- `404 Not Found`: The requested resource was not found.
- `500 Internal Server Error`: An unexpected error occurred on the server.