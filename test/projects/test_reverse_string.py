import pytest

from test.fixtures import project_permutations
from test.project import ProjectType


@pytest.fixture(params=project_permutations[ProjectType.ReverseString].params,
                ids=project_permutations[ProjectType.ReverseString].ids)
def reverse_string(request):
    yield request.param
    request.param.cleanup()


def test_reverse_string(reverse_string):
    actual = reverse_string.run(params='"Hello, World"')
    assert actual.strip() == 'dlroW ,olleH'
