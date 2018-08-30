from CodeChallengeJune18 import parents, activities


def nice_print(message, data=None):
    """
    Print a well formatted report
    :param message: A message string to print to the terminal
    :param data: A list of dictionaries
    :return: The main message
    """
    if message is not '':
        print(message)
        return message

    for item in data:
        temp_message = '\n'
        temp_message += f'Hi {item.get("parent_name")}\n'

        list_activities = '\n'.join(item.get('activities'))

        if not item.get('child_name'):
            temp_message += 'Sorry, no child name found!\n\n'
        elif not item.get('age'):
            temp_message += f'Sorry, no age found for {item.get("child_name")}!\n\n'
        elif not list_activities:
            temp_message += f'Sorry, no activity for {item.get("child_name")}!\n\n'
        else:
            temp_message += f'Here\'s a list of activities for {item.get("child_name")}:\n\n'
            temp_message += f'{list_activities}\n\n'

        temp_message += 'Curriculum complete!\n'
        temp_message += '\n'

        message += temp_message

    print(message)
    return message


def get_activities(parents_dict, activities_list):
    """
    Get activities for a parent's child
    :param parents_dict: Dictionary of parents anc child details
    :param activities_list: A list of activities per age
    :return: A list of dictionaries with parents and child's activities
    """
    child_data = {}
    result = []

    # Create a mapping of age to activities
    for activity in activities_list:
        child_data[activity['age']] = activity['activity']

    for parent in parents_dict:
        # Get activities from child_data or an empty list
        child_details = parents_dict.get(parent)

        temp = {
            'parent_name': parent,
            'child_name': child_details.get('childName'),
            'age': child_details.get('age'),
            'activities': child_data.get(child_details.get('age'), [])
        }

        result.append(temp)

    return result


def check_binary(user_input):
    try:
        integer_input = int(user_input)
        if integer_input in [0, 1]:
            return True

    except ValueError:
        pass

    return False


def check_validity(user_input, type_fn=int):
    try:
        if type_fn is int:
            return int(user_input) > 0

        if type_fn(user_input):
            return True

        return False

    except ValueError:
        return False


def prompter(message, error, type_fn):
    user_input = input(message)
    is_valid_integer = check_validity(user_input, type_fn)

    if not is_valid_integer:
        nice_print(error)
        return prompter(message, error, type_fn)

    if type_fn == check_binary and int(user_input) == 0:
        return False

    return user_input


def add_parent(parents_dict):
    opt_in = 'Would you like to add a parent?\n'
    opt_in += 'Enter 0 for No, or 1 for Yes: '
    opt_in_error = 'Value should either be 0 or 1\n'

    # User enters 0
    if not prompter(opt_in, opt_in_error, type_fn=check_binary):
        return

    parent_name = input('Please enter a parent name: ')
    child_name = input (f'Please enter {parent_name}\'s child\'s name: ')

    # Validate child's age
    age_message = f'Please enter {child_name}\'s age: '
    age_error = 'Value should be a positive integer.\n'
    child_age = prompter(age_message, age_error, type_fn=int)

    parents_dict[parent_name] = {
        'childName': child_name,
        'age': int(child_age)
    }
    nice_print(parents_dict)

    # Add another parent...
    add_parent(parents_dict)


def add_activity(activities_list):
    opt_in = 'Would you like to add an activity?\n'
    opt_in += 'Enter 0 for No, or 1 for Yes: '
    opt_in_error = 'Value should either be 0 or 1'

    # User enters 0
    if not prompter(opt_in, opt_in_error, type_fn=check_binary):
        return

    # Validate activity's age
    age_message = 'Please enter activity age: '
    age_error = 'Value should be a positive integer.\n'
    activity_age = prompter(age_message, age_error, type_fn=int)

    activity = input(f'Please enter activity for age {activity_age}: ')

    # Check if activity age exists in current activities
    age_or_none = next(
        (ind for ind, activity in enumerate(activities_list) if activity.get('age') == int(activity_age)), None
    )

    # If it doesn't...
    if age_or_none is None:
        activity_obj = {
            'age': activity_age,
            'activity': [activity]
        }

        # Add activity object to list of activities
        activities_list.append(activity_obj)
    else:
        activities_list[age_or_none]['activity'].append(activity)

    nice_print(activities_list)

    # Add another activity...
    add_activity(activities_list)


def sentry():
    # User add's a parent
    add_parent(parents)

    # User add's an activity
    add_activity(activities)

    # Get all the activities per child
    child_activities = get_activities(parents, activities)

    # Print nicely formatted info to the terminal
    nice_print('', data=child_activities)


if __name__ == '__main__':
    sentry()
