
# MULTIPLE INHERITANCES

class Calendar:
    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

class Hour:
    def __init__(self, hour):
        self.hour = hour

    def get_hour(self):
        return self.hour


class FlightTime(Calendar, Hour):
    def __init__(self, date, hour, country_from, country_to):
        # multiple inheritance
        Calendar.__init__(self, date)
        Hour.__init__(self, hour)
        self.country_from = country_from
        self.country_to = country_to

    def flight_data(self):
        return "your flight data: \ndate: {}\nhour: {} \nFrom: {} \nTo: {}".format(self.date,
                                                                                   self.hour,
                                                                                   self.country_from,
                                                                                   self.country_to)


# out

flight1 = FlightTime("24/10/2019", "19:00", "Peru", "EE.UU")
print(flight1.flight_data())

date = flight1.get_date()
hour = flight1.get_hour()
print(date, hour)