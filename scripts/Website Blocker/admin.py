from datetime import datetime
from start_website_blocker import Blocker

end_time = datetime(2021, 10, 1, 20)  # y, m, d, h, min
sites_to_block = ['www.facebook.com', 'facebook.com']
block = Blocker(end_time, sites_to_block)
block.block_websites()
