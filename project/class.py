class student:
    def __init__(self, id, name, major):
        self.id=id
        self.name = name
        self.major = major

    def __str__(self):
        return f"Nombre: {self.name}\n 
        carrera: {self.major}

luis = student(1, "Luis Maltez", "ISI")
print(Luis)
print(Luis.__str__())