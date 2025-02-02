class Utils:
    @staticmethod
    def validate_digit_input(text):
        # Разрешаем только цифры
        return text.isdigit() or text == ""
