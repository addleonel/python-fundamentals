
class Calendary:
    def __init__(self, fecha):
        self.fecha = fecha

    def get_date(self):
        return self.fecha

class Hora:
    def __init__(self, hora):
        self.hora = hora

    def get_hour(self):
        return self.hora


class Horariovuelo(Calendary, Hora):
    def __init__(self, fecha, hora, country_from, country_to):
        # multiple inheritance
        Calendary.__init__(self, fecha)
        Hora.__init__(self, hora)
        self.country_from = country_from
        self.country_to = country_to

    def flight_data(self):
        return "your flight data: \ndate: {}\nhour: {} \nFrom: {} \nTo: {}".format(self.fecha,
                                                                                   self.hora,
                                                                                   self.country_from,
                                                                                   self.country_to)


# out

flight1 = Horariovuelo("24/10/2019", "19:00", "Peru", "EE.UU")
print(flight1.flight_data())

date = flight1.get_date()
hour = flight1.get_hour()
print(date, hour)