def leiaDinheiro(text):
    while True:
        num = input(text).replace(',', '.').strip()
        if num.isalpha():
            print(f'\033[0;31mERRO! "{num}" não é válido!\033[m')
        else:
            break
        return float(num)
