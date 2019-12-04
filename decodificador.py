#Primeira parte é fazer a leitura do arquivo de cada instrução, ou seja, linha à linha

arquivo = open('exemplo.s', 'r')
instrucao = []

for linha in arquivo:
    linha = linha.strip() #Para tirar espaços em branco no início e no fim da string. tira tbm o \n 
    instrucao.append(linha) #função capaz de adicionar elementos, sem ela imprimiria só a última linha

##print(instrucao)
arquivo.close()

i = 0
x = 0
labels = []
labels_linha = []
aux = 0

num_de_instrucao = len(instrucao)

while(aux < num_de_instrucao):

    palavra1 = instrucao[aux].split()
    ##print(palavra)
    
    label = palavra1[0].split()
    label = label[0]
    label1 = label
    label1 = label1.replace(".","")
    label1 = label1.replace(":","")

    if(label != label1):


        labels.append(label1)

        labels_linha.append(aux + 1)


        x += 1

    aux = aux + 1


#---------------------------------------------salvar as posições da lebal------------------------------------------------------------#
  

#Primeira parte é fazer a leitura do arquivo de cada instrução, ou seja, linha à linha

arquivo = open('exemplo.s', 'r')
instrucao = []

for linha in arquivo:
    linha = linha.strip() #Para tirar espaços em branco no início e no fim da string. tira tbm o \n 
    instrucao.append(linha) #função capaz de adicionar elementos, sem ela imprimiria só a última linha

##print(instrucao)
arquivo.close()

arquivo = open('nome.out','w')

aux = 0
ajuda = 0
num_de_instrucao = len(instrucao)
address = 0
count_concatenar = 0
while(aux < num_de_instrucao):

    palavra = instrucao[aux].split()
    ##print(palavra)

    if ("lsl" in palavra):
        
        c = 0
        for macona in palavra:
            c = c + 1


        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")

            arquivo.writelines(address)
            arquivo.writelines(" : ")

            
            address = int(address,16)

        if(c==4):
    
                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                rm = palavra[2].split()
                rm = rm[0]
                rm1 = rm
                rm1 = rm1.replace("r","")

                im = palavra[3].split()
                im = im[0]
                im1  = im
                im1 = im1.replace("#","")

                #print('teste')
                lsl = 0
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rm1 = rm1.replace(",","")
                rm = int(rm1)
                im = int(im1)
                lsl = lsl  + rd + rm*8 + im*64

                lsl = format(lsl,"x")
                    
                if(count_concatenar%2 !=0):
                    if(im<8):
                        lsl = str(lsl)
                        lsl = "00" + lsl
                        pqp = lsl
                    else:
                        lsl = str(lsl)
                        lsl = "0" + lsl
                        pqp = lsl                      

                else:
                    if(im<8):
                        arquivo.writelines(lsl)
                        arquivo.writelines("00")
                        arquivo.writelines(pqp)
                        arquivo.writelines("\n")
                    else:  
                        arquivo.writelines(lsl)
                        arquivo.writelines("0")
                        arquivo.writelines(pqp)
                        arquivo.writelines("\n")

        if(c==3):

            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rs = palavra[2].split()
            rs = rs[0]
            rs1 = rs
            rs1 = rs1.replace("r","")

            #print('teste')
            lsl = 16512
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rs1 = rs1.replace(",","")
            rs = int(rs1)
            lsl = lsl  + rd + rs*8


            lsl = format(lsl,"x")
            
            if(count_concatenar%2 !=0):
                pqp = lsl
            else:
                    pqp = str(pqp)
                    lsl = str(lsl)
                    arquivo.writelines(lsl)
                    arquivo.writelines(pqp)
                    arquivo.writelines("\n")

    if("lsr" in palavra):
        
        c = 0
        for macona in palavra:
            c = c + 1


        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
        if(c==4):
    
                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                rm = palavra[2].split()
                rm = rm[0]
                rm1 = rm
                rm1 = rm1.replace("r","")

                im = palavra[3].split()
                im = im[0]
                im1  = im
                im1 = im1.replace("#","")

                #print('teste')
                lsr = 1024
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rm1 = rm1.replace(",","")
                rm = int(rm1)
                im = int(im1)
                lsr = lsr  + rd + rm*8 + im*64

                lsr = format(lsr,"x")
                
                if(count_concatenar%2 !=0):
                    lsr = str(lsr)
                    lsr = "0" + lsr
                    pqp = lsr
                else:
                    lsr = str(lsr)
                    lsr = "0" + lsr
                    pqp = str(pqp)
                    arquivo.writelines(lsr)
                    arquivo.writelines(pqp)
                    arquivo.writelines("\n")
        if(c==3):

            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rs = palavra[2].split()
            rs = rs[0]
            rs1 = rs
            rs1 = rs1.replace("r","")

            #print('teste')
            lsr = 16576
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rs1 = rs1.replace(",","")
            rs = int(rs1)
            lsr = lsr  + rd + rs*8

            lsr = format(lsr,"x")   
            
            if(count_concatenar%2 !=0):
                pqp = lsr
            else:
                    pqp = str(pqp)
                    lsr = str(lsr)
                    arquivo.writelines(lsr)
                    arquivo.writelines(pqp)
                    arquivo.writelines("\n")   




    if("asr" in palavra):
        c = 0
        for macona in palavra:
            c = c + 1

        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if(c==4):

            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = rm[0]
            rm1 = rm
            rm1 = rm1.replace("r","")

            im = palavra[3].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")

            #print('teste')
            asr = 4096
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")
            rm = int(rm1)
            im = int(im1)
            asr = asr  + rd + rm*8 + im*64


        if(c==3):

            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rs = palavra[2].split()
            rs = rs[0]
            rs1 = rs
            rs1 = rs1.replace("r","")

            #print('teste')
            asr = 16640
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rs1 = rs1.replace(",","")
            rs = int(rs1)
            asr = asr  + rd + rs*8




        asr = format(asr,"x")
        
        if(count_concatenar%2 !=0):
            pqp = asr
        else:
                pqp = str(pqp)
                asr = str(asr)
                arquivo.writelines(asr)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")         


    if("add" in palavra):
        c = 0
        for macona in palavra:
            c = c + 1

        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
        
        if(c == 4):

            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = rm[0]
            rm1 = rm
            rm1 = rm1.replace("r","")

            im = palavra[3].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")


            if(rd != rd1 and rm != rm1 and im != im1):
                #print('teste')
                add = 7168
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rm1 = rm1.replace(",","")
                rm = int(rm1)
                im = int(im1)
                add = add  + rd + rm*8 + im*64
            
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = rm[0]
            rm1 = rm
            rm1 = rm1.replace("r","")

            rn = palavra[3].split()
            rn = rn[0]
            rn1  = rn
            rn1 = rn1.replace("r","")

            if(rd != rd1 and rn != rn1 and rm != rm1):
                add = 6144
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rm1 = rm1.replace(",","")
                rm = int(rm1)
                rn1 = rn1.replace(",","")
                rn = int(rn1)
                add = add  + rd + rn*64 + rm*8
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            pc = palavra[2].split()
            pc = pc[0]
            pc1 = pc
            pc1 = pc1.replace("p","")

            im = palavra[3].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")

            if(rd != rd1 and pc != pc1 and im != im1):
                add = 36864
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                im1 = im1.replace(",","")
                im = int(im1)
                add = add  + rd*256 + im

            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            sp = palavra[2].split()
            sp = sp[0]
            sp1 = sp
            sp1 = sp1.replace("s","")

            im = palavra[3].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")

            if(rd != rd1 and sp != sp1 and im != im1):
                add = 43008
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                im1 = im1.replace(",","")
                im = int(im1)
                add = add  + rd*256 + im


        if(c==3):
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            im = palavra[2].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")
            
            
            
            if(rd != rd1 and im != im1):
                #print('teste')
                add = 12288
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                im = int(im1)
                add = add  + rd*256 + im

            sp = palavra[1].split()
            sp = sp[0]
            sp1 = sp
            sp1 = sp1.replace("s","")

            im = palavra[2].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")

            if(sp != sp1 and im != im1):
                add = 45056
                im1 = im1.replace(",","")
                im = int(im1)
                add = add  + im        

            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")


            rm = palavra[2].split()
            rm = rm[0]
            rm1 = rm
            rm1 = rm1.replace("r","")

            if(rd != rd1 and rm != rm1):
                rd1 = rm1.replace(",","")
                rd = int(rd1)
                rm1 = rm1.replace(",","")
                rm = int(rm1)

                if(rd < 8 and rm < 8):
                    add = 17408
                    add = add + rm*8 + rd

                if(rd > 7 and rm < 8):
                    add = 17408
                    add = add + 128 #h1
                    add = add + rm*8 + rd

                if(rd < 8 and rm > 7):
                    add = 17408
                    add = add + 64  #h2
                    add = add + rm*8 + rd

                if(rd > 7 and rm > 7):
                    add = 17408   
                    add = add + 128 #h1
                    add = add + 64  #h2
                    add = add + rm*8 + rd

        add = format(add,"x")
        
        if(count_concatenar%2 !=0):
            pqp = add
        else:
                pqp = str(pqp)
                add = str(add)
                arquivo.writelines(add)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    if("sub" in palavra):
        c = 0
        for macona in palavra:
            c = c + 1

        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16) 
        
        if(c == 4):

            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = rm[0]
            rm1 = rm
            rm1 = rm1.replace("r","")

            im = palavra[3].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")


            if(rd != rd1 and rm != rm1 and im != im1):
                #print('teste')
                sub = 7680
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rm1 = rm1.replace(",","")
                rm = int(rm1)
                im = int(im1)
                sub = sub  + rd + rm*8 + im*64
            
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = rm[0]
            rm1 = rm
            rm1 = rm1.replace("r","")

            rn = palavra[3].split()
            rn = rn[0]
            rn1  = rn
            rn1 = rn1.replace("r","")

            if(rd != rd1 and rn != rn1 and rm != rm1):
                sub = 6656
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rm1 = rm1.replace(",","")
                rm = int(rm1)
                rn1 = rn1.replace(",","")
                rn = int(rn1)
                sub = sub  + rd + rn*64 + rm*8

        if(c == 5):

            sp = palavra[1].split()
            sp = sp[0]
            sp1 = sp
            sp1 = sp1.replace("s","")

            im = palavra[2].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")                        

            sub = 45184
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            im1 = im1.replace(",","")
            im = int(im1)
            sub = sub  + im


        if(c==3):
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            im = palavra[2].split()
            im = im[0]
            im1  = im
            im1 = im1.replace("#","")
            
            
            
            if(rd != rd1 and im != im1):
                #print('teste')
                sub = 14336
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                im = int(im1)
                sub = sub  + rd*256 + im



        sub = format(sub,"x")
        
        if(count_concatenar%2 !=0):
            pqp = sub
        else:
                pqp = str(pqp)
                sub = str(sub)
                arquivo.writelines(sub)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 
        
    if("mov" in palavra):
        piroca = palavra[2].split()
        piroca = piroca[0]
        piroca1 = piroca.replace("#","")

        
        count_concatenar = count_concatenar + 1


        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)            

        if(piroca != piroca1):
            

            re = palavra[1].split()
            re = re[0]
            re = re.replace("r","")
            re = re.replace(",","")
            re = int(re)
            piroca1 = int(piroca1)

            if(re < 8 and piroca1 < 8):
                mov = 8192
                mov = mov + re*256 + piroca1

            if(re > 7 and piroca1 < 8):
                mov = 17920
                mov = mov + 128
                mov = mov + re*256 + piroca1
            if(re < 8 and piroca1 > 7):
                mov = 17920
                mov = mov + 64
                mov = mov + re*256 + piroca1

            if(re > 7 and piroca1 < 8):
                mov = 17920
                mov = mov + 128 + 64
                mov = mov + re*256 + piroca1

        if(piroca == piroca1):

            mov = 7168
            if("r0," in palavra):
                mov = mov+0
            if("r1," in palavra):
                mov = mov+1
            if("r2," in palavra):
                mov = mov+2
            if("r3," in palavra):
                mov = mov+3
            if("r4," in palavra):
                mov = mov+4
            if("r5," in palavra):
                mov = mov+5
            if("r6," in palavra):
                mov = mov+6
            if("r7," in palavra):
                mov = mov+7
        
            if("r0" in palavra):
                mov = mov+0
            if("r1" in palavra):
                mov = mov+8
            if("r2" in palavra):
                mov = mov+16
            if("r3" in palavra):
                mov = mov+24
            if("r4" in palavra):
                mov = mov+32
            if("r5" in palavra):
                mov = mov+40 
            if("r6" in palavra):
                mov = mov+48
            if("r7" in palavra):
                mov = mov+56
        
        mov = format(mov,"x")
        
        if(count_concatenar%2 !=0):
            pqp = mov
        else:
                pqp = str(pqp)
                mov = str(mov)
                arquivo.writelines(mov)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")
        

    if("cmp" in palavra):
        
        count_concatenar = count_concatenar + 1


        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd
        rd1 = rd1.replace("r","")

        rs = palavra[2].split()
        rs = rs[0]
        rs1 = rs
        rs1 = rs1.replace("r","")

        if(rd != rd1 and rs != rs1):
            rn = rd1.replace(",","")
            rm = rs1.replace(",","")
            rn = int(rn)
            rm = int(rm)

            if(rm<8 and rn<8):  
                cmpp = 17024
                if("r0," in palavra):
                    cmpp = cmpp+0
                if("r1," in palavra):
                    cmpp = cmpp+1
                if("r2," in palavra):
                    cmpp = cmpp+2
                if("r3," in palavra):
                    cmpp = cmpp+3
                if("r4," in palavra):
                    cmpp = cmpp+4
                if("r5," in palavra):
                    cmpp = cmpp+5
                if("r6," in palavra):
                    cmpp = cmpp+6
                if("r7," in palavra):
                    cmpp = cmpp+7

                if("r0" in palavra):
                    cmpp = cmpp+0
                if("r1" in palavra):
                    cmpp = cmpp+8
                if("r2" in palavra):
                    cmpp = cmpp+16
                if("r3" in palavra):
                    cmpp = cmpp+24
                if("r4" in palavra):
                    cmpp = cmpp+32
                if("r5" in palavra):
                    cmpp = cmpp+40
                if("r6" in palavra):
                    cmpp = cmpp+48
                if("r7" in palavra):
                    cmpp = cmpp+56

            if(rm<8 and rn>7): 
                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                rs = palavra[2].split()
                rs = rs[0]
                rs1 = rs
                rs1 = rs1.replace("r","")

                #print('teste')
                cmpp = 17792
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rs1 = rs1.replace(",","")
                rs = int(rs1)
                cmpp = cmpp  + rd + rs*8

            if(rm>7 and rn<8): 
                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                rs = palavra[2].split()
                rs = rs[0]
                rs1 = rs
                rs1 = rs1.replace("r","")

                #print('teste')
                cmpp = 17728
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rs1 = rs1.replace(",","")
                rs = int(rs1)
                cmpp = cmpp  + rd + rs*8

            if(rm>7 and rn>7): 
                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                rs = palavra[2].split()
                rs = rs[0]
                rs1 = rs
                rs1 = rs1.replace("r","")

                #print('teste')
                cmpp = 17856
                rd1 = rd1.replace(",","")
                rd = int(rd1)
                rs1 = rs1.replace(",","")
                rs = int(rs1)
                cmpp = cmpp  + rd + rs*8


        rn = palavra[1].split()
        rn = rn[0]
        rn1 = rn
        rn1 = rn1.replace("r","")

        im = palavra[2].split()
        im = im[0]
        im1 = im
        im1 = im1.replace("#","")


        if(rn != rn1 and im != im1):
            cmpp = 10240
            rn1 = rn1.replace(",","")
            rn = int(rn1)
            im = int(im1)
            cmpp = cmpp  + im + rn*256
        

        cmpp = format(cmpp,"x")

        if(count_concatenar%2 !=0):
            pqp = cmpp
        else:
                pqp = str(pqp)
                cmpp = str(cmpp)
                arquivo.writelines(cmpp)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("and" in palavra):
        count_concatenar = count_concatenar + 1
        andd = 16384
        
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            andd = andd+0
        if("r1," in palavra):
            andd = andd+1
        if("r2," in palavra):
            andd = andd+2
        if("r3," in palavra):
            andd = andd+3
        if("r4," in palavra):
            andd = andd+4
        if("r5," in palavra):
            andd = andd+5
        if("r6," in palavra):
            andd = andd+6
        if("r7," in palavra):
            andd = andd+7

        if("r0" in palavra):
            andd = andd+0
        if("r1" in palavra):
            andd = andd+8
        if("r2" in palavra):
            andd = andd+16
        if("r3" in palavra):
            andd = andd+24
        if("r4" in palavra):
            andd = andd+32
        if("r5" in palavra):
            andd = andd+40
        if("r6" in palavra):
            andd = andd+48
        if("r7" in palavra):
            andd = andd+56

        andd = format(andd,"x")
        
        if(count_concatenar%2 !=0):
            pqp = andd
        else:
                pqp = str(pqp)
                andd = str(andd)
                arquivo.writelines(andd)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")


    if("eor" in palavra):
        
        count_concatenar = count_concatenar + 1
        eor = 16448

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            eor = eor+0
        if("r1," in palavra):
            eor = eor+1
        if("r2," in palavra):
            eor = eor+2
        if("r3," in palavra):
            eor = eor+3
        if("r4," in palavra):
            eor = eor+4
        if("r5," in palavra):
            eor = eor+5
        if("r6," in palavra):
            eor = eor+6
        if("r7," in palavra):
            eor = eor+7

        if("r0" in palavra):
            eor = eor+0
        if("r1" in palavra):
            eor = eor+8
        if("r2" in palavra):
            eor = eor+16
        if("r3" in palavra):
            eor = eor+24
        if("r4" in palavra):
            eor = eor+32
        if("r5" in palavra):
           eor = eor+40
        if("r6" in palavra):
            eor = eor+48
        if("r7" in palavra):
            eor = eor+56

        eor = format(eor,"x")

        if(count_concatenar%2 !=0):
            pqp = eor
        else:
                pqp = str(pqp)
                eor = str(eor)
                arquivo.writelines(eor)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 


    if("adc" in palavra):
        count_concatenar = count_concatenar + 1
        adc = 16704

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            adc = adc+0
        if("r1," in palavra):
            adc = adc+1
        if("r2," in palavra):
            adc = adc+2
        if("r3," in palavra):
            adc = adc+3
        if("r4," in palavra):
            adc = adc+4
        if("r5," in palavra):
            adc = adc+5
        if("r6," in palavra):
            adc = adc+6
        if("r7," in palavra):
            adc = adc+7
    
        if("r0" in palavra):
            adc = adc+0
        if("r1" in palavra):
            adc = adc+8
        if("r2" in palavra):
            adc = adc+16
        if("r3" in palavra):
            adc = adc+24
        if("r4" in palavra):
            adc = adc+32
        if("r5" in palavra):
            adc = adc+40 
        if("r6" in palavra):
            adc = adc+48
        if("r7" in palavra):
            adc = adc+56
        
        adc = format(adc,"x")
        
        if(count_concatenar%2 !=0):
            #print(adc, end="")
            pqp = adc
        else:
                pqp = str(pqp)
                adc = str(adc)
                arquivo.writelines(adc)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    if("sbc" in palavra):
        
        count_concatenar = count_concatenar + 1
        sbc = 16768

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            sbc = sbc+0
        if("r1," in palavra):
            sbc = sbc+1
        if("r2," in palavra):
            sbc = sbc+2
        if("r3," in palavra):
            sbc = sbc+3
        if("r4," in palavra):
            sbc = sbc+4
        if("r5," in palavra):
            sbc = sbc+5
        if("r6," in palavra):
            sbc = sbc+6
        if("r7," in palavra):
            sbc = sbc+7
    
        if("r0" in palavra):
            sbc = sbc+0
        if("r1" in palavra):
            sbc = sbc+8
        if("r2" in palavra):
            sbc = sbc+16
        if("r3" in palavra):
            sbc = sbc+24
        if("r4" in palavra):
            sbc = sbc+32
        if("r5" in palavra):
            sbc = sbc+40 
        if("r6" in palavra):
            sbc = sbc+48
        if("r7" in palavra):
            sbc = sbc+56
        
        sbc = format(sbc,"x")
        
        if(count_concatenar%2 !=0):
            pqp = sbc
        else:
                pqp = str(pqp)
                sbc = str(sbc)
                arquivo.writelines(sbc)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    if("ror" in palavra):
        count_concatenar = count_concatenar + 1
        ror = 16832

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd
        rd1 = rd1.replace("r","")

        rm = palavra[2].split()
        rm = rm[0]
        rm1 = rm
        rm1 = rm1.replace("r","")

        rd1 = rd1.replace(",","")
        rd = int(rd1)
        rm1 = rm1.replace(",","")
        rm = int(rm1)

        ror = ror  + rd + rm*8


        ror = format(ror,"x")
        
        if(count_concatenar%2 !=0):
            pqp = ror
        else:
                pqp = str(pqp)
                ror = str(ror)
                arquivo.writelines(ror)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 


    if("tst" in palavra):
        
        count_concatenar = count_concatenar + 1
        tst = 16896

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            tst = tst+0
        if("r1," in palavra):
            tst = tst+1
        if("r2," in palavra):
            tst = tst+2
        if("r3," in palavra):
            tst = tst+3
        if("r4," in palavra):
            tst = tst+4
        if("r5," in palavra):
            tst = tst+5
        if("r6," in palavra):
            tst = tst+6
        if("r7," in palavra):
            tst = tst+7
    
        if("r0" in palavra):
            tst = tst+0
        if("r1" in palavra):
            tst = tst+8
        if("r2" in palavra):
            tst = tst+16
        if("r3" in palavra):
            tst = tst+24
        if("r4" in palavra):
            tst = tst+32
        if("r5" in palavra):
            tst = tst+40 
        if("r6" in palavra):
            tst = tst+48
        if("r7" in palavra):
            tst = tst+56
        
        tst = format(tst,"x")
        
        if(count_concatenar%2 !=0):
            pqp = tst
        else:
                pqp = str(pqp)
                tst = str(tst)
                arquivo.writelines(tst)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")


    if("neg" in palavra):
        
        count_concatenar = count_concatenar + 1
        neg = 16960

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            neg = neg+0
        if("r1," in palavra):
            neg = neg+1
        if("r2," in palavra):
            neg = neg+2
        if("r3," in palavra):
            neg = neg+3
        if("r4," in palavra):
            neg = neg+4
        if("r5," in palavra):
            neg = neg+5
        if("r6," in palavra):
            neg = neg+6
        if("r7," in palavra):
            neg = neg+7
    
        if("r0" in palavra):
            neg = neg+0
        if("r1" in palavra):
            neg = neg+8
        if("r2" in palavra):
            neg = neg+16
        if("r3" in palavra):
            neg = neg+24
        if("r4" in palavra):
            neg = neg+32
        if("r5" in palavra):
            neg = neg+40 
        if("r6" in palavra):
            neg = neg+48
        if("r7" in palavra):
            neg = neg+56
        
        neg = format(neg,"x")
        
        if(count_concatenar%2 !=0):
            pqp = neg
        else:
                pqp = str(pqp)
                neg = str(neg)
                arquivo.writelines(neg)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("cmn" in palavra):
        count_concatenar = count_concatenar + 1
        cmn = 17088

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            cmn = cmn+0
        if("r1," in palavra):
            cmn = cmn+1
        if("r2," in palavra):
            cmn = cmn+2
        if("r3," in palavra):
            cmn = cmn+3
        if("r4," in palavra):
            cmn = cmn+4
        if("r5," in palavra):
            cmn = cmn+5
        if("r6," in palavra):
            cmn = cmn+6
        if("r7," in palavra):
            cmn = cmn+7

        if("r0" in palavra):
            cmn = cmn+0
        if("r1" in palavra):
            cmn = cmn+8
        if("r2" in palavra):
            cmn = cmn+16
        if("r3" in palavra):
            cmn = cmn+24
        if("r4" in palavra):
            cmn = cmn+32
        if("r5" in palavra):
           cmn = cmn+40
        if("r6" in palavra):
            cmn = cmn+48
        if("r7" in palavra):
            cmn = cmn+56

        cmn = format(cmn,"x")

        if(count_concatenar%2 !=0):
            pqp = cmn
        else:
                pqp = str(pqp)
                cmn = str(cmn)
                arquivo.writelines(cmn)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("orr" in palavra):
        
        count_concatenar = count_concatenar + 1
        orr = 17152

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            orr = orr+0
        if("r1," in palavra):
            orr = orr+1
        if("r2," in palavra):
            orr = orr+2
        if("r3," in palavra):
            orr = orr+3
        if("r4," in palavra):
            orr = orr+4
        if("r5," in palavra):
            orr = orr+5
        if("r6," in palavra):
            orr = orr+6
        if("r7," in palavra):
            orr = orr+7
    
        if("r0" in palavra):
            orr = orr+0
        if("r1" in palavra):
            orr = orr+8
        if("r2" in palavra):
            orr = orr+16
        if("r3" in palavra):
            orr = orr+24
        if("r4" in palavra):
            orr = orr+32
        if("r5" in palavra):
            orr = orr+40 
        if("r6" in palavra):
            orr = orr+48
        if("r7" in palavra):
            orr = orr+56
        
        orr = format(orr,"x")
        
        if(count_concatenar%2 !=0):
            pqp = orr
        else:
                pqp = str(pqp)
                orr = str(orr)
                arquivo.writelines(orr)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 
        
    if("mul" in palavra):
        
        count_concatenar = count_concatenar + 1
        mul = 17216

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            mul = mul+0
        if("r1," in palavra):
            mul = mul+1
        if("r2," in palavra):
            mul = mul+2
        if("r3," in palavra):
            mul = mul+3
        if("r4," in palavra):
            mul = mul+4
        if("r5," in palavra):
            mul = mul+5
        if("r6," in palavra):
            mul = mul+6
        if("r7," in palavra):
            mul = mul+7
    
        if("r0" in palavra):
            mul = mul+0
        if("r1" in palavra):
            mul = mul+8
        if("r2" in palavra):
            mul = mul+16
        if("r3" in palavra):
            mul = mul+24
        if("r4" in palavra):
            mul = mul+32
        if("r5" in palavra):
            mul = mul+40 
        if("r6" in palavra):
            mul = mul+48
        if("r7" in palavra):
            mul = mul+56
        
        mul = format(mul,"x")
        
        if(count_concatenar%2 !=0):
            pqp = mul
        else:
                pqp = str(pqp)
                mul = str(mul)
                arquivo.writelines(mul)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

        

    if("bic" in palavra):
        count_concatenar = count_concatenar + 1
        bic = 17280

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            bic = bic+0
        if("r1," in palavra):
            bic = bic+1
        if("r2," in palavra):
            bic = bic+2
        if("r3," in palavra):
            bic = bic+3
        if("r4," in palavra):
            bic = bic+4
        if("r5," in palavra):
            bic = bic+5
        if("r6," in palavra):
            bic = bic+6
        if("r7," in palavra):
            bic = bic+7

        if("r0" in palavra):
            bic = bic+0
        if("r1" in palavra):
            bic = bic+8
        if("r2" in palavra):
            bic = bic+16
        if("r3" in palavra):
            bic = bic+24
        if("r4" in palavra):
            bic = bic+32
        if("r5" in palavra):
            bic = bic+40
        if("r6" in palavra):
            bic = bic+48
        if("r7" in palavra):
            bic = bic+56

        bic = format(bic,"x")

        if(count_concatenar%2 !=0):
            pqp = bic
        else:
                pqp = str(pqp)
                bic = str(bic)
                arquivo.writelines(bic)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")
        
    if("mvn" in palavra):
        
        count_concatenar = count_concatenar + 1
        mvn = 17344

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            mvn = mvn+0
        if("r1," in palavra):
            mvn = mvn+1
        if("r2," in palavra):
            mvn = mvn+2
        if("r3," in palavra):
            mvn = mvn+3
        if("r4," in palavra):
            mvn = mvn+4
        if("r5," in palavra):
            mvn = mvn+5
        if("r6," in palavra):
            mvn = mvn+6
        if("r7," in palavra):
            mvn = mvn+7
    
        if("r0" in palavra):
            mvn = mvn+0
        if("r1" in palavra):
            mvn = mvn+8
        if("r2" in palavra):
            mvn = mvn+16
        if("r3" in palavra):
            mvn = mvn+24
        if("r4" in palavra):
            mvn = mvn+32
        if("r5" in palavra):
            mvn = mvn+40 
        if("r6" in palavra):
            mvn = mvn+48
        if("r7" in palavra):
            mvn = mvn+56
        
        mvn = format(mvn,"x")
        
        if(count_concatenar%2 !=0):
            pqp = mvn
        else:
                pqp = str(pqp)
                mvn = str(mvn)
                arquivo.writelines(mvn)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("cpy" in palavra):

        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

            rd = palavra[1].split()
            rd = rd[0]
            rd = rd.replace("r","")
            rd = rd.replace(",","")
            
            rm = palavra[2].split()
            rm = rm[0]
            rm = rm.replace("r","")
            rm = rm.replace(",","")

            rd = int(rd)
            rm = int(rm)

            cpy = 17920
            cpy = cpy  + rd + rm*8

        cpy = format(cpy,"x")
        
        if(count_concatenar%2 !=0):
            pqp = cpy
        else:
                pqp = str(pqp)
                cpy = str(cpy)
                arquivo.writelines(cpy)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")


    if("bx" in palavra):
        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd
        rd1 = rd1.replace("r","")

        if(rd != rd1):
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            krl = 0

            if(rd > 7):
                krl = 64

            bx = 18176 + krl

            bx = bx + rd*8


        bx = format(bx,"x")
        
        if(count_concatenar%2 !=0):
            pqp = bx
        else:
                pqp = str(pqp)
                bx = str(bx)
                arquivo.writelines(bx)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")       


    if("blx" in palavra):
        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd
        rd1 = rd1.replace("r","")

        if(rd != rd1):
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            krl = 0

            if(rd > 7):
                krl = 64

            blx = 18304 + krl

            blx = blx + rd*8


        pika = 0

        if(rd == rd1):

            label = palavra[1].split()
            label = label[0]
            label1 = label
            label1 = label1.replace(".","")
            label1 = label1.replace(":","")

            while(pika < x):
                if(label1 == labels[pika] ):

                    off_set = labels_linha[pika]

                pika += 1

            off_set = int(off_set)
            off_set += 1
            blx = 59392

            blx = blx + off_set



        blx = format(blx,"x")
        
        if(count_concatenar%2 !=0):
            pqp = blx
        else:
                pqp = str(pqp)
                blx = str(blx)
                arquivo.writelines(blx)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("ldr" in palavra):

        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        c = 0
        for macona in palavra:
            c = c + 1

            if(c==4):
                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                rm = palavra[2].split()
                rm = rm[0]
                rm1 = rm
                rm1 = rm1.replace("r","")

                im = palavra[3].split()
                im = im[0]
                im1  = im
                im1 = im1.replace("#","")

                if(rd != rd1 and rm != rm1 and im != im1):
                    ldr = 26624
                    rd1 = rd1.replace(",","")
                    rd = int(rd1)
                    rm1 = rm1.replace(",","")
                    rm1 = rm1.replace("[","")
                    rm = int(rm1)
                    im1 = im1.replace("]","")
                    im = int(im1)
                    ldr = ldr  + rd + rm*8 + im*64

                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                rn = palavra[2].split()
                rn = rn[0]
                rn1  = rn
                rn1 = rn1.replace("r","")

                rm = palavra[3].split()
                rm = rm[0]
                rm1 = rm
                rm1 = rm1.replace("r","")

                if(rd != rd1 and rm != rm1 and rn != rn1):
                    ldr = 26624
                    rd1 = rd1.replace(",","")
                    rd = int(rd1)
                    rm1 = rm1.replace("[","")
                    rm1 = rm1.replace(",","")
                    rm = int(rm1)
                    rn1 = rn1.replace("]","")
                    rn = int(rn1)
                    ldr = ldr  + rd + rn*8 + rm*64

                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                pc = palavra[2].split()
                pc = pc[0]
                pc1 = pc
                pc1 = pc1.replace("p","")

                im = palavra[3].split()
                im = im[0]
                im1  = im
                im1 = im1.replace("#","")

                if(rd != rd1 and pc != pc1 and im != im1):
                    ldr = 18432
                    rd1 = rd1.replace(",","")
                    rd1 = rd1.replace("[","")
                    rd = int(rd1)
                    im1 = im1.replace(",","")
                    im1 = im1.replace("]","")
                    im = int(im1)
                    ldr = ldr  + rd*256 + im

                rd = palavra[1].split()
                rd = rd[0]
                rd1 = rd
                rd1 = rd1.replace("r","")

                sp = palavra[2].split()
                sp = sp[0]
                sp1 = sp
                sp1 = sp1.replace("p","")

                im = palavra[3].split()
                im = im[0]
                im1  = im
                im1 = im1.replace("#","")

                if(rd != rd1 and sp != sp1 and im != im1):
                    ldr = 38912
                    rd1 = rd1.replace(",","")
                    rd1 = rd1.replace("[","")
                    rd = int(rd1)
                    im1 = im1.replace(",","")
                    im1 = im1.replace("]","")
                    im = int(im1)
                    ldr = ldr  + rd*256 + im


        ldr = format(ldr,"x")
        
        if(count_concatenar%2 !=0):
            pqp = ldr
        else:
                pqp = str(pqp)
                ldr = str(ldr)
                arquivo.writelines(ldr)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")  

    if("str" in palavra):
        
        count_concatenar = count_concatenar + 1
        strr = 20480

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            strr = strr+0
        if("r1," in palavra):
            strr = strr+1
        if("r2," in palavra):
            strr = strr+2
        if("r3," in palavra):
            strr = strr+3
        if("r4," in palavra):
            strr = strr+4
        if("r5," in palavra):
            strr = strr+5
        if("r6," in palavra):
            strr = strr+6
        if("r7," in palavra):
            strr = strr+7

        if("[r0," in palavra):
            strr = strr+0
        if("[r1," in palavra):
            strr = strr+8
        if("[r2," in palavra):
            strr = strr+16
        if("[r3," in palavra):
            strr = strr+24
        if("[r4," in palavra):
            strr = strr+32
        if("[r5," in palavra):
            strr = strr+40
        if("[r6," in palavra):
            strr = strr+48
        if("[r7," in palavra):
            strr = strr+56
        

        if("r0]" in palavra):
            strr = strr+0
        if("r1]" in palavra):
            strr = strr+64
        if("r2]" in palavra):
            strr = strr+128
        if("r3]" in palavra):
            strr = strr+192
        if("r4]" in palavra):
            strr = strr+256
        if("r5]" in palavra):
            strr = strr+320
        if("r6]" in palavra):
            strr = strr+384
        if("r7]" in palavra):
            strr = strr+448
        
        strr = format(strr,"x")
        
        if(count_concatenar%2 !=0):
            pqp = strr
        else:
                pqp = str(pqp)
                strr = str(strr)
                arquivo.writelines(strr)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    if("strh" in palavra):
        
        count_concatenar = count_concatenar + 1
        strh = 20992

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            strh = strh+0
        if("r1," in palavra):
            strh = strh+1
        if("r2," in palavra):
            strh = strh+2
        if("r3," in palavra):
            strh = strh+3
        if("r4," in palavra):
            strh = strh+4
        if("r5," in palavra):
            strh = strh+5
        if("r6," in palavra):
            strh = strh+6
        if("r7," in palavra):
            strh = strh+7

        if("[r0," in palavra):
            strh = strh+0
        if("[r1," in palavra):
            strh = strh+8
        if("[r2," in palavra):
            strh = strh+16
        if("[r3," in palavra):
            strh = strh+24
        if("[r4," in palavra):
            strh = strh+32
        if("[r5," in palavra):
            strh = strh+40
        if("[r6," in palavra):
            strh = strh+48
        if("[r7," in palavra):
            strh = strh+56
        

        if("r0]" in palavra):
            strh = strh+0
        if("r1]" in palavra):
            strh = strh+64
        if("r2]" in palavra):
            strh = strh+128
        if("r3]" in palavra):
            strh = strh+192
        if("r4]" in palavra):
            strh = strh+256
        if("r5]" in palavra):
            strh = strh+320
        if("r6]" in palavra):
            strh = strh+384
        if("r7]" in palavra):
            strh = strh+448
        
        strh = format(strh,"x")
        
        if(count_concatenar%2 !=0):
            pqp = strh
        else:
                pqp = str(pqp)
                strh = str(strh)
                arquivo.writelines(strh)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("strb" in palavra):
        
        count_concatenar = count_concatenar + 1
        strb = 21504

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            strb = strb+0
        if("r1," in palavra):
            strb = strb+1
        if("r2," in palavra):
            strb = strb+2
        if("r3," in palavra):
            strb = strb+3
        if("r4," in palavra):
            strb = strb+4
        if("r5," in palavra):
            strb = strb+5
        if("r6," in palavra):
            strb = strb+6
        if("r7," in palavra):
            strb = strb+7

        if("[r0," in palavra):
            strb = strb+0
        if("[r1," in palavra):
            strb = strb+8
        if("[r2," in palavra):
            strb = strb+16
        if("[r3," in palavra):
            strb = strb+24
        if("[r4," in palavra):
            strb = strb+32
        if("[r5," in palavra):
            strb = strb+40
        if("[r6," in palavra):
            strb = strb+48
        if("[r7," in palavra):
            strb = strb+56
        

        if("r0]" in palavra):
            strb = strb+0
        if("r1]" in palavra):
            strb = strb+64
        if("r2]" in palavra):
            strb = strb+128
        if("r3]" in palavra):
            strb = strb+192
        if("r4]" in palavra):
            strb = strb+256
        if("r5]" in palavra):
            strb = strb+320
        if("r6]" in palavra):
            strb = strb+384
        if("r7]" in palavra):
            strb = strb+448
        
        strb = format(strb,"x")
        
        if(count_concatenar%2 !=0):
            pqp = strb
        else:
                pqp = str(pqp)
                strb = str(strb)
                arquivo.writelines(strb)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 


    if("ldrb" in palavra):
        count_concatenar = count_concatenar+1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd
        rd1 = rd1.replace("r","")

        rm = palavra[2].split()
        rm = rm[0]
        rm1 = rm
        rm1 = rm1.replace("r","")

        im = palavra[3].split()
        im = im[0]
        im1  = im
        im1 = im1.replace("#","")

        if(rd != rd1 and rm != rm1 and im != im1):
            ldrb = 30720
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")
            rm1 = rm1.replace("[","")
            rm = int(rm1)
            im1 = im1.replace("]","")
            im = int(im1)
            ldrb = ldrb  + rd + rm*8 + im*64

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd
        rd1 = rd1.replace("r","")

        rn = palavra[2].split()
        rn = rn[0]
        rn1  = rn
        rn1 = rn1.replace("r","")

        rm = palavra[3].split()
        rm = rm[0]
        rm1 = rm
        rm1 = rm1.replace("r","")

        if(rd != rd1 and rm != rm1 and rn != rn1):
            ldrb = 23552
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace("[","")
            rm1 = rm1.replace(",","")
            rm = int(rm1)
            rn1 = rn1.replace("]","")
            rn = int(rn1)
            ldrb = ldrb  + rd + rn*8 + rm*64


        ldrb = format(ldrb,"x")
        
        if(count_concatenar%2 !=0):
            pqp = ldrb
        else:
                pqp = str(pqp)
                ldrb = str(ldrb)
                arquivo.writelines(ldrb)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")   


    if("ldrsb" in palavra):
        
        count_concatenar = count_concatenar + 1
        ldrsb = 22016

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            ldrsb = ldrsb+0
        if("r1," in palavra):
            ldrsb = ldrsb+1
        if("r2," in palavra):
            ldrsb = ldrsb+2
        if("r3," in palavra):
            ldrsb = ldrsb+3
        if("r4," in palavra):
            ldrsb = ldrsb+4
        if("r5," in palavra):
            ldrsb = ldrsb+5
        if("r6," in palavra):
            ldrsb = ldrsb+6
        if("r7," in palavra):
            ldrsb = ldrsb+7

        if("[r0," in palavra):
            ldrsb = ldrsb+0
        if("[r1," in palavra):
            ldrsb = ldrsb+8
        if("[r2," in palavra):
            ldrsb = ldrsb+16
        if("[r3," in palavra):
            ldrsb = ldrsb+24
        if("[r4," in palavra):
            ldrsb = ldrsb+32
        if("[r5," in palavra):
            ldrsb = ldrsb+40
        if("[r6," in palavra):
            ldrsb = ldrsb+48
        if("[r7," in palavra):
            ldrsb = ldrsb+56
        

        if("r0]" in palavra):
            ldrsb = ldrsb+0
        if("r1]" in palavra):
            ldrsb = ldrsb+64
        if("r2]" in palavra):
            ldrsb = ldrsb+128
        if("r3]" in palavra):
            ldrsb = ldrsb+192
        if("r4]" in palavra):
            ldrsb = ldrsb+256
        if("r5]" in palavra):
            ldrsb = ldrsb+320
        if("r6]" in palavra):
            ldrsb = ldrsb+384
        if("r7]" in palavra):
            ldrsb = ldrsb+448
        
        ldrsb = format(ldrsb,"x")
        
        if(count_concatenar%2 !=0):
            pqp = ldrsb
        else:
                pqp = str(pqp)
                ldrsb = str(ldrsb)
                arquivo.writelines(ldrsb)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")
        

    if("ldrh" in palavra):

        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd
        rd1 = rd1.replace("r","")

        rm = palavra[2].split()
        rm = rm[0]
        rm1 = rm
        rm1 = rm1.replace("r","")

        im = palavra[3].split()
        im = im[0]
        im1  = im
        im1 = im1.replace("#","")

        if(rd != rd1 and rm != rm1 and im != im1):
            ldrh = 34816
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")
            rm1 = rm1.replace("[","")
            rm = int(rm1)
            im1 = im1.replace("]","")
            im = int(im1)
            ldrh = ldrh  + rd + rm*8 + im*64

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd
        rd1 = rd1.replace("r","")

        rn = palavra[2].split()
        rn = rn[0]
        rn1  = rn
        rn1 = rn1.replace("r","")

        rm = palavra[3].split()
        rm = rm[0]
        rm1 = rm
        rm1 = rm1.replace("r","")

        if(rd != rd1 and rm != rm1 and rn != rn1):
            ldrh = 23040
            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace("[","")
            rm1 = rm1.replace(",","")
            rm = int(rm1)
            rn1 = rn1.replace("]","")
            rn = int(rn1)
            ldrh = ldrh  + rd + rn*8 + rm*64        
 
        ldrh = format(ldrb,"x")
        
        if(count_concatenar%2 !=0):
            pqp = ldrh
        else:
                pqp = str(pqp)
                ldrh = str(ldrh)
                arquivo.writelines(ldrh)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")   


    if("ldrsh" in palavra):
        
        count_concatenar = count_concatenar + 1
        ldrsh = 24064

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        if("r0," in palavra):
            ldrsh = ldrsh+0
        if("r1," in palavra):
            ldrsh = ldrsh+1
        if("r2," in palavra):
            ldrsh = ldrsh+2
        if("r3," in palavra):
            ldrsh = ldrsh+3
        if("r4," in palavra):
            ldrsh = ldrsh+4
        if("r5," in palavra):
            ldrsh = ldrsh+5
        if("r6," in palavra):
            ldrsh = ldrsh+6
        if("r7," in palavra):
            ldrsh = ldrsh+7

        if("[r0," in palavra):
            ldrsh = ldrsh+0
        if("[r1," in palavra):
            ldrsh = ldrsh+8
        if("[r2," in palavra):
            ldrsh = ldrsh+16
        if("[r3," in palavra):
            ldrsh = ldrsh+24
        if("[r4," in palavra):
            ldrsh = ldrsh+32
        if("[r5," in palavra):
            ldrsh = ldrsh+40
        if("[r6," in palavra):
            ldrsh = ldrsh+48
        if("[r7," in palavra):
            ldrsh = ldrsh+56
        

        if("r0]" in palavra):
            ldrsh = ldrsh+0
        if("r1]" in palavra):
            ldrsh = ldrsh+64
        if("r2]" in palavra):
            ldrsh = ldrsh+128
        if("r3]" in palavra):
            ldrsh = ldrsh+192
        if("r4]" in palavra):
            ldrsh = ldrsh+256
        if("r5]" in palavra):
            ldrsh = ldrsh+320
        if("r6]" in palavra):
            ldrsh = ldrsh+384
        if("r7]" in palavra):
            ldrsh = ldrsh+448
        
        ldrsh = format(ldrsh,"x")
        
        if(count_concatenar%2 !=0):
            pqp = ldrsh
        else:
                pqp = str(pqp)
                ldrsh = str(ldrsh)
                arquivo.writelines(ldrsh)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("sxth" in palavra):

        count_concatenar = count_concatenar + 1
        sxth = 45568

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
          
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = im[0]
            rm1  = rm
            rm1 = rm1.replace("r","")




            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")            
            rm = int(rm1)

            sxth = sxth  + rd + rm*8


        sxth = format(sxth,"x")
        
        if(count_concatenar%2 !=0):
            pqp = sxth
        else:
                pqp = str(pqp)
                sxth = str(sxth)
                arquivo.writelines(sxth)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")               



    if("sxtb" in palavra):

        count_concatenar = count_concatenar + 1
        sxtb = 45632

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
          
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = im[0]
            rm1  = rm
            rm1 = rm1.replace("r","")




            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")            
            rm = int(rm1)

            sxtb = sxtb  + rd + rm*8


        sxtb = format(sxtb,"x")
        
        if(count_concatenar%2 !=0):
            pqp = sxtb
        else:
                pqp = str(pqp)
                sxtb = str(sxtb)
                arquivo.writelines(sxtb)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")      


    if("uxth" in palavra):
        
        count_concatenar = count_concatenar + 1
        uxth = 45696

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
          
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = im[0]
            rm1  = rm
            rm1 = rm1.replace("r","")




            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")            
            rm = int(rm1)

            uxth = uxth  + rd + rm*8


        uxth = format(uxth,"x")
        
        if(count_concatenar%2 !=0):
            pqp = uxth
        else:
                pqp = str(pqp)
                uxth = str(uxth)
                arquivo.writelines(uxth)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("uxtb" in palavra):
        
        count_concatenar = count_concatenar + 1
        uxtb = 45760

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
          
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = im[0]
            rm1  = rm
            rm1 = rm1.replace("r","")




            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")            
            rm = int(rm1)

            uxtb = uxtb  + rd + rm*8


        uxtb = format(uxtb,"x")
        
        
        if(count_concatenar%2 !=0):
            pqp = uxtb
        else:
                pqp = str(pqp)
                uxtb = str(uxtb)
                arquivo.writelines(uxtb)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")     

    if("rev" in palavra):

        count_concatenar = count_concatenar + 1
        rev = 47616

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
          
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = im[0]
            rm1  = rm
            rm1 = rm1.replace("r","")




            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")            
            rm = int(rm1)

            rev = rev  + rd + rm*8


        rev = format(rev,"x")
        
        if(count_concatenar%2 !=0):
            pqp = rev
        else:
                pqp = str(pqp)
                rev = str(rev)
                arquivo.writelines(rev)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")       


    if("rev16" in palavra):
        
        count_concatenar = count_concatenar + 1
        rev16 = 47680

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
          
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = im[0]
            rm1  = rm
            rm1 = rm1.replace("r","")




            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")            
            rm = int(rm1)

            rev16 = rev16  + rd + rm*8


        rev16 = format(rev16,"x")
        
        if(count_concatenar%2 !=0):
            pqp = rev16
        else:
                pqp = str(pqp)
                rev16 = str(rev16)
                arquivo.writelines(rev16)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    if("revsh" in palavra):
        
        count_concatenar = count_concatenar + 1
        revsh = 47808

        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)
          
            rd = palavra[1].split()
            rd = rd[0]
            rd1 = rd
            rd1 = rd1.replace("r","")

            rm = palavra[2].split()
            rm = im[0]
            rm1  = rm
            rm1 = rm1.replace("r","")




            rd1 = rd1.replace(",","")
            rd = int(rd1)
            rm1 = rm1.replace(",","")            
            rm = int(rm1)

            revsh = revsh  + rd + rm*8


        revsh = format(revsh,"x")
        
        if(count_concatenar%2 !=0):
            pqp = revsh
        else:
                pqp = str(pqp)
                revsh = str(revsh)
                arquivo.writelines(revsh)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("push" in palavra):

        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16) 


        c = 0
        for macona in palavra:
            c = c + 1


        if(c == 4):
            rl1 = palavra[1].split()
            rl1 = rl1[0]
            rl1 = rl1.replace("{","")
            rl1 = rl1.replace("}","") 
            rl1 = rl1.replace("r","")                
            rl1 = int(rl1)

            coisa = palavra[2].split()
            coisa = coisa[0]


            rl2 = palavra[3].split()
            rl2 = rl2[0]
            rl2 = rl2.replace("{","")        
            rl2 = rl2.replace("}","")
            rl2 = rl2.replace("r","")        
            rl2 = int(rl2)

            if(coisa == "-"):
                if(rl1 < rl2):
                    contador = 0

                    x = rl1

                    for contar in range(rl1,rl2+1):

                        if(x == 0):
                            contador = contador + 1
                        if(x == 1):
                            contador = contador + 2
                        if(x == 2):
                            contador = contador + 4
                        if(x == 3):
                            contador = contador + 8
                        if(x == 4):
                            contador = contador + 16
                        if(x == 5):
                            contador = contador + 32
                        if(x == 6):
                            contador = contador + 64
                        if(x == 7):
                            contador = contador + 128                                                       
                        x = x+1

                if(rl1 > rl2):
                    contador = 0

                    x = rl2

                    for contar in range(rl2,rl1+1):

                        if(x == 0):
                            contador = contador + 1
                        if(x == 1):
                            contador = contador + 2
                        if(x == 2):
                            contador = contador + 4
                        if(x == 3):
                            contador = contador + 8
                        if(x == 4):
                            contador = contador + 16
                        if(x == 5):
                            contador = contador + 32
                        if(x == 6):
                            contador = contador + 64
                        if(x == 7):
                            contador = contador + 128                                                       
                        x = x+1

            if(coisa == ","):
                contador = 0

                if(rl1 == 0):
                    contador = contador + 1
                if(rl1 == 1):
                    contador = contador + 2
                if(rl1 == 2):
                    contador = contador + 4
                if(rl1 == 3):
                    contador = contador + 8
                if(rl1 == 4):
                    contador = contador + 16
                if(rl1 == 5):
                    contador = contador + 32
                if(rl1 == 6):
                    contador = contador + 64
                if(rl1 == 7):
                    contador = contador + 128
                if(rl1 == 15):
                    contador = contador + 256 

                if(rl2 == 0):
                    contador = contador + 1
                if(rl2 == 1):
                    contador = contador + 2
                if(rl2 == 2):
                    contador = contador + 4
                if(rl2 == 3):
                    contador = contador + 8
                if(rl2 == 4):
                    contador = contador + 16
                if(rl2 == 5):
                    contador = contador + 32
                if(rl2 == 6):
                    contador = contador + 64
                if(rl2 == 7):
                    contador = contador + 128
                if(rl2 == 15):
                    contador = contador + 256 


        if(c == 2):

            rl1 = palavra[1].split()
            rl1 = rl1[0]
            rl1 = rl1.replace("{","")
            rl1 = rl1.replace("}","") 
            rl1 = rl1.replace("r","")                
            rl1 = int(rl1)
            contador = 0

            if(rl1 == 0):
                contador = contador + 1
            if(rl1 == 1):
                contador = contador + 2
            if(rl1 == 2):
                contador = contador + 4
            if(rl1 == 3):
                contador = contador + 8
            if(rl1 == 4):
                contador = contador + 16
            if(rl1 == 5):
                contador = contador + 32
            if(rl1 == 6):
                contador = contador + 64
            if(rl1 == 7):
                contador = contador + 128
            if(rl1 == 15):
                contador = contador + 256 


        push = 46080
        push = push + contador



        push = format(push,"x")
        
        if(count_concatenar%2 !=0):
            pqp = push
        else:
                pqp = str(pqp)
                push = str(push)
                arquivo.writelines(push)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")  





    if("pop" in palavra):
        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16) 


        c = 0
        for macona in palavra:
            c = c + 1


        if(c == 4):
            rl1 = palavra[1].split()
            rl1 = rl1[0]
            rl1 = rl1.replace("{","")
            rl1 = rl1.replace("}","") 
            rl1 = rl1.replace("r","")                
            rl1 = int(rl1)

            coisa = palavra[2].split()
            coisa = coisa[0]


            rl2 = palavra[3].split()
            rl2 = rl2[0]
            rl2 = rl2.replace("{","")        
            rl2 = rl2.replace("}","")
            rl2 = rl2.replace("r","")        
            rl2 = int(rl2)

            if(coisa == "-"):
                if(rl1 < rl2):
                    contador = 0

                    x = rl1

                    for contar in range(rl1,rl2+1):

                        if(x == 0):
                            contador = contador + 1
                        if(x == 1):
                            contador = contador + 2
                        if(x == 2):
                            contador = contador + 4
                        if(x == 3):
                            contador = contador + 8
                        if(x == 4):
                            contador = contador + 16
                        if(x == 5):
                            contador = contador + 32
                        if(x == 6):
                            contador = contador + 64
                        if(x == 7):
                            contador = contador + 128                                                       
                        x = x+1

                if(rl1 > rl2):
                    contador = 0

                    x = rl2

                    for contar in range(rl2,rl1+1):

                        if(x == 0):
                            contador = contador + 1
                        if(x == 1):
                            contador = contador + 2
                        if(x == 2):
                            contador = contador + 4
                        if(x == 3):
                            contador = contador + 8
                        if(x == 4):
                            contador = contador + 16
                        if(x == 5):
                            contador = contador + 32
                        if(x == 6):
                            contador = contador + 64
                        if(x == 7):
                            contador = contador + 128                                                       
                        x = x+1

            if(coisa == ","):
                contador = 0

                if(rl1 == 0):
                    contador = contador + 1
                if(rl1 == 1):
                    contador = contador + 2
                if(rl1 == 2):
                    contador = contador + 4
                if(rl1 == 3):
                    contador = contador + 8
                if(rl1 == 4):
                    contador = contador + 16
                if(rl1 == 5):
                    contador = contador + 32
                if(rl1 == 6):
                    contador = contador + 64
                if(rl1 == 7):
                    contador = contador + 128
                if(rl1 == 15):
                    contador = contador + 256 

                if(rl2 == 0):
                    contador = contador + 1
                if(rl2 == 1):
                    contador = contador + 2
                if(rl2 == 2):
                    contador = contador + 4
                if(rl2 == 3):
                    contador = contador + 8
                if(rl2 == 4):
                    contador = contador + 16
                if(rl2 == 5):
                    contador = contador + 32
                if(rl2 == 6):
                    contador = contador + 64
                if(rl2 == 7):
                    contador = contador + 128
                if(rl2 == 15):
                    contador = contador + 256 


        if(c == 2):

            rl1 = palavra[1].split()
            rl1 = rl1[0]
            rl1 = rl1.replace("{","")
            rl1 = rl1.replace("}","") 
            rl1 = rl1.replace("r","")                
            rl1 = int(rl1)
            contador = 0

            if(rl1 == 0):
                contador = contador + 1
            if(rl1 == 1):
                contador = contador + 2
            if(rl1 == 2):
                contador = contador + 4
            if(rl1 == 3):
                contador = contador + 8
            if(rl1 == 4):
                contador = contador + 16
            if(rl1 == 5):
                contador = contador + 32
            if(rl1 == 6):
                contador = contador + 64
            if(rl1 == 7):
                contador = contador + 128
            if(rl1 == 15):
                contador = contador + 256 


        pop = 48128
        pop = pop + contador



        pop = format(pop,"x")
        
        if(count_concatenar%2 !=0):
            pqp = pop
        else:
                pqp = str(pqp)
                pop = str(pop)
                arquivo.writelines(pop)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")


    if("setend le" in palavra):
        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)



        setend_le = 46672

        setend_le = format(setend_le,"x")
        
        if(count_concatenar%2 !=0):
            pqp = setend_le
        else:
                pqp = str(pqp)
                setend_le = str(setend_le)
                arquivo.writelines(setend_le)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    if("setend be" in palavra):
        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)



        setend_be = 46680

        setend_be = format(setend_be,"x")
        
        if(count_concatenar%2 !=0):
            pqp = setend_be
        else:
                pqp = str(pqp)
                setend_be = str(setend_be)
                arquivo.writelines(setend_be)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("cpsie" in palavra):
        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        cpsie = 46688


        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd

        rd1 = rd1.replace("a","")

        if(rd != rd1):
            cpsie = cpsie + 4

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd

        rd1 = rd1.replace("i","")

        if(rd != rd1):            
            cpsie = cpsie + 2

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd

        rd1 = rd1.replace("f","")

        if(rd != rd1):
            cpsie = cpsie + 1



        cpsie = format(cpsie,"x")
        
        if(count_concatenar%2 !=0):
            pqp = cpsie
        else:
                pqp = str(pqp)
                cpsie = str(cpsie)
                arquivo.writelines(cpsie)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")


    if("cpsid" in palavra):
        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        cpsid = 46704


        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd

        rd1 = rd1.replace("a","")

        if(rd != rd1):
            cpsid = cpsid + 4

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd

        rd1 = rd1.replace("i","")

        if(rd != rd1):            
            cpsid = cpsid + 2

        rd = palavra[1].split()
        rd = rd[0]
        rd1 = rd

        rd1 = rd1.replace("f","")

        if(rd != rd1):
            cpsid = cpsid + 1



        cpsid = format(cpsid,"x")
        
        if(count_concatenar%2 !=0):
            pqp = cpsid
        else:
                pqp = str(pqp)
                cpsid = str(cpsid)
                arquivo.writelines(cpsid)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    if("stmia" in palavra):

        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16) 

        rn = palavra[1].split()
        rn = rn[0]
        rn = rn.replace("r","")
        rn = rn.replace("!","")
        rn = int(rn)

        rl1 = palavra[2].split()
        rl1 = rl1[0]
        rl1 = rl1.replace("{","")
        rl1 = int(rl1)

        coisa = palavra[3].split()
        coisa = coisa[0]


        rl2 = palavra[4].split()
        rl2 = rl2[0]
        rl2 = rl2.replace("}","")
        rl2 = int(rl2)

        if(coisa == "-"):
            if(rl1 < rl2):
                contador = 0

                x = rl1

                for contar in range(rl1,rl2+1):

                    if(x == 0):
                        contador = contador + 1
                    if(x == 1):
                        contador = contador + 2
                    if(x == 2):
                        contador = contador + 4
                    if(x == 3):
                        contador = contador + 8
                    if(x == 4):
                        contador = contador + 16
                    if(x == 5):
                        contador = contador + 32
                    if(x == 6):
                        contador = contador + 64
                    if(x == 7):
                        contador = contador + 128                                                       
                    x = x+1

            if(rl1 > rl2):
                contador = 0

                x = rl2

                for contar in range(rl2,rl1+1):

                    if(x == 0):
                        contador = contador + 1
                    if(x == 1):
                        contador = contador + 2
                    if(x == 2):
                        contador = contador + 4
                    if(x == 3):
                        contador = contador + 8
                    if(x == 4):
                        contador = contador + 16
                    if(x == 5):
                        contador = contador + 32
                    if(x == 6):
                        contador = contador + 64
                    if(x == 7):
                        contador = contador + 128                                                       
                    x = x+1

        if(coisa == ","):

            if(rl1 == 0):
                contador = contador + 1
            if(rl1 == 1):
                contador = contador + 2
            if(rl1 == 2):
                contador = contador + 4
            if(rl1 == 3):
                contador = contador + 8
            if(rl1 == 4):
                contador = contador + 16
            if(rl1 == 5):
                contador = contador + 32
            if(rl1 == 6):
                contador = contador + 64
            if(rl1 == 7):
                contador = contador + 128 

            if(rl2 == 0):
                contador = contador + 1
            if(rl2 == 1):
                contador = contador + 2
            if(rl2 == 2):
                contador = contador + 4
            if(rl2 == 3):
                contador = contador + 8
            if(rl2 == 4):
                contador = contador + 16
            if(rl2 == 5):
                contador = contador + 32
            if(rl2 == 6):
                contador = contador + 64
            if(rl2 == 7):
                contador = contador + 128


        stmia = 49152
        stmia = stmia + rn*256 + contador



        stmia = format(stmia,"x")
        
        if(count_concatenar%2 !=0):
            pqp = stmia
        else:
                pqp = str(pqp)
                stmia = str(stmia)
                arquivo.writelines(stmia)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("ldmia" in palavra):
    
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)      

        rn = palavra[1].split()
        rn = rn[0]
        rn1 = rn
        rn1 = rn1.replace("r","")

        im = palavra[2].split()
        im = im[0]
        im1  = im
        im1 = im1.replace("#","")

            #print('teste')
        ldmia = 51200
        rn1 = rn1.replace(",","")
        rn1 = rn1.replace("!","")        
        rn = int(rn1)
        im = int(im1)
        ldmia = ldmia + rn*256 + im




        ldmia = format(ldmia,"x")
        
        if(count_concatenar%2 !=0):
            pqp = ldmia
        else:
                pqp = str(pqp)
                ldmia = str(ldmia)
                arquivo.writelines(ldmia)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")       



    if("b" in palavra):

        im = palavra[1].split()
        im = im[0]
        im2 = im.replace(".","")

        if(im != im2):
            break


        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0


        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]

            pika += 1

        off_set = int(off_set)
        off_set += 2

        b = 57344

        b = b + off_set




        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")              

    if("beq" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        off_set = 0
        pika = 0

        if(rd == rd1):

            label = palavra[1].split()
            label = label[0]
            label1 = label
            label1 = label1.replace(".","")
            label1 = label1.replace(":","")

            while(pika < x):
                if(label1 == labels[pika] ):

                    off_set = labels_linha[pika]

                pika += 1

        off_set = int(off_set)
        off_set += 1



        b = 53248
        cond = 0
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 


    if("bne" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bcs" in palavra or "bhs" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 2*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bcc" in palavra or "blo" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 3*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bmi" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 4*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")  

    if("bpl" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 5*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 


    if("bvs" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)



        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 6*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bvc" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 7*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bhi" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 8*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bls" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 9*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bge" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 10*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("blt" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        b = 53248
        cond = 11*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bgt" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        #print('teste')
        b = 53248
        cond = 12*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("ble" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        #print('teste')
        b = 53248
        cond = 13*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n") 

    if("bal" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)


        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        #print('teste')
        b = 53248
        cond = 14*256
        b = b + off_set + cond



        b = format(b,"x")
        
        if(count_concatenar%2 !=0):
            pqp = b
        else:
                pqp = str(pqp)
                b = str(b)
                arquivo.writelines(b)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    if("bkpt" in palavra):
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        #print('teste')
        bkpt = 48640
        bkpt = bkpt + off_set



        if(count_concatenar%2 !=0):
            pqp = bkpt
        else:
                pqp = str(pqp)
                bkpt = str(bkpt)
                arquivo.writelines(bkpt)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")   


    if("swi" in palavra):
        
        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        im = palavra[1].split()
        im = im[0]

        swi = 57088
        im = im.replace("#","")
        im = int(im)
        swi = swi + im



        swi = format(swi,"x")
        
        if(count_concatenar%2 !=0):
            pqp = swi
        else:
                pqp = str(pqp)
                swi = str(swi)
                arquivo.writelines(swi)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")  


    if("bl" in palavra):

        count_concatenar = count_concatenar + 1
        if(count_concatenar%2 != 0):
            address = address + 4*ajuda
            ajuda = 1
            address = format(address,"x")
            arquivo.writelines(address)
            arquivo.writelines(" : ")
            address = int(address,16)

        pika = 0
        off_set = 0
        label = palavra[1].split()
        label = label[0]
        label1 = label
        label1 = label1.replace(".","")
        label1 = label1.replace(":","")

        while(pika < x):
            if(label1 == labels[pika] ):

                off_set = labels_linha[pika]
                pika += 1

        off_set = int(off_set)
        off_set += 1

        bl = 63488

        bl = bl + off_set



        bl = format(bl,"x")
        
        if(count_concatenar%2 !=0):
            pqp = bl
        else:
                pqp = str(pqp)
                bl = str(bl)
                arquivo.writelines(bl)
                arquivo.writelines(pqp)
                arquivo.writelines("\n")

    aux+=1