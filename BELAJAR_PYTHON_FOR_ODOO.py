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

