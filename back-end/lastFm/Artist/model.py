
## create the database model for each Artist

import peewee

class Artist:
    def __init__(self, artist_id, artist_name):
        '''
        definition of the artist object
        '''
        self.id = artist_id
        self.name = artist_name
        self.tag = dict()
        self.tag_normalized = dict()

    def __repr__(self):
        return 'Artist: %s %s Tags: %s>' % (str(self.id), self.name, self.tag)

    def insert_tag(self,tag_id):
        '''
        insert a tag/add tagging times by the user labeled by a user for the artist
        '''
        if self.tag.has_key(tag_id):
            self.tag[tag_id] += 1
        else:
            self.tag[tag_id] = 1

    def get_top_tags(self):
        top_tag = -1
        max_weight = 0
        for key, value in self.tag.iteritems():
            if value > max_weight:
                max_weight = value
                top_tag = key
        return top_tag
