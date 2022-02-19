"""Test the _cli.py module."""
from pathlib import Path
from mockito import expect, any_
from efi_monitor import _cli as sut


def test_check_with_dump_files(tmp_path: Path, capsys):
    """Test the check function with dump files."""
    search_path = tmp_path / "dump*"
    dump = tmp_path / "dump-junk"
    dump.write_text("stuff", encoding="utf8")
    with expect(sut.os.environ).get("EFI_MONITOR_FILE_PATH", any_(str)).thenReturn(
        str(search_path)
    ):
        sut.check()
    captured = capsys.readouterr()
    assert captured.out == f"{dump}\n"


def test_check_without_dump_files(tmp_path: Path, capsys):
    """Test the check function without dump files."""
    search_path = tmp_path / "dump*"
    with expect(sut.os.environ).get("EFI_MONITOR_FILE_PATH", any_(str)).thenReturn(
        str(search_path)
    ):
        sut.check()
    captured = capsys.readouterr()
    assert captured.out == ""


def test_clear_with_dump_files(tmp_path: Path):
    """Test the clear function with dump files."""
    search_path = tmp_path / "dump*"
    dump = tmp_path / "dump-junk"
    dump.write_text("stuff", encoding="utf8")
    with expect(sut.os.environ).get("EFI_MONITOR_FILE_PATH", any_(str)).thenReturn(
        str(search_path)
    ):
        sut.clear()
    assert not dump.exists()


def test_clear_without_dump_files(tmp_path: Path):
    """Test the clear function without dump files."""
    search_path = tmp_path / "dump*"
    with expect(sut.os.environ).get("EFI_MONITOR_FILE_PATH", any_(str)).thenReturn(
        str(search_path)
    ):
        sut.clear()
