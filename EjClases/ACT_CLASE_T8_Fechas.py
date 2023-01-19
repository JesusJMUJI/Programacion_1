class Fecha:
    def __init__(self, dia, mes, año):
        self.__dia = dia
        self.__mes = mes
        self.__año = año

    def __str__(self) -> str:
        return '{0}/{1}/{2}'.format(self.__dia, self.__mes, self.__año)

    def __eq__(self, fecha2):
        return self.__dia == fecha2.__dia and \
            self.__mes == fecha2.__dia and \
            self.__año == fecha2.__año

    def __lt__ (self, fecha2):
        if self.__año < fecha2.