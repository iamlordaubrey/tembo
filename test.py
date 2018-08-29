import unittest

import solution
from CodeChallengeJune18 import parents, activities


class TestChildActivities(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
