from speedtest import SpeedTest
from twitter import TwitterBot

speedtest = SpeedTest()
speedtest.get_up_and_down_speeds()

twitter_bot = TwitterBot()
twitter_bot.log_in_to_twitter()
twitter_bot.publish_complain_tweet(down_speed=speedtest.download_speed, up_speed=speedtest.upload_speed)
