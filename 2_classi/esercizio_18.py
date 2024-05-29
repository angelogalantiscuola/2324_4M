from datetime import datetime

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.make} {self.model} ({self.year})"
    def __str__(self):
        return self.display_info()

class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
    def __str__(self):
        return f"Customer: {self.name}, Address: {self.address}, Phone: {self.phone_number}"

class Salesperson:
    def __init__(self, name, employee_id, territory):
        self.name = name
        self.employee_id = employee_id
        self.territory = territory
    def __str__(self):
        return f"Salesperson: {self.name}, ID: {self.employee_id}, Territory: {self.territory}"


class Showroom:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def __str__(self):
        return f"Showroom at {self.location} with {len(self.vehicles)} vehicles"

class Sale:
    def __init__(self, vehicle, customer, salesperson, price):
        self.vehicle = vehicle
        self.customer = customer
        self.salesperson = salesperson
        self.price = price
        self.date = datetime.now()

    def display_info(self):
        return f"Vendita: {self.vehicle.display_info()} a {self.customer.name} da {self.salesperson.name} per {self.price} euro il {self.date.strftime('%d/%m/%Y')}"
    def __str__(self):
        return f"Showroom at {self.location} with {len(self.vehicles)} vehicles"

def main_menu():
    showroom = []  # Crea un nuovo showroom
    salespeople = []  # Lista dei venditori
    customers = []  # Lista dei clienti
    vehicle=[ ]
    sales=[ ]
    
    

    while True:
        print("\n1) Aggiungi showroom")
        print("2) Aggiungi venditore")
        print("3) Aggiungi cliente")
        print("4) Aggiungi veicolo")
        print("5) Effettua vendita")
        print("6) Mostra veicoli in vendita")
        print("7) Mostra vendite effettuate")
        print("8) Esci")

        choice = input("\nSeleziona un'opzione: ")

        if choice == '1':
            # Aggiungi showroom
            showroom_name = input("Inserisci il nome del showroom: ")
            showroom = Showroom(showroom_name)
        elif choice == '2':
            # Aggiungi venditore
            salesperson_name = input("Inserisci il nome del venditore: ")
            salesperson_employee_id = input("Inserisci l'ID del venditore:")
            salesperson_territory = input("Inserisci il territorio del venditore: ")
            salespeople.append(Salesperson(salesperson_name))
            salespeople.append(Salesperson(salesperson_employee_id))
            salespeople.append(Salesperson(salesperson_territory))

        elif choice == '3':
            # Aggiungi cliente
            customer_name = input("Inserisci il nome del cliente: ")
            customer_address = input("Inserisci l'indirizzo del cliente: ")
            customer_phone_number = input("Inserisci il numero di telefono del cliente: ")
            customers.append(Customer(customer_name))
            customers.append(Customer(customer_address))
            customers.append(Customer(customer_phone_number))
        elif choice == '4':
            # Aggiungi veicolo
            vehicle_name = input("Inserisci il nome del veicolo: ")
            vehicle_model = input("Inserisci il modello del veicolo: ")
            vehicle_year = input("Inserisci l'anno del veicolo: ")
            vehicle = Vehicle(vehicle_name, vehicle_model, vehicle_year)
            nome_showroom = input("Inserisci il nome del showroom: ")
            for s in showroom:
                if s.name == nome_showroom:
                    s.add_vehicle(vehicle)
                    break
            showroom.append(vehicle)
        elif choice == '5':
            # Effettua vendita
            vehicle_name = input("Inserisci il nome del veicolo venduto: ")
            customer_name = input("Inserisci il nome del cliente: ")
            salesperson_name = input("Inserisci il nome del venditore: ")
            price = input("Inserisci il prezzo di vendita: ")

            vehicle = None
            for v in showroom.vehicles:
                if v.name == vehicle_name:
                    vehicle = v
                    break

            customer = None
            for c in customers:
                if c.name == customer_name:
                    customer = c
                    break

            salesperson = None
            for s in salespeople:
                if s.name == salesperson_name:
                    salesperson = s
                    break

            if vehicle and customer and salesperson:
                sale = Sale(vehicle, customer, salesperson, price)
                sales.append(sale)
                showroom.remove_vehicle(vehicle)
                print("Vendita effettuata.")
        elif choice == '6':
            # Mostra veicoli in vendita
            for vehicle in showroom.display_inventory():
                print(vehicle)
        elif choice == '7':
            # Mostra vendite effettuate
            for sale in sales:
                print(sale)
        elif choice == '8':
            print("Esci dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

main_menu()