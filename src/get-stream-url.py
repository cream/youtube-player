#!/usr/bin/env python
import youtube
import sys

video_id = sys.argv[1]
if 'v=' in video_id:
    import urlparse
    video_id = urlparse.parse_qs(urlparse.urlparse(video_id).query)['v'][0]
video = youtube.Video(video_id=video_id)
video.request_video_info()

try:
    resolution = sys.argv[2]
    if resolution == '-':
        raise IndexError
except IndexError:
    print video.stream_urls.keys()
    resolution = video.stream_urls.iterkeys().next()
else:
    # TODO: Think about new names for stuff like 480p
    resolution = {
        'low' : '360p',
        'middle' : '720p',
        'mid' : '720p',
        'high' : '1080p',
        '360' : '360p',
        '480' : '480p',
        '480+' : '480p+',
        '720' : '720p',
        '1080' : '1080p'
    }.get(resolution, resolution)
    if resolution not in video.stream_urls:
        print "Warning: Requested video {video_id} is not available in {resolution}!".format(**globals())
        resolution = video.stream_urls.iterkeys().next()

video_url = video.stream_urls[resolution]

try:
    program = sys.argv[3]
except IndexError:
    pass
else:
    import os
    os.system("%s '%s'" % (program, video_url))

print "mp4 URL for {video_id} ({resolution}) is\n{video_url}".format(**globals())
