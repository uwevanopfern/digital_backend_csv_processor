import pytest

from dsrs.models import DSR, Resource, Currency, Territory
from datetime import datetime


@pytest.mark.django_db
def test_add_dsr(client):
    dsrs = DSR.objects.all()
    assert len(dsrs) == 0


@pytest.mark.django_db
def test_get_single_dsr(client, add_dsr):
    dsr = add_dsr("path_one")
    res = client.get(f"/dsrs/{dsr.id}/")
    assert res.status_code == 200
    assert res.data["path"] == "path_one"


def test_get_incorrect_dsrs_id(client):
    res = client.get(f"/dsrs/foo/")
    assert res.status_code == 404


@pytest.mark.django_db
def test_get_all_dsrs(client, add_dsr):
    dsr_one = add_dsr("path_one")
    dsr_two = add_dsr("path_two")
    res = client.get(f"/dsrs/")
    assert res.status_code == 200
    assert res.data[0]["path"] == dsr_one.path
    assert res.data[1]["path"] == dsr_two.path


@pytest.mark.django_db
def test_get_resource(client, add_resource):
    resource = add_resource()
    res = client.get(
        f"/resources/percentile/10/?period_start=2020-01-01 00:00:00&period_end=2020-05-31 00:00:00&territory=NO"
    )
    print(res)
    assert res.status_code == 200


@pytest.mark.django_db
def test_get_resource_incorrect_number(client, add_resource):
    resource = add_resource()
    res = client.get(f"/resources/percentile/101/")
    assert res.status_code == 400
