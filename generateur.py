import random 
import string
# string.ascii_lowercase = alphabet miniscule
#string.ascii_uppercase = alphabet maj
#string.digit = 1-9
#string.punctuation = !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~

def build_charset(use_upper , use_digit, use_special):
   
    charset= string.ascii_lowercase
    
    if use_upper:
        charset= charset + string.ascii_uppercase
    
    if use_digit:
            charset = charset + string.digits
    
    if use_special:
            charset = charset + string.punctuation
    
    return charset
def generate_mdp(taille,charset):
      password = ""
      for i in range(i,taille):
            password += random.choice(charset)
      return password


def complexite_mdp(mdp):
      score = 0
      if len(mdp) >= 8 : 
            score+=1
      if len(mdp)>= 12 :
            score +=1
      if any (c in string.ascii_uppercase for c in mdp):
            score+=1
      if any (c in string.digits for c in mdp):
            score+=1
      if any (c in string.punctuation for c in mdp):
            score+=1

      if score <= 2:
            print("le mdp est Faible.")
      elif score == 3 or score == 4 :
            print("Le mdp est moyen.")
      else:
            print("Bravo,Le mdp est fort")
      return score     

def sauvegarder_mdp(mdp):
      with open("mdp_sauv.txt","a") as f:
            f.write(mdp+"\n")
            
def main():
      longueur = int(input("Longueur du mot de passe? :"))
      reponse = input("Inclure des maj? (o/n):")
      if reponse == "o":
            use_upper = True
      else:
            use_upper = False

      reponse = input("Inclure des chiffres? (o/n):")

      if reponse == "o":
            use_digit = True
      else:
            use_digit = False

      reponse = input("Inclure des caractere spéciaux ? (o/n):")

      if reponse == "o":
            use_special = True
      else:
            use_special = False

      charset =build_charset(use_upper,use_digit,use_special)
      mdp = generate_mdp(longueur,charset)
      sauvegarder_mdp(mdp)
      print("Mot de passe generer:",mdp)
      complexite_mdp(mdp)
main()