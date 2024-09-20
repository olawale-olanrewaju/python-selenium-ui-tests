import pytest

from pages.search import DuckDuckGoSearchPage
from pages.results import DuckDuckGoResultPage


def test_basic_duckduckgo_search(browser):

    PHRASE = 'panda'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    results_page = DuckDuckGoResultPage(browser)
    assert results_page.link_div_count() > 0
    assert results_page.phrase_results_count(PHRASE) > 0
    assert results_page.search_input_value() == PHRASE


