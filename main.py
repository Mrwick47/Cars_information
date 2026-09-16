from source.car_brand_inventory import Cars

def main():
    try:
        
        result = Cars()
        
        print("** Welcome to the Car's world **")

        print('Your choice')
        while True:
            print('1. Select a brand')
            print("2. Update brand detils")
            print('3. Delete brand details')
            print('4. Add new detail')
            print('5. Entire brands')
            print('6. Exit>>>')
            your_choice = int(input('Enter the number: '))

            if your_choice == 1:
                while True:
                    print('Select Option')
                    print('1. BMW: ')
                    print('2. Ferrari: ')
                    print('3. Ford: ')
                    print('4. Honda: ')
                    print('5. Tata: ')
                    print('6. Toyota: ')
                    print('7. Volkswagen: ')
                    print('8. Exit>>>: ') 
                    select_number = int(input('enter your choice: ')) 

                    if select_number == 1:
                        result.select_car(select_number)           
                    elif select_number == 2:
                        result.select_car(select_number)
                    elif select_number == 3:
                        result.select_car(select_number)
                    elif select_number == 4:
                        result.select_car(select_number)
                    elif select_number == 5:
                        result.select_car(select_number) 
                    elif select_number == 6:
                        result.select_car(select_number)
                    elif select_number == 7:
                        print("Deleted, choose other")
                    elif select_number == 8:
                        print('Exit...')
                        break 
                    else:
                        print('Invalid value')



            elif your_choice == 2:
                while True:
                        print('Select Option')
                        print('1. enter your choice: ')
                        print('2. enter your choice: ')
                        print('3. enter your choice: ')
                        print('4. enter your choice: ')
                        print('5. enter your choice: ')
                        print('6. enter your choice: ')
                        print('7. enter your choice: ')
                        print('8. enter your choice: ') 
                        select_number = int(input('Enter your choice: ')) 
                        if select_number > 6:
                            print('Do not need to update')
                        else:
                            new_model = int(input('Update no of models of the brand: '))
    
                        if select_number == 1:
                            result.update_car_details(select_number, new_model)        
                        elif select_number == 2:
                            result.update_car_details(select_number, new_model)
                        elif select_number == 3:
                            result.update_car_details(select_number, new_model)
                        elif select_number == 4:
                            result.update_car_details(select_number, new_model)
                        elif select_number == 5:
                            result.update_car_details(select_number, new_model)
                        elif select_number == 6:
                            result.update_car_details(select_number, new_model)
                        elif select_number == 7:
                            result.update_car_details(select_number, new_model)
                        elif select_number == 8:
                            print('Exit...')
                            break 
                        else:
                            print('Invalid value')


            elif your_choice == 3:
                while True:
                    print('Select a number')
                    print('1. Enter the number')
                    print('2. Enter the number')
                    print('3. Enter the number')
                    print('4. Enter the number')
                    print('5. Enter the number')
                    print('6. Enter the number')
                    print('7. Enter the number')
                    print('8. Enter the number')
                    select_number = int(input())

                    if select_number == 1:
                        result.delete_brand_details(select_number)
                    elif select_number == 2:
                        result.delete_brand_details(select_number)
                    elif select_number == 3:
                        result.delete_brand_details(select_number)
                    elif select_number == 4:
                        result.delete_brand_details(select_number)
                    elif select_number == 5:
                        result.delete_brand_details(select_number)
                    elif select_number == 6:
                        result.delete_brand_details(select_number)
                    elif select_number == 7:
                        result.delete_brand_details(select_number)
                    elif select_number == 8:
                        print('Exit...')
                        break 
                    else:
                        print('Invalid value')
                        

            elif your_choice == 4:
                
                brand = input("Enter the brand name :")
                website = input("Enter website :")
                year = int(input("Enter year :"))
                ceo = input("Enter name of the CEO :")
                models = int(input("Enter models :"))
                headquarters = input("Enter name of headquarters :")
                country = input("Enter name of the country :")
                result.add_new_brand(brand, website, year, ceo, models, headquarters, country)

            elif your_choice == 5:
                result.entire_inventory()
             

            elif your_choice == 6:
                print('Exit>>>')
                break 
            else:
                print('Invalid input')
            
    except Exception as error:
        print(f"Error of {error}")



if __name__ == "__main__":
    main()
    
    