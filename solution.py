from CodeChallengeJune18 import parents, activities


def nice_print(data):
    """
    Print a well formatted report
    :param data: A list of dictionaries
    :return: The main message
    """
    main_message = ''

    for item in data:
        message = '\n'
        message += f'Hi {item.get("parent_name")}\n'

        list_activities = '\n'.join(item.get('activities'))

        if not item.get('child_name'):
            message += 'Sorry, no child name found!\n\n'
        elif not item.get('age'):
            message += f'Sorry, no age found for {item.get("child_name")}!\n\n'
        elif not list_activities:
            message += f'Sorry, no activity for {item.get("child_name")}!\n\n'
        else:
            message += f'Here\'s a list of activities for {item.get("child_name")}:\n\n'
            message += f'{list_activities}\n\n'

        message += 'Curriculum complete!\n'
        message += '\n'

        main_message += message

    print(main_message)
    return main_message


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


def sentry():
    child_activities = get_activities(parents, activities)
    nice_print(child_activities)


if __name__ == '__main__':
    sentry()
