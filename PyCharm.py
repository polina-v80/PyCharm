def testfunction():
    def innerfunction():
        print("Я в области видимости функции testfunction")

    innerfunction()


testfunction()

# Если вызвать innerfunction вне функции testfunction, будет ошибка
# innerfunction()