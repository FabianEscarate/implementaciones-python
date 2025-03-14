from Classes.some_services import SomeServices

class Main:
  def __init__(self):
    self.service = SomeServices()

  def run(self):
    result = self.service.perform_action()
    print(f"Result: {result}")


async def service_add():
  main = Main()
  result = await main.service.async_add(1, 2)
  print(f"Result: {result}")
  return result

async def service_get_data():
  main = Main()
  result = await main.service.async_get_data()
  print(f"Result: {result}")
  return result

if __name__ == "__main__":
  main = Main()
  main.run()