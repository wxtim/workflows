# Tests for gnome message util
from subprocess import run
from pathlib import Path

app = Path(__file__).parent.parent / 'gnome-message'

def test_gnome_message(monkeypatch):
    """
    Test the gnome message utility.

    Becasue we are testing a GUI application, this test can only
    be fully checked by looking at the desktop environment.
    However, we can check that the application runs without error
    and that it accepts command line arguments as expected.
    """

    # Test without message:
    assert run([str(app)]).returncode == 0

    # Test with a simple message
    assert run([str(app), 'Testing is manual']).returncode == 0

    # Test with a message and an icon
    assert run([str(app), 'Can you see this message', 'face-smile']).returncode == 0

    # Test with message and icon set by environment variables
    monkeypatch.setenv('N_MSG', 'Environment message')
    monkeypatch.setenv('N_ICON', 'face-sad')
    assert run([str(app)]).returncode == 0
