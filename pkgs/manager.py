
class Manager(object):

# Constructor
#----------------------------------------------------------------------------------------------
     def __init__( self ): #{{{

         self.msg_id =''
         self.user_id =''
         self.phrase = []
         self.token = ''
         self.voice = ()

    #}}}
#----------------------------------------------------------------------------------------------

# Save message user and id
#----------------------------------------------------------------------------------------------
     def set_msg_id( self, msg_id ): #{{{

        self.msg_id = msg_id

    #}}}

     def set_user_id( self, user_id): #{{{

        self.user_id = user_id

    #}}}

     def get_msg_id( self ): #{{{

        return self.msg_id

    #}}}

     def get_user_id( self ): #{{{

        return self.user_id

    #}}}
#----------------------------------------------------------------------------------------------


# Read phrases
#----------------------------------------------------------------------------------------------
     def set_phrases( self ): #{{{

        # Opening file
        try:
            _phrases_ = open('phrase_data.dat', "r")

        except IOError:

            print('Unable to open file! check again.')


        self.phrase = _phrases_.readlines()

    #}}}

     def get_phrases( self ): #{{{
 
        return self.phrase

     #}}}
#----------------------------------------------------------------------------------------------

# Protect token ( separate file )
#----------------------------------------------------------------------------------------------
     def set_token( self, filepath ): #{{{

        # Opening file
        try:
            _token_ = open(filepath, "r")

        except IOError:

            print('Unable to open file! check again.')


        self.token = _token_.readline()

        return str(self.token)
    #}}}
#----------------------------------------------------------------------------------------------

# VoiceClient connection control
#----------------------------------------------------------------------------------------------
     def create_voice_client( self, voicech ): #{{{
        
         self.voice = voicech

    #}}}
     
     def quit_voice_client( self ): #{{{
        
         return self.voice

    #}}}
#----------------------------------------------------------------------------------------------
