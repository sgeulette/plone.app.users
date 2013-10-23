import doctest
from unittest import TestSuite
from Testing.ZopeTestCase import FunctionalDocFileSuite
from Products.PloneTestCase.PloneTestCase import setupPloneSite
from plone.app.users.tests.base import TestCase


setupPloneSite()
OPTIONFLAGS = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


def test_suite():
    tests = ['flexible_user_registration.txt',
             'forms_navigationroot.txt',
             'registration_forms.txt',
             'userdata.txt',
             'userdata_prefs_user_details.txt',
             'personal_preferences.txt',
             'personal_preferences_prefs_user_details.txt',
             'password.txt',
             'email_login.txt',
             '../vocabularies.py'
             ]
    suite = TestSuite()
    for test in tests:
        suite.addTest(FunctionalDocFileSuite(
            test,
            optionflags=OPTIONFLAGS,
            package="plone.app.users.tests",
            test_class=TestCase
        ))
    return suite
