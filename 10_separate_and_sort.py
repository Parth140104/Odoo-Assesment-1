def sort_letters_digits(s):
    letters = sorted([ch for ch in s if ch.isalpha()])
    digits = sorted([ch for ch in s if ch.isdigit()])
    return ''.join(letters + digits)

# Example usage
input_str = "B4A1D3"
output = sort_letters_digits(input_str)
print("Output:", output)
