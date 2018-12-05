from php import BaseCar


class CrashableCar(BaseCar):
    def __add__(self, other: 'CrashableCar') -> None:
        if isinstance(other, CrashableCar):
            raise CarAccident('Crash!')


class CarAccident(BaseException):
    pass


class GasCar(CrashableCar):
    def drive(self) -> str:
        return 'brrrum'


class DieselCar(CrashableCar):
    def drive(self) -> str:
        return 'pyr pyr pyr'
