from unittest.mock import patch


class TestServer:
    def test_correct_post_request(self, client):
        with patch('server.views.post_view.sqlite3.connect') as mock_connect:
            mock_cursor = mock_connect.return_value.__enter__.return_value.cursor
            mock_execute = mock_cursor.return_value.execute

            response = client.post('/post', json={"created_datetime": "20240101 12:00:00", "content": "Test Content", "push_num": 1})
            
            assert mock_execute.called
            assert response.status_code == 200
            
    def test_incorrect_post_request(self, client):
        response = client.post('/post', json={"created_datetime": "20240101 12:00:00", "content": "Test Content", "push_num": "1"})
        assert response.status_code == 400

    def test_get_request_response(self, client):
        with patch('server.views.get_view.sqlite3') as mock_sqlite:
            mock_connection = mock_sqlite.connect.return_value.__enter__.return_value
            mock_cursor = mock_connection.cursor.return_value
            mock_cursor.fetchall.return_value = [{"created_datetime": "2024-01-01 12:00:00", "content": "Test Content", "push_num": 1}]

            response = client.get('/get')
            
            assert response.status_code == 200
            assert response.json == [{"content": "Test Content", "created_datetime": "2024-01-01 12:00:00", "push_num": 1}]


