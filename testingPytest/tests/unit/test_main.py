import pytest
from main import Main
from Classes.some_services import SomeServices
from unittest.mock import MagicMock, AsyncMock, patch
from tests.unit.mocks.mock_db_some_data import mock_data
from Classes.data_service import DataService
from main import Main, service_add, service_get_data

def test_main_init():
  main_instance = Main()
  assert isinstance(main_instance.service, SomeServices)

def test_main_run():
  main_instance = Main()
  main_instance.service.perform_action = MagicMock(return_value="mocked result")
  main_instance.run()
  main_instance.service.perform_action.assert_called_once()
  

@pytest.fixture
def mock_main_instance():
  return Main()

@pytest.mark.asyncio
async def test_service_add(mock_main_instance):
  mock_main_instance.service.async_add = AsyncMock(return_value=3)
  with patch("main.Main", return_value=mock_main_instance):
    result = await service_add()
    mock_main_instance.service.async_add.assert_called_once_with(1, 2)
    assert result == 3

@pytest.mark.asyncio
async def test_service_get_data(mock_main_instance):
  with patch("main.Main", return_value=mock_main_instance), \
       patch.object(DataService,"get_data", return_value=mock_data) as mock_get_data:
    result = await service_get_data()
    mock_get_data.assert_called_once()
    assert result == mock_data