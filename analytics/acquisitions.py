"""Acquisition analytics facade."""

from utils.runtime import (
    acquisition_conversion_rates,
    acquisition_pipeline_metrics,
    acquisition_recommendation,
    calculate_acquisition_score,
    enrich_acquisition_deals,
)

__all__ = [
    "acquisition_conversion_rates",
    "acquisition_pipeline_metrics",
    "acquisition_recommendation",
    "calculate_acquisition_score",
    "enrich_acquisition_deals",
]
