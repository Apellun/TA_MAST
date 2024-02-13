import pytest
from client.interface import MainWindow


@pytest.fixture
def window(qtbot):
    main_window = MainWindow()
    qtbot.addWidget(main_window)
    return main_window