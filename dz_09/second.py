class TextProcessor:

    marks = [",", ":", "-", "!", "?", "==", ";", '.', '/', '\\']
    symbol = ""

    def get_clean_string(self, text):
        for i in self.marks:
            text = text.replace(i, " ")
        return text

    def __is_punktiantian(self):
        if self.symbol in self.marks:
            return True
        else:
            return False

a = TextProcessor()
a.symbol = "."
print(a.get_clean_string("I don't know: if I can, or I cannot - who knows, tell me?"))
# print(a._TextProcessor__is_punktiantian())

# ДАЛІ Я НЕ ЗНАЙШОВ СПОСОБУ ВИРІШИТИ ЗАВДАННЯ
# class TextLoader(TextProcessor):
#
#     def __init__(self, text_processor, clean_string):
#         self.__text_processor = TextProcessor
#         self.__clean_string = clean_string
#
#
#     def set_clean_text(self):
#         self.__text_processor = __clean_string
#         return __clean_string
#
#
# b = TextLoader()