import pyglet
song = pyglet.media.load('/home/balerion/Downloads/whatsapp_iphone.mp3')
song.play()
pyglet.app.run()


# import datetime
#
# my_file = open('msg_logs', 'a')
# current_datetime = datetime.datetime.now()
# my_file.write(str(current_datetime)+'\n')
# my_file.close()
