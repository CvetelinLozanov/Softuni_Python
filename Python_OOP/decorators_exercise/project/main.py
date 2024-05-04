from project.computer_store_app import ComputerStoreApp

computer_store = ComputerStoreApp()
print(computer_store.build_computer("Desktop Computer", "Dell", "Kosh", "AMD AARyzen 7 5700G", 128))
print(computer_store.sell_computer(1200, "AMD Ryzen 7 5700G", 32))
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple AAAM1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
print(computer_store.profits)