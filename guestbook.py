import json
import argparse 

entries = 'entries.txt'


# guestbook
def load_guestbook():
    try:
        with open(entries, 'r') as f:
            notes = f.read().splitlines()
    except FileNotFoundError:
        notes = []
    return notes

def save_guestbook(notes):
    with open(entries, 'w') as f:
        f.write('\n'.join(notes))

def add_note(note):
    notes = load_guestbook()
    notes.append(note)
    save_guestbook(notes)

def list_notes():
    notes = load_guestbook()
    for i, note in enumerate(notes):
        print('{}. {}'.format(i + 1, note))

def edit_note(index, new_note):
    notes = load_guestbook()
    notes[-index] = new_note
    save_guestbook(notes)

def delete_note(index):
    notes = load_guestbook()
    del notes[-index]
    save_guestbook(notes)

def export_guestbook():
    notes = load_guestbook()
    data = {'notes': notes}
    print(json.dumps(data, indent=4))

# commands
parser = argparse.ArgumentParser(description='Guestbook')
subparsers = parser.add_subparsers(dest='command')

new_parser = subparsers.add_parser('new', help='Write a new note')
new_parser.add_argument('note', type=str, help='Whats inside your note')

list_parser = subparsers.add_parser('list', help='List all the notes')

edit_parser = subparsers.add_parser('edit', help='Edit existing note')
edit_parser.add_argument('index', type=int, help='Index of the note to edit')
edit_parser.add_argument('note', type=str, help='New content of the note')

delete_parser = subparsers.add_parser('delete', help='Delete an existing note')
delete_parser.add_argument('index', type=int, help='Index of the note to delete')

export_parser = subparsers.add_parser('export', help='Export the guestbook as JSON')

args = parser.parse_args()
if args.command == 'new':
    add_note(args.note)
elif args.command == 'list':
    list_notes()
elif args.command == 'edit':
    edit_note(args.index, args.note)
elif args.command == 'delete':
    delete_note(args.index)
elif args.command == 'export':
    export_guestbook()
else:
    print('Invalid command')