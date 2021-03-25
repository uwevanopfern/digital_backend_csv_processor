import pytest

from dsrs.models import DSR, Currency, Territory, Resource


@pytest.fixture(scope="function")
def add_dsr():
    def _add_dsr(path):
        currency = Currency.objects.create(
            name="Norwegian Krone", symbol="kr", code="NOK"
        )

        territory = Territory.objects.create(
            name="Norway", code_2="NO", code_3="NO", local_currency=currency
        )

        dsr = DSR.objects.create(
            path=path,
            period_start="2020-01-01 00:00:00",
            period_end="2020-01-01 00:00:00",
            territory=territory,
            currency=currency,
        )
        return dsr

    return _add_dsr


@pytest.fixture(scope="function")
def add_resource():
    def _add_resource():
        currency = Currency.objects.create(
            name="Norwegian Krone", symbol="kr", code="NOK"
        )

        territory = Territory.objects.create(
            name="Norway", code_2="NO", code_3="NO", local_currency=currency
        )
        DSR.objects.create(
            path="path",
            period_start="2020-01-01 00:00:00",
            period_end="2020-05-31 00:00:00",
            territory=territory,
            currency=currency,
        )

        dsr_object = DSR.objects.get(path="path")
        dsr = dsr_object.id
        resource = Resource.objects.create(
            dsp_id="ahjasdjahsjd",
            title="Pytest resource",
            artists="Michel tero",
            isrc="23423",
            usages=45545,
            revenue=45.2,
        )
        resource.dsrs.add(dsr)
        return resource

    return _add_resource