from __future__ import unicode_literals

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
         self.player = youtube_dl # youtubedl player
         self.ydl_opt = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                                            'key': 'FFmpegExtractAudio',
                                            'preferredcodec': 'opus',
                                            'preferredquality': '192',
                                           }],
                        }
         self.source = discord.AudioSource # discord audio source
         self.opus_file = object  # opus file downloaded

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
     
     def get_voice_client( self ): #{{{
        
         return self.voice

    #}}}
#----------------------------------------------------------------------------------------------


# audo player control
#----------------------------------------------------------------------------------------------
     def play( self, url ): #{{{
       
         # download opus file
         with self.player.YoutubeDL(self.ydl_opt) as ydl:
            ydl.download([url])

         # searching opus filename
         os.chdir("./")
         for file in glob.glob('*.opus'):
             self.opus_file = str(file)

         # FFmpegOpusAudio instance with opus file
         sourceaudio = discord.FFmpegOpusAudio(self.opus_file)

         # returns the AudioSource
         return sourceaudio
         

    #}}}
#----------------------------------------------------------------------------------------------
