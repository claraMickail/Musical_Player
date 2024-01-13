from note import *

class Melody:
    @classmethod
    def __init__ (self, filename):
        '''        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> print (hot_cross_buns.notes [5])
        1.0 G 4 natural
        >>> print (hot_cross_buns.notes [2])
        1.0 G 4 natural
        >>> len(hot_cross_buns.notes)
        17
        
        >>> tetris = Melody("tetris.txt")
        >>> len(tetris.notes)
        40
        >>> print(type(tetris.notes[0]))
        <class 'note.Note'>
        >>> print (tetris.notes[-2])
        0.5 A 4 natural
        
        >>> twinkle = Melody("twinkle.txt")
        >>> len(twinkle.notes)
        42
        >>> twinkle.title
        'Twinkle Twinkle Little Star'
        >>> twinkle.author
        'Traditional'
        
        '''
        fobj = open(filename, 'r')
        file_content = fobj.read()
        file_lines = file_content.split('\n')
        
        self.title = file_lines[0]
        self.author = file_lines[1]
        temp_list = file_lines[2:]
        
        self.notes = []
        repeater = False
        repeater_count = 0
        my_repeated =[]
        
        for elements in temp_list:
            element_list = elements.split()
           
            if element_list [1] != 'R':
                new_elements = Note(float(element_list[0]), element_list[1],int(element_list[2]), element_list[3].lower())
                new_elmt_copy = Note(float(element_list[0]), element_list[1],int(element_list[2]), element_list[3].lower())
            else:
                new_elements = Note(float(element_list[0]), element_list[1])
                
            self.notes.append(new_elements)
                
            if 'true' in elements or repeater == True:
                repeater = True
                repeater_count +=1
                my_repeated.append(new_elmt_copy)
                if 'true' in elements and repeater_count != 1:
                    repeater = False
                    repeater_count = 0
                        
            if repeater == False and len(my_repeated) != 0:
                self.notes += my_repeated
                my_repeated =[]                
                    
        fobj.close()
        
    def play(self, music_player):
        for note_list in self.notes:
            note_list.play(music_player)
            
    def get_total_duration(self):
        '''
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        '''
        total_duration = 0.0
        
        for elements in self.notes:
            total_duration += float((str(elements).split(" "))[0])
        return total_duration
    
    def update_octave (self,factor):
        for elmt in self.notes:
            if elmt.pitch != 'R':
                elmt.octave += factor
                
    def lower_octave (self):
        for elements in self.notes:
            if elements.pitch != 'R' and elements.octave <= Note.OCTAVE_MIN:
                return False
        self.update_octave(-1)
        return True
    
    def upper_octave(self):
        for elements in self.notes:
            if elements.pitch != 'R' and elements.octave >= Note.OCTAVE_MAX:
                return False
        self.update_octave(1)
        return True
    
    def change_tempo(self, num):
        for note in self.notes:
            note.duration *= num