import os
import json
import pytest
from guestbook import add_note, list_notes, edit_note, delete_note, export_guestbook

test_entries = 'test_entries.txt'

def setup_module(module):
    with open(test_entries, 'w') as f:
        pass

def teardown_module(module):
    os.remove(test_entries)

def test_add_note():
    add_note('Test 1')
    add_note('Test 2')
    notes = []
    with open(test_entries, 'r') as f:
        notes = f.read().splitlines()
    assert len(notes) == 2
    assert notes[0] == 'Test 1'
    assert notes[1] == 'Test 2'

def test_list_notes(capsys):
    add_note('Test 1')
    add_note('Test 2')
    list_notes()
    captured = capsys.readouterr()
    assert captured.out == '1. Test 1\n2. Test 2\n'

def test_edit_note():
    add_note('Test 1')
    add_note('Test 2')
    edit_note(1, 'New test')
    notes = []
    with open(test_entries, 'r') as f:
        notes = f.read().splitlines()
    assert len(notes) == 2
    assert notes[0] == 'New yest'
    assert notes[1] == 'Test 2'

def test_delete_note():
    add_note('Test 1')
    add_note('Test 2')
    delete_note(1)
    notes = []
    with open(test_entries, 'r') as f:
        notes = f.read().splitlines()
    assert len(notes) == 1
    assert notes[0] == 'Test 2'

def test_export_guestbook(capsys):
    add_note('Test 1')
    add_note('Test 2')
    export_guestbook()
    captured = capsys.readouterr()
    data = json.loads(captured.out)
    assert len(data['notes']) == 2
    assert data['notes'][0] == 'Test 1'
    assert data['notes'][1] == 'Test 2'