import os
import master_gdd_zonales
import credenciales
import master_stock
import master_promocion
import master_matriz_gdd
import master_general

def esc(code):
    return f'\033[{code}m'

def menu():
    os.system('clear')
    print(esc('41'), 'Selecciona una Opcion', esc('0'),'\n')
    print(esc('44'),"=========GDD=========", esc('0'),'\n')
    print("\t",esc('46'),"====3AM====",esc('0'))
    print("\t1 - Cenacop;\t2 - Dapromach;\t3 - Disproalza;\t4 - Madeli")
    print("\t5 - Paul_Fl;\t6 - Prooriente;\t7 - Disprovalles;\t8 - Posso_Cueva")
    print("")
    print("\t",esc('46'),"====4AM_t1====",esc('0'))
    print("\t9 - GarvelProd;\t10 - Almabi;\t11 - Dismag;\t12 - Grampir")
    print("\t13 - Alsodi;\t14 - Disanahisa;\t15 - Judispro;")
    print("")
    print("\t",esc('46'),"====4AM_t2====",esc('0'))
    print("\t16 - Dimmia;\t17 - PatricioC;\t18 - Skandinar;\t19 - Pronacnor")
    print("\t20 - H_M;\t21 - Apronam;\t22 - Discarnicos;\t23 - Ecoal")
    print("")
    print("\t24 - Pronaca")
    print("")
    print("\t",esc('46'),"====STOCK====",esc('0'))
    print("\t100 - Stock 3AM;\t101 - Stock 4AM_1t;\t102 - Stock 4AM_2t;\t103 - Stock Almacenes")
    print("")
    print("\t",esc('46'),"====PROMOCIONES GENERICOS====",esc('0'))
    print("\t104 - PG 3AM; \t105 - PG 4AM_1t;\t106 - PG 4AM_2t")
    print("")
    print("\t",esc('46'),"====MATRIZ GDD====",esc('0'))
    print("\t120- GDD 3AM; \t121 - GDD 4AM_1t;\t122 - GDD 4AM_2t")
    print("")
    print("\t",esc('46'),"====GENERAL====",esc('0'))
    print("\t123- G 3AM; \t124 - G 4AM_1t;\t125 - G 4AM_2t")
    print("")
    print("\t9 - salir")


while True:

    menu()

    # solicituamos una opcion al usuario

    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
        master_gdd_zonales.Complex("CENACOP","C3N@COP@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "2":
        master_gdd_zonales.Complex("DAPROMACH","D@PROM@CH#SUPPORT@2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "3":
        master_gdd_zonales.Complex("DISPROALZA","DISPRO@LZ@@supp0rt#2018")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "4":
        master_gdd_zonales.Complex("MADELI","M@DELI@supp0rt#2018")
        input("pulsa una tecla para continuar")
  
    elif opcionMenu == "5":
        master_gdd_zonales.Complex("PAUL_FLORENCIA","P@UL_FLORENCI@@supp0rt#2018")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "6":
        os.system('python master_gdd_prooriente.py -u PROORIENTE -c PR00RIENTE@supp0rt#2020')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "7":
        master_gdd_zonales.Complex("DISPROVALLES","DI$PR0V@LL3$@supp0rt#2018")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "8":
        master_gdd_zonales.Complex("POSSO_CUEVA","POSSO_CU3V@@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "9":
        master_gdd_zonales.Complex("GARVELPRODUCT","G@RVELPRODUCT@supp0rt#2018")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "10":
        master_gdd_zonales.Complex("ALMABI","@LMABI@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "11":
        master_gdd_zonales.Complex("DISMAG","DISMAG@supp0rt#2021")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "12":
        master_gdd_zonales.Complex("GRAMPIR","GR@MPIR@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "13":
        master_gdd_zonales.Complex("ALSODI","@LS0DI@supp0rt#2018")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "14":
        master_gdd_zonales.Complex("DISANAHISA","DIS@N@HIS@@supp0rt#2018")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "15":
        master_gdd_zonales.Complex("JUDISPRO","JUDISPRO@supp0rt#2018")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "16":
        master_gdd_zonales.Complex("DIMMIA","DIMMI@@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "17":
        master_gdd_zonales.Complex("PATRICIO_CEVALLOS","P@TRICIO_C3V@LLOS@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "18":
        master_gdd_zonales.Complex("SKANDINAR","SK@NDIN@R@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "19":
        master_gdd_zonales.Complex("PRONACNOR","PRON@CNOR@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "20":
        master_gdd_zonales.Complex("H_M","H_M@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "21":
        master_gdd_zonales.Complex("APRONAM","@PRONAM@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "22":
        master_gdd_zonales.Complex("DISCARNICOS","DISCARNICOS@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "23":
        master_gdd_zonales.Complex("ECOAL","ECOAL@supp0rt#2019")
        input("pulsa una tecla para continuar")

    elif opcionMenu == "24":
        os.system('python master_gdd_pronaca.py -u PRONACA -c PR0N@C@supp0rt#2018')
        input("pulsa una tecla para continuar") 

    elif opcionMenu == "100":
        master_stock.Complex(credenciales.Credenciales.am3())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "101":
        master_stock.Complex(credenciales.Credenciales.am4_1())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "102":
        master_stock.Complex(credenciales.Credenciales.am4_2())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "103":
        os.system('python stck.py')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "104":
        master_promocion.Complex(credenciales.Credenciales.am3())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "105":
        master_promocion.Complex(credenciales.Credenciales.am4_1())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "106":
        master_promocion.Complex(credenciales.Credenciales.am4_2())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "120":
        master_matriz_gdd.Complex(credenciales.Credenciales.am3())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "121":
        master_matriz_gdd.Complex(credenciales.Credenciales.am4_1())
        input("pulsa una tecla para continuar")
    
    elif opcionMenu == "122":
        master_matriz_gdd.Complex(credenciales.Credenciales.am4_2())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "123":
        master_general.Complex(credenciales.Credenciales.am3())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "124":
        master_general.Complex(credenciales.Credenciales.am4_1())
        input("pulsa una tecla para continuar")

    elif opcionMenu == "125":
        master_general.Complex(credenciales.Credenciales.am4_2())
        input("pulsa una tecla para continuar")


    elif opcionMenu == "300":
        os.system('clear')

    elif opcionMenu == "9":

        break

    else:

        print("")

        input(
            "No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar"
        )
