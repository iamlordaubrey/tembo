from unittest import TestCase, main, mock

import solution
from CodeChallengeJune18 import parents, activities


class TestChildActivities(TestCase):
    def test_activities_for_child(self):
        parent_name = 'Henry'
        child_name = 'Calvin'
        activity01 = 'Go outside and feel surfaces.'
        activity02 = 'Point and name objects.'

        # Get a list of dictionaries containing parent, child and activities
        children_activities = solution.get_activities(parents, activities)

        for child in children_activities:
            if child.get('parent_name') == parent_name:
                self.assertIn(child_name, child.get('child_name'))
                self.assertIn(activity01, child.get('activities'))
                self.assertIn(activity02, child.get('activities'))

    def test_edge_case_for_child(self):
        test_message = 'Sorry, no child name found!'
        data = [{
            'parent_name': 'Milo',
            'child_name': None,
            'age': None,
            'activities': []
        }]

        formatted_message = solution.nice_print('', data)
        self.assertIn(test_message, formatted_message)


class TestAddParent(TestCase):
    @mock.patch('solution.input', create=True)
    def test_user_adds_parent(self, mocked_input):
        parent_dict = {'Henry': {'childName': 'Calvin', 'age': 1}}
        mocked_input.side_effect = [1, 'Abraham', 'Isaac', 2, 0]
        solution.add_parent(parent_dict)
        self.assertIsNotNone(parent_dict.get('Abraham'))
        self.assertEqual({'childName': 'Isaac', 'age': 2}, parent_dict.get('Abraham'))
        self.assertEqual(len(parent_dict), 2)


class TestAddActivity(TestCase):
    @mock.patch('solution.input', create=True)
    def test_user_adds_activity(self, mocked_input):
        activities_list = [{
            'age': 1,
            'activity': [
                'Go outside and feel surfaces.',
                'Try singing a song together.',
                'Point and name objects.'
            ]
        }]
        mocked_input.side_effect = [1, 1, 'Learn ABC.', 0]
        solution.add_activity(activities_list)
        for item in activities_list:
            self.assertIsNotNone(item['activity'])
            self.assertIn('Learn ABC.', item['activity'])
            self.assertEqual(len(activities_list), 1)
            self.assertEqual(len(item['activity']), 4)


if __name__ == '__main__':
    main()
