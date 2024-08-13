#Import biblioteki Faker, by móc generować losowe dane
from faker import Faker
fake = Faker()

#Definiujemy klase na podstawie której bedą tworzone instancje dla kontaktów podstawowych
class BaseContact:
   def __init__(self, name, surname, private_phone, e_mail):
       self.name = name
       self.surname = surname
       self.private_phone = private_phone
       self.e_mail = e_mail

   def __str__(self):
        return f'{self.name} {self.surname}'
   
#Definiujemy funkcję w klasie która bedzie która w konsoli bedzie wyświetlała napis wymagany dla wizytówki prywatnej
   def contact(self):
       print("Wybieram numer ", self.private_phone, " i dzwonię do ", self.name, self.surname)

#definiujemy dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby dla wizytówek prywatnych
   @property
   def label_length(self):
       return len(self.name) + len(self.surname)

#Definiujemy klase na podstawie której bedą tworzone instancje dla kontaktów biznesowych 
class BusinessContact(BaseContact):
    def __init__(self, position, company, company_phone, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.company_phone = company_phone
    
    def contact(self):
       print("Wybieram numer ", self.company_phone, " i dzwonię do ", self.name, self.surname)

#definicja funkcji która pobiera 2 zmienne wprowadzone przez użytkownika i na tej podstawie tworzy listę biznesową lub prywatną wypełnioną ilością wizytówek zadeklarowaną
#przez użytkownika. Zwraca listę wizytówek.
def create_contacts(number_of_gen_cards,priv_or_busin):
        temp_cards_list = []
        for i in range(number_of_gen_cards):
            if priv_or_busin == "P":
                temp_cards_list.append(BaseContact(name=fake.first_name(), surname=fake.last_name(), private_phone=fake.phone_number(), e_mail=fake.email()))
            else:
                temp_cards_list.append(BusinessContact(name=fake.first_name(), surname=fake.last_name(), private_phone=fake.phone_number(), e_mail=fake.email() ,position=fake.job(), company=fake.company(), company_phone = fake.phone_number()))
        return temp_cards_list      

#Funkcja wyświetlająca informację o wprowadzeniu niepoprawnych danych przez użytkownika, gdy program np oczekuje "P" lub "B" a użytkownik wpisuje inne dane   
def wrong_number():
    print("Nie wprowadzono poprawnie danych, spróbuj jeszcze raz. ")

# funkcja odpowiedzialna za sprawdzenie czy podany nr osoby znajduje się w liście
def person_number():
    while True:
        contact_number = input("Podaj nr osoby na liście wizytówek: ")
        try:
            contact_number = int(contact_number)
            if contact_number in range(1,numb_of_cards+1):
                return contact_number
            else:
                wrong_number()
        except: 
            wrong_number()

#______________Początek głównego programu___________________
#użytkownik definiuje czy chce stworzyć wizytówki biznesowe czy prywatne
if __name__ == "__main__":

    while True:
        priv_or_busin = input("Podaj rodzaj wizytówek do wygenerowania (B-Biznesowa, P-Prywatna): ")
        if priv_or_busin in {"B","P"}:
            break
        else:
            wrong_number()

    #użytkownik definiuje ile wizytówek ma zostać wygenerowanych
    while True:
        numb_of_cards = input("Podaj ile wizytówek chesz wygenerować (licz. całkowita, > 0): ")
        try:
            numb_of_cards = int(numb_of_cards)
            if numb_of_cards < 1:
                wrong_number()
            else:    
                break
        except:
            wrong_number()

    #W zależności od wyborów użytkownika generowane są wizytówki biznesowe lub prywatne w okreslonej ilości i zapisywane w listach
    card_list = create_contacts(numb_of_cards, priv_or_busin)
    print("Stworzono listę zawierającą wizytówki w liczbie: %d" % numb_of_cards)

    #program którego zadaniem jets wizualizacja operacji wymaganych w zadaniu. Program daje 4 możliwości do wyboru i można je powtarzać w dowolnej kolejnosci aż zostanie wpisana
    #cyfra 4 która zakończy dziłanie programu. Przy wyborze 1 zostaną ponumerowane i wyswietlone wszystkie kontakty z danej listy. Na podstawie nadanych numerów poszczególnym kontaktom
    # można wybrać osobę do której zadzwonimy lub osobę dla której wyświtetlimy ilość znaków w imieniu i nazwisku. 
    while True:
        while True:
    #Uzytkownik definiuje jaką czynność program ma wykonać
            print("Podaj cyfrę odpowiadającą czynności ktorą chcesz wykonać: \n 1 - Ponumeruj i wyświetl dane wszystkich wizytówek w osobnych liniach \n 2 - Zadzwoń do konkretnej osoby z jednej z wizytówek \n 3 - Zwróć długość imienia i nazwiska osoby z jednej wizytówki \n 4 - Wyjście z programu.")
            activity = input("Wybrana opcja to: ")
            try:
                activity = int(activity)
                if activity in {1,2,3,4}:
                    break
                else:    
                    wrong_number()
            except:
                wrong_number()

    #W przypadku wybrania 1 program Ponumeruje i wyświetli dane wszystkich wizytówek w osobnych liniach 
        if activity == 1:
            for i in range(len(card_list)):   
                    print("%d. " %(i+1), card_list[i])

    #W przypadku wybrania 2 program "zadzwoni" do jednej osoby której numer podano w poprzedniej opcji, tj 1,2,3,4,5 itd
        elif activity == 2:
            contact_number = person_number()
            card_list[contact_number-1].contact()

    #w przypadku wybrania 3 program Zwróci długość imienia i nazwiska osoby z jednej wizytówki, Osobę dla której wykonamy tą operację wybieramy na podstawie informacji wygenerowanej
    #podczas opcji "1". Numer osoby to 1,2,3,4,5 itd 
        elif activity == 3:
            contact_number = person_number()
            print("Łączna długość imienia i nazwiska dla ", card_list[contact_number-1],"to: ",card_list[contact_number-1].label_length)
  
    #Program się kończy gdy zostanie wybrana cyfra 4
        else:
            print("Kończymy na dzisiaj.")
            exit(0)
