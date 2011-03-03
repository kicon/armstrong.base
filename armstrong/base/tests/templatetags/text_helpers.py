import fudge

from .._utils import TestCase
from ...templatetags import text_helpers


def generate_random_request():
    request = fudge.Fake()
    request.has_attr(META={"HTTP_REFERER": "http://localhost/?q=some"})
    fudge.clear_calls()
    return request


def generate_random_request_and_context(text):
    request = generate_random_request()
    context = {
        "request": request,
        "text": text,
    }
    return request, context


class HelloWorld(TestCase):
    def test_replaces_words_with_highlighted_word(self):
        text = "This is some text"
        request, context = generate_random_request_and_context(text)

        node = text_helpers.HighlightedSearchTermNode("text")
        result = node.render(context)

        expected = 'This is <span class="search_term">some</span> text'
        self.assertEqual(expected, result)

    def test_can_handle_mismatched_case(self):
        text = "This is SOME text"
        request, context = generate_random_request_and_context(text)

        node = text_helpers.HighlightedSearchTermNode("text")
        result = node.render(context)
        expected = 'This is <span class="search_term">SOME</span> text'
        self.assertEqual(expected, result)
