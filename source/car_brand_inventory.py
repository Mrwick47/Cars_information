import os
import oracledb
from dotenv import load_dotenv 

load_dotenv() 

class Cars:    
    def __init__(self):
        try:    
            user = os.getenv("ORACLE_USER")
            password = os.getenv("ORACLE_PASSWORD")
            dsn = os.getenv("ORACLE_DSN")

            self.connection = oracledb.connect(
                user=user,
                password=password,
                dsn=dsn)
            self.cursor = self.connection.cursor()

        except oracledb.Error as error:
            print(f"Connection failed: {error}")
                
                
        
    def car_inventory(self):
        try:                
            insert_datas = """INSERT INTO Car_Inventory (Brand,
            Company_Website, 
            Established_Year, 
            CEO,
            Total_Models, 
            Headquarters, 
            Country)
            VALUES(:1, :2, :3, :4, :5, :6, :7) """ 

            data = [
                ('BMW',
                'https://www.bmwgroup.com/en/company.html',
                    1916,
                'Milan Nedeljković',
                    23,
                'Munich',
                'Germany'
                ),
                ('Ferrari',
                'https://www.ferrari.com/en-IN',
                    1939,
                'Benedetto Vigna',
                    20,
                'Maranello',
                'Italy'
                ),
                ('Ford',
                'https://corporate.ford.com/operations/locations/global-plants/',
                    1903,
                'Jim Farley',
                    30,
                'Dearborn',
                'United States'
                ),
                ('Honda',
                'https://global.honda/en/about/history-digest/',
                1946,
                'Toshihiro Mibe',
                    0,
                'Minato-ku',
                'Japan'
                ),
                ('Tata',
                'https://www.tatamotors.com/',
                1945,
                'Shailesh Chandra',
                16,
                'Mumbai',
                'India'
                ),
                ('Toyota',
                'https://global.toyota/en/',
                1937,
                'Kenta Kon',
                50,
                'Aichi Prefecture',
                'Japan'
                ),  
                ('Volkswagen',
                'https://www.vw.com/en.html',
                    1937,
                'Oliver Blume',
                30,
                'Wolfsburg',
                'Germany'
                )                      
                ] 

            self.cursor.executemany(insert_datas, data) 
            view_cars = 'SELECT * FROM Car_Inventory'
            views = self.cursor.execute(view_cars) 
            self.connection.commit()
            for i in views:
                    print(i)                                        
        except Exception as e:
            print(f'Facing the error of {e}')                    

    def select_car(self, select_number):                
        try:            
            query = 'SELECT * FROM Car_Inventory WHERE Car_id = :1' 
            data = [select_number]
            self.cursor.execute(query, data) 
            fetch_car = self.cursor.fetchone()
            print(f"ID: {fetch_car[0]}") 
            print(f"Brand: {fetch_car[1]}") 
            print(f"Company_Website: {fetch_car[2]}")
            print(f"Established_Year: {fetch_car[3]} ")
            print(f"CEO: {fetch_car[4]}")
            print(f"Total_Models: {fetch_car[5]}")
            print(f"Headquarters: {fetch_car[6]}")
            print(f"Country: {fetch_car[7]}")               
        except Exception as err:
            print(f'Error of {err}')                                            
            
    def update_car_details(self,select_number, new_model):
        try:                        
            query = 'UPDATE Car_Inventory SET Total_Models = :1 WHERE Car_id = :2'
            data = [new_model, select_number]            
            self.cursor.execute(query, data) 
            self.connection.commit()
            update_model = 'SELECT * FROM Car_Inventory WHERE Car_id = :1'  
            data_1 = [select_number]      
            print(f"** Updated successfully **")
            self.cursor.execute(update_model, data_1)
            fetch_car = self.cursor.fetchone()
            print(f"ID: {fetch_car[0]} / Brand: {fetch_car[1]} / Company_Website: {fetch_car[2]} / Established_Year: {fetch_car[3]} / CEO: {fetch_car[4]} / Total_Models: {fetch_car[5]} / Headquarters: {fetch_car[6]} / Country: {fetch_car[7]}")   
        except Exception as err:
                    print(f'Error of {err}')                                                                                                                                                                          

    def delete_brand_details(self, select_number):

        try:
            query = 'DELETE FROM Car_Inventory WHERE Car_id = :1' 
            data = [select_number] 
            self.cursor.execute(query, data)
            self.connection.commit()
            print('Deleted Successfully') 
        except Exception as error:
            print(f'Error of {error}')         
        
    def add_new_brand(self,brand, website, year, ceo, models, headquarters, country):
        try:
            insert_datas = """INSERT INTO Car_Inventory (Brand,
                        Company_Website, 
                        Established_Year, 
                        CEO,
                        Total_Models, 
                        Headquarters, 
                        Country)
                        VALUES(:1, :2, :3, :4, :5, :6, :7) """ 
            data = [
                                (brand,
                                website,
                                year,
                                ceo,
                                models,
                                headquarters,
                                country)]
            self.cursor.executemany(insert_datas,data)
            self.connection.commit()
            print('Added successfully')
        except Exception as error:
            print(f'Error of {error}')
    
    def entire_inventory(self):
        try:
            query = 'SELECT * FROM Car_Inventory order by Car_id'
            self.cursor.execute(query)
            fetch_car = self.cursor.fetchall()
            for i in fetch_car:
                print(f"ID: {i[0]} / Brand: {i[1]} / Company_Website: {i[2]} / Established_Year: {i[3]} / CEO: {i[4]} / Total_Models: {i[5]} / Headquarters: {i[6]} / Country: {i[7]}")
            
        except Exception as error:
            print(f'Error of {error}')          
            
    


if __name__ == "__main__":
    pass


    



