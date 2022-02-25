def main():
    seconds = int(
        input("Por favor, entre com o número de segundos que deseja converter: "))

    hours = seconds // 3600
    seconds_leftover = seconds % 3600
    minuts = seconds_leftover // 60
    seconds_leftover_final = seconds_leftover % 60

    days = hours // 24
    hours_leftover = hours % 24

    print(f"{days} dias, {hours_leftover} horas, {minuts} minutos e {seconds_leftover_final} segundos. ")


main()
