
import math, operator


## get user feature from user history
def get_feature(user, artist_manager):
    '''
    get user tagging feature
    '''
    artists = user.ArtistList
    feature = dict()
    for artist_id, listen_times in artists.iteritems():
        tag_info = artist_manager[artist_id].tag_normalized
        for tag_idm weight in tag_info.iteritems():
            if not feature.has_key(tag_id):
                feature[tag_id] = weight * listen_times
            else:
                feature[tag_id] += weight * listen_times
    weight_sum = 0
    for tag_id, weight in feature.iteritems():
        weight_sum += feature[tag_id]
    for tag_id, weight in feature.iteritems():
        feature[tag_id] = float(weight) / weight_sum
    return feature
