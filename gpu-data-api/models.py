import db

from sqlalchemy import Column, Integer, String, Float

class gpuBenchmarks(db.Base):
    __tablename__ = 'gpu_benchmark'

    #id = Column(Integer, primary_key=True)
    gpuName = Column(String(128), primary_key=True, nullable=False)
    averageScore = Column(Integer, nullable=False)
    price = Column(Float)

    def __init__(self, gpuName, averageScore, price):
        self.gpuName = gpuName
        self.averageScore = averageScore
        self.price = price
    
    def __repr__(self):
        return f'gpuName: {self.gpuName}, averageScore: {self.averageScore}, price: {self.price}'

    def __str__(self):
        return self.gpuName
    



class gpu_spec(db.Base):
    __tablename__ = 'gpu_spec'
    manufacturer = Column(String(30))
    gpuName = Column(String(50), primary_key=True)
    releaseYear = Column(Integer)
    memSize=Column(Integer)
    memBusWidth=Column(Integer)
    gpuClock=Column(Integer)
    memClock=Column(Integer)
    unifiedShader=Column(Integer)
    tmu=Column(Integer)
    rop=Column(Integer)
    pixelShader=Column(String(10))
    vertexShader=Column(String(10))
    igp=Column(String(10))
    bus=Column(String(30))
    memType=Column(String(20))
    gpuChip=Column(String(20))


    def __init__(self, manufacturer, gpuName, releaseYear, memSize, memBusWidth, gpuClock, memClock, unifiedShader, tmu, rop, pixelShader, vertexShader, igp, bus, memType, gpuChip):
        self.manufacturer = manufacturer
        self.gpuName = gpuName
        self.releaseYear = releaseYear
        self.memSize = memSize
        self.memBusWidth = memBusWidth
        self.gpuClock = gpuClock
        self.memClock = memClock
        self.unifiedShader = unifiedShader
        self.tmu = tmu
        self.rop = rop
        self.pixelShader = pixelShader
        self.vertexShader = vertexShader
        self.igp = igp
        self.bus = bus
        self.memType = memType
        self.gpuChip = gpuChip
       
    def __repr__(self):
        return f'manufacturer: {self.manufacturer}, gpuName: {self.gpuName},releaseYear: {self.releaseYear}, memSize: {self.memSize},memBusWidth: {self.memBusWidth}, gpuClock: {self.gpuClock}, memClock: {self.memClock}, unifiedShader: {self.unifiedShader}, tmu: {self.tmu}, rop: {self.rop}, pixelShader: {self.pixelShader}, vertexShader:{self.vertexShader} ,igp: {self.igp}, bus: {self.bus}, memType: {self.memType}, gpuChip: {self.gpuChip}'

    def __str__(self):
        return self.gpuName