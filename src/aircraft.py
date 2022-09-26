class Aircraft:
    def __init__(self, a_name, price, speed, rng, rwy, capacity, a_type, picture, manufacturer, fuel, co2, acheck_price, acheck_time, pilots, crew, engineers, tech, e_name):
        self.a_shortname = a_name
        self.a_name = a_name
        self.a_type = a_type # pax | vip | cargo
        self.price = price
        self.e_name = e_name
        self.fuel = float(fuel)
        self.co2 = float(co2)
        self.speed = int(speed)
        self.rng = int(rng)
        self.rwy = int(rwy)
        self.capacity = int(capacity)
        self.picture = picture
        self.manufacturer = manufacturer
        self.acheck_price, self.acheck_time = int(acheck_price), int(acheck_time)
        self.pilots, self.crew, self.engineers, self.tech = int(pilots), int(crew), int(engineers), int(tech)