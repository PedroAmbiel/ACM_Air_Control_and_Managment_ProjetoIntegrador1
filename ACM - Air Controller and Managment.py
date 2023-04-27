import os
from time import sleep

print("ACM - Air Controller and Managment")

msgValor_Inv = "Favor entre com números positivos"


while True:# Laço do programa, irá repetir o programa todo
    while True:
        try:#Verifica se há alguma letra sendo inserida 
            #if's usados para verificar se o número inserido para cada variável é positivo    
            mp10 = float(input("Entre com o valor de MP10: "))
            if mp10 < 0: print (msgValor_Inv); break
            mp25 = float(input("Entre com o valor de MP2,5: "))
            if mp25 < 0: print (msgValor_Inv); break
            o3 = float(input("Entre com o valor de O3: "))
            if o3 < 0: print (msgValor_Inv); break
            co = float(input("Entre com o valor de CO: "))
            if co < 0: print (msgValor_Inv); break
            no2 = float(input("Entre com o valor de NO2: "))
            if no2 < 0: print (msgValor_Inv); break
            so2 = float(input("Entre com o valor de SO2: ")) 
            if so2 < 0: print (msgValor_Inv); break
         
        except ValueError:
            #os.system('cls')
            print("Favor, entre somente com números") 
            break
        else: # Indice inicial + ((indicefinal-indiceinicial)/(concentracaofinal - concentracaoinicial))*(concentracaomedida-concentracaoinicial)

            ###### Cálculo dos parâmetros médidos ######
            if mp10 != 0:
                if mp10 <= 50:
                  mp10_calc =  0 + ((40-0)/(50-0))*(mp10-0)
                elif mp10 <= 100:
                    mp10_calc =  41 + ((80-41)/(100-50))*(mp10-50)
                elif mp10 <= 150:
                    mp10_calc =  81 + ((120-81)/(150-100))*(mp10-100)
                elif mp10 <= 250:
                    mp10_calc =  121 + ((200-121)/(250-150))*(mp10-150)
                else:
                    mp10_calc =  200 + ((300)/(200))*(mp10-250)

                print(mp10_calc)
            else:
                mp10_calc = 0

            if mp25 != 0:
                if mp25 <= 25:
                  mp25_calc =  0 + ((40-0)/(25-0))*(mp25-0)
                elif mp25 <= 50:
                    mp25_calc =  41 + ((80-41)/(50-25))*(mp25-25)
                elif mp25 <= 75:
                    mp25_calc =  81 + ((120-81)/(75-50))*(mp25-50)
                elif mp25 <= 125:
                    mp25_calc =  121 + ((200-121)/(125-75))*(mp25-75)
                else:
                    mp25_calc =  200 + ((225)/(125))*(mp25-125)

                print(mp25_calc)            
            else:
                mp25_calc = 0

            if o3 != 0:
                if o3 <= 100:
                  o3_calc =  0 + ((40-0)/(100-0))*(o3-0)
                elif o3 <= 130:
                    o3_calc =  41 + ((80-41)/(130-100))*(o3-100)
                elif o3 <= 160:
                    o3_calc =  81 + ((120-81)/(160-130))*(o3-130)
                elif o3 <= 200:
                    o3_calc =  121 + ((200-121)/(200-160))*(o3-160)
                else:
                    o3_calc =  200 + ((300)/(200))*(o3-200)

                print(o3_calc)
            else:
                o3_calc = 0

            if co != 0:
                if co <= 9:
                  co_calc =  0 + ((40-0)/(9-0))*(co-0)
                elif co <= 11:
                    co_calc =  41 + ((80-41)/(11-9))*(co-9)
                elif co <= 13:
                    co_calc =  81 + ((120-81)/(13-11))*(co-11)
                elif co <= 15:
                    co_calc =  121 + ((200-121)/(15-13))*(co-13)
                else:
                    co_calc =  200 + ((25)/(15))*(co-15)

                print(co_calc)
            else:
                co_calc = 0

            if no2 != 0:
                if no2 <= 200:
                  no2_calc =  0 + ((40-0)/(200-0))*(no2-0)
                elif no2 <= 240:
                    no2_calc =  41 + ((80-41)/(240-200))*(no2-200)
                elif no2 <= 320:
                    no2_calc =  81 + ((120-81)/(320-240))*(no2-240)
                elif no2 <= 1130:
                    no2_calc =  121 + ((200-121)/(1130-320))*(no2-320)
                else:
                    no2_calc =  200 + ((1230)/(1130))*(no2-1130)

                print(no2_calc)
            else:
                no2_calc = 0

            if so2 != 0:
                if so2 <= 20:
                  so2_calc =  0 + ((40-0)/(20-0))*(so2-0)
                elif so2 <= 40:
                    so2_calc =  41 + ((80-41)/(40-20))*(so2-20)
                elif so2 <= 365:
                    so2_calc =  81 + ((120-81)/(365-40))*(so2-40)
                elif so2 <= 800:
                    so2_calc =  121 + ((200-121)/(800-365))*(so2-365)
                else:
                    so2_calc =  200 + ((900)/(800))*(so2-800)

                print(so2_calc)
            else:
                so2_calc = 0
            

            ###### Indicação do Índice #####
            if mp10_calc <= 40 and mp25_calc <= 40 and o3_calc <= 40 and co_calc <= 40 and no2_calc <= 40 and so2_calc <= 40:
                print(f"{'Qualidade': <25}" + '|' + f"{'Indice' : >10}")
                print(f"{'N1 - Qualidade Boa' : <25}"  + '|' + f"{'0 -- 40' : >9}")
                            
            elif  mp10_calc <= 80 and  mp25_calc <= 80 and  o3_calc <= 80 and co_calc <= 80 and  no2_calc <= 80 and so2_calc <= 80:
                print(f"{'Qualidade': <25}" + '|' + f"{'Indice' : >10}")
                print(f"{'N2 - Qualidade Moderada' : <25}"  + '|' + f"{'41 -- 80' : >9}")        
                print("\nSignificado:" + "\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
                    
                    
            elif  mp10_calc <= 120 and  mp25_calc <= 120  and o3_calc <= 120  and co_calc <= 120 and no2_calc <= 120 and so2_calc <= 120:
                print(f"{'Qualidade': <25}" + '|' + f"{'Indice' : >10}")
                print(f"{'N3 - Qualidade Ruim' : <25}"  + '|' + f"{'81 -- 120' : >9}")
                print("\nSignificado:" + "\nToda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
        
                    
            elif  mp10_calc <= 200 and mp25_calc <= 200  and o3_calc <= 200  and co_calc <= 200 and no2_calc <= 200 and so2_calc <= 200:
                print(f"{'Qualidade': <25}" + '|' + f"{'Indice' : >10}")
                print(f"{'N4 - Qualidade Muito Ruim' : <25}"  + '|' + f"{'121 -- 200' : >9}")
                print("\nSignificado:" + "\nToda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
                    
                    
            elif mp10_calc > 200 or mp25_calc > 200 or o3_calc > 200 or co_calc > 200 or no2_calc > 200 or so2_calc > 200:
                print(f"{'Qualidade': <25}" + '|' + f"{'Indice' : >10}")
                print(f"{'N5 - Qualidade Muito Ruim' : <25}"  + '|' + f"{'>200' : >9}")
                print("\nSignificado:" + "\nToda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")    
                    
  
            
    
                        
                    
        while True:
            reinicio_aux = input("Gostaria de realizar um novo teste? (S/N)\n").lower()
                                
            if reinicio_aux in ['s','n']:
                break
            else:
                print("Favor, entre somente com os caractéres S / N ")
                                
                            
        if reinicio_aux == 'n':
            print('Obrigado por utilizar nosso sistema!')
            sleep(3)
            break
    
    
    
    


