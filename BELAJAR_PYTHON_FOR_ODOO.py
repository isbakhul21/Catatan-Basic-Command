import os
import math

sistem_operasi = os.name
match sistem_operasi:
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")


class Onepiece():
        __jumlah_bajak_laut = 0
        
        def __init__(self, name, hakki):
                self.__name = name
                self.__hakki = hakki
                Onepiece.__jumlah_bajak_laut += 1
        #method ini untuk objek
        def getjumlah_bajak_laut(self):
                return Onepiece.__jumlah_bajak_laut
        #method ini untuk class
        def getjumlah_bajak_laut_satu():
                return Onepiece.__jumlah_bajak_laut
        # =method ini untuk class dan objek
        @staticmethod
        def getjumlah_bajak_laut_dua():
                return Onepiece.__jumlah_bajak_laut
        #
        @classmethod
        def getjumlah_bajak_laut_tiga(apapun):
                return apapun.__jumlah_bajak_laut

luffy = Onepiece("luffy", 100)
zorro = Onepiece("Zoro", 50)

print(luffy.getjumlah_bajak_laut())
print(Onepiece.getjumlah_bajak_laut_satu())
print(luffy.getjumlah_bajak_laut_dua())
print(Onepiece.getjumlah_bajak_laut_dua())
print(luffy.getjumlah_bajak_laut_tiga())



########################################################## Belajar Enkapsulasi ##############################

import os
import math

sistem_operasi = os.name
match sistem_operasi:
	case "posix" : os.system("clear")
	case "nt" : os.system("cls")
     
class Hero():

    __jumlah = 0
    def __init__(self, name, health, attpower, armor ):
                    self.__name = name
                    self.__healthstandard = health
                    self.__attpowerstandard = attpower
                    self.__armorstandard = armor
                    self.__level = 1
                    self.__exp = 0

                    self.__healthmax = self.__healthstandard * self.__level
                    self.__attpower = self.__attpowerstandard * self.__level
                    self.__armor = self.__armorstandard * self.__level

                    self.__health = self.__healthmax

                    Hero.__jumlah += 1
    @property                
    def info(self):
            return "{} : \n\t level {} \n\t health = {}/{} \n\t attack {} \n\t armor {}".format(self.__name, self.__level, self.__health, self.__healthmax, self.__attpower, self.__armor)
    
    @property
    def gainexp(self):
             pass
    
    @gainexp.setter
    def gainexp(self, addexp):
        self.__exp =+ addexp
        if (self.__exp >=  100):
                print(self.__name , 'level up')
                self.__level += 1
                self.__exp -= 100

                self.__healthmax = self.__healthstandard * self.__level
                self.__attpower = self.__attpowerstandard * self.__level
                self.__armor = self.__armorstandard * self.__level


    def attack(self, musuh):
            self.gainexp = 100


luffy = Hero("luffy", 100, 5, 10)
zoro = Hero("zoro", 90, 10, 20)

print(luffy.info)
luffy.attack(zoro)
luffy.attack(zoro)
luffy.attack(zoro)
luffy.attack(zoro)
print(luffy.info)


######################################################################################### end enkapsulasi #########################
##################################INHERTANCE PYTHON ###########################################
import os
import math

sistem_operasi = os.name
match sistem_operasi:
	case "posix" : os.system("clear")
	case "nt" : os.system("cls")
     
class Anime:
	
        def __init__(self, name, health):
                self.name = name
                self.health = health
        
        def showinfo(self):
                print(" {} dengan health {}".format(self.name, self.health))


class Onepiece(Anime):
        def __init__(self, name):
                #Anime.__init__(self,name, 100)
                super().__init__(name, 100)
                super().showinfo()

class Avatar(Anime):
        def __init__(self, name):
                super().__init__(name, 200)
                super().showinfo()


luffy = Onepiece("luffy")
katara = Avatar("katara")


######################################################### END OF INHERITANCE ##########################################




















