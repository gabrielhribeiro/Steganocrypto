#!/usr/bin/python
# -*- coding: utf-8 -*-

#Importa funcoes e algumas utilidades da biblioteca tkinter
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from tkFileDialog import *
from PIL import Image
import aes #criptografia
import stepic #esteganografia
import tkSimpleDialog
import tkMessageBox

#-------------------------------------\funcoes\---------------------------------------------
def but1(): print('Buttonon was pushed')
def Save(): tkinter.filedialog.asksaveasfile()		#Define Funcao
def Quit(): root.destroy()				#Define Funcao
def Help(): tkinter.messagebox()

#-------------------------\funcao Criptografia\--------------------------------
def Cripto():
	a_texto = askopenfilename(filetypes=[("Arquivos de Texto","*.txt")])
	f = open(a_texto)
	plaintext = f.read()
	print plaintext	
	
	blocksize = 256 #128, 192, 256
 	key = tkSimpleDialog.askstring('Criptografia AES', 'Digite a chave:')
	crypted = aes.encrypt( plaintext, key, blocksize ) 
	print 'o Texto Criptografado:'
	print crypted

	return crypted

#---------------------------\descriptografia\---------------------------------

def Descripto():
	s = Stegana()
	blocksize = 256
	key = tkSimpleDialog.askstring('Criptografia AES', 'Digite a chave:')
	txt_descripto = aes.decrypt(s  , key, blocksize )

	
	salva_text = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
	salva_text.write(txt_descripto)

	print 'O texto Descriptografado'
	print txt_descripto
	return Descripto

#-------------------------\funções Esteganografia\----------------------------

def Stegano():
	img_stegano = askopenfilename(filetypes=[("Arquivo PNG","*.png")])
	im = Image.open(img_stegano)
	i = Cripto()
	im2 = stepic.encode(im, i)
	print 'Imagem foi salva'
	salva_foto = asksaveasfile(mode='w', defaultextension=".png")
	im2.save(salva_foto)
	
#----------------------------\Steganalise\-----------------------------------       

def Stegana():

       	img_stegana = askopenfilename(filetypes=[("Imagem PNG","*.png")])
        im = Image.open(img_stegana)
        s = stepic.decode(im)
	data = s.decode()
	print'Imagem Steganalise' 
	print s
	return data	
#------------------------------------INTERFACE GRAFICA------------------------------------------

#---------------------\cria janela root e menus principais-topo\--------------------------------

root = Tk() 						#cria tabela grafica geral
menubar = Menu(root)					#cria menu na tabela root
root.config(menu=menubar)				# PESQUISAR
root.title('Esteganocriptografia')			#configra titulo da janela


filemenu = Menu(menubar)				#cria aba de menu
filemenu2 = Menu(menubar)				#cria aba de menu
filemenu3 = Menu(menubar)				#cria aba de menu
filemenu4 = Menu(menubar)

#Layout--------------------------------/Cabeçalho/-----------------------------------------------

Label (root, text="Esteganografia").grid(row=0, padx= 10, pady=10)

#--------------------------------------------------/botoes/-------------------------------------

#Layout ----------------- inferior Esteganalise------------
 

#---------------\Escolher imagem p cripto\---------------------------

Label (root, text='Steganocripto:').grid(row = 1, padx=10, pady=10)
botao_cript = Button(root, text = 'Stegano', height=1, width=14)
botao_cript.grid(row = 1, column = 2, padx = 10, pady=10 )
botao_cript.configure(command = Stegano)

#cabeçalho inferior
Label (root, text="Esteganalise").grid(row=2, padx= 8, pady=1)

#---------------\Escolha imagem p ddescripto\-----------------------------

Label (root, text='Descriptostegano:').grid(row = 3, padx=10, pady=10)
botao_cript = Button(root, text = 'Descripto', height=1, width=14)
botao_cript.grid(row = 3, column = 2, padx = 10, pady=10 )
botao_cript.configure(command = Descripto)



#----------------------------Configuração das opcoes d---------------------------------------#
menubar.add_cascade(label='Arquivos', menu=filemenu)	#nomeia menu 1
menubar.add_cascade(label='Opções', menu=filemenu2)	#nomeia menu 2
menubar.add_cascade(label='Sobre', menu=filemenu3)	#nomeia menu 3
menubar.add_cascade(label='Ajuda', menu=filemenu4)	#nomeia menu 4


#------------------------------------\Atribuiçoes e configuracoes da janela\-------------------
filemenu.add_command(label='Abrir...', command=Cripto)

filemenu.add_command(label='Salvar como...', command=Cripto)

filemenu2.add_command(label='criptografia')

filemenu.add_separator()

filemenu2.add_command(label="esteganografia")

filemenu.add_command(label='Sair', command=Quit)

filemenu3.add_command(label='Sobre')

root.mainloop()   #loop da janela
