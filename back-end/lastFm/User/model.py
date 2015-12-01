from api import *

class KNN:
    '''
    initial for KNN opreator
    '''
    def __init__(self, k) :
        self.nodes = dict()
        self.K = k

    def training(self, user_manager, artist_manager):
        for user_id, user in user_manager.iteritems():
            self.nodes[user_id] = get_feature(user, artist_manager)
