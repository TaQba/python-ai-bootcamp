
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def calc(operation, a=0, b=0):
    logging.debug("Parameter pierwszy {} w funkcji calc()".format(operation))

    if operation not in [1, 2, 3, 4]:
       logging.info("Operacja niedozwolona!")

    if operation == 1:
        logging.debug("Dodaje {} + {}".format(a, b))
        return a+b
    elif operation == 2:
        logging.debug("Odejmuje {} - {}".format(a, b))
        return a-b
    elif operation == 2:
        logging.debug("Mnoże {} * {}".format(a, b))
        return a*b
    elif operation == 2:
        if b == 0:
            logging.info("Delenie przez zero niedozwolone!")
        else:
            logging.debug("Dziele {} / {}".format(a, b))
            return a/b

if __name__ == "__main__":
    logging.debug("Start")


    print("Kalkulator")
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    logging.info("Parameter dzialanie is {}" .format(operation))

    a = input("Podaj składnik 1: ")
    logging.info("Parameter pierwszy {}".format(a))

    b = input("Podaj składnik 2: ")
    logging.info("Parameter drugi is {}".format(b))

    print("Wynik to {}" .format(calc(int(operation), float(a),float(b))))
    logging.debug("Koniec")
