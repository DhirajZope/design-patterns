# Builder pattern is a creational design pattern that lets you construct complex objects step by step.
# separating the construction process from the final representation.
from typing import Any, Self


class User:
    __slots__ = (
        "_username",
        "_password",
        "_email",
        "_fullname",
        "_age",
        "_is_verified",
    )

    def __init__(self, builder) -> None:
        object.__setattr__(self, "_username", builder._username)
        object.__setattr__(self, "_password", builder._password)
        object.__setattr__(self, "_email", builder._email)
        object.__setattr__(self, "_fullname", builder._fullname)
        object.__setattr__(self, "_age", builder._age)
        object.__setattr__(self, "_is_verified", builder._is_verified)

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("User is immutable")

    def __delattr__(self, name: str) -> None:
        raise AttributeError("User is immutable")

    class Builder:
        def __init__(self, username: str, password: str) -> None:
            self._username = username
            self._password = password
            self._email = None
            self._fullname = None
            self._age = None
            self._is_verified = False

        def age(self, age: int) -> Self:
            self._age = age
            return self

        def email(self, email: str) -> Self:
            self._email = email
            return self

        def fullname(self, fullname: str) -> Self:
            self._fullname = fullname
            return self

        def is_verified(self, is_verified: bool) -> Self:
            self._is_verified = is_verified
            return self

        def build(self) -> "User":
            return User(self)


# Driver code
user = (
    User.Builder("dhiraj", "dhiraj123")
    .fullname("Dhiraj Zope")
    .email("dhiraj@email.com")
    .age(29)
    .is_verified(True)
    .build()
)
