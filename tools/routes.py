from enum import Enum


class AppRoute(str, Enum):
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"

    DASHBOARD = "./#/dashboard"

    COURSES = "./#/courses"
    COURSES_CREATE = "./#/courses/create"
