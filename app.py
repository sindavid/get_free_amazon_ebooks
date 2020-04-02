from service.abstract_selenium import AbstractSelenium


if __name__ == '__main__':
    import sys
    try:
        if sys.argv[1] == "0":
            hidden = True
        elif sys.argv[1] == "1":
            hidden = False
        webcrawling = AbstractSelenium(hidden)
        webcrawling.start_process()
    except IndexError:
        print("É necessário informar todos os argumentos\n"
              "0 para iniciar sem interface grafica\n"
              "1 para iniciar com interface grafica\n"
              "Por exemplo: 'python app.py 0'")
