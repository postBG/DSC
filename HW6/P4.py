class Calculator:
    def __init__(self):
        super().__init__()
        self._current_result = 0
        self._current_digits_buffer = []
        self._recent_operator = '+'

    def digit(self, num):
        self._current_digits_buffer.append(str(num))

    def plus(self):
        if len(self._current_digits_buffer) == 0:
            self._recent_operator = '+'
            return
        number = self._digit_buffer_to_digits_and_clear_buffer()
        self._do_calculation(number)
        self._recent_operator = '+'

    def minus(self):
        if len(self._current_digits_buffer) == 0:
            self._recent_operator = '-'
            return
        number = self._digit_buffer_to_digits_and_clear_buffer()
        self._do_calculation(number)
        self._recent_operator = '-'

    def clear(self):
        self._current_result = 0
        self._current_digits_buffer = []
        self._recent_operator = '+'

    def equal(self):
        number = self._digit_buffer_to_digits_and_clear_buffer()
        self._do_calculation(number)
        return self._current_result

    def _digit_buffer_to_digits_and_clear_buffer(self):
        current_number = int(''.join(self._current_digits_buffer))
        self._current_digits_buffer = []
        return current_number

    def _do_calculation(self, operand):
        if self._recent_operator == '+':
            self._current_result += operand
        else:
            self._current_result -= operand
