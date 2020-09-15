
'''
python program for creating our own sticky notes
'''

def note_creation(num):
    '''
    function for creating notes from user.
    '''
    notes = []
    for i in range(1,num+1):
        note = input("\nEnter your Note - {} :".format(i))
        notes.append(note)
    return notes

def print_notes(name_given,notes_given):
    '''
    function to print the sticky notes.
    '''
    print()
    print(name_given.capitalize(),"- here is your Sticky Notes")
    for i,note_given in enumerate(notes_given,1):
        print("\nNote",i,"-",note_given)

def save_notes(name_given,notes_given):
    '''
    function to save the yours stickynote as txt file.
    '''
    file_name = "%s_Sticky_Notes.txt" %name_given.capitalize()
    file = open(file_name, "w")
    file.write("\n{} - here is your Sticky Notes".format(name_given.capitalize()))
    for i,note_given in enumerate(notes_given,1):
        file.write("\n\nNote {} - {}".format((i),note_given))
    file.close()
    print("\nFILE HAS BEEN SAVED SUCCESSFULLY...")

def main():
    '''
    function which is used to call other functions.
    '''
    print("\nCREATE YOUR OWN STICKY NOTES...")
    user_name = input("\nEnter your Name - ")
    notes_num = int(input("\nEnter number of notes needed - "))
    user_notes = note_creation(notes_num)
    print_notes(user_name,user_notes)
    print()
    save_notes(user_name,user_notes)
