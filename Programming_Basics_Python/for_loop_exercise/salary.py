facebook_penalty = 150
instagram_penalty = 100
reddit_penalty = 50

number_of_tabs = int(input())
salary = float(input())

for tab in range(number_of_tabs):

    website_name = input()

    if website_name == 'Facebook':
        salary -= facebook_penalty

    elif website_name == 'Instagram':
        salary -= instagram_penalty

    elif website_name == 'Reddit':
        salary -= instagram_penalty

    if salary <= 0:
        print('You have lost your salary.')
        break

else:
    print(int(salary))
