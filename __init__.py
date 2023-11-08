from mycroft import MycroftSkill, intent_file_handler


class PlayStrangeMusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('music.strange.play.intent')
    def handle_music_strange_play(self, message):
        self.speak_dialog('music.strange.play')


def create_skill():
    return PlayStrangeMusic()

