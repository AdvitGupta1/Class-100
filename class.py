class Car(object):
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
    self.company = company
    self.color = color
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarting...")
    "Accelaration settings"

  def gear_change(self):
    print("changing gear...")
    "Gear related settings"


audi = Car("A6","red","audi",80)

print(audi.start())
