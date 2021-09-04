class Notas:
    def __init__(self,bimestre1,bimestre2,bimestre3,bimestre4,id_alumno=0):
        self.bimestre1 = bimestre1,
        self.bimestre2 = bimestre2,
        self.bimestre3 = bimestre3,
        self.bimestre4 = bimestre4,
        self.id_alumno = id_alumno

    def __str__(self):
        return f"{self.bimestre1} - {self.bimestre2} - {self.bimestre3} - {self.bimestre4}"