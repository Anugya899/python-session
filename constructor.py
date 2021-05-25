class Mobile:
    def __init__(self,processor,camera):
        self.processor=processor
        self.camera=camera 
    def getProcessorName(self):
        return self.processor

    def getCamera(self):
        return self.camera
Redmi=Mobile("SnapDragon",13)
print("The processor of Redmi is",Redmi.processor)
print("The camera of Redmi is", Redmi.camera)

Samsung=Mobile("Quad Core",35)
print("The processor of Smasung is",Samsung.getProcessorName())
print("The Camera of Samsung is", Samsung.getCamera())


class Movies:
    pass
