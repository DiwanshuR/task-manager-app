from datetime import datetime, timezone


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_as_utc__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_as_utc__mutmut)
def as_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def x_as_utc__mutmut_orig(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def x_as_utc__mutmut_1(value: datetime) -> datetime:
    if value.tzinfo is not None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def x_as_utc__mutmut_2(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=None)
    return value.astimezone(timezone.utc)


def x_as_utc__mutmut_3(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(None)

mutants_x_as_utc__mutmut['_mutmut_orig'] = x_as_utc__mutmut_orig # type: ignore # mutmut generated
mutants_x_as_utc__mutmut['x_as_utc__mutmut_1'] = x_as_utc__mutmut_1 # type: ignore # mutmut generated
mutants_x_as_utc__mutmut['x_as_utc__mutmut_2'] = x_as_utc__mutmut_2 # type: ignore # mutmut generated
mutants_x_as_utc__mutmut['x_as_utc__mutmut_3'] = x_as_utc__mutmut_3 # type: ignore # mutmut generated
