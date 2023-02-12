import time


class Player:
    def __init__(self, film_name):
        default_quality = "auto"
        default_volume = 50
        default_state = "play"
        # As player's state is "play" by default, the count starts when you initialize the player.
        self.last_time = 0
        self.start_time = time.time()
        self.film_playing = film_name
        self.quality = default_quality
        self.subtitles = False
        self.fullscreen = False
        self.volume = default_volume
        self.state = default_state

    def switch_state(self):
        if self.state == "play":
            self.state = "pause"
            self.save_last_time()
        elif self.state == "pause":
            self.state = "play"
            self.start_time = time.time()
        else:
            self.state = "stop"
            self.save_last_time()

    def change_quality(self):
        user_quality = input("Choose the quality (480p, 720p, 1080p, 2160p): ")
        self.quality = user_quality

    def set_volume(self):
        try:
            self.volume = int(input("Enter desired volume level: "))
        except ValueError:
            print("This is not an integer. Try again.")

    def switch_subtitles(self):
        if not self.subtitles:
            self.subtitles = True
        elif self.subtitles:
            self.subtitles = False

    def save_last_time(self):
        if not self.last_time:
            self.last_time = time.time() - self.start_time
        elif self.last_time:
            self.last_time += (time.time - self.start_time)

    def close_player(self):
        self.state = "stop"
        self.save_last_time()
