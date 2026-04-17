"""Tests for the HAESC model definitions."""
import pytest
from haesc.model import HAESCModel, ConstructType


def test_all_constructs_present():
    assert set(HAESCModel.CONSTRUCTS.keys()) == {"X", "M", "Y"}


def test_construct_types():
    assert HAESCModel.CONSTRUCTS["X"].construct_type == ConstructType.INDEPENDENT
    assert HAESCModel.CONSTRUCTS["M"].construct_type == ConstructType.MEDIATING
    assert HAESCModel.CONSTRUCTS["Y"].construct_type == ConstructType.DEPENDENT


def test_indicators_total():
    assert len(HAESCModel.INDICATORS) == 23


def test_indicators_per_construct():
    assert len(HAESCModel.indicators_by_construct("X")) == 11
    assert len(HAESCModel.indicators_by_construct("M")) == 6
    assert len(HAESCModel.indicators_by_construct("Y")) == 6


def test_hypotheses_count():
    assert len(HAESCModel.HYPOTHESES) == 4


def test_h4_is_mediation():
    h4 = next(h for h in HAESCModel.HYPOTHESES if h.code == "H4")
    assert h4.via is not None


def test_summary_runs():
    summary = HAESCModel.summary()
    assert "HAESC" in summary
    assert "H1" in summary
