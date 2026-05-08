def print_separator(char="=", length=40):
    print(char * length)

def print_header(title):
    print_separator()
    print(f"  {title}")
    print_separator()

def get_input(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("  ⚠️  Không được để trống. Vui lòng nhập lại.")

def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val is not None and value < min_val:
                print(f"  ⚠️  Vui lòng nhập số >= {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"  ⚠️  Vui lòng nhập số <= {max_val}.")
                continue
            return value
        except ValueError:
            print("  ⚠️  Vui lòng nhập một số hợp lệ.")

def confirm(prompt):
    answer = input(f"{prompt} (y/n): ").strip().lower()
    return answer == 'y'
