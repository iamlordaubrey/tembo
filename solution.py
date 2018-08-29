from CodeChallengeJune18 import parents, activities


def nice_print(data):
    """
    Print a well formatted report
    :param data: A list of dictionaries
    :return: None
    """
    main_message = ''
    for item in data:
        list_activities = '\n'.join(item.get('activities'))

        message = '\n'
        message += f'Hi {item.get("parent_name")}\n'
        message += f'Here\'s a list of activities for {item.get("child_name")}:\n\n'
        message += f'{list_activities}\n\n'
        message += 'Curriculum complete!\n'
        message += '\n'

        main_message += message

    print(main_message)


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
