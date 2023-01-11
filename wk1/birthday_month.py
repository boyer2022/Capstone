from datetime import datetime

def main():
    # start program here
    name = input('What is your name: ')
    birth_month = input('What is your birthday month? ')
    current_month = get_current_month()
    if compare_case_insensitive(birth_month, current_month):
        print(f'It is your Happy Birthday month {name}!')
    else:
        print(f'I hope you have a Happy Birthday month in {birth_month.upper()}!')

def get_current_month():
    today = datetime.today()
    month_text = today.strftime('%B')
    return month_text

def compare_case_insensitive(st1, st2):
    return st1.lower() == st2.lower()

# Remember to call main function!
main()
print('End of program, Thank you')