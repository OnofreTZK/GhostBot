from __future__ import unicode_literals
from collections import deque
import discord
import youtube_dl
import ffmpeg
import os
import glob
import asyncio
import copy


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
         self.queue = deque() # audio queue
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
        
         temp_queue = self.queue.copy()
    
         # current auido file playing
         if filename == self.playing:
             return False

         if not len(temp_queue) == 0:
            while not len(temp_queue) == 0:
                if filename == temp_queue.popleft():
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
         self.queue.append(self.opus_file)

    #}}}
     
     
     def download( self, url ): #{{{
        
         # download opus file
         with self.player.YoutubeDL(self.ydl_opt) as ydl:
            ydl.download([url])

         self._search_opus_file_()

    #}}}
     
     def add_to_queue( self, url ): #{{{
    
         self.download( url )

         temp_queue = copy.deepcopy(self.queue)
         while not len(temp_queue) == 0:
             print(temp_queue.popleft())
    #}}}


     async def next( self ): #{{{

         if not self.voice_panel:
             return

         if not len(self.queue) == 0 and not self.voice.is_playing():

            os.remove(self.playing)

            self.playing = self.queue.popleft()

            newSource = discord.FFmpegOpusAudio(self.playing)

            self.voice.play(newSource)
         else:
             return
    #}}}

     def skip( self ): #{{{
        
        self.voice.stop()

        os.remove(self.playing)

        self.playing = self.queue.popleft()

        newSource = discord.FFmpegOpusAudio(self.playing)

        self.voice.play(newSource)
         
    #}}}

     def pause( self ): #{{{
    
         self.voice.pause()

         self.voice_panel = False
    #}}}
     
     def resume( self ): #{{{
    
         self.voice.resume()

         self.voice_panel = True
    #}}}
     
     def queue_empty( self ): #{{{
    
         return len(self.queue) == 0
    #}}}
     

     def generate_source( self, url ): #{{{
        
         # downloading video
         self.download( url )

         # remove from queue
         self.playing = self.queue.popleft()

         # FFmpegOpusAudio instance with opus file
         sourceaudio = discord.FFmpegOpusAudio(self.playing)

         # returns the AudioSource
         return sourceaudio

    #}}}
     
     def clear_queue( self ): #{{{
        
         # The current audio is already out of the queue
         os.remove(self.playing)

         # clear the queue
         while not len(self.queue) == 0:
             self.playing = self.queue.popleft()
             os.remove(self.playing)
         
         # in case of fail in add_to_queue, remove all files downloaded 
         os.chdir("./")
         for file in glob.glob('*.opus'):
             os.remove(str(file))
         
         # thid method will be called when voiceclient disconnect.
         self.voice_panel = False
    #}}}
#----------------------------------------------------------------------------------------------
