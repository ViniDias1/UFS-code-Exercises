'''
Nome: Vinicius Dias Valenca
Matricula: 202100045850

'''
import sys
import time
import ctypes


arqInput = open(sys.argv[1],'r')
arqOutput = open(sys.argv[2],'w')

hexa = []
aux = 0
binario = [("0b00000000000000000000000000000000")]*(32765)
mem = ([("0x00000000")]*(32765))
i = 0

def tX(a):
    a = a.replace("X","x")
    return a
def completaZeroHexa(a):
    
    while True:
        
        if len(a) < 10 and a[0] != "-":
            a =  "0x"+ "0" + a[2:]
        elif len(a) < 11 and a[0] == "-":
            a =  "-0x"+ "0" + a[3:]
        else:
            return a
def completaZeroHexa8(a):
    
    while True:
        
        if len(a) < 4 and a[0] != "-":
            a =  "0x"+ "0" + a[2:]
        elif len(a) < 5 and a[0] == "-":
            a =  "-0x"+ "0" + a[3:]
        if len(a) > 4 and a[0] != "-":
            a =  "0x" + (a[3:])
        elif len(a) < 5 and a[0] == "-":
            a =  "-0x" + (a[3:])
        else:
            return a
def completaZeroHexa16(a):
    
    while True:
        
        if len(a) < 6 and a[0] != "-":
            a =  "0x"+ "0" + a[2:]
        elif len(a) < 7 and a[0] == "-":
            a =  "-0x"+ "0" + a[3:]
        if len(a) > 6 and a[0] != "-":
            a =  "0x" + (a[3:])
        elif len(a) < 7 and a[0] == "-":
            a =  "-0x" + (a[3:])
        else:
            return a
def completaZeroHexa64(a):
    
    while True:
        
        if len(a) < 18 and a[0] != "-":
            a =  "0x"+ "0" + a[2:]
        elif len(a) < 19 and a[0] == "-":
            a =  "-0x"+ "0" + a[3:]
        else:
            return a
def completaZero(b):
    for i in range(32):
        bms = "0"
        if len(b) < 32:
            b = bms + b
        else:
            break
    return b
def completaZero64(b):
    for i in range(64):
        bms = "0"
        if len(b) < 64:
            b = bms + b
        else:
            break
    return b
def completaZeroBin(b):
    for i in range(32):
        bms = b[0]
        if len(b) < 32:
            b = bms + b
        else:
            break
    return b
def completaZeroBin64(c):

    for i in range(64):
        cms = c[0]
        if len(c) < 64:
            c = cms + c
        else:
            break
    return c
def completaTamanho(c):

    for i in range(32):
        if len(c) < 32:
            c = '0' + c
        else:
            break
    return c
def complementa2(str):
    n = len(str)
    i = n - 1
    if str == '0':
        return "0"
    if len(str) == 31:
        if str[:6] == '111111':
            return str
    while(i >= 0):
        if (str[i] == '1'):
            break
        i -= 1
 
    if (i == -1):
        return '1'+str
 
    k = i - 1
    while(k >= 0):
         
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)
        k -= 1
 
    return str

for codigoHexa in arqInput:
    aux = bin(int(codigoHexa,16)).strip("\n")
    hexa.append(codigoHexa.strip("\n")) #le o arquivo e armazena numa lista de Hexas
    mem[i] = (codigoHexa.strip("\n"))
    if aux == '0b0':
        binario[i] =(aux) + "0"*31
    else:
        for b in range(len(aux)+1):
            if len(aux) < 34:
                aux = "0b" + "0" + aux[2:] 
            else:
                binario[i] = aux
                break
    i = i + 1

                               
arqOutput.write("[START OF SIMULATION]\n")
proxPC = 0
sp = 32764
variavel = 0
pulo = bin(0)
num1,num2 = 0,0
ultimaLinha = 0
registradorL4 = 0
listaRegisDEC = []
pc = completaZeroHexa(hex(0))
listaRegistradores = ["0x00000000"] * 32
listaRegistradores[0] = "0x00000000"
proxIns = completaZeroHexa(binario[0])

regisEsp = ["r0","r1","r2","r3","r4","r5","r6","r7","r8","r9","r10","r11","r12","r13","r14","r15","r16","r17","r18","r19","r20","r21","r22","r23","r24","r25","r26","r27","ir","pc","sp","sr"]

for e in range(32):
    listaRegisDEC.append(0)

sr = ['0'] * 32

for d in range(180):
    
    c = proxIns

    if c.rfind("1") != -1:
        
        pc=tX(completaZeroHexa(hex(proxPC)).upper())
        
        zn,zd,sn,ov,iv,cy = '0','0','0','0','0','0'
        if c[2:4] == "00": 

            operacao,opZ,opX,opY,imed = c[2:8], c[8:13], c[13:18], c[18:23], c[23:]

            
            if operacao == "000000" and c.rfind("1") != -1:  

                instrucao = "mov"
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                rZ = int(opZ,2)
                registradorZ = regisEsp[rZ]
                
                variavelDEC = int((opX+opY+imed),2)
                variavelHEXA = tX(completaZeroHexa(hex(variavelDEC)).upper())
                listaRegisDEC[rZ] = variavelDEC
                listaRegistradores[rZ] = variavelHEXA
                if registradorZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    listaRegisDEC[rZ] = 0
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                    listaRegisDEC[rZ] = listaRegisDEC[rZ]

                imprimir = f"   {instrucao} {registradorZ},{variavelDEC:<20}{tX(registradorZ.upper())}={variavelHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")


            elif operacao == "000001":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "movs"                         
                rZ = int(opZ,2)
                registradorZ = regisEsp[rZ]
                variavelBin = completaZeroBin(opX+opY+imed)
                variavelDEC = int(variavelBin,2)
                variavelHEXA = tX(completaZeroHexa(hex(variavelDEC)).upper())
                if variavelBin[0] == '1':
                    variavelDEC = int(complementa2(variavelBin),2) * -1

                listaRegisDEC[rZ] = variavelDEC
                listaRegistradores[rZ] = variavelHEXA
                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    listaRegisDEC[rZ] = 0
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                    listaRegisDEC[rZ] = listaRegisDEC[rZ]

                imprimir = f"   {instrucao} {registradorZ},{variavelDEC:<5}         	{registradorZ.upper()}={variavelHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "000010":                      # ADD #
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "add"
                rZ = int(opZ,2)
                rX = int(opX,2)
                rY = int(opY,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                registradorY = regisEsp[rY]
                
                num1 = listaRegisDEC[rX]
                num2 = listaRegisDEC[rY]
                n1 = complementa2(completaZeroBin(bin(num1).strip("-")[2:]))
                n2 = complementa2(completaZeroBin(bin(num2).strip("-")[2:]))
                if n1[0] == "1":
                    num1 = num1 * -1
                if n2[0] == "1":
                    num2 = num2 * -1
                soma = num1 + num2
                if soma >= 0:
                    somaBin = completaZero(bin(soma).strip("-")[2:])
                else:
                    somaBin = completaZeroBin(bin(soma).strip("-")[2:])
                
                listaRegistradores[rZ] = completaZeroHexa(hex(soma))
                listaRegisDEC[rZ] = soma
                if len(somaBin) >32:
                    cy = "1"
                    sr[31] = cy
                else:
                    sr[31] = "0"
                if (somaBin[0] == "1") and soma < 0:
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"
                if ((n1[0] == n2[0]) and (somaBin[0]) != n1[0]):
                    ov = "1"
                    sr[28] = ov
                else:
                    sr[28] = "0"
                if listaRegistradores[rZ] == "0x00000000":
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"

                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    listaRegisDEC[rZ] = 0
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                    listaRegisDEC[rZ] = listaRegisDEC[rZ]

                
                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorZ},{registradorX},{registradorY}           	{registradorZ.upper()}={registradorX.upper()}+{registradorY.upper()}={tX(listaRegistradores[rZ].upper())},SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")


            elif operacao == "000011":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "sub"              
                rZ = int(opZ,2)
                rX = int(opX,2)
                rY = int(opY,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                registradorY = regisEsp[rY]
                
                num1 = listaRegisDEC[rX]
                num2 = listaRegisDEC[rY]
                n1 = (completaZeroBin(bin(int(listaRegistradores[rX],16)).strip("-")[2:]))
                n2 = (completaZeroBin(bin(int(listaRegistradores[rY],16)).strip("-")[2:]))
                
                subtracao = num1 - num2
                subBin = completaZero(bin(int(listaRegistradores[rX],16)-int(listaRegistradores[rY],16)).strip("-")[2:])
                listaRegistradores[rZ] = completaZeroHexa(hex(subtracao))
                listaRegisDEC[rZ] = subtracao
                variavelHEXA = completaZeroHexa(hex(int(subBin,2)))
                listaRegistradores[rZ] = variavelHEXA
                listaRegisDEC[rZ] = subtracao 
                
                if len(subBin) >31:
                    cy = "1"
                    sr[31] = cy
                else:
                    sr[31] = "0"
                
                if (subBin[0] == "1"):
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"
                
                if ((n1[0] != n2[0]) and (subBin[0]) != n1[0]):
                    ov = "1"
                    sr[28] = ov

                if listaRegistradores[rZ] == "0x00000000":
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
                

                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    listaRegisDEC[rZ] = 0
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                    listaRegisDEC[rZ] = listaRegisDEC[rZ]

                
                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorZ},{registradorX},{registradorY}           	{registradorZ.upper()}={registradorX.upper()}-{registradorY.upper()}={tX(variavelHEXA.upper())},SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")


            elif operacao == "000101":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "cmp"
                rZ = int(opZ,2)
                rX = int(opX,2)
                rY = int(opY,2)
                registradorX = regisEsp[rX]
                registradorY = regisEsp[rY]
                
                num1 = listaRegisDEC[rX]
                num2 = listaRegisDEC[rY]
                n1 = (completaZero(bin(int(listaRegistradores[rX],16)).strip("-")[2:]))
                n2 = (completaZero(bin(int(listaRegistradores[rY],16)).strip("-")[2:]))
                
                cmp = num1 - num2
                if cmp<0:
                    cmpBin = complementa2(completaZero(bin(abs(int(listaRegistradores[rX],16))-abs(int(listaRegistradores[rY],16))).strip("-")[2:]))
                else:
                    cmpBin = completaZero(bin(int(listaRegistradores[rX],16)-int(listaRegistradores[rY],16)).strip("-")[2:])

                variavelHEXA = completaZeroHexa(hex(int(cmpBin,2)))
                
                if (cmpBin[0] == "1") or (int(cmpBin,2)>=4294967295)or (cmp <= -2147483647):
                    cy = "1"
                    sr[31] = cy
                else:
                    sr[31] = "0"
                
                if (cmpBin[0] == "1"):
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"
                
                if ((n1[0] != n2[0]) and (cmpBin[0]) != n1[0]):
                    ov = "1"
                    sr[28] = ov
                else:
                    sr[28] = "0"

                if cmp == 0:
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
                

                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    listaRegisDEC[rZ] = 0
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                    listaRegisDEC[rZ] = listaRegisDEC[rZ]

                
                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorX},{registradorY}                	SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")


            elif operacao == "000100":

                if imed[:3] == "000":
                    listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                    listaRegisDEC[28] = int(c,2)
                    listaRegistradores[29] = pc
                    listaRegisDEC[29] = int(pc,16)
                    instrucao = "mul"                    
                    rZ = int(opZ,2)
                    rX = int(opX,2)
                    rY = int(opY,2)
                    L4 = int(imed,2)
                    registradorZ = regisEsp[rZ]
                    registradorX = regisEsp[rX]
                    registradorY = regisEsp[rY]
                    rl4 = regisEsp[L4]
                    
                    num1 = listaRegisDEC[rX]
                    num2 = listaRegisDEC[rY]
                    n1 = complementa2(completaZeroBin(bin(num1).strip("-")[2:]))
                    n2 = complementa2(completaZeroBin(bin(num2).strip("-")[2:]))
                    if n1[0] == "1":
                        num1 = num1 * -1
                    if n2[0] == "1":
                        num2 = num2 * -1
                    multiplicacao = num1 * num2
                    multBin = completaZero64(bin(int(listaRegistradores[rX],16)*int(listaRegistradores[rY],16)).strip("-")[2:])
                    variavelHexa = completaZeroHexa64(hex(int(multBin,2)))
                    listaRegistradores[L4] = "0x"+variavelHexa[2:10]
                    listaRegisDEC[L4] = int(listaRegistradores[L4],16)
                    listaRegistradores[rZ] = "0x"+variavelHexa[10:]
                    listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)

                    if L4 == 0:
                        listaRegistradores[L4] = completaZeroHexa(hex(0))
                        listaRegisDEC[L4] = 0
                    
                    
                    if listaRegisDEC[L4] != 0:
                        cy = "1"
                        sr[31] = cy
                    else:
                        sr[31] = "0"
                    if multiplicacao == 0 :
                        zn = "1"
                        sr[25] = zn
                    else:
                        sr[25] = "0"
                    
                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                    listaRegistradores[31] = srHEXA
                    imprimir = f"   {instrucao} {rl4},{registradorZ},{registradorX},{registradorY:<12}{rl4.upper()}:{registradorZ.upper()}={registradorX.upper()}*{registradorY.upper()}={tX(variavelHexa.upper())}, SR={srHEXA}"
                    arqOutput.write(pc+":"+imprimir+"\n")


                elif imed[:3] == "010":
                    listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                    listaRegisDEC[28] = int(c,2)
                    listaRegistradores[29] = pc
                    listaRegisDEC[29] = int(pc,16)
                    instrucao = "muls"                 
                    rZ = int(opZ,2)
                    rX = int(opX,2)
                    rY = int(opY,2)
                    L4 = int(imed[6:],2)
                    registradorZ = regisEsp[rZ]
                    registradorX = regisEsp[rX]
                    registradorY = regisEsp[rY]
                    rl4 = regisEsp[L4]
                    
                    num1 = listaRegisDEC[rX]
                    num2 = listaRegisDEC[rY]
                    n1 = (completaZeroBin(bin(num1).strip("-")[2:]))
                    n2 = (completaZeroBin(bin(num2).strip("-")[2:]))
                    if num1>0:
                        if  int(n1,2) != ctypes.c_int32(int(n1,2)).value:
                            n1 = complementa2(completaZeroBin(bin(num1).strip("-")[2:]))
                    if num2>0:
                        if  int(n2,2) != ctypes.c_int32(int(n2,2)).value:
                            n2 = complementa2(completaZeroBin(bin(num2).strip("-")[2:]))
                    multiplicacao = num1 * num2
                    multbin = n2+n1
                    if rl4 == "r21":
                        h1 = "0x"+"C" + completaZeroHexa(hex(int(n1,2)))[3:]
                        h2 = completaZeroHexa(hex(int(n2,2)))
                        variavelHexa = "0x"+h2[2:]+h1[2:]
                    else:
                        h1 = completaZeroHexa(hex(int(n1,2)))
                        h2 = completaZeroHexa(hex(int(n2,2)))
                        variavelHexa = "0x"+h2[2:]+h1[2:]
                    
                    if n1[0] == "1":
                        listaRegisDEC[rZ] = int(complementa2(n1),2) * -1
                        listaRegistradores[rZ] = "0x"+variavelHexa[10:]
                    else:
                        listaRegistradores[rZ] = "0x"+variavelHexa[10:]
                        listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)
                    if n2[0] == "1":
                        listaRegisDEC[L4] = int(complementa2(n2),2) * -1
                        listaRegistradores[L4] = "0x"+variavelHexa[2:10]
                    else:
                        listaRegistradores[L4] = "0x"+variavelHexa[2:10]
                        listaRegisDEC[L4] = int(listaRegistradores[L4],16)
                    
                    if L4 == 0:
                        listaRegistradores[L4] = completaZeroHexa(hex(0))
                        listaRegisDEC[L4] = 0
                    
                    if listaRegisDEC[L4] != 0:
                        ov = "1"
                        sr[28] = ov
                    else:
                        sr[31] = "0"
                    if multiplicacao == 0 :
                        zn = "1"
                        sr[25] = zn
                    else:
                        sr[25] = "0"
                    
                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                    listaRegistradores[31] = srHEXA
                    imprimir = f"   {instrucao} {rl4},{registradorZ},{registradorX},{registradorY:<11}{rl4.upper()}:{registradorZ.upper()}={registradorX.upper()}*{registradorY.upper()}={tX(variavelHexa.upper())}, SR={srHEXA}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                
                
                elif imed[:3] == "100":
                    listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                    listaRegisDEC[28] = int(c,2)
                    listaRegistradores[29] = pc
                    listaRegisDEC[29] = int(pc,16)
                    instrucao = "div"
                    rZ = int(opZ,2)
                    rX = int(opX,2)
                    rY = int(opY,2)
                    L4 = int(imed[6:],2)
                    registradorZ = regisEsp[rZ]
                    registradorX = regisEsp[rX]
                    registradorY = regisEsp[rY]
                    rl4 = regisEsp[L4]
                    
                    num1 = listaRegisDEC[rX]
                    num2 = listaRegisDEC[rY]
                    if num2 == 0:
                        zd = "1"
                        sr[26] = zd
                        num2 = 1
                    else:
                        sr[26] = "0"
                    n1 = (completaZeroBin(bin(num1).strip("-")[2:]))
                    n2 = (completaZeroBin(bin(num2).strip("-")[2:]))
                                
                    divisaoNormal = abs(num1//num2)
                    divisaoResto = abs(num1%num2)
                    if (num1 < 0) or (num2 < 0):
                        divisaoNormal = divisaoNormal * -1
                        divisaoResto = divisaoResto * -1
                    
                    if divisaoNormal < 0:
                        dvn = complementa2(completaZero(bin(abs(divisaoNormal))))
                        dvn = completaZeroHexa(hex(int(dvn,2)))
                    else:
                        dvn = completaZeroHexa(hex(divisaoNormal))
                    
                    if divisaoResto < 0:
                        dvr = complementa2(completaZero(bin(abs(divisaoResto))))
                        dvr = completaZeroHexa(hex(int(dvr,2)))
                    else:
                        dvr = completaZeroHexa(hex(divisaoResto))
                    variavelHEXA = tX(dvn.upper())
                    variavelHEXA2 = tX(dvr.upper())
                    listaRegistradores[rZ] = variavelHEXA
                    listaRegistradores[L4] = variavelHEXA2
                    listaRegisDEC[rZ] = divisaoNormal
                    listaRegisDEC[L4] = divisaoResto
                    if registradorZ == 0:
                        listaRegistradores[rZ] = completaZeroHexa(hex(0))
                        listaRegistradores[L4] = completaZeroHexa(hex(0))
                        listaRegisDEC[rZ] = 0
                        listaRegisDEC[L4] = 0
                    
                    if listaRegisDEC[rZ] == 0:
                        zn = '1'
                        sr[25] = zn
                    else:
                        sr[25] = "0"
                    if bin(int(dvr,16)) != 0:
                        cy = '1'
                        sr[31] = cy
                    else:
                        sr[31] = "0"
                    
                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                    listaRegistradores[31] = srHEXA
                    imprimir = f"   {instrucao} {rl4},{registradorZ},{registradorX},{registradorY:<13}{rl4.upper()}={registradorX.upper()}%{registradorY.upper()}={tX(dvr.upper())},{tX(registradorZ.upper())}={tX(registradorX.upper())}/{tX(registradorY.upper())}={tX(dvn.upper())},SR={srHEXA}"
                    arqOutput.write(pc+":"+imprimir+"\n")

                
                elif imed[:3] == "110":
                    listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                    listaRegisDEC[28] = int(c,2)
                    listaRegistradores[29] = pc
                    listaRegisDEC[29] = int(pc,16)
                    instrucao = "divs"
                    rZ = int(opZ,2)
                    rX = int(opX,2)
                    rY = int(opY,2)
                    L4 = int(imed[6:],2)
                    registradorZ = regisEsp[rZ]
                    registradorX = regisEsp[rX]
                    registradorY = regisEsp[rY]
                    rl4 = regisEsp[L4]
                    
                    num1 = (bin(listaRegisDEC[rX]).strip("-")[2:])
                    num2 = (bin(listaRegisDEC[rY]).strip("-")[2:])
                    if num1[0] == "1":
                        num1 = complementa2(bin(listaRegisDEC[rX]).strip("-")[2:])
                        num1 = int(num1,2) * -1
                    if num2[0] == "1":
                        num2 = complementa2(bin(listaRegisDEC[rY]).strip("-")[2:])
                        num2 = int(num2,2) * -1
                    
                    if num2 == 0:
                        zd = "1"
                        sr[26] = zd
                        num2 = 1
                    else:
                        sr[26] = "0"
                    n1 = (completaZeroBin(bin(num1).strip("-")[2:]))
                    n2 = (completaZeroBin(bin(num2).strip("-")[2:]))
                                
                    divisaoNormal = (num1//num2)
                    divisaoResto = (num1%num2)
                    if divisaoNormal < 0:
                        dvn = completaZeroBin(bin(divisaoNormal).strip("-")[2:])
                        dvn = completaZeroHexa(hex(int(dvn,2)))
                    else:
                        dvn = completaZeroHexa(hex(divisaoNormal))

                    if divisaoResto < 0:
                        dvr = completaZeroBin(bin(divisaoResto).strip("-")[2:])
                        dvr = hex(int(dvr,2))
                    else:
                        dvr = completaZeroHexa(hex(divisaoResto))
                    
                    variavelHEXA = dvn
                    variavelHEXA2 = dvr
                    listaRegistradores[rZ] = variavelHEXA
                    listaRegistradores[L4] = variavelHEXA2
                    listaRegisDEC[rZ] = divisaoNormal
                    listaRegisDEC[L4] = divisaoResto
                    if registradorZ == 0:
                        listaRegistradores[rZ] = completaZeroHexa(hex(0))
                        listaRegistradores[L4] = completaZeroHexa(hex(0))
                        listaRegisDEC[rZ] = 0
                        listaRegisDEC[L4] = 0
                    
                    if listaRegisDEC[rZ] == 0:
                        zn = '1'
                        sr[25] = zn
                    else:
                        sr[25] = "0"
                    if listaRegistradores[L4] != "0x00000000":
                        cy = '1'
                        sr[31] = cy
                    else:
                        sr[31] = "0"

                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                    listaRegistradores[31] = srHEXA
                    imprimir = f"   {instrucao} {rl4},{registradorZ},{registradorX},{registradorY:<12}{rl4.upper()}={registradorX.upper()}%{tX(registradorY.upper())}={tX(dvr.upper())},{tX(registradorZ.upper())}={tX(registradorX.upper())}/{tX(registradorY.upper())}={tX(dvn.upper())},SR={srHEXA}"
                    arqOutput.write(pc+":"+imprimir+"\n")


                elif imed[:3] == "001":
                    listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                    listaRegisDEC[28] = int(c,2)
                    listaRegistradores[29] = pc
                    listaRegisDEC[29] = int(pc,16)
                    instrucao = "sll"
                    rZ = int(opZ,2)
                    rX = int(opX,2)           
                    rY = int(opY,2)
                    L4 = int(imed[6:],2)
                    registradorZ = regisEsp[rZ]
                    registradorX = regisEsp[rX]
                    registradorY = regisEsp[rY]
                    num1 = listaRegisDEC[rZ]
                    num2 = listaRegisDEC[rY]
                    n1 = complementa2(completaZeroBin(bin(num1).strip("-")[2:]))
                    n2 = complementa2(completaZeroBin(bin(num2).strip("-")[2:]))
                    nl4 = complementa2(completaZeroBin(bin(L4).strip("-")[2:]))
                    if n1[0] == "1" and (num1 < 0):
                        num1 = num1 * -1
                    if n2[0] == "1" and (num2 < 0):
                        num2 = num2 * -1
                    if nl4[0] == "1" and (L4 < 0):
                        L4 = L4 * -1
                    teste = "0x"+(listaRegistradores[rZ])[2:] +(listaRegistradores[rY])[2:]
                    pross = (int(teste,16)) << L4+1 #parei aqui
                    prossBin = completaZero(bin(pross).strip("-")[2:])
                    
                    deslocamento = completaZeroHexa64(hex(pross)).strip('-')
                    listaRegistradores[rZ] = "0x"+deslocamento[2:10]
                    listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)
                    listaRegistradores[rX] = "0x"+deslocamento[10:]
                    listaRegisDEC[rX] = int(listaRegistradores[rX],16)
                    if rX == 0:
                        listaRegistradores[rX] = completaZeroHexa(hex(0))
                        listaRegisDEC[rX] = 0
                    else:
                        listaRegistradores[rX] = "0x"+deslocamento[10:]
                        listaRegisDEC[rX] = int(listaRegistradores[rX],16)

                    if deslocamento == "0x0000000000000000":
                        zn = "1"
                        sr[25] = zn
                    else:
                        sr[25] = "0"
                    if listaRegisDEC[rZ] != 0:
                        cy = "1"
                        sr[31] = cy
                    else:
                        sr[31] = "0"

                    if rZ == 0:
                        listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    else:
                        listaRegistradores[rZ] = listaRegistradores[rZ]
                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                    listaRegistradores[31] = srHEXA
                    imprimir = f"   {instrucao} {registradorZ},{registradorX},{registradorY},{L4:<12}{registradorZ.upper()}:{registradorX.upper()}={registradorZ.upper()}:{registradorX.upper()}<<{L4+1}={tX(deslocamento.upper())},SR={srHEXA}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                
                
                elif imed[:3] == "011":
                    listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                    listaRegisDEC[28] = int(c,2)
                    listaRegistradores[29] = pc
                    listaRegisDEC[29] = int(pc,16)
                    instrucao = "sla"
                    rZ = int(opZ,2)
                    rX = int(opX,2)           
                    rY = int(opY,2)
                    L4 = int(imed[6:],2)
                    registradorZ = regisEsp[rZ]
                    registradorX = regisEsp[rX]
                    registradorY = regisEsp[rY]
                    num1 = listaRegisDEC[rZ]
                    num2 = listaRegisDEC[rY]
                    n1 = complementa2(completaZeroBin(bin(num1).strip("-")[2:]))
                    n2 = complementa2(completaZeroBin(bin(num2).strip("-")[2:]))
                    nl4 = complementa2(completaZeroBin(bin(L4).strip("-")[2:]))
                    if n1[0] == "1" and (num1 < 0):
                        num1 = num1 * -1
                    if n2[0] == "1" and (num2 < 0):
                        num2 = num2 * -1
                    if nl4[0] == "1" and (L4 < 0):
                        L4 = L4 * -1

                    pross = (num1+num2) << L4+1
                    
                    if pross >= 0:
                        prossBin = completaZero(bin(pross).strip("-")[2:])
                    else:
                        prossBin = completaZeroBin(bin(pross).strip("-")[2:])
                    deslocamento = completaZeroHexa64(hex(pross)).strip('-')
                    listaRegistradores[rZ] = "0x"+deslocamento[2:10]
                    listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)
                    listaRegistradores[rX] = "0x"+deslocamento[10:]
                    listaRegisDEC[rX] = int(listaRegistradores[rX],16)
                    if rX == 0:
                        listaRegistradores[rX] = completaZeroHexa(hex(0))
                        listaRegisDEC[rX] = 0
                    else:
                        listaRegistradores[rX] = "0x"+deslocamento[10:]
                        listaRegisDEC[rX] = int(listaRegistradores[rX],16)

                
                    if deslocamento == "0x0000000000000000":
                        zn = "1"
                    if listaRegisDEC[rZ] != 0:
                        ov = "1"
                    
                    sr[25] = zn
                    sr[28] = ov
                    
                    if rZ == 0:
                        listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    else:
                        listaRegistradores[rZ] = listaRegistradores[rZ]
                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                    listaRegistradores[31] = srHEXA
                    
                    imprimir = f"   {instrucao} {registradorZ},{registradorX},{registradorY},{L4}          	{registradorZ.upper()}:{registradorX.upper()}={registradorZ.upper()}:{registradorX.upper()}<<{L4+1}={tX(deslocamento.upper())},SR={srHEXA}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                    

                elif imed[:3] == "101":
                    listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                    listaRegisDEC[28] = int(c,2)
                    listaRegistradores[29] = pc
                    listaRegisDEC[29] = int(pc,16)
                    instrucao = "srl"
                    rZ = int(opZ,2)
                    rX = int(opX,2)           
                    rY = int(opY,2)
                    L4 = int(imed[6:],2)
                    registradorZ = regisEsp[rZ]
                    registradorX = regisEsp[rX]
                    registradorY = regisEsp[rY]
                    num1 = listaRegisDEC[rZ]
                    num2 = listaRegisDEC[rY]
                    n1 = complementa2(completaZeroBin(bin(num1).strip("-")[2:]))
                    n2 = complementa2(completaZeroBin(bin(num2).strip("-")[2:]))
                    nl4 = complementa2(completaZeroBin(bin(L4).strip("-")[2:]))
                    if n1[0] == "1" and (num1 < 0):
                        num1 = num1 * -1
                    if n2[0] == "1" and (num2 < 0):
                        num2 = num2 * -1
                    if nl4[0] == "1" and (L4 < 0):
                        L4 = L4 * -1
                    teste = "0x"+(listaRegistradores[rZ])[2:] +(listaRegistradores[rY])[2:]
                    pross = (int(teste,16)) >> L4+1 #parei aqui
                    if pross >= 0:
                        prossBin = completaZero(bin(pross).strip("-")[2:])
                    else:
                        prossBin = completaZeroBin(bin(pross).strip("-")[2:])
                    deslocamento = completaZeroHexa64(hex(pross)).strip('-')
                    listaRegistradores[rZ] = "0x"+deslocamento[2:10]
                    listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)
                    listaRegistradores[rX] = "0x"+deslocamento[10:]
                    listaRegisDEC[rX] = int(listaRegistradores[rX],16)
                    if rX == 0:
                        listaRegistradores[rX] = completaZeroHexa(hex(0))
                        listaRegisDEC[rX] = 0
                    else:
                        listaRegistradores[rX] = "0x"+deslocamento[10:]
                        listaRegisDEC[rX] = int(listaRegistradores[rX],16)

                
                    if deslocamento == "0x0000000000000000":
                        zn = "1"
                    if listaRegisDEC[rZ] != 0:
                        ov = "1"

                    if ((ov=='1') or (zn == '1')):
                        sr = ['0'] * 32
                        sr[31] = cy
                        sr[27] = sn
                        sr[28] = ov
                        sr[25] = zn
                    else:
                        sr = sr
                    if rZ == 0:
                        listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    else:
                        listaRegistradores[rZ] = listaRegistradores[rZ]
                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                    listaRegistradores[31] = srHEXA
                    imprimir = f"   {instrucao} {registradorZ},{registradorX},{registradorY},{L4}          	{registradorZ.upper()}:{registradorX.upper()}={registradorZ.upper()}:{registradorX.upper()}>>{L4+1}={deslocamento.upper()},SR={srHEXA.upper()}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                
                
                elif imed[:3] == "111":
                    listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                    listaRegisDEC[28] = int(c,2)
                    listaRegistradores[29] = pc
                    listaRegisDEC[29] = int(pc,16)
                    instrucao = "sra"
                    rZ = int(opZ,2)
                    rX = int(opX,2)           
                    rY = int(opY,2)
                    L4 = int(imed[6:],2)
                    registradorZ = regisEsp[rZ]
                    registradorX = regisEsp[rX]
                    registradorY = regisEsp[rY]
                    num1 = listaRegisDEC[rZ]
                    num2 = listaRegisDEC[rY]
                    n1 = (completaZeroBin(bin(num1).strip("-")[2:]))
                    n2 = (completaZeroBin(bin(num2).strip("-")[2:]))
                    nl4 = (completaZeroBin(bin(L4).strip("-")[2:]))
                    if num1>0:
                        if  int(n1,2) != ctypes.c_int32(int(n1,2)).value:
                            n1 = complementa2(completaZeroBin(bin(num1).strip("-")[2:]))

                    if num2>0:
                        if  int(n2,2) != ctypes.c_int32(int(n2,2)).value:
                            n2 = complementa2(completaZeroBin(bin(num2).strip("-")[2:]))
                    pross = (num1 + num2) >> L4+1        
                    if (num1 < 0) or (num2 < 0):
                        pross = pross * -1
                    if pross >= 0:
                        prossBin = completaZero(bin(pross).strip("-")[2:])
                    else:
                        prossBin = completaZeroBin64(bin(pross).strip("-")[2:])

                    deslocamento = completaZeroHexa64(hex(int(prossBin,2))).strip('-')

                    
                    listaRegistradores[rX] = "0x"+deslocamento[10:]
                    listaRegisDEC[rX] = int(listaRegistradores[rX],16)                

                    listaRegistradores[rZ] = "0x"+deslocamento[2:10]
                    listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)

                    if rX == 0:
                        listaRegistradores[rX] = completaZeroHexa(hex(0))
                        listaRegisDEC[rX] = 0
                    elif rZ == 0:
                        listaRegistradores[rZ] = completaZeroHexa(hex(0))
                        listaRegisDEC[rZ] = 0

                    if deslocamento == "0x0000000000000000":
                        zn = "1"
                        sr[25] = zn
                    else:
                        sr[25] = "0"
                    if listaRegisDEC[rZ] != 0:
                        ov = "1"
                        sr[28] = ov
                    else:
                        sr[28] = "0"

                    if rZ == 0:
                        listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    else:
                        listaRegistradores[rZ] = listaRegistradores[rZ]
                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                    listaRegistradores[31] = srHEXA
                    listaRegisDEC[31] = int(srHEXA,16)
                    
                    imprimir = f"   {instrucao} {registradorZ},{registradorX},{registradorY},{L4:<12}{registradorZ.upper()}:{registradorX.upper()}={registradorZ.upper()}:{registradorX.upper()}>>{L4+1}={tX(deslocamento.upper())},SR={srHEXA}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                
            
            elif operacao == "000110":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "and"
                rZ = int(opZ,2)
                rX = int(opX,2)           
                rY = int(opY,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                registradorY = regisEsp[rY]
                num1 = listaRegisDEC[rX]
                num2 = listaRegisDEC[rY]
                anD = (num1 & num2)
                listaRegistradores[rZ] = completaZeroHexa(hex(int(listaRegistradores[rX],16) & int(listaRegistradores[rY],16)))
                listaRegisDEC[rZ] = anD

                if listaRegistradores[rZ] == "0x00000000":
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
                if anD < 0:
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"

                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                
                imprimir =f"   {instrucao} {registradorZ},{registradorX},{registradorY}            	{registradorZ.upper()}={registradorX.upper()}&{registradorY.upper()}={tX(listaRegistradores[rZ].upper())},SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "000111":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "or"
                rZ = int(opZ,2)
                rX = int(opX,2)           
                rY = int(opY,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                registradorY = regisEsp[rY]
                num1 = listaRegisDEC[rX]
                num2 = listaRegisDEC[rY]
                oR = (num1 | num2)
                listaRegistradores[rZ] = completaZeroHexa(hex(int(listaRegistradores[rX],16) | int(listaRegistradores[rY],16)))
                listaRegisDEC[rZ] = oR
                if listaRegistradores[rZ] == "0x00000000":
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
                if oR < 0:
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"

                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                
                
                if registradorZ == "sr":
                    srHEXA = listaRegistradores[rZ]
                    aux = completaZero(bin(int(srHEXA,16)).strip("-")[2:])
                    sr[25] = aux[25]
                    sr[26] = aux[26]
                    sr[27] = aux[27]
                    sr[28] = aux[28]
                    sr[29] = aux[29]
                    sr[30] = aux[30]
                    sr[31] = aux[31]
                else:
                    srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir =f"   {instrucao} {registradorZ},{registradorX},{registradorY}            	{registradorZ.upper()}={registradorX.upper()}|{registradorY.upper()}={tX(listaRegistradores[rZ].upper())},SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")
                
            elif operacao == "001000":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "not"
                rZ = int(opZ,2)
                rX = int(opX,2)    
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX] 
                num1 = listaRegisDEC[rX]
                noT = (~num1)
                if noT<0:
                    noTBin = (complementa2(completaZero(bin(noT).strip("-")[2:]))) ## parei aqui
                else:
                    noTBin =  ((completaZero(bin(noT).strip("-")[2:])))

                listaRegistradores[rZ] = completaZeroHexa(hex(int(noTBin,2)))
                listaRegisDEC[rZ] = noT

                if listaRegistradores[rZ] == "0x00000000":
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
                if noTBin[0] == '1':
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"
                
                if registradorZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
            
                imprimir =f"    {instrucao} {registradorZ},{registradorX}               	{registradorZ.upper()}=~{registradorX.upper()}={tX(listaRegistradores[rZ].upper())},SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            
            elif operacao == "001001":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "xor"
                rZ = int(opZ,2)
                rX = int(opX,2)           
                rY = int(opY,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                registradorY = regisEsp[rY]
                num1 = listaRegisDEC[rX]
                num2 = listaRegisDEC[rY]
                xor = (num1 ^ num2)
                listaRegistradores[rZ] = completaZeroHexa(hex(int(listaRegistradores[rX],16) ^ int(listaRegistradores[rY],16)))
                listaRegisDEC[rZ] = xor

                if listaRegistradores[rZ] == "0x00000000":
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
                if xor < 0:
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"

                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]

                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                if registradorZ == "sr":
                    srHEXA = "0x00000040"
                    listaRegistradores[31] = srHEXA
                    sr = ["0"]*32
                    sr[25] = "1"
                imprimir =f"   {instrucao} {registradorZ},{registradorX},{registradorY}            	{registradorZ.upper()}={registradorX.upper()}^{registradorY.upper()}={tX(listaRegistradores[rZ].upper())},SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "001010":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "push"
                ipush = [0]*5
                ipush[0] = int(imed[:5],2)
                ipush[1] = int(imed[5:],2)
                ipush[2] = int(opX,2)
                ipush[3] = int(opY,2)
                ipush[4] = int(opZ,2)
                cont = 0
                topo = tX((listaRegistradores[30]).upper())
                resulpush = [0]*5
                for i in ipush:
                    if i != 0:
                        rI = int(i)
                        registradorI = regisEsp[i]
                        mem[sp] = listaRegistradores[i]
                        resulpush[cont] = tX((mem[sp]).upper())
                        valor = listaRegistradores[i]
                        sp = sp - 4
                        listaRegistradores[30] = completaZeroHexa(hex(sp))
                        end = completaZeroHexa(hex(int(completaZeroBin((bin(sp)[2:])),2)))
                        cont = cont + 1
                    else:
                        break
                if cont == 0:
                    imprimir = f"   {instrucao} -                   	MEM[{topo}]"+"{"+"}={"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 1:
                    imprimir = f"   {instrucao} {regisEsp[ipush[0]]}     	MEM[{topo}]"+"{"+ f"{resulpush[0]}" +"}={"+f"{(regisEsp[ipush[0]]).upper()}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 2:
                    imprimir = f"   {instrucao} {regisEsp[ipush[0]]},{regisEsp[ipush[1]]}     	MEM[{topo}]"+"{"+ f"{resulpush[0]},{resulpush[1]}" +"}="+"{"+f"{(regisEsp[ipush[0]]).upper()},{(regisEsp[ipush[1]]).upper()}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 3:
                    imprimir = f"   {instrucao} {regisEsp[ipush[0]]},{regisEsp[ipush[1]]},{regisEsp[ipush[2]]}     	MEM[{topo}]"+"{"+ f"{resulpush[0]},{resulpush[1]},{resulpush[2]}" +"}={"+f"{(regisEsp[ipush[0]]).upper()},{(regisEsp[ipush[1]]).upper()},{(regisEsp[ipush[2]]).upper()}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 4:
                    imprimir = f"   {instrucao} {regisEsp[ipush[0]]},{regisEsp[ipush[1]]},{regisEsp[ipush[2]]},{regisEsp[ipush[3]]}     	MEM[{topo}]"+"{"+ f"{resulpush[0]},{resulpush[1]},{resulpush[2]},{resulpush[3]}" +"}={"+f"{(regisEsp[ipush[0]]).upper()},{(regisEsp[ipush[1]]).upper()},{(regisEsp[ipush[2]]).upper()},{(regisEsp[ipush[3]]).upper()}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 5:
                    imprimir = f"   {instrucao} {regisEsp[ipush[0]]},{regisEsp[ipush[1]]},{regisEsp[ipush[2]]},{regisEsp[ipush[3]]},{regisEsp[ipush[4]]}     	MEM[{topo}]"+"{"+ f"{resulpush[0]},{resulpush[1]},{resulpush[2]},{resulpush[3]},{resulpush[4]}" +"}={"+f"{(regisEsp[ipush[0]]).upper()},{(regisEsp[ipush[1]]).upper()},{(regisEsp[ipush[2]]).upper()},{(regisEsp[ipush[3]]).upper()},{(regisEsp[ipush[4]]).upper()}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                
                
            elif operacao == "001011":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "pop"
                ipop = [0]*5
                ipop[0] = int(imed[:5],2)
                ipop[1] = int(imed[5:],2)
                ipop[2] = int(opX,2)
                ipop[3] = int(opY,2)
                ipop[4] = int(opZ,2)
                cont = 0
                topo = tX((listaRegistradores[30]).upper())
                resulpop = [0]*5
                for i in ipop:
                    if i != 0:
                        sp = sp + 4
                        listaRegistradores[30] = completaZeroHexa(hex(sp))
                        rI = int(i)
                        registradorI = regisEsp[i]
                        listaRegistradores[i] = mem[sp] 
                        resulpop[cont] = tX((mem[sp]).upper())
                        valor = listaRegistradores[i]
                        
                        end = completaZeroHexa(hex(int(completaZeroBin((bin(sp)[2:])),2)))
                        cont = cont + 1
                    else:
                        break
                if cont == 0:
                    imprimir = f"   {instrucao} -                   	"+"{"+"}="+""f"MEM[{topo}]"+"{"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 1:
                    imprimir = f"   {instrucao} {regisEsp[ipop[0]]}     	"+"{"+f"{(regisEsp[ipop[0]]).upper()}"+"}="+f"MEM[{topo}]"+"{"+f"{resulpop[0]}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 2:
                    imprimir = f"   {instrucao} {regisEsp[ipop[0]]},{regisEsp[ipop[1]]}     	"+"{"+f"{(regisEsp[ipop[0]]).upper()},{(regisEsp[ipop[1]]).upper()}"+"}="+f"MEM[{topo}]"+"{"+f"{resulpop[0]},{resulpop[1]}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 3:
                    imprimir = f"   {instrucao} {regisEsp[ipop[0]]},{regisEsp[ipop[1]]},{regisEsp[ipop[2]]}     	"+"{"+f"{(regisEsp[ipop[0]]).upper()},{(regisEsp[ipop[1]]).upper()},{(regisEsp[ipop[2]]).upper()}"+"}="+f"MEM[{topo}]"+"{"+f"{resulpop[0]},{resulpop[1]},{resulpop[2]}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 4:
                    imprimir = f"   {instrucao} {regisEsp[ipop[0]]},{regisEsp[ipop[1]]},{regisEsp[ipop[2]]},{regisEsp[ipop[3]]}     	"+"{"+f"{(regisEsp[ipop[0]]).upper()},{(regisEsp[ipop[1]]).upper()},{(regisEsp[ipop[2]]).upper()},{(regisEsp[ipop[3]]).upper()}"+"}="+f"MEM[{topo}]"+"{"+f"{resulpop[0]},{resulpop[1]},{resulpop[2]},{resulpop[3]}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")
                elif cont == 5:
                    imprimir = f"   {instrucao} {regisEsp[ipop[0]]},{regisEsp[ipop[1]]},{regisEsp[ipop[2]]},{regisEsp[ipop[3]]},{regisEsp[ipop[4]]}     	"+"{"+f"{(regisEsp[ipop[0]]).upper()},{(regisEsp[ipop[1]]).upper()},{(regisEsp[ipop[2]]).upper()},{(regisEsp[ipop[3]]).upper()},{(regisEsp[ipop[4]]).upper()}"+"}="+f"MEM[{topo}]"+"{"+f"{resulpop[0]},{resulpop[1]},{resulpop[2]},{resulpop[3]},{resulpop[4]}"+"}"
                    arqOutput.write(pc+":"+imprimir+"\n")


        elif c[2:3] == "1": #S

            operacao,imed = c[2:8],c[8:]

            if operacao == "110111":   
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bun", int(imed,2)
                pulo = completaZeroHexa(hex(((variavel*4)+proxPC)+4))
                
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")


            elif operacao == "101010":   
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bae", int(imed,2)
                proxPC = proxPC + 4
                if sr[31] == '0':
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "101011":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bat", int(imed,2)
                proxPC = proxPC + 4
                if (sr[31] == '0') and (sr[25] == '0'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            
            elif operacao == "101100":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bbe", int(imed,2)
                proxPC = proxPC + 4
                if (sr[31] == '1') or (sr[25] == '1'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                 
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "101101":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bbt", int(imed,2)
                proxPC = proxPC + 4
                if (sr[31] == '1'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
             
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "101110":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "beq", int(imed,2)
                proxPC = proxPC + 4
                if sr[25] == '1':
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                 
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "101111":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bge", int(imed,2)
                proxPC = proxPC + 4
                if (sr[27] == sr[28]):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")
            

            elif operacao == "110000":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bgt", int(imed,2)
                proxPC = proxPC + 4
                if ((sr[27] == sr[28]) and (sr[25]) == '0'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                 
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "110001":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "biv", int(imed,2)
                proxPC = proxPC + 4
                if (sr[29] == '1'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                 
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "110010":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "ble", int(imed,2)
                proxPC = proxPC + 4
                if (sr[28] != sr[27]) or (sr[25] == '1'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                 
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "110011":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "blt", int(imed,2)
                proxPC = proxPC + 4
                if (sr[28] != sr[27]):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                 
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "110100":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bne", int(imed,2)
                proxPC = proxPC + 4
                if (sr[25] == '0'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")
             
            elif operacao == "110101":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bni", int(imed,2)
                proxPC = proxPC + 4
                if (sr[29] == '0'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                 
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "110110":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bnz", int(imed,2)
                proxPC = proxPC + 4
                if (sr[26] == '0'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "111000":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao, variavel = "bzd", int(imed,2)
                proxPC = proxPC + 4
                if (sr[26] == '1'):
                    pulo = completaZeroHexa(hex((proxPC)+(variavel<<2)))
                else:
                    pulo = completaZeroHexa(hex(proxPC))
                imprimir = f"   {instrucao} {variavel}                    	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")


            elif operacao == "111001":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "call"
                variavel = int(completaZeroBin(complementa2(imed)),2)
                if imed[0] == "1":
                    variavel = variavel * -1
                else:
                    variavel = variavel
                
                pc4 = tX(completaZeroHexa(hex(proxPC+4)).upper())
                binario[sp] = binario[((proxPC+4)//4)]
                mem[sp] = completaZeroHexa(hex(int(binario[sp],2)))
                
                pulo = completaZeroHexa(hex(((variavel*4)+proxPC)+4))
                
                imprimir = f"   {instrucao} {variavel}                 	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())},MEM[{tX(listaRegistradores[30].upper())}]={pc4}"
                arqOutput.write(pc+":"+imprimir+"\n")
                sp = sp - 4
                listaRegistradores[30] = completaZeroHexa(hex(sp))
                listaRegisDEC[30] = sp


            elif operacao == "111111":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "int"
                imediato = int(imed,2)
                imprimir = f"   {instrucao} {imediato}                    	CR=0x00000000,PC=0x00000000"
                arqOutput.write(pc+":"+imprimir+"\n")
                break

        else: 
            operacao,opZ,opX,imed = c[2:8],c[8:13],c[13:18],c[18:]

            if operacao == "010010":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "addi"
                rZ = int(opZ,2)
                rX = int(opX,2)
                im = int(imed,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
            
                
                num1 = listaRegisDEC[rX]
                num2 = im
                n1 = (completaZeroBin(bin(num1).strip("-")[2:]))
                n2 = (completaZeroBin(bin(num2).strip("-")[2:]))
                if n1[0] == "1":
                    num1 = num1 * -1
                if n2[0] == "1":
                    num2 = num2 * -1
                somai = num1 + num2
                somaBini = (bin((int(listaRegistradores[rX],16) + im))[2:])
                
                listaRegistradores[rZ] = completaZeroHexa(hex(somai))
                listaRegisDEC[rZ] = somai
                if somaBini[0] == "1":
                    cy = "1"
                    sr[31] = cy
                if (somaBini[0] == "1") and somai < 0:
                    sn = "1"
                    sr[27] = sn
                if ((n1[0] == n2[0] and somaBini[0] != n1[0])):
                    ov = "1"
                    sr[28] = ov
                if listaRegistradores[rZ] == "0x00000000":
                    zn = "1"
                    sr[25] = zn

                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    listaRegisDEC[rZ] = 0
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                    listaRegisDEC[rZ] = listaRegisDEC[rZ] 
                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorZ},{registradorX},{im}           	{registradorZ.upper()}={registradorX.upper()}+{completaZeroHexa(hex(im))}={tX(listaRegistradores[rZ].upper())},SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")

            elif operacao == "010011":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "subi"
                rZ = int(opZ,2)
                rX = int(opX,2)
                im = int(imed,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
    
                num1 = listaRegisDEC[rX]
                num2 = im
                n1 = complementa2(completaZeroBin(bin(num1).strip("-")[2:]))
                n2 = complementa2(completaZeroBin(bin(num2).strip("-")[2:]))
                if n1[0] == "1" and (num1 < 0):
                    num1 = num1 * -1
                if n2[0] == "1" and (num2 < 0):
                    num2 = num2 * -1
                subtracaoI = num1 - num2
                subBinI = completaZero(bin((int(listaRegistradores[rX],16) - im))[2:])

                listaRegistradores[rZ] = completaZeroHexa(hex(subtracaoI))
                listaRegisDEC[rZ] = subtracaoI
                variavelHEXA = completaZeroHexa(hex(int(subBinI,2)))
                listaRegistradores[rZ] = variavelHEXA
                listaRegisDEC[rZ] = subtracaoI
                if len(subBinI) >32:
                    cy = "1"
                    sr[31] = cy
                else:
                    sr[31] = "0"
                if (subBinI[0] == "1") and subtracaoI < 0:
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"
                if ((n1[0] != n2[0]) and (subBinI[0]) != n1[0]):
                    ov = "1"
                    sr[28] = ov
                else:
                    sr[28] = "0"

                if listaRegistradores[rZ] == "0x00000000":
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
                
                
                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    listaRegisDEC[rZ] = 0
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                    listaRegisDEC[rZ] = listaRegisDEC[rZ]

                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorZ},{registradorX},{im}           	{registradorZ.upper()}={registradorX.upper()}-{completaZeroHexa(hex(im))}={tX(completaZeroHexa(hex(num1-num2)).upper())},SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "010111":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "cmpi"
                rZ = int(opZ,2)
                rX = int(opX,2)
                im = int(imed,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
    
                num1 = listaRegisDEC[rX]
                num2 = im
                n1 = (completaZero(bin(num1).strip("-")[2:]))
                n2 = (completaZero(bin(num2).strip("-")[2:]))
                if imed[0] == "1":
                    num2 = complementa2(imed)
                    num2 = int(num2,2)*-1

                cmpi = num1 - num2
            
                if cmpi<0:
                    cmpiBin = complementa2(completaZero(bin(abs(int(listaRegistradores[rX],16))-abs(int(imed,2))).strip("-")[2:]))
                else:
                    cmpiBin = completaZero(bin(int(listaRegistradores[rX],16)-int(imed,2)).strip("-")[2:])

                variavelHEXA = completaZeroHexa(hex(int(cmpiBin,2)))
                
                listaRegistradores[rZ] = completaZeroHexa(hex(cmpi))
                listaRegisDEC[rZ] = cmpi
                variavelHEXA = completaZeroHexa(hex(int(cmpiBin,2)))
                listaRegistradores[rZ] = variavelHEXA
                listaRegisDEC[rZ] = cmpi
                if (cmpiBin[0] == "1") or (int(cmpiBin,2)>=4294967295)or (cmpi <= -2147483647):
                    cy = "1"
                    sr[31] = cy
                else:
                    sr[31] = "0"
                
                if (cmpiBin[0] == "1"):
                    sn = "1"
                    sr[27] = sn
                else:
                    sr[27] = "0"
                
                if ((n1[0] != n2[0]) and (cmpiBin[0]) != n1[0]):
                    ov = "1"
                    sr[28] = ov
                else:
                    sr[28] = "0"

                if cmpi == 0:
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
                
                if rZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))
                    listaRegisDEC[rZ] = 0
                else:
                    listaRegistradores[rZ] = listaRegistradores[rZ]
                    listaRegisDEC[rZ] = listaRegisDEC[rZ]
                
                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorX},{num2}              	SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "010100":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "muli"
                rZ = int(opZ,2)
                rX = int(opX,2)
                if imed[0] == "1":
                    imed = complementa2(imed)
                    im = int(imed,2) * -1
                else:
                    im = int(imed,2)
                
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]

                num1 = listaRegisDEC[rX]
                num2 = im
                n1 = (completaZeroBin(bin(num1).strip("-")[2:]))
                if num2 < 0:
                    n2 = (completaZeroBin(((bin(num2).strip("-")[2:]))))
                else:
                    n2 = complementa2(completaZeroBin(((bin(num2).strip("-")[2:]))))
                
                multiplicacao = num1 * num2
                multBin = completaZeroBin64((bin(int(listaRegistradores[rX],16)*int(imed,2)).strip("-")[2:]))
                if multiplicacao > 0:
                    multBin = complementa2(multBin)

                variavelHexa = ((completaZeroHexa(hex(int(multBin,2)))))
                if len(variavelHexa)>10:
                    variavelHexa = ("0x"+(completaZeroHexa(hex(int(multBin,2))))[10:])
                listaRegistradores[rZ] = variavelHexa
                listaRegisDEC[rZ] = multiplicacao
                
                if int(multBin[:33],2) != 0:
                    ov = "1"
                    sr[28] = ov
                else:
                    sr[28] = "0"
                if multiplicacao == 0 :
                    zn = "1"
                    sr[25] = zn
                else:
                    sr[25] = "0"
               
                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorZ},{registradorX},{im}         	{registradorZ.upper()}={registradorX.upper()}*{tX(completaZeroHexa(hex(int(n2,2))).upper())}={tX(variavelHexa.upper())}, SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "010101":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "divi"
                rZ = int(opZ,2)
                rX = int(opX,2)
                if imed[0] == "1":
                    imed = complementa2(imed)
                    im = int(imed,2) * -1
                else:
                    im = int(imed,2)
                
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]

                num1 = listaRegisDEC[rX]
                num2 = im
                n1 = (completaZeroBin(bin(num1).strip("-")[2:]))
                n2 = (completaZeroBin(bin(num2).strip("-")[2:]))
                if n1[0] == "1":
                    n1 = complementa2(completaZero(bin(listaRegisDEC[rX]).strip("-")[2:]))
                    
                if n2[0] == "1":
                    n2 = (completaZero(imed))
                
                if num2 == 0:
                    zd = "1"
                    sr[26] = zd
                else:
                    sr[26] = "0"
                
                if num2 < 0:
                    divHex = complementa2(completaZero(bin(abs(num2))))
                    divHex = completaZeroHexa(hex(int(divHex,2)))
                elif num2 == 0:
                    divHex = completaZeroHexa(hex(0))
                    num2 = 1
                else:
                    divHex = completaZeroHexa(hex(num2))
                        
                divisaoNormal = int((num1/num2))
                if im == 0:
                    divisaoNormal = 4
                    dvn = "0x00000004"
                elif divisaoNormal < 0:
                    dvn = complementa2(completaZero(bin(abs(divisaoNormal)).strip("-")[2:]))
                    dvn = completaZeroHexa(hex(int(dvn,2)))
                else:
                    dvn = completaZeroHexa(hex(divisaoNormal))
                
                variavelHEXA = tX(dvn.upper())
                listaRegistradores[rZ] = variavelHEXA
                listaRegisDEC[rZ] = divisaoNormal
                if registradorZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))                    
                    listaRegisDEC[rZ] = 0
                    
                if (listaRegisDEC[rZ] == 0) or (dvn == "0x00000004"):
                    zn = '1'
                    sr[25] = zn
                else:
                    sr[25] = "0"
                sr[28] = "0"

                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorZ},{registradorX},{im:<10}{registradorZ.upper()}={registradorX.upper()}/{tX(divHex.upper())}={variavelHEXA}, SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "010110":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "modi"
                rZ = int(opZ,2)
                rX = int(opX,2)
                if imed[0] == "1":
                    imed = complementa2(imed)
                    im = int(imed,2) * -1
                else:
                    im = int(imed,2)
                
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]

                num1 = listaRegisDEC[rX]
                num2 = im
                n1 = (completaZeroBin(bin(num1).strip("-")[2:]))
                n2 = (completaZeroBin(bin(num2).strip("-")[2:]))
                if n1[0] == "1":
                    n1 = complementa2(completaZero(bin(listaRegisDEC[rX]).strip("-")[2:]))
                    
                if n2[0] == "1":
                    n2 = (completaZero(imed))
                    
                
                if num2 == 0:
                    zd = "1"
                    sr[26] = zd
                    num2 = 1
                else:
                    sr[26] = "0"
                
                            
                divisaoNormal=((abs(num1)%abs(num2)))
                if num2 < 0:
                    divHex = complementa2(completaZero(bin(abs(num2))))
                    divHex = tX(completaZeroHexa(hex(int(divHex,2)))).upper()
                else:
                    divHex = completaZeroHexa(hex(num2))
                if (num1 < 0) or (num2<0):
                    divisaoNormal = divisaoNormal * -1
                if divisaoNormal < 0:
                    dvn = complementa2(completaZero(bin(abs(divisaoNormal)).strip("-")[2:]))
                    dvn = completaZeroHexa(hex(int(dvn,2)))
                else:
                    dvn = completaZeroHexa(hex(divisaoNormal))
                variavelHEXA = tX(dvn.upper())
                listaRegistradores[rZ] = variavelHEXA
                listaRegisDEC[rZ] = divisaoNormal
                if registradorZ == 0:
                    listaRegistradores[rZ] = completaZeroHexa(hex(0))                    
                    listaRegisDEC[rZ] = 0
                    
                if (listaRegisDEC[rZ] == 0):
                    zn = '1'
                    sr[25] = zn
                else:
                    sr[25] = "0"
                if listaRegistradores[L4] != "0x00000000":
                    sr[28] = "0"

                srHEXA = tX(completaZeroHexa(hex(int("0b"+"".join(sr),2))).upper())
                listaRegistradores[31] = srHEXA
                imprimir = f"   {instrucao} {registradorZ},{registradorX},{num2:<10}{registradorZ.upper()}={tX(registradorX.upper())}%{tX(divHex.upper())}={variavelHEXA}, SR={srHEXA}"
                arqOutput.write(pc+":"+imprimir+"\n")
        
            elif operacao == "011000":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "l8"
                rZ = int(opZ,2)
                rX = int(opX,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                i = int(imed,2)
                if ((listaRegisDEC[rX] + i)//4) != 0:
                    parte = ((listaRegisDEC[rX] + i)%4)
                    if parte == 0:
                        listaRegistradores[rZ] = (mem[(listaRegisDEC[rX] + i)//4])[:4]
                    elif parte == 1:
                        listaRegistradores[rZ] = "0x"+(mem[(listaRegisDEC[rX] + i)//4])[4:6]
                    elif parte == 2:
                        listaRegistradores[rZ] = "0x"+(mem[(listaRegisDEC[rX] + i)//4])[6:8]
                    elif parte == 3:
                        listaRegistradores[rZ] = "0x"+(mem[(listaRegisDEC[rX] + i)//4])[8:]
                    else:    
                        listaRegistradores[rZ] = (mem[(listaRegisDEC[rX] + i)//4])[:4]
                listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)
                end = tX(completaZeroHexa(hex((listaRegisDEC[rX] + i))).upper())
                valor = completaZeroHexa8(listaRegistradores[rZ])
                imprimir = f"   {instrucao} {registradorZ},[{registradorX}+{i}]           	{registradorZ.upper()}=MEM[{end}]={valor}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "011001":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "l16"
                rZ = int(opZ,2)
                rX = int(opX,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                i = int(imed,2)
                if ((listaRegisDEC[rX] + i)//4) != 0:
                    parte = ((listaRegisDEC[rX] + i)%2)
                    if parte == 0:
                        listaRegistradores[rZ] = (mem[((listaRegisDEC[rX] + i))//2])[:6]
                    elif parte == 1:
                        listaRegistradores[rZ] = "0x"+(mem[(listaRegisDEC[rX] + i)//2])[6:]
                    else:    
                        listaRegistradores[rZ] = (mem[(listaRegisDEC[rX] + i)//2])[:4]
                listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)
                end = tX(completaZeroHexa(hex((listaRegisDEC[rX] + i)<<1)).upper())
                valor = (listaRegistradores[rZ])         
                imprimir = f"   {instrucao} {registradorZ},[{registradorX}+{i}]           	{registradorZ.upper()}=MEM[{end}]={valor}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "011010":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "l32"
                rZ = int(opZ,2)
                rX = int(opX,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                i = int(imed,2)
                listaRegistradores[rZ] = mem[((listaRegisDEC[rX]+i)<<2)//4]
                listaRegisDEC[rZ] = int(listaRegistradores[rZ],16)
                end = tX(completaZeroHexa(hex((listaRegisDEC[rX] + i)<<2)).upper())
                valor = (listaRegistradores[rZ])                
                imprimir = f"   {instrucao} {registradorZ},[{registradorX}+{i}]           	{registradorZ.upper()}=MEM[{end}]={valor}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "011011":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "s8"
                rZ = int(opZ,2)
                rX = int(opX,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                i = int(imed,2)
                mem[(listaRegisDEC[rX] + i)] = listaRegistradores[rZ]
                end = tX((completaZeroHexa(hex(listaRegisDEC[rX] + i))).upper())
                valor = completaZeroHexa8(mem[int(end,16)])               
                imprimir = f"   {instrucao} [{registradorX}+{i}],{registradorZ}         	MEM[{end}]={registradorZ.upper()}={valor}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "011100":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "s16"
                rZ = int(opZ,2)
                rX = int(opX,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                i = int(imed,2)
                mem[((listaRegisDEC[rX] + i)<<1)] = listaRegistradores[rZ]
                end = tX((completaZeroHexa(hex((listaRegisDEC[rX] + i)<<1))).upper())
                valor = completaZeroHexa16(mem[int(end,16)])
                imprimir = f"   {instrucao} [{registradorX}+{i}],{registradorZ}         	MEM[{end}]={registradorZ.upper()}={valor}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "011101":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "s32"
                rZ = int(opZ,2)
                rX = int(opX,2)
                registradorZ = regisEsp[rZ]
                registradorX = regisEsp[rX]
                i = int(imed,2)
                mem[((listaRegisDEC[rX] + i)<<2)] = listaRegistradores[rZ]
                end = tX((completaZeroHexa(hex((listaRegisDEC[rX] + i)<<2))).upper())
                valor = completaZeroHexa(mem[int(end,16)])
                imprimir = f"   {instrucao} [{registradorX}+{i}],{registradorZ}           	MEM[{end}]={registradorZ.upper()}={valor}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
            elif operacao == "011110":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "call"
                variavel = int(completaZeroBin((imed)),2)
                rX = int(opX,2)
                registradorX = regisEsp[rX]
                if imed[0] == "1":
                    variavel = variavel * -1
                else:
                    variavel = variavel
                
                pc4 = tX(completaZeroHexa(hex(proxPC+4)).upper())
                mem[sp] = pc4
                binario[sp] = binario[((proxPC+4)//4)]
                pulo = completaZeroHexa(hex(int(listaRegisDEC[rX] + variavel)*4))
                proxIns = binario[variavel+(listaRegisDEC[rX])]
                imprimir = f"   {instrucao} [{registradorX}+{variavel}]             	PC={tX(completaZeroHexa(hex(int(pulo,16))).upper())},MEM[{tX(listaRegistradores[30].upper())}]={pc4}"
                arqOutput.write(pc+":"+imprimir+"\n")
                sp = sp - 4
                listaRegistradores[30] = completaZeroHexa(hex(sp))
                listaRegisDEC[30] = sp


            elif operacao == "011111":
                listaRegistradores[28] = completaZeroHexa(hex(int(c,2)))
                listaRegisDEC[28] = int(c,2)
                listaRegistradores[29] = pc
                listaRegisDEC[29] = int(pc,16)
                instrucao = "ret"
                sp= sp + 4
                listaRegistradores[30] = completaZeroHexa(hex(sp))
                listaRegisDEC[30] = sp
                pulo = pc4
                proxPC = int(pulo,16) 
                proxIns = binario[sp]
                imprimir = f"   {instrucao}                      	PC=MEM[{tX(listaRegistradores[30].upper())}]={tX(pc4.upper())}"
                arqOutput.write(pc+":"+imprimir+"\n")
            
    if (variavel != 0) and proxIns == c:
        proxPC = int(pulo,16)
        proxIns = binario[(proxPC//4)]
        
    elif (proxIns != c) and instrucao == "ret":
        proxPC = proxPC
        proxIns = binario[sp]
        
    elif (proxIns != c) and instrucao == "call":
        proxPC = int(pulo,16)
        proxIns = proxIns
        
    else:
        proxPC = proxPC +4
        proxIns = binario[(proxPC//4)]

    variavel = 0
    
arqOutput.write("[END OF SIMULATION]")
arqInput.close()
arqOutput.close()
