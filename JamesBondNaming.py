from win32com.client import Dispatch

speaker = Dispatch("SAPI.spVoice")

name = str(input("Adınızı giriniz: "))

change = name.split(" ")

liste = list()

liste.append( change [ ( len ( change ) - 1 ) ] )
liste.append( " ".join(change) )

print(liste)

print( f"{liste[0]} , {liste[1]}" )

speaker.Speak(liste)