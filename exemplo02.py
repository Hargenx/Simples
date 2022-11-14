from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

def main():
    pessoa = Pessoa('Raphael', 38)
    print(pessoa)

if __name__ == "__main__":
    main()