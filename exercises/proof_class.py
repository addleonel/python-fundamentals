# I'm going to use a class and its components
# component : properties and behavior

class Computer:

    # initial status from the properties(this is 'constructor' method)
    def __init__(self):
        # create its properties
        self.status = False
        self.processor = "intel core i3"
        self.name_device = "LAPTOP-QJ1KIUUR"
        self.RAM = 4
        self.identify_device = "5201B0D5-6952-4113-AE3F-0E8D58DB7960"
        # I need to use the concept about encapsulation. For this just add '__' before of the properties or function
        self.__type_system = "operative system 64 bits"  # this is encapsulated. With this we can't change outside its
        # initial argument
        # windows properties
        self.__edition = "windows 10 Home Single Language"  # it is encapsulated
        self.version = "1903"
        self.date_installation = "9/10/2019"
        self.__so_version = "18362.418"  # it is encapsulated
        # support
        self.__fabricante = "Acer"  # it is encapsulated

    # Behavior
    # this is the correct type a function 'on_off()' in this case
    def on_off(self):
        self.status = True

    def run_program(self, inputRAM):
        if self.RAM < inputRAM:
            return "your system can't support this program"
        else:
            return "this program is perfect to your system"

    def view_properties(self):
        print(
            "This is all properties:\n"
            "processor: {}\n".format(self.processor),
            "Device's name: {}\n".format(self.name_device),
            "RAM: {} GB\n".format(self.RAM),
            "Identification: {}\n".format(self.identify_device),
            "Type of system: {}\n".format(self.__type_system),
            "Edition windows: {}\n".format(self.__edition),
            "version windows: {}\n".format(self.version),
            "date of installation: {}\n".format(self.date_installation),
            "system operative's version: {}\n".format(self.__so_version),
            "device's factory: {}\n".format(self.__fabricante)
        )

    # Create a method encapsulate
    def __method(self):
        print("this method is encapsulated")


if __name__ == '__main__':
    # outside of class called 'Computer'
    my_compu = Computer()
    my_compu.view_properties()
    yoursystem = int(input("type your RAM: "))
    print(my_compu.run_program(yoursystem))
