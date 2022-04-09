"""Pour Julie B. et Corday T. (pull bleu) et toutes les autres personnes avec des couleurs différentes de pull
2022.04.09 tentative de débuter avec du python et des paramètres en ligne de commande
AVANT tout il faut installer argparse
Donc dans un terminal : 

cd C:\MODULE122_BASH\python_vigenere
pip3 install --upgrade pip
pip3 install argparse

et après dans le terminal
python main.py Julie 24

https://zetcode.com/python/argparse/"""


import argparse

# positional args

parser = argparse.ArgumentParser()
   
parser.add_argument('name')
parser.add_argument('age')

args = parser.parse_args()

print(f'{args.name} is {args.age} years old')