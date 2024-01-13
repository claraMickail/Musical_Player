class Note:
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave = 1, accidental = 'natural'):
        '''(
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'
        
        >>> test_two = Note (2, "B", 4, "natural")
        Traceback (most recent call last):
        AssertionError: Duration input is not valid
        
        >>> test_three = Note (2.0, "R")
        >>> test_three.accidental
        'natural'
        '''
        
        pitch_list = ['A','B','C','D','E','F','G','R']
        accidental_list = ['sharp', 'flat', 'natural']
        
        if type(duration) != float or duration <= 0:
            raise AssertionError ("Duration input is not valid")
        elif pitch not in pitch_list:
            raise AssertionError ( "Pitch input is invalid")
        elif type(octave) != int or octave < 1 or octave > 7:
            raise AssertionError ("Octave input is invalid")
        elif type(accidental) != str or accidental.lower() not in accidental_list:
            raise AssertionError ("accidental input is invalid")
        else:
            self.duration = duration
            self.pitch = pitch
            self.octave = octave
            self.accidental = accidental.lower()
            
            
    def __str__(self):
        return (str(self.duration) + " " + self.pitch + " " + str(self.octave) + " "+ self.accidental)
    
    def play(self, player_object):
        
        if self.pitch == 'R':
            player_string = 'pause'
        else: 
            player_string = self.pitch + str(self.octave)
            if self.accidental.lower() == 'sharp':
                player_string += '#'
            elif self.accidental.lower() == 'flat':
                player_string += 'b'
        
        player_object.play_note(player_string , self.duration)