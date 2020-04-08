from __future__ import unicode_literals
from queue import SimpleQueue

# Main module --> discord API
import discord
import youtube_dl
import ffmpeg
import os
import glob


class Manager(object):

# Constructor
#----------------------------------------------------------------------------------------------
     def __init__( self ): #{{{

         self.msg_id ='' 
         self.user_id =''
         self.phrase = [] # list of phrases
         self.token = '' # token string
         self.voice = discord.VoiceClient # voice client
         self.voice_panel = False # voice client status
         self.player = youtube_dl # youtubedl player
         self.ydl_opt = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                                            'key': 'FFmpegExtractAudio',
                                            'preferredcodec': 'opus',
                                            'preferredquality': '192',
                                           }],
                        }
         self.opus_file = object  # opus file downloaded
         self.queue = SimpleQueue() # audio queue
         self.playing = '' # current file playing

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
         self.voice_panel = True

    #}}}
     
     def get_voice_client( self ): #{{{
        
         return self.voice

    #}}}
#----------------------------------------------------------------------------------------------


# audio player control
#----------------------------------------------------------------------------------------------
     # True --> playing, False --> no audio
     def voice_status( self ): #{{{

        return self.voice_panel

     #}}}

     def valid_file( self, filename ): #{{{
        
         temp_queue = self.queue

         while not temp_queue.empty():
             if filename == temp.queue.get():
                 return False

         return True


    #}}}


     def _search_opus_file_( self ): #{{{
       
         # searching opus filename
         os.chdir("./")
         for file in glob.glob('*.opus'):
             if self.valid_file(str(file)):
                self.opus_file = str(file)

         # enqueue filename
         self.queue.put(self.opus_file)

    #}}}
     
     
     def download( self, url ): #{{{
        
         # download opus file
         with self.player.YoutubeDL(self.ydl_opt) as ydl:
            ydl.download([url])

         self._search_opus_file_()

    #}}}
     
     def add_to_queue( self, url ): #{{{
    
         self.download( url )
    #}}}


     def next( self ): #{{{
    
         os.remove(self.playing)

         self.playing = self.queue.get()

         self.voice.source = discord.FFmpegOpusAudio(self.playing)

         self.voice.play(self.voice.source)
    #}}}


     def queue_empty( self ): #{{{
    
         return self.queue.empty()
    #}}}
     

     def generate_source( self, url ): #{{{
        
         # downloading video
         self.download( url )

         # remove from queue
         self.playing = self.queue.get()

         # FFmpegOpusAudio instance with opus file
         sourceaudio = discord.FFmpegOpusAudio(self.playing)

         # returns the AudioSource
         return sourceaudio

    #}}}
     
     def clear_queue( self ): #{{{
        
         # The current audio is already out of the queue
         os.remove(self.playing)

         while not self.queue.empty():
             print('entrou mno loop')
             self.playing = self.queue.get()
             os.remove(self.playing)
         
         # thid method will be called when voiceclient disconnect.
         self.voice_panel = False

    #}}}
#----------------------------------------------------------------------------------------------
