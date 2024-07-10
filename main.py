import rsa
import os

publicKey, privateKey = rsa.newkeys(2048)

def rsaEncript(frase):
    frase = rsa.encrypt(frase.encode(), publicKey)
    return frase

def rsaDecript(frase):
    frase = rsa.decrypt(frase, privateKey).decode()
    return frase


def morse(a):
  a = str(a)
  a = a.lower()
  caractere = {
      "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": " "
  }
  new_a = ''
  for letra in a:
      if letra in caractere:
          new_a += caractere[letra] + ' '
      else:
          new_a += letra + ' '
  a = new_a
  return a

def noMorse(a):
  a = str(a).lower()
  caractere = {
      ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", " ": ' ' 
  }
  morse_text = a.split(' ')
  new_a = ''
  for letra in morse_text:
      if letra in caractere:
          new_a += caractere[letra]
      else:
          new_a += letra
  a = new_a
  return a

print('Vamos criptografar!!');print()
sair = None

while True:
  message = input('Digite o que deseja criptografar = ').strip()
  if len(message) != 0:
      rsa_message = rsaEncript(message)
      morse_encript_message = morse(rsa_message)
      message_dec = noMorse(rsaDecript(rsa_message))
      print(morse_encript_message)
      decript_true = input('Deseja descriptografar? [ S para sim OU outra tecla para digitar novamente]')
      if decript_true.lower() == 's':
        print(f'A descriptografia: ', message)
      else:
          continue
      sair = input('Deseja sair? [Digite N para reiniciar ou outro caractere para sair]')
      if sair.lower() == 'n' or sair[0].lower() == 'n':
        print('O programa será reiniciado...')
        os.system('cls')
        continue
      elif len(sair) == "":
        print('Até a proxima!');break
      else:
        print("Não entendi, digite novamente.")
        continue
  else:
      print('O campo precisa ser preenchido. Digite novamente!')
      print()  
