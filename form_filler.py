#! python3
"""Automatic Form Filler

This script allows the user to automatically fill a contact
information generic form.

This tool is for learning purposes only and as such it is
demonstrated with four different hardcoded entries. In a real world scenario,
this data might come from a spreadsheet, a plaintext file, or a
website.

This script requires that `PyAutoGUI` be installed within the Python
environment you are running the script in.
"""

import pyautogui, time

submit_another_link = (1701, 404)

form_data = [{'name': 'Abby Benton', 'email': 'a_benton@example.com',
              'address': '93 Ivy Road Winston Salem, NC 27103',
              'phone_number': '(557) 621-8508', 'hub_city': 'Raleigh',
              'survey_question': 1},
             {'name': 'Todd Blackburn', 'email': 't_blackburn@example.com',
              'address': '8378 Colonial Dr. Texarkana, TX 75501',
              'phone_number': '(418) 797-9189', 'hub_city': 'Plano',
              'survey_question': 4},
             {'name': 'Suellen Michael', 'email': 's_micheal@example.com',
              'address': '283 Oakwood St. Dallas, TX 75228',
              'phone_number': '(779) 528-7693', 'hub_city': 'Plano',
              'survey_question': 2},
             {'name': 'Jonty Reeve', 'email': 'j_reeve@example.com',
              'address': '16 W. Bishop Ave. Nashville, TN 76112',
              'phone_number': '(942) 942-3140', 'hub_city': 'Nashville',
              'survey_question': 3}]

# Pause variable to wait half a second after each function call.
pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

# Iterates over each of the dictionaries in the form_data list
for person in form_data:
    # Give the user a chance to kill the script.
    print('>>> 5-SECOND PAUSE TO LET THE USER PRESS CTRL-C <<<')
    time.sleep(5)

    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t', '\t', '\t', '\t'])

    # Fill out the name field.
    pyautogui.write(person['name'] + '\t')

    # Fill out the email field.
    pyautogui.write(person['email'] + '\t')

    # Fill out address field.
    pyautogui.write(person['address'] + '\t')

    # Fill out the phone number field.
    pyautogui.write(person['phone_number'] + '\t')

    # Fill out the hub city field.
    if person['hub_city'] == 'Plano':
        pyautogui.write(['down', ' ', '\t'], 0.5)
    elif person['hub_city'] == 'Atlanta':
        pyautogui.write(['down', 'down', ' ', '\t'], 0.5)
    elif person['hub_city'] == 'Nashville':
        pyautogui.write(['down', 'down', 'down', ' ', '\t'], 0.5)
    elif person['hub_city'] == 'Raleigh':
        pyautogui.write(['down', 'down', 'down', 'down', ' ', '\t'], 0.5)
    elif person['hub_city'] == 'Chicago':
        pyautogui.write(['down', 'down', 'down', 'down', 'down', ' ', '\t'], 0.5)

    # Fill out the survey field.
    if person['survey_question'] == 1:
        pyautogui.write([' ', '\t'], 0.5)
    elif person['survey_question'] == 2:
        pyautogui.write(['right', '\t'], 0.5)
    elif person['survey_question'] == 3:
        pyautogui.write(['right', 'right', '\t'], 0.5)
    elif person['survey_question'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t'], 0.5)
    elif person['survey_question'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t'], 0.5)

    # Skip over "clear selection" button
    pyautogui.write(['\t'], 0.5)

    # "Click" submit button by pressing enter.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)

    # Click the submit another response link.
    pyautogui.click(submit_another_link[0], submit_another_link[1])
