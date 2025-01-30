"""
    :codeauthor: :email:`Anthony Shaw <anthonyshaw@apache.org>`
"""

import pytest
import salt.modules.napalm_netacl as napalm_acl
import tests.support.napalm as napalm_test_support
from tests.support.mock import MagicMock, patch


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {
            "config.get": MagicMock(
                return_value={"test": {"driver": "test", "key": "2orgk34kgk34g"}}
            ),
            "file.file_exists": napalm_test_support.true,
            "file.join": napalm_test_support.join,
            "file.get_managed": napalm_test_support.get_managed_file,
            "random.hash": napalm_test_support.random_hash,
            "capirca.get_term_config": mock_capirca_term_config,
            "capirca.get_policy_config": mock_capirca_policy_config,
            "capirca.get_filter_config": mock_capirca_filter_config,
            "capirca.get_filter_pillar": mock_capirca_get_filter_pillar,
            "capirca.get_term_pillar": mock_capirca_get_term_pillar,
            "net.load_config": mock_net_load_config,
        },
        "__grains__": {"os": "ios", "vendor": "cisco", "model": "3750X"},
    }

    return {napalm_acl: module_globals}


def mock_capirca_term_config(platform, filter_name, term_name, *args, **kwargs):
    assert platform == "cisco"
    assert filter_name == "test_filter"
    assert term_name == "test_term"
    return "test_config"


def mock_capirca_filter_config(platform, filter_name, *args, **kwargs):
    assert platform == "cisco"
    assert filter_name == "test_filter"
    return "test_config"


def mock_capirca_policy_config(platform, *args, **kwargs):
    assert platform == "cisco"
    return "test_config"


def mock_net_load_config(text, *args, **kwargs):
    assert text == "test_config"
    return napalm_test_support.TEST_TERM_CONFIG


def mock_capirca_get_filter_pillar(filter_, *args, **kwargs):
    assert filter_ == "test_filter"
    return {"test": "value"}


def mock_capirca_get_term_pillar(filter_, term, *args, **kwargs):
    assert filter_ == "test_filter"
    assert term == "test_term"
    return {"test": "value"}


def test_load_term_config():
    with patch(
        "salt.utils.napalm.get_device",
        MagicMock(return_value=napalm_test_support.MockNapalmDevice()),
    ):
        ret = napalm_acl.load_term_config("test_filter", "test_term")
        assert ret["already_configured"] is False


def test_load_filter_config():
    with patch(
        "salt.utils.napalm.get_device",
        MagicMock(return_value=napalm_test_support.MockNapalmDevice()),
    ):
        ret = napalm_acl.load_filter_config("test_filter", "test_term")
        assert ret["already_configured"] is False


def test_load_policy_config():
    with patch(
        "salt.utils.napalm.get_device",
        MagicMock(return_value=napalm_test_support.MockNapalmDevice()),
    ):
        ret = napalm_acl.load_policy_config("test_filter", "test_term")
        assert ret["already_configured"] is False


def test_get_filter_pillar():
    ret = napalm_acl.get_filter_pillar("test_filter")
    assert ret["test"] == "value"


def test_get_term_pillar():
    ret = napalm_acl.get_term_pillar("test_filter", "test_term")
    assert ret["test"] == "value"
