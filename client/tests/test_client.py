from PyQt6.QtCore import Qt
from unittest.mock import patch, MagicMock


class TestInterface:

    def test_list_view_update_after_button_click(self, window, qtbot):
        sample_data = [
            {"content": "Test content 1", "created_datetime": "2022-01-01 12:00:00", "push_num": 1},
            {"content": "Test content 2", "created_datetime": "2022-01-02 12:00:00", "push_num": 2},
            {"content": "Test content 3", "created_datetime": "2022-01-03 12:00:00", "push_num": 3},
        ]
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_data

        with patch('client.utils.requests.get', return_value=mock_response):
            qtbot.mouseClick(window.send_get_button, Qt.MouseButton.LeftButton)
            qtbot.wait_until(lambda: window.list_view.model().rowCount() > 0)
            assert window.list_view.model().rowCount() == len(sample_data)

    def test_list_view_update_after_button_click_wrong(self, window, qtbot):
        mock_response = MagicMock()
        mock_response.status_code = 400

        with patch('client.utils.requests.get', return_value=mock_response):
            with patch('client.interface.ErrorPopup') as MockErrorPopup:
                qtbot.mouseClick(window.send_get_button, Qt.MouseButton.LeftButton)
                assert window.list_view.model().rowCount() == 0
                assert MockErrorPopup.called

    def test_post_button_click(self, window, qtbot):
        mock_response = MagicMock()
        mock_response.status_code = 200

        with patch('client.utils.requests.post', return_value=mock_response):
            with patch('client.interface.SuccessPopup') as MockSuccessPopup:
                qtbot.mouseClick(window.send_post_button, Qt.MouseButton.LeftButton)
                assert MockSuccessPopup.called
                assert window.list_view.model().rowCount() == 0
