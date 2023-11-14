#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Ian Alexander The Great", job = 'self.name = name'):
        if type(name) != str or name == '':
            print('Name must be string between 1 and 25 characters.')
        elif len(name) < 26:
            self.name = name.title()
        else:
            print('Name must be string between 1 and 25 characters.')

        if job not in APPROVED_JOBS:
            print('Job must be in list of approved jobs.')
        else:
            self.job = job

