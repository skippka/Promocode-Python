class Promocode:
    codes = [
        {
            "Код": "ADMIN",
            "Монеты": 100000000,
            "Скидка": 100,
        },
        {
            "Код": "BETA",
            "Монеты": 500,
            "Скидка": 5,
        },
        {
            "Код": "TEST",
            "Монеты": 2000,
            "Скидка": 20,
              
        }
    ]
    
    
    
  
def main():
    while True:
        print("Привет! Это программа для ввода промокода")

        user_input = input(" ||| Введите промокод: ")

        found = next((code for code in Promocode.codes if code["Код"] == user_input), None)

        if found:
            print(f"Промокод успешно активирован!\n📌 Монеты: {found['Монеты']}, Скидка: {found['Скидка']}%")
            main()
            
        else:
            print("Ошибка: промокод недействителен")
        
        
if __name__ == "__main__":
    main()        
