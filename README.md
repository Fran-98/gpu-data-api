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
### ```GET /gpu_info_all```

### Response
Returns a json with all the GPUs that are inside the database.
### Example
#### Request
```
GET /gpu_info_all/
```
#### Response
```
{
  "all gpus": [
    {
      "bus": "PCIe 4.0 x16",
      "gpu_chip": "AD106",
      "gpu_clock": 1925,
      "igp": "No",
      "manufacturer": "NVIDIA",
      "memory_bus_width": 128.0,
      "memory_clock": 2250.0,
      "memory_size": 8.0,
      "memory_type": "GDDR6",
      "name": "GeForce RTX 4050",
      "pixel_shader": NaN,
      "releaseYear": 2023.0,
      "rop": 48,
      "tmu": 120,
      "unified_shader": 3840.0,
      "vertex_shader": NaN
    },
    {
        ...
    },
    ...
  ]
}
```
### ```GET /gpu_info``` 
Returns all the data of the GPU.

### Parameters
- `name`: Name of the GPU, it can admit multiple names at once.

### Response
Return a JSON object with the following properties:
- `gpus`: A list with GPU objects, each with the following properties:
    - `name`: Name of the graphics card.
    - `manufacturer`: Manufacturer of the GPU.
    - `release`: Release date.
    - `memory_size`: VRAM memory size.
    - `memory_bus_width`: Width of the memory bus.
    - `gpu_clock`: GPU clock.
    - `memory_clock`: Memory clock.
    - `unified_shader`: Unified shaders.
    - `tmu`: TMU. (if it exist in the DB)
    - `rop`: ROP. (if it exist in the DB)
    - `pixel_shader`: Pixel shard. (if it exist in the DB)
    - `vertex_shader`: Vertex shader. (if it exist in the DB)
    - `igp`: If it has IGP.
    - `bus`: BUS type.
    - `memory_type`: Memory Type.
    - `gpu_chip`: GPU chipset.

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



### GET `/gpu_compare/{gpu1}&{gpu2}` 
Returns a json with the comparison of the GPUs.
### Parameters
WIP
### Response
WIP
### Example
WIP
 

### GET `/gpu_in_rank/{rank}`
Returns a json with the GPU in the rank inserted.
### Parameters
`rank`: Position of the best performance ranking in which the gpu is located. The value must be only a one number.
### Example
#### Request
```
GET /gpu_in_rank/1
```
#### Response
```
{
  "gpu in rank": [
    {
      "averageScore": "9,983",
      "gpuName": "NVIDIA A40",
      "price": null
    }
  ]
}
```


### GET `/gpu_info/{manufacturer}`
Return a json with the gpus made by the manufacturer.
### Parameters
`manufacturer`:name of the company that manufactured the gpu. The available companies are: AMD, NVIDIA or Intel
### Example
#### Request
```
GET /gpu_info/amd
```
#### Response
```
{
  "gpu according to manufacturer": [
    {
      "bus": "PCIe 4.0 x8",
      "gpu_chip": "Rembrandt",
      "gpu_clock": 1500,
      "igp": "Yes",
      "memory_bus_width": NaN,
      "memory_clock": NaN,
      "memory_size": NaN,
      "memory_type": "System Shared",
      "name": "Radeon 660M",
      "pixel_shader": NaN,
      "releaseYear": 2022.0,
      "rop": 16,
      "tmu": 24,
      "unified_shader": 384.0,
      "vertex_shader": NaN
    },
    ...
  ]
}
```

### POST `/gpu_info_post`
Route to send data using POST method. The data is saved in the specs table and in the benchmarks table.

### Example
#### Request
```
POST /gpu_info_post



body:
{
  "manufacturer": "string",
  "gpuName": "string",
  "releaseYear": int,
  "memSize": int,
  "memBusWidth": int,
  "gpuClock": int,
  "memClock": int,
  "unifiedShader": int,
  "tmu": int,
  "rop": int,
  "pixelShader": "",
  "vertexShader": "",
  "ipg": "string",
  "bus": "string",
  "memType": "string",
  "gpuChip": "string",
  "averageScore": int,
  "price": int
}

```
#### Response
```
if everything goes well:
{
  "Messege": "GPU added"
}

else:
error {error}
```

### DELETE `/gpu_delete/{gpu_name}`
This route uses DELETE method to delete all data from the specified gpu.
### Parameters
`gpu_name`: name of the gpu from which you want to remove.

### Example
#### Request
```
DELETE /gpu_delete/{gtx 1060}

```
#### Response
```
if everything goes well:
{
    'Messege':'GPU delete'
}

else:
error {error}
```

### PUT `/gpu_update/{gpu_name}`
This route uses PUT method to update the data from the specified gpu.
### Parameters
`gpu_name`: name of the gpu from which you want to update.

### Example
#### Request
```
PUT /gpu_update/{gtx 1060}


body:
{
  "manufacturer": "string",
  "gpuName": "string",
  "releaseYear": int,
  "memSize": int,
  "memBusWidth": int,
  "gpuClock": int,
  "memClock": int,
  "unifiedShader": int,
  "tmu": int,
  "rop": int,
  "pixelShader": "",
  "vertexShader": "",
  "ipg": "string",
  "bus": "string",
  "memType": "string",
  "gpuChip": "string",
  "averageScore": int,
  "price": int
}
```
#### Response
```
if everything goes well:
{
    'Messege':'GPU update'
}

else:
error {error}
```

#### Errors
This API uses the following error codes:
- `400 Bad Request`: The request was malformed or missing required parameters.
<!-- - `401 Unauthorized`: The API key provided was invalid or missing. -->
- `404 Not Found`: The requested resource was not found.
- `500 Internal Server Error`: An unexpected error occurred on the server.
