from abc import ABC, abstractmethod

# Define blueprint of the Builder (Abstract Builder)
class Builder(ABC):
    """Abstract Builder Interface for constructing forms."""
    
    @abstractmethod
    def set_id(self, id):
        pass
    
    @abstractmethod
    def set_name(self, name):
        pass
    
    @abstractmethod
    def set_yoe(self, yoe):
        pass
    
    @abstractmethod
    def set_gradYear(self, gradYear):
        pass
    
    @abstractmethod
    def set_psp(self, psp):
        pass
    
    @abstractmethod
    def set_batchName(self, batchName):
        pass

# Implement the Director
class Student: # Student class
    """Director for constructing complex forms using a specific builder."""

    def __init__(self, builder):
        self.id = builder.id
        self.name = builder.name
        self.yoe = builder.yoe
        self.gradYear = builder.gradYear
        self.psp = builder.psp
        self.batchName = builder.batchName
        
    @staticmethod
    def builder():
        b = Student.StudentBuilder()
        return b
    
    # Implement the Concrete Builder
    class StudentBuilder(Builder): # Builder class
        """Concrete Builder for constructing forms."""

        def __init__(self):
            self.id = None
            self.name = None
            self.yoe = None
            self.gradYear = None
            self.psp = None
            self.batchName = None

        def set_id(self, id):
            """set id"""
            self.id = id
            return self

        def set_name(self, name):
            """set name"""
            self.name = name
            return self

        def set_yoe(self, yoe):
            """set yoe"""
            self.yoe = yoe
            return self

        def set_gradYear(self, gradYear):
            """set gradYear"""
            self.gradYear = gradYear
            return self
        
        def set_psp(self, psp):
            """set id"""
            self.psp = psp
            return self

        def set_batchName(self, batchName):
            """set name"""
            self.batchName = batchName
            return self
        
        def build(self):
            if(self.yoe < 1):
                raise Exception("Invalid Years of experience")
            if(self.gradYear > 2022):
                raise Exception("Invalid Grad year exception")
            if(self.psp < 75):
                raise Exception("Invalid PSP exception")

            s = Student(self)
            return s

# Step 5: Implement the Client
class Client:
    def create_client(self):
        s = Student.builder().set_id(1).set_gradYear(2021).set_yoe(2).set_psp(80).build()
        print(s.id, s.name, s.yoe, s.gradYear, s.psp, s.batchName)

if __name__ == "__main__":
    Client().create_client()
    