"""Tests for the HAESC survey questionnaire."""
import pytest
from haesc.instruments.questionnaire import Questionnaire


@pytest.fixture
def q():
    return Questionnaire()


def test_three_sections(q):
    assert len(q.sections) == 3


def test_total_items(q):
    assert q.total_items == 23


def test_to_dict_structure(q):
    d = q.to_dict()
    assert "screening" in d
    assert "demographics" in d
    assert "sections" in d
    assert d["total_items"] == 23


def test_all_items_have_bilingual_text(q):
    for section in q.sections:
        for item in section.items:
            assert item.text_id
            assert item.text_en
