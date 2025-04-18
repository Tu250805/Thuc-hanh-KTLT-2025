print('sinh viên Đậu Đức Tú')
print('Msv 235752020710009')

class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

# Ví dụ sử dụng
input_str = 'hello .py'
manipulator = StringManipulator(input_str)
output_str = manipulator.reverse_words()
print(output_str)
