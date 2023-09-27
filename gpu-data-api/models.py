import db

from sqlalchemy import Column, Integer, String, Float

class gpuBenchmarks(db.Base):
    __tablename__ = 'gpu_benchmark'

    #id = Column(Integer, primary_key=True)
    gpuName = Column(String(128), primary_key=True, nullable=False)
    score = Column(Integer, nullable=False)
    price = Column(Float)

    def __init__(self, name, score, price):
        self.name = name
        self.score = score
        self.price = price
    
    def __repr__(self):
        return f'{self.name}, score: {self.score}, price: {self.price}'

    def __str__(self):
        return self.name
    



class gpu_spec(db.Base):
    __tablename__ = 'gpu_spec'
    manufacturer = Column(String(30))
    gpuName = Column(String(50), primary_key=True)
    releaseYear = Column(Integer)
    memSize=Column(Integer)
    memBusWidth=Column(Integer)
    gpuClock=Column(Integer)
    unifiedShader=Column(Integer)
    tmu=Column(Integer)
    rop=Column(Integer)
    pixelShader=Column(String(10))
    ipg=Column(String(10))
    bus=Column(String(30))
    memType=Column(String(20))
    gpuChip=Column(String(20))


    def __init__(self, manufacturer, gpuName, releaseYear, memSize, memBusWidth, gpuClock, unifiedShader, tmu, rop, pixelShader, ipg, bus, memType, gpuChip):
        self.manufacturer = manufacturer
        self.gpuName = gpuName
        self.releaseYear = releaseYear
        self.memSize = memSize
        self.memBusWidth = memBusWidth
        self.gpuClock = gpuClock
        self.unifiedShader = unifiedShader
        self.tmu = tmu
        self.rop = rop
        self.pixelShader = pixelShader
        self.ipg = ipg
        self.bus = bus
        self.memType = memType
        self.gpuChip = gpuChip
       
    def __repr__(self):
        return f'{self.gpuName}, manufacturer: {self.manufacturer}, releaseYear: {self.releaseYear}, memSize: {self.memSize},memBusWidth: {self.memBusWidth}, gpuClock: {self.gpuClock},unifiedShader: {self.unifiedShader}, tmu: {self.tmu}, rop: {self.rop}, pixelShader: {self.pixelShader}, ipg: {self.ipg}, bus: {self.bus}, memType: {self.memType}, gpuChip: {self.gpuChip}'

    def __str__(self):
        return self.gpuName