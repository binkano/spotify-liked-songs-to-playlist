playlist_name = "Test"              # (str) insert playlist name
playlist_description = None         # [Optional] (str) insert playlist description
is_playlist_public = True           # (boolean) determines if the created playlist is public
track_limit = 20                    # (int) the number of tracks per offset to be transferred, minimum 1, maximum 50
offset = 0                          # (int) the multiple of track limits to be transferred.
                                    # e.g. if track = 20 and offset = 4, total tracks transferred = 20*4=80